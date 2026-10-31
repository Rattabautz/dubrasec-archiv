#!/usr/bin/env python3
"""Generate archive DOCX/PDF from daily Markdown. Uses public-source report content only."""
from pathlib import Path
from datetime import datetime
from xml.sax.saxutils import escape
import re, sys
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.opc.constants import RELATIONSHIP_TYPE as RT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.units import mm

NAVY='#152c49'
TEAL='#168b91'
INK='#1b2b40'
MUTED='#66778a'
def clean(s):
    s=re.sub(r'\*\*(.*?)\*\*',r'\1',s)
    return s.replace('  ',' ').strip()
URL_RE=re.compile(r'https?://\S+')
def link_parts(text):
    pos=0
    for match in URL_RE.finditer(text):
        raw=match.group(0)
        url=raw.rstrip('.,;)]}')
        if match.start()>pos: yield False,text[pos:match.start()]
        if url: yield True,url
        if len(raw)>len(url): yield False,raw[len(url):]
        pos=match.end()
    if pos<len(text): yield False,text[pos:]
def add_linkified(doc, paragraph, text):
    for is_url,part in link_parts(text):
        if not is_url:
            paragraph.add_run(part)
            continue
        rid=paragraph.part.relate_to(part,RT.HYPERLINK,is_external=True)
        hyperlink=OxmlElement('w:hyperlink');hyperlink.set(qn('r:id'),rid)
        run=OxmlElement('w:r');rpr=OxmlElement('w:rPr')
        color=OxmlElement('w:color');color.set(qn('w:val'),'168B91');rpr.append(color)
        underline=OxmlElement('w:u');underline.set(qn('w:val'),'single');rpr.append(underline)
        run.append(rpr)
        t=OxmlElement('w:t');t.text=part;run.append(t)
        hyperlink.append(run);paragraph._p.append(hyperlink)
def pdf_linkified(text):
    chunks=[]
    for is_url,part in link_parts(text):
        if is_url:
            safe=escape(part,{'"':'&quot;'})
            chunks.append('<link href="'+safe+'" color="#168b91"><u>'+safe+'</u></link>')
        else:chunks.append(escape(part))
    return ''.join(chunks)
def read_sections(path):
    chunks=[]
    for line in path.read_text(encoding='utf-8').splitlines():
        s=line.strip()
        if not s: continue
        if s.startswith('# '):chunks.append(('title',clean(s[2:])))
        elif s.startswith('## '):chunks.append(('heading',clean(s[3:])))
        elif s.startswith('### '):chunks.append(('subheading',clean(s[4:])))
        elif re.match(r'^\d+\. ',s):chunks.append(('body',clean(s)))
        else:chunks.append(('body',clean(s)))
    return chunks
def build(md):
    date=md.name[:10]
    weekly=(md.parent.name=='Wochenberichte')
    week_label=('KW%02d_%d' % (datetime.strptime(date,'%Y-%m-%d').isocalendar().week,datetime.strptime(date,'%Y-%m-%d').isocalendar().year)) if weekly else ''
    week_display=week_label.replace('_','/') if weekly else ''
    try:datetime.strptime(date,'%Y-%m-%d')
    except ValueError:raise SystemExit('Bad report filename: '+md.name)
    docx=md.with_name('DubraSec_Wochenbericht_'+week_label+'.docx' if weekly else 'DubraSec_Tagesbericht_'+date+'.docx')
    pdf=md.with_name('DubraSec_Wochenbericht_'+week_label+'.pdf' if weekly else 'DubraSec_Tagesbericht_'+date+'.pdf')
    chunks=read_sections(md)
    doc=Document()
    sec=doc.sections[0]
    sec.top_margin=Cm(2.2);sec.bottom_margin=Cm(2);sec.left_margin=Cm(2.1);sec.right_margin=Cm(2.1)
    normal=doc.styles['Normal'];normal.font.name='Calibri';normal.font.size=Pt(9);normal.font.color.rgb=RGBColor(27,43,64)
    for nm,size,color in [('Title',19,(21,44,73)),('Heading 1',13,(21,44,73)),('Heading 2',11,(21,44,73))]:
        st=doc.styles[nm];st.font.name='Calibri';st.font.size=Pt(size);st.font.color.rgb=RGBColor(*color);st.font.bold=True
    header=sec.header.paragraphs[0];header.text='DUBRASEC  /  SECURITY INTELLIGENCE  /  '+('WOCHENBERICHT' if weekly else 'TAGESBERICHT');header.style='Caption'
    foot=sec.footer.paragraphs[0];foot.text='DubraSec · OSINT · '+(week_display if weekly else date);foot.alignment=WD_ALIGN_PARAGRAPH.CENTER
    for kind,txt in chunks:
        if weekly and kind=='heading' and txt.startswith('A. Kritische'):doc.add_page_break()
        if kind=='title':doc.add_paragraph(txt,style='Title')
        elif kind=='heading':doc.add_paragraph(txt,style='Heading 1')
        elif kind=='subheading':doc.add_paragraph(txt,style='Heading 2')
        else:
            p=doc.add_paragraph()
            add_linkified(doc,p,txt)
    doc.core_properties.title='DubraSec Security Intelligence '+('Wochenbericht '+week_display if weekly else 'Tagesbericht '+date)
    doc.core_properties.author='DubraSec'
    doc.save(docx)
    font='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
    bold='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
    pdfmetrics.registerFont(TTFont('DS',font));pdfmetrics.registerFont(TTFont('DSB',bold))
    sty={
      'title':ParagraphStyle('Title',fontName='DSB',fontSize=17,leading=23,textColor=HexColor(NAVY),spaceAfter=12),
      'heading':ParagraphStyle('Heading',fontName='DSB',fontSize=12,leading=17,textColor=HexColor(NAVY),spaceBefore=13,spaceAfter=8,keepWithNext=True),
      'subheading':ParagraphStyle('Sub',fontName='DSB',fontSize=10,leading=14,textColor=HexColor(NAVY),spaceBefore=9,spaceAfter=5,keepWithNext=True),
      'body':ParagraphStyle('Body',fontName='DS',fontSize=8.6,leading=13,textColor=HexColor(INK),spaceAfter=5,wordWrap='CJK')
    }
    flow=[]
    for kind,txt in chunks:
        if weekly and kind=='heading' and txt.startswith('A. Kritische'):flow.append(PageBreak())
        flow.append(Paragraph(pdf_linkified(txt),sty[kind]))
    def page(c,d):
        c.saveState();w,h=A4;c.setStrokeColor(HexColor(TEAL));c.line(19*mm,h-18*mm,w-19*mm,h-18*mm)
        c.setFont('DS',7);c.setFillColor(HexColor(MUTED))
        c.drawString(19*mm,15*mm,'DubraSec · Security Intelligence · '+('KW 43/2026' if weekly else date))
        c.drawRightString(w-19*mm,15*mm,'Seite '+str(d.page));c.restoreState()
    SimpleDocTemplate(str(pdf),pagesize=A4,leftMargin=19*mm,rightMargin=19*mm,topMargin=23*mm,bottomMargin=22*mm,title='DubraSec '+('Wochenbericht '+week_display if weekly else 'Tagesbericht '+date)).build(flow,onFirstPage=page,onLaterPages=page)
    print('generated',docx,pdf)
if __name__=='__main__':
    if len(sys.argv)>1: files=[Path(x) for x in sys.argv[1:]]
    else: files=sorted(Path('Tagesberichte').glob('????-??-??_Security_Intelligence.md'))[-1:]
    for f in files:build(f)
