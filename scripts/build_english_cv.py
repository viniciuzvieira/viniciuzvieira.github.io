from pathlib import Path
import runpy,tokenize,io,ast
base=Path(__file__).resolve().parent
lang=runpy.run_path(str(base/'build_english.py'))
pairs=lang['pairs'].copy()
more='''
CURRÍCULO / ENGENHARIA DE SOFTWARE|RESUME / SOFTWARE ENGINEERING
Visite viniciuzvieira.github.io|Visit viniciuzvieira.github.io
28 anos · Casado|28 years old · Married
CONTATO|CONTACT
COMPETÊNCIAS|SKILLS
IDIOMA|LANGUAGE
Inglês avançado|Advanced English
PERFIL|PROFILE
EXPERIÊNCIA|EXPERIENCE
FORMAÇÃO|EDUCATION
CERTIFICAÇÕES & CURSOS|CERTIFICATIONS & COURSES
DA ESPECIFICAÇÃO À ENTREGA.|FROM SPECIFICATION TO DELIVERY.
IA aplicada|Applied AI
Microsoft Azure desde 2019 · AZ-900. AWS: Lambda, S3 e SQS.|Microsoft Azure since 2019 · AZ-900. AWS: Lambda, S3 and SQS.
Claude Code e Codex · SDD · OpenSpec · proposal, delta specs, design, tasks, verify e archive.|Claude Code and Codex · SDD · OpenSpec · proposals, delta specs, design, tasks, verify and archive.
Trajetória em tecnologia desde 2016. Atuação fullstack na Reply Brasil desde 2019, conectando APIs .NET e NestJS, interfaces e dados. Azure desde 2019 e experiência com AWS: Lambda, S3 e SQS. Experiência em arquitetura orientada a eventos, Kafka e webhooks. Desenvolvimento com IA guiado por especificações, revisão e critérios de aceitação.|Working in technology since 2016 and in fullstack development at Reply Brasil since 2019, connecting .NET and NestJS APIs, interfaces and data. Azure experience since 2019 and AWS experience with Lambda, S3 and SQS. Event-driven architecture, Kafka and webhooks. Specification-guided AI-assisted development, code review and acceptance criteria.
Desenvolvedor Sênior / Fullstack|Senior Fullstack Developer
REPLY · JAN. 2022 - ATUAL|REPLY · JAN. 2022 - PRESENT
APIs e serviços .NET e Node.js integrados a React, Vue.js e Nuxt. Interfaces React com hooks. Arquitetura orientada a eventos com Kafka e webhooks. Claude Code e Codex com OpenSpec e SDD para especificação, implementação, revisão e validação.|.NET and Node.js APIs and services integrated with React, Vue.js and Nuxt. React interfaces with hooks. Event-driven architecture with Kafka and webhooks. Claude Code and Codex with OpenSpec and SDD for specification, implementation, review and validation.
APIs .NET, evolução de aplicações para serviços integráveis e integração com a API do Google Drive. Azure e bancos relacionais e não relacionais.|.NET APIs, evolving applications into services and integrating with the Google Drive API. Azure and relational and non-relational databases.
Consultas, procedures, funções, views e rotinas de processamento no SQL Server. Análise e rastreamento de consultas.|SQL Server queries, stored procedures, functions, views and processing routines. Query analysis and tracing.
Criação de tabelas, relacionamentos e consultas SQL.|Creating tables, relationships and SQL queries.
Tecnólogo · Centro Universitário Senac · conclusão em 2019.|Undergraduate technology degree · Centro Universitário Senac · completed in 2019.
curso preparatório|preparatory course
Modelagem dimensional|Dimensional modeling
ABR. 2017|APR. 2017
SET. 2016|SEP. 2016
'''
pairs.update(line.split('|',1) for line in more.strip().splitlines())
import re
pattern=re.compile('|'.join(re.escape(k) for k in sorted(pairs,key=len,reverse=True)))
def tr(s):return pattern.sub(lambda m:pairs[m.group()],s)
s=(base/'design_cv.py').read_text(encoding='utf-8')
tokens=[]
for t in tokenize.generate_tokens(io.StringIO(s).readline):
 if t.type==tokenize.STRING and not t.string.lower().startswith('f'):
  try:
   value=ast.literal_eval(t.string)
   if isinstance(value,str):
    value=tr(value).replace('Vinicius_Vieira_CV.pdf','Vinicius_Vieira_CV_EN.pdf').replace('https://viniciuzvieira.github.io/','https://viniciuzvieira.github.io/?lang=en')
    t=t._replace(string=repr(value))
  except (ValueError,SyntaxError):pass
 tokens.append(t)
s=tokenize.untokenize(tokens)
s=s.replace(')-22',')-18').replace(')-14',')-11')
(base/'design_cv_en.py').write_text(s,encoding='utf-8')
runpy.run_path(str(base/'design_cv_en.py'),run_name='__main__')
