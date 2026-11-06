from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from pypdf import PdfReader
root=Path(__file__).resolve().parent.parent
out=root/'outputs/Vinicius_Vieira_CV.pdf'
out.parent.mkdir(exist_ok=True)
for name,file in [('Sans','arial.ttf'),('SansB','arialbd.ttf'),('Serif','georgia.ttf'),('Mono','consola.ttf')]:pdfmetrics.registerFont(TTFont(name,'C:/Windows/Fonts/'+file))
pdfmetrics.registerFontFamily('Sans',normal='Sans',bold='SansB')
ink='#1a1d21';rust='#0b514b';muted='#65655f';paper='#f3efe6'
c=canvas.Canvas(str(out),pagesize=(595.28,841.89));c.setTitle('Vinícius Vieira - Desenvolvedor Fullstack Sênior');c.setAuthor('Vinícius Vieira da Silva')
c.setFillColor(HexColor(paper));c.rect(0,0,596,842,fill=1,stroke=0)
c.setStrokeColor(HexColor('#e6e1d6'));c.setLineWidth(.25)
for x in range(28,570,9):c.line(x,680,x,812)
for y in range(680,813,9):c.line(28,y,567,y)
c.setStrokeColor(HexColor(ink));c.setLineWidth(.6);c.rect(28,680,539,132,fill=0,stroke=1)
def txt(x,y,s,font='Sans',size=9,color=ink):
 c.setFillColor(HexColor(color));c.setFont(font,size);c.drawString(x,y,s)
def para(x,y,w,s,size=9.2,leading=13,color=ink,font='Sans'):
 p=Paragraph(s,ParagraphStyle('p',fontName=font,fontSize=size,leading=leading,textColor=HexColor(color)));_,h=p.wrap(w,800);p.drawOn(c,x,y-h);return y-h

txt(42,791,'CURRÍCULO / ENGENHARIA DE SOFTWARE','Mono',8,rust)
txt(42,753,'Vinícius Vieira','Serif',34)
txt(43,734,'Visite viniciuzvieira.github.io','SansB',11,rust)
c.linkURL('https://viniciuzvieira.github.io/',(42,730,210,746),relative=0,thickness=0)
c.setStrokeColor(HexColor(rust));c.setLineWidth(1.3);c.line(42,724,340,724)
txt(42,704,'Desenvolvedor Fullstack Sênior','SansB',12)
txt(388,788,'SÃO PAULO, BRASIL','Mono',8)
txt(388,774,'REPLY BRASIL / 2019+','Mono',8,rust)
txt(388,760,'28 anos · Casado','Sans',9,ink)
# White sidebar with diagram-inspired rules.
c.setFillColor(HexColor('#ffffff'));c.setStrokeColor(HexColor('#b6b2a8'));c.setLineWidth(.5);c.rect(28,53,177,610,fill=1,stroke=1)
def section(x,y,w,n,title):
 txt(x,y,n+' / '+title,'Mono',8,rust);c.setStrokeColor(HexColor('#b6b2a8'));c.setLineWidth(.4);c.line(x,y-8,x+w,y-8);return y-19
x=40;w=153;y=644
y=section(x,y,w,'01','CONTATO')
for label,url in [('vinicius.silva@zcore.com.br','mailto:vinicius.silva@zcore.com.br'),('LinkedIn / viniciuzvieira','https://www.linkedin.com/in/viniciuzvieira/'),('GitHub / viniciuzvieira','https://github.com/viniciuzvieira'),('viniciuzvieira.github.io','https://viniciuzvieira.github.io/')]:
 y=para(x,y,w,f'<link href="{url}">{label}</link>',8,12)-6
y-=8;y=section(x,y,w,'02','COMPETÊNCIAS')
for title,body in [('Backend','.NET · NestJS · Python · APIs REST'),('Frontend','React · Vue.js · Nuxt · Angular'),('Eventos & integrações','Kafka · Webhooks'),('Dados','SQL Server · PostgreSQL · Oracle · MongoDB · Firebase · Cosmos DB'),('Cloud','Microsoft Azure desde 2019 · AZ-900. AWS: Lambda, S3 e SQS.'),('IA aplicada','Claude Code e Codex · SDD · OpenSpec · proposal, delta specs, design, tasks, verify e archive.')]:
 y=para(x,y,w,title,9,12,font='SansB')-3;y=para(x,y,w,body,8.4,12,color=muted)-13
