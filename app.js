'use strict';
let reports=[];
const $=id=>document.getElementById(id);
const types={day:'Tagesbericht',week:'Wochenbericht',month:'Monatsbericht'};
const format=date=>new Intl.DateTimeFormat('de-DE',{day:'2-digit',month:'2-digit',year:'numeric'}).format(new Date(date+'T12:00:00'));
function el(tag,className,text){const node=document.createElement(tag);if(className)node.className=className;if(text!==undefined)node.textContent=text;return node;}
function normalize(value){return value.toLocaleLowerCase('de').normalize('NFD').replace(/[\u0300-\u036f]/g,'');}
function matchRanges(text,words){
 let folded='',offsets=[];
 for(let i=0;i<text.length;){const char=String.fromCodePoint(text.codePointAt(i)),part=normalize(char);for(let j=0;j<part.length;j++)offsets.push([i,i+char.length]);folded+=part;i+=char.length;}
 const ranges=[];for(const word of words){let start=0,index;while((index=folded.indexOf(word,start))!==-1){ranges.push([offsets[index][0],offsets[index+word.length-1][1]]);start=index+word.length;}}
 ranges.sort((a,b)=>a[0]-b[0]);const merged=[];for(const range of ranges){const previous=merged[merged.length-1];if(previous&&range[0]<=previous[1])previous[1]=Math.max(previous[1],range[1]);else merged.push(range.slice());}return merged;
}
function highlighted(text,words){
 const node=el('span');let cursor=0;for(const [start,end]of matchRanges(text,words)){node.append(document.createTextNode(text.slice(cursor,start)),el('mark','',text.slice(start,end)));cursor=end;}node.append(document.createTextNode(text.slice(cursor)));return node;
}
function addSearchExcerpts(body,r,words){
 if(!words.length)return;
 const passages=[];let heading='';for(const p of r.paragraphs){if(p.heading){heading=p.text;continue;}if(words.some(word=>normalize(p.text+' '+heading).includes(word)))passages.push({text:p.text,heading});}
 const section=el('div','search-excerpts');section.append(el('div','excerpt-label',passages.length?'Passende Textstellen · '+passages.length:'Treffer in Titel, Zusammenfassung oder Schlagwörtern'));
 if(!passages.length){const text=[r.title,r.subtitle,r.summary,...r.tags].filter(Boolean).filter(t=>words.some(w=>normalize(t).includes(w))).join(' · ');const p=el('p','excerpt');p.append(highlighted(text,words));section.append(p);}
 for(const passage of passages.slice(0,3)){const item=el('div','excerpt');if(passage.heading){const title=el('div','excerpt-heading');title.append(highlighted(passage.heading,words));item.append(title);}const ranges=matchRanges(passage.text,words),first=ranges.length?ranges[0][0]:0;let start=Math.max(0,first-100),end=Math.min(passage.text.length,Math.max(first+220,start+320));if(start>0){const space=passage.text.indexOf(' ',start);if(space>=0&&space<first)start=space+1;}if(end<passage.text.length){const space=passage.text.lastIndexOf(' ',end);if(space>first)end=space;}const p=el('p');p.append(highlighted((start?'… ':'')+passage.text.slice(start,end)+(end<passage.text.length?' …':''),words));item.append(p);section.append(item);}
 if(passages.length>3)section.append(el('div','excerpt-more','Weitere '+(passages.length-3)+' passende Textstellen im Bericht.'));
 body.append(section);
}
function render(){
 const words=normalize($('search').value.trim()).split(/\s+/).filter(Boolean);
 const type=$('type').value,from=$('from').value,to=$('to').value;
 const bad=Boolean(from&&to&&from>to);$('validation').hidden=!bad;$('validation').textContent=bad?'Das Startdatum liegt nach dem Enddatum. Bitte korrigiere den Zeitraum.':'';
 const shown=bad?[]:reports.filter(r=>{const hay=normalize([r.title,r.subtitle,r.summary,...r.tags,...r.paragraphs.map(p=>p.text)].join(' '));return(type==='all'||r.type===type)&&(!from||r.date>=from)&&(!to||r.date<=to)&&words.every(w=>hay.includes(w));}).sort((a,b)=>b.date.localeCompare(a.date)||a.title.localeCompare(b.title,'de'));
 $('result-count').textContent=shown.length+' von '+reports.length+' Berichten';$('list').replaceChildren();$('empty').hidden=shown.length>0||bad;
 for(const r of shown){
  const article=el('article','report'),body=el('div'),meta=el('div','report-top');meta.append(el('span','badge '+r.type,types[r.type]),el('span','',format(r.date)));if(r.example)meta.append(el('span','example','Beispielausgabe'));body.append(meta,el('h3','',r.title),el('p','',r.summary),el('div','period','Berichtszeitraum '+format(r.start)+' – '+format(r.end)));
  const tags=el('div','tags');for(const tag of r.tags){const button=el('button','tag',tag);button.type='button';button.setAttribute('aria-label','Nach '+tag+' suchen');button.addEventListener('click',()=>{$('search').value=tag;render();});tags.append(button);}body.append(tags);
  addSearchExcerpts(body,r,words);
  const actions=el('div','report-actions'),read=el('button','primary','Bericht lesen');read.addEventListener('click',()=>openReport(r));const download=el('a','secondary','Word herunterladen');download.href='./'+encodeURIComponent(r.file);download.download=r.file;actions.append(read,download);article.append(body,actions);$('list').append(article);
 }
}
function openReport(r){
 $('reader-title').textContent=r.title;$('reader-meta').textContent=types[r.type]+' · '+format(r.date)+(r.example?' · Beispielausgabe':'');$('reader-summary').textContent=r.summary;
 $('reader-download').href='./'+encodeURIComponent(r.file);$('reader-download').download=r.file;$('reader-body').replaceChildren();
 const words=normalize($('search').value.trim()).split(/\s+/).filter(Boolean);
 for(const p of r.paragraphs){if(p.text===r.title||p.text==='powered by DubraSec')continue;const node=el(p.heading?'h3':'p');node.append(highlighted(p.text,words));$('reader-body').append(node);}
 $('reader-sources').replaceChildren();for(const url of r.sources){if(!/^https:\/\//.test(url))continue;const a=el('a','',new URL(url).hostname);a.href=url;a.target='_blank';a.rel='noopener noreferrer';$('reader-sources').append(a);}$('reader').showModal();
}
function reset(){$('search').value='';$('type').value='all';$('from').value='';$('to').value='';render();}
async function load(){
 $('load-error').hidden=true;$('empty').hidden=true;$('result-count').textContent='Berichte werden geladen';
 try{const response=await fetch('reports.json');if(!response.ok)throw Error('Archiv nicht erreichbar');reports=await response.json();if(!Array.isArray(reports))throw Error('Ungültiges Archiv');$('total').textContent=reports.length;for(const [type,id]of[['day','days'],['week','weeks'],['month','months']])$(id).textContent=reports.filter(r=>r.type===type).length;render();}
 catch(error){$('load-error').hidden=false;$('result-count').textContent='Archiv nicht verfügbar';$('list').replaceChildren();}
}
for(const id of ['search','type','from','to'])$(id).addEventListener(id==='search'?'input':'change',render);
$('reset').addEventListener('click',reset);$('empty-reset').addEventListener('click',reset);$('retry').addEventListener('click',load);$('close').addEventListener('click',()=>$('reader').close());
load();

