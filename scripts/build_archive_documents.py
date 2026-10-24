#!/usr/bin/env python3
"""Generate archive DOCX/PDF from daily Markdown. Uses public-source report content only."""
from pathlib import Path
from datetime import datetime
from xml.sax.saxutils import escape
import re, sys
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
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
    try:datetime.strptime(date,'%Y-%m-%d')
    except ValueError:raise SystemExit('Bad report filename: '+md.name)
    docx=md.with_name('DubraSec_Tagesbericht_'+date+'.docx')
    pdf=md.with_name('DubraSec_Tagesbericht_'+date+'.pdf')
    chunks=read_sections(md)
    doc=Document()
    sec=doc.sections[0]
    sec.top_margin=Cm(2.2);sec.bottom_margin=Cm(2);sec.left_margin=Cm(2.1);sec.right_margin=Cm(2.1)
    normal=doc.styles['Normal'];normal.font.name='Calibri';normal.font.size=Pt(9);normal.font.color.rgb=RGBColor(27,43,64)
    for nm,size,color in [('Title',19,(21,44,73)),('Heading 1',13,(21,44,73)),('Heading 2',11,(21,44,73))]:
        st=doc.styles[nm];st.font.name='Calibri';st.font.size=Pt(size);st.font.color.rgb=RGBColor(*color);st.font.bold=True
    header=sec.header.paragraphs[0];header.text='DUBRASEC  /  SECURITY INTELLIGENCE';header.style='Caption'
    foot=sec.footer.paragraphs[0];foot.text='DubraSec · OSINT · '+date;foot.alignment=WD_ALIGN_PARAGRAPH.CENTER
    for kind,txt in chunks:
        if kind=='title':doc.add_paragraph(txt,style='Title')
        elif kind=='heading':doc.add_paragraph(txt,style='Heading 1')
        elif kind=='subheading':doc.add_paragraph(txt,style='Heading 2')
        else:doc.add_paragraph(txt)
    doc.core_properties.title='DubraSec Security Intelligence Tagesbericht '+date
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
    flow=[Paragraph(escape(txt),sty[kind]) for kind,txt in chunks]
    def page(c,d):
        c.saveState();w,h=A4;c.setStrokeColor(HexColor(TEAL));c.line(19*mm,h-18*mm,w-19*mm,h-18*mm)
        c.setFont('DS',7);c.setFillColor(HexColor(MUTED))
        c.drawString(19*mm,15*mm,'DubraSec · Security Intelligence · '+date)
        c.drawRightString(w-19*mm,15*mm,'Seite '+str(d.page));c.restoreState()
    SimpleDocTemplate(str(pdf),pagesize=A4,leftMargin=19*mm,rightMargin=19*mm,topMargin=23*mm,bottomMargin=22*mm,title='DubraSec Tagesbericht '+date).build(flow,onFirstPage=page,onLaterPages=page)
    print('generated',docx,pdf)
if __name__=='__main__':
    if len(sys.argv)>1: files=[Path(x) for x in sys.argv[1:]]
    else: files=sorted(Path('Tagesberichte').glob('????-??-??_Security_Intelligence.md'))[-1:]
    for f in files:build(f)
