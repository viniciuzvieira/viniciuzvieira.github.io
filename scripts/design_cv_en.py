from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from pypdf import PdfReader
root=Path(__file__).resolve().parent.parent
out=root/'outputs/Vinicius_Vieira_CV_EN.pdf'
out.parent.mkdir(exist_ok=True)
for name,file in [('Sans','arial.ttf'),('SansB','arialbd.ttf'),('Serif','georgia.ttf'),('Mono','consola.ttf')]:pdfmetrics.registerFont(TTFont(name,'C:/Windows/Fonts/'+file))
pdfmetrics.registerFontFamily('Sans',normal='Sans',bold='SansB')
ink='#1a1d21';rust='#0b514b';muted='#65655f';paper='#f3efe6'
c=canvas.Canvas(str(out),pagesize=(595.28,841.89));c.setTitle('Vinícius Vieira - Senior Fullstack Developer');c.setAuthor('Vinícius Vieira da Silva')
c.setFillColor(HexColor(paper));c.rect(0,0,596,842,fill=1,stroke=0)
c.setStrokeColor(HexColor('#e6e1d6'));c.setLineWidth(.25)
for x in range(28,570,9):c.line(x,680,x,812)
for y in range(680,813,9):c.line(28,y,567,y)
c.setStrokeColor(HexColor(ink));c.setLineWidth(.6);c.rect(28,680,539,132,fill=0,stroke=1)
def txt(x,y,s,font='Sans',size=9,color=ink):
 c.setFillColor(HexColor(color));c.setFont(font,size);c.drawString(x,y,s)
def para(x,y,w,s,size=9.2,leading=13,color=ink,font='Sans'):
 p=Paragraph(s,ParagraphStyle('p',fontName=font,fontSize=size,leading=leading,textColor=HexColor(color)));_,h=p.wrap(w,800);p.drawOn(c,x,y-h);return y-h

txt(42,791,'RESUME / SOFTWARE ENGINEERING','Mono',8,rust)
txt(42,753,'Vinícius Vieira','Serif',34)
txt(43,734,'Visit viniciuzvieira.github.io','SansB',11,rust)
c.linkURL('https://viniciuzvieira.github.io/?lang=en',(42,730,210,746),relative=0,thickness=0)
c.setStrokeColor(HexColor(rust));c.setLineWidth(1.3);c.line(42,724,340,724)
txt(42,704,'Senior Fullstack Developer','SansB',12)
txt(388,788,'SÃO PAULO, BRAZIL','Mono',8)
txt(388,774,'REPLY BRASIL / 2019+','Mono',8,rust)
txt(388,760,'28 years old · Married','Sans',9,ink)
# White sidebar with diagram-inspired rules.
c.setFillColor(HexColor('#ffffff'));c.setStrokeColor(HexColor('#b6b2a8'));c.setLineWidth(.5);c.rect(28,53,177,610,fill=1,stroke=1)
def section(x,y,w,n,title):
 txt(x,y,n+' / '+title,'Mono',8,rust);c.setStrokeColor(HexColor('#b6b2a8'));c.setLineWidth(.4);c.line(x,y-8,x+w,y-8);return y-19
x=40;w=153;y=644
y=section(x,y,w,'01','CONTACT')
for label,url in [('vinicius.silva@zcore.com.br','mailto:vinicius.silva@zcore.com.br'),('LinkedIn / viniciuzvieira','https://www.linkedin.com/in/viniciuzvieira/'),('GitHub / viniciuzvieira','https://github.com/viniciuzvieira'),('viniciuzvieira.github.io','https://viniciuzvieira.github.io/?lang=en')]:
 y=para(x,y,w,f'<link href="{url}">{label}</link>',8,12)-6