y=section(x,y,w,'03','IDIOMA');y=para(x,y,w,'Inglês avançado',9,13)
# Main editorial column.
x=224;w=331;y=644
y=section(x,y,w,'04','PERFIL')
y=para(x,y,w,'Trajetória em tecnologia desde 2016. Atuação fullstack na Reply Brasil desde 2019, conectando APIs .NET e NestJS, interfaces e dados. Azure desde 2019 e experiência com AWS: Lambda, S3 e SQS. Experiência em arquitetura orientada a eventos, Kafka e webhooks. Desenvolvimento com IA guiado por especificações, revisão e critérios de aceitação.',9.2,13)-22
y=section(x,y,w,'05','EXPERIÊNCIA')
for title,date,body in [
('Desenvolvedor Sênior / Fullstack','REPLY · JAN. 2022 - ATUAL','APIs e serviços .NET e Node.js integrados a React, Vue.js e Nuxt. Interfaces React com hooks. Arquitetura orientada a eventos com Kafka e webhooks. Claude Code e Codex com OpenSpec e SDD para especificação, implementação, revisão e validação.'),
('Desenvolvedor Júnior','REPLY · MAR. 2019 - JAN. 2022','APIs .NET, evolução de aplicações para serviços integráveis e integração com a API do Google Drive. Azure e bancos relacionais e não relacionais.'),
('Desenvolvedor Backend','INTERPLAYERS · ABR. 2017 - MAR. 2019','Consultas, procedures, funções, views e rotinas de processamento no SQL Server. Análise e rastreamento de consultas.'),
('Estagiário','INTERPLAYERS · SET. 2016 - MAR. 2017','Criação de tabelas, relacionamentos e consultas SQL.')]:
 y=para(x,y,w,title,11,14,font='Serif')-4;y=para(x,y,w,date,7.3,10,color=rust,font='Mono')-5;y=para(x,y,w,body,9,12.7)-14
y=section(x,y,w,'06','FORMAÇÃO')
y=para(x,y,w,'<b>Análise e Desenvolvimento de Sistemas</b><br/>Tecnólogo · Centro Universitário Senac · conclusão em 2019.',9,13)-19
y=section(x,y,w,'07','CERTIFICAÇÕES & CURSOS')
certs=[('Azure Fundamentals / AZ-900 · Microsoft · 2022','https://www.credly.com/badges/eb3c4c9d-fefa-4d54-8015-ee4c4fc6cfbf'),('Inteligência Artificial e Computacional · FIAP · 80h · 2022','https://on.fiap.com.br/pluginfile.php/1/local_nanocourses/certificado_nanocourse/36987/65b13cdd8247f8f136aef5a73ac76e29/certificado.png'),('AWS · Udemy · curso preparatório · 46h · 2021','https://www.udemy.com/certificate/UC-dec44fde-0438-456b-8ddf-2f050d90f591/'),('Modelagem dimensional · EBAC · 6h · 2021','https://static.lms.ebaconline.com.br/certs/7152c019-4bca-42eb-a20d-1c522cd311ef.pdf'),('Data Access in C# and .NET Core · Microsoft / edX · 2018','https://courses.edx.org/certificates/e2994fd1796e4d0490be2d85a069e93e')]
for label,url in certs:y=para(x,y,w,f'<link href="{url}">{label}</link>',8,11.5)-4
assert y>49, y
c.setStrokeColor(HexColor(ink));c.line(28,40,567,40);txt(28,25,'DA ESPECIFICAÇÃO À ENTREGA.','Mono',7,rust);txt(454,25,'VINÍCIUS VIEIRA / 01','Mono',7)
c.save()
(root/'dist/docs/Vinicius_Vieira_CV.pdf').write_bytes(out.read_bytes())
print('PDF:',len(PdfReader(out).pages),'page; final text y:',round(y))