y-=8;y=section(x,y,w,'02','SKILLS')
for title,body in [('Backend','PHP (11 years) · .NET · NestJS · Python · APIs REST'),('Frontend','React · Vue.js · Nuxt · Angular'),('Events & integrations','Kafka · Webhooks'),('Data','SQL Server · PostgreSQL · Oracle · MongoDB · Firebase · Cosmos DB'),('Cloud','Microsoft Azure since 2019 · AZ-900. AWS: Lambda, S3 and SQS.'),('Applied AI','Claude Code and Codex · SDD · OpenSpec · proposals, delta specs, design, tasks, verify and archive.')]:
 y=para(x,y,w,title,9,12,font='SansB')-3;y=para(x,y,w,body,8.4,12,color=muted)-13
y=section(x,y,w,'03','LANGUAGE');y=para(x,y,w,'Advanced English',9,13)
# Main editorial column.
x=224;w=331;y=644
y=section(x,y,w,'04','PROFILE')
y=para(x,y,w,'11 years of PHP experience. Fullstack development at Reply Brasil since 2019, building .NET and NestJS APIs and integrating interfaces and data. Azure since 2019, with AZ-900 certification, and AWS Lambda, S3 and SQS. Event-driven architecture with Kafka and webhooks. Specification-guided AI-assisted development, code review and acceptance criteria.',9.2,13)-18
y=section(x,y,w,'05','EXPERIENCE')
for title,date,body in [
('Senior Fullstack Developer','REPLY · JAN. 2022 - PRESENT','.NET and Node.js APIs and services integrated with React, Vue.js and Nuxt. React interfaces with hooks. Event-driven architecture with Kafka and webhooks. Claude Code and Codex with OpenSpec and SDD for specification, implementation, review and validation.'),
('Junior Developer','REPLY · MAR. 2019 - JAN. 2022','.NET APIs, evolving applications into services and integrating with the Google Drive API. Azure and relational and non-relational databases.'),
('Backend Developer','INTERPLAYERS · APR. 2017 - MAR. 2019','SQL Server queries, stored procedures, functions, views and processing routines. Query analysis and tracing.'),
('Intern','INTERPLAYERS · SEP. 2016 - MAR. 2017','Creating tables, relationships and SQL queries.')]:
 y=para(x,y,w,title,11,14,font='Serif')-4;y=para(x,y,w,date,7.3,10,color=rust,font='Mono')-5;y=para(x,y,w,body,9,12.7)-11
y=section(x,y,w,'06','EDUCATION')
y=para(x,y,w,'<b>Systems Analysis and Development</b><br/>Undergraduate technology degree · Centro Universitário Senac · completed in 2019.',9,13)-19
y=section(x,y,w,'07','CERTIFICATIONS & COURSES')
certs=[('Azure Fundamentals / AZ-900 · Microsoft · 2022','https://www.credly.com/badges/eb3c4c9d-fefa-4d54-8015-ee4c4fc6cfbf'),('Artificial and Computational Intelligence · FIAP · 80h · 2022','https://on.fiap.com.br/pluginfile.php/1/local_nanocourses/certificado_nanocourse/36987/65b13cdd8247f8f136aef5a73ac76e29/certificado.png'),('AWS · Udemy · preparatory course · 46h · 2021','https://www.udemy.com/certificate/UC-dec44fde-0438-456b-8ddf-2f050d90f591/'),('Dimensional modeling · EBAC · 6h · 2021','https://static.lms.ebaconline.com.br/certs/7152c019-4bca-42eb-a20d-1c522cd311ef.pdf'),('Data Access in C# and .NET Core · Microsoft / edX · 2018','https://courses.edx.org/certificates/e2994fd1796e4d0490be2d85a069e93e')]
for label,url in certs:y=para(x,y,w,f'<link href="{url}">{label}</link>',8,11.5)-4
assert y>49, y
c.setStrokeColor(HexColor(ink));c.line(28,40,567,40);txt(28,25,'FROM SPECIFICATION TO DELIVERY.','Mono',7,rust);txt(454,25,'VINÍCIUS VIEIRA / 01','Mono',7)
c.save()
(root/'dist/docs/Vinicius_Vieira_CV_EN.pdf').write_bytes(out.read_bytes())
print('PDF:',len(PdfReader(out).pages),'page; final text y:',round(y))
