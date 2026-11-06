from pathlib import Path
import re,json,ast
root=Path(__file__).resolve().parent.parent
pairs={}
def add(lines):
 for line in lines.strip().splitlines():
  a,b=line.split('|',1);pairs[a]=b
add('''
Pular para o conteúdo|Skip to content
Desenvolvedor Fullstack Sênior|Senior Fullstack Developer
Desenvolvedor Sênior|Senior Developer
Vinícius Vieira, início|Vinícius Vieira, home
Navegação principal|Main navigation
Fit com a vaga|Job fit
Experiência|Experience
Na prática|In practice
IA Aplicada|Applied AI
Certificados|Credentials
Contato|Contact
Baixar CV|Download CV
Abrir menu|Open menu
Fechar menu|Close menu
SÃO PAULO, BRASIL|SÃO PAULO, BRAZIL
NA REPLY BRASIL DESDE 2019|AT REPLY BRASIL SINCE 2019
Da API à interface, conecto sistemas com .NET, NestJS, React e Vue. Atuo com Azure desde 2019, com certificação AZ-900, e tenho experiência com AWS, incluindo Lambda, S3 e SQS. Arquitetura orientada a eventos com Kafka, webhooks e desenvolvimento assistido por IA, guiado por especificações.|From APIs to user interfaces, I connect systems with .NET, NestJS, React and Vue. I have worked with Azure since 2019, hold the AZ-900 certification, and have experience with AWS Lambda, S3 and SQS. My work includes event-driven architecture with Kafka, webhooks, and specification-guided AI-assisted development.
Explorar fit com a vaga|Explore job fit
E-mail|Email
Retrato de Vinícius conectado às suas áreas de atuação|Vinícius connected to his areas of expertise
O desenvolvedor Fullstack e suas conexões|The Fullstack developer and his connections
ESQUEMÁTICO|SCHEMATIC
Retrato transparente de Vinícius Vieira com varredura animada e lupa em meio-tom|Transparent portrait of Vinícius Vieira with animated scanning and a halftone magnifier
contexto · implementação · revisão|context · implementation · review
Eventos & integrações|Events & integrations
Apps commitados|Apps committed
Mais de 60 apps commitados|More than 60 apps committed
DESDE 2016 · ENGENHARIA DE SOFTWARE|SINCE 2016 · SOFTWARE ENGINEERING
Fig. 01 · transparência, varredura e fluxos ilustrativos|Fig. 01 · transparency, scanning and illustrative flows
Pausar|Pause
início da trajetória|start of my journey
em tecnologia|in technology
backend, interface|backend, interfaces
e dados|and data
Eventos|Events
Kafka e webhooks|Kafka and webhooks
em integrações|in integrations
SDD + IA|SDD + AI
especificação como|specifications as
ponto de partida|the starting point
01 · PARA RECRUTADORES|01 · FOR RECRUITERS
Sua próxima contratação|Your next hire
começa com uma boa conexão.|starts with a good connection.
Edite o rascunho e acompanhe a aderência em tempo real: nota ponderada, nível por requisito, evidências e pontos para conversar.|Edit the draft to see the fit update in real time: weighted score, coverage per requirement, evidence and discussion points.
DESCRIÇÃO DA VAGA|JOB DESCRIPTION
Usar exemplo|Use example
Ex.: Desenvolvedor sênior com .NET, React, APIs REST, Kafka e experiência com IA…|E.g. Senior developer with .NET, React, REST APIs, Kafka and AI experience…
Analisar aderência|Analyze fit
Comparação local por palavras-chave e evidências declaradas. A nota mede cobertura dos requisitos reconhecidos e apoia a entrevista técnica.|Local comparison based on keywords and declared evidence. The score measures coverage of recognized requirements and supports the technical interview.
CURRÍCULO EM CONTEXTO|RESUME IN CONTEXT
Vamos encontrar|Let's find
os pontos de encontro.|the connections.
Backend, frontend, integrações, dados e desenvolvimento com IA. Uma leitura objetiva do que combina com sua vaga.|Backend, frontend, integrations, data and AI-assisted development. A clear view of how my profile matches your role.
02 · EXPERIÊNCIA|02 · EXPERIENCE
Uma trajetória que conecta|A journey connecting
dados, serviços e pessoas.|data, services and people.
Da base em SQL ao desenvolvimento full stack. Evolução contínua, colaboração com o time e atenção a cada camada da aplicação.|From SQL foundations to fullstack development. Continuous growth, teamwork and attention to every application layer.
2022 — ATUAL|2022 — PRESENT
APIs e serviços com .NET e Node.js, interfaces com React, Vue.js e Nuxt. Integração de sistemas com arquitetura orientada a eventos, Kafka e webhooks. Desenvolvimento assistido por IA com Claude Code e Codex e SDD.|APIs and services with .NET and Node.js; interfaces with React, Vue.js and Nuxt. System integration using event-driven architecture, Kafka and webhooks. AI-assisted development with Claude Code and Codex and SDD.
Claude Code e Codex|Claude Code and Codex
Desenvolvedor Júnior|Junior Developer
Desenvolvimento de APIs .NET e evolução de aplicações para serviços integráveis. Integração com a API do Google Drive, atuação com Azure e bancos relacionais e não relacionais.|Developing .NET APIs and evolving applications into services that integrate with other systems. Google Drive API integration, Azure, and relational and non-relational databases.
Desenvolvedor Backend|Backend Developer
Desenvolvimento de consultas, procedures, funções, views e rotinas de processamento no SQL Server. Análise e rastreamento de consultas para apoiar as aplicações.|Developing SQL Server queries, stored procedures, functions, views and processing routines. Query analysis and tracing to support applications.
Modelagem de dados|Data modeling
Estagiário|Intern
Início da trajetória com criação de tabelas, relacionamentos e desenvolvimento de consultas SQL.|Started my career creating tables, relationships and SQL queries.
Ver trajetória no LinkedIn|View career on LinkedIn
03 · NA PRÁTICA|03 · IN PRACTICE
Visão de ponta a ponta.|An end-to-end perspective.
Cuidado em cada conexão.|Care in every connection.
As frentes em que aplico minha experiência, do contrato de uma API à interação com quem usa o produto.|Where I apply my experience, from API contracts to interactions with the people using the product.
Serviços que se integram.|Services that work together.
Desenvolvimento de APIs .NET e Node.js, integração entre aplicações e acesso a dados relacionais e não relacionais.|Developing .NET and Node.js APIs, integrating applications, and accessing relational and non-relational data.
Aplicação, API e dados|Application, API and data
Aplicação|Application
Dados|Data
02 / EVENTOS|02 / EVENTS
Conexões além da requisição.|Connections beyond the request.
Arquitetura orientada a eventos, mensageria com Kafka e webhooks para conectar fluxos entre sistemas.|Event-driven architecture, Kafka messaging and webhooks to connect workflows across systems.
Evento, Kafka e serviço|Event, Kafka and service
Evento|Event
Serviço|Service
Interfaces para o dia a dia.|Interfaces for everyday use.
Aplicações com React e hooks, Vue.js, Nuxt e Angular, conectadas aos serviços e às necessidades do produto.|Applications built with React and hooks, Vue.js, Nuxt and Angular, connected to services and product needs.
Interface, estado e API|Interface, state and API
Estado|State
04 · IA APLICADA AO DESENVOLVIMENTO|04 · AI APPLIED TO DEVELOPMENT
Antes do código,|Before the code,
uma boa especificação.|a good specification.
Uso SDD —|I use SDD —
— com OpenSpec para estruturar mudanças: proposal, delta specs, design e tasks. Claude Code e Codex trabalham com contexto versionado, requisitos verificáveis e critérios de aceitação.|— with OpenSpec to structure changes: proposals, delta specs, design and tasks. Claude Code and Codex work with versioned context, verifiable requirements and acceptance criteria.
Ao dividir o trabalho em tarefas e carregar apenas as especificações relevantes, consigo manter o contexto focado e evitar repetir instruções extensas. Isso pode reduzir o consumo de tokens e as idas e vindas com a IA. Decisões registradas e critérios de aceitação claros também ajudam a reduzir retrabalho, retomar sessões e revisar se a implementação atende ao que foi definido.|Breaking work into tasks and loading only relevant specifications helps me keep context focused and avoid repeating lengthy instructions. This can reduce token usage and back-and-forth with AI. Recorded decisions and clear acceptance criteria also help reduce rework, resume sessions and check that the implementation meets the agreed requirements.
Revisão de código|Code review
Validação|Validation
FLUXO DE TRABALHO|WORKFLOW
Especificar|Specify
OpenSpec: proposal define escopo e motivação; delta specs descrevem requisitos e cenários de aceitação.|OpenSpec: proposals define scope and motivation; delta specs describe requirements and acceptance scenarios.
Implementar com contexto|Implement with context
Design registra decisões técnicas; tasks decompõem a implementação para Claude Code e Codex, mantendo rastreabilidade com a especificação.|Design records technical decisions; tasks break down implementation for Claude Code and Codex while maintaining traceability to the specification.
Revisar e validar|Review and validate
Verificar implementação, testes e cenários; sincronizar as mudanças com as specs e arquivar a proposta concluída.|Verify implementation, tests and scenarios; synchronize changes with the specs and archive the completed proposal.
05 · CERTIFICAÇÃO & FORMAÇÃO|05 · CREDENTIALS & EDUCATION
Aprendizado contínuo.|Continuous learning.
Com evidências para conferir.|With evidence to explore.
Uma certificação Microsoft, cursos em cloud, IA e dados, e minha graduação. Abra cada comprovante para ver a imagem e acessar a fonte.|A Microsoft certification, courses in cloud, AI and data, and my degree. Open each credential to view the image and its source.
Filtrar certificados|Filter credentials
Todos|All
Inteligência artificial|Artificial intelligence
Dados & .NET|Data & .NET
Graduação|Degree
Os documentos identificam o tipo de credencial e sua data de emissão. O comprovante da graduação está disponível com os identificadores pessoais omitidos.|Documents identify the credential type and issue date. The degree certificate is available with personal identifiers redacted.
CAIXA DE FERRAMENTAS|TOOLBOX
Backend & integrações|Backend & integrations
Dados & cloud|Data & cloud
IA no desenvolvimento|AI in development
Claude Code e Codex · SDD · OpenSpec · Especificações · Revisão e validação|Claude Code and Codex · SDD · OpenSpec · Specifications · Review and validation
06 · CONHEÇA MEU PERFIL|06 · GET TO KNOW ME
Um pouco mais,|A little more,
antes da conversa.|before we talk.
Respostas rápidas sobre minha experiência e meu jeito de desenvolver software.|Quick answers about my experience and how I develop software.
Como você se apresenta em 30 segundos?|How do you introduce yourself in 30 seconds?
Sou Vinícius, desenvolvedor sênior full stack em São Paulo. Minha trajetória começou com dados e evoluiu para APIs .NET, interfaces React e Vue e integrações. Também trabalho com Kafka, webhooks e desenvolvimento assistido por IA com Claude Code e Codex e SDD.|I'm Vinícius, a senior fullstack developer based in São Paulo. My career began in data and evolved into .NET APIs, React and Vue interfaces, and integrations. I also work with Kafka, webhooks and AI-assisted development using Claude Code and Codex and SDD.
Onde entram Kafka e webhooks?|Where do Kafka and webhooks fit in?
Na integração entre sistemas: Kafka para mensageria e fluxos orientados a eventos; webhooks para comunicar acontecimentos entre aplicações. São competências que complementam minha atuação com APIs e serviços.|In system integration: Kafka for messaging and event-driven workflows; webhooks to communicate events between applications. These skills complement my work with APIs and services.
Como você usa IA no desenvolvimento?|How do you use AI in development?
Com Claude Code e Codex, SDD e OpenSpec: parto de proposal, specs, design e tasks, descrevo cenários e critérios de aceitação e uso a IA como apoio à implementação. A revisão do código e a validação do comportamento fazem parte do processo.|With Claude Code and Codex, SDD and OpenSpec: I start with proposals, specs, design and tasks, define scenarios and acceptance criteria, and use AI to support implementation. Code review and behavior validation are part of the process.
Qual é sua formação e seu nível de inglês?|What is your education and English level?
Sou formado em Análise e Desenvolvimento de Sistemas pelo Centro Universitário Senac, com conclusão em 2019. Tenho inglês avançado. Minha certificação Azure e os comprovantes de cursos estão disponíveis nesta página.|I hold a degree in Systems Analysis and Development from Centro Universitário Senac, completed in 2019. I have advanced English proficiency. My Azure certification and course credentials are available on this page.
07 · VAMOS CONVERSAR|07 · LET'S TALK
Seu próximo desafio.|Your next challenge.
Uma nova conexão.|A new connection.
Vamos conversar sobre desenvolvimento, integrações e soluções que fazem sentido para o seu time.|Let's talk about development, integrations and solutions that make sense for your team.
CURRÍCULO|RESUME
Baixar CV em PDF|Download CV as PDF
São Paulo, Brasil · Da especificação à entrega.|São Paulo, Brazil · From specification to delivery.
Voltar ao topo|Back to top
Fechar certificado|Close credential
Abrir comprovante na fonte|Open original credential
''')
add('''
Certificação profissional|Professional certification
Curso · 80 horas|Course · 80 hours
Curso com certificado verificado|Course with a verified certificate
Curso preparatório · 46 horas|Preparatory course · 46 hours
Workshop · 6 horas|Workshop · 6 hours
Graduação · Tecnólogo|Undergraduate technology degree
Inteligência Artificial e Computacional|Artificial and Computational Intelligence
Análise e Desenvolvimento de Sistemas|Systems Analysis and Development
Desmistificando a modelagem dimensional|Demystifying dimensional modeling
Microsoft Certified · AZ-900. Fundamentos de serviços, arquitetura e recursos do Microsoft Azure.|Microsoft Certified · AZ-900. Microsoft Azure services, architecture and resource fundamentals.
Nano Course de Inteligência Artificial e Computacional. Concluído em 4 de janeiro de 2022.|Artificial and Computational Intelligence Nano Course. Completed on January 4, 2022.
DEV258x · Curso Microsoft na edX. Certificado emitido em 21 de junho de 2018.|DEV258x · Microsoft course on edX. Certificate issued on June 21, 2018.
AWS Certified 2021 – 4 Certifications! Conclusão de curso preparatório na Udemy, em 21 de dezembro de 2021.|AWS Certified 2021 – 4 Certifications! Preparatory course completed on Udemy on December 21, 2021.
Workshop online ministrado por Luiz Filipe Santos. Declaração de participação emitida em dezembro de 2021.|Online workshop taught by Luiz Filipe Santos. Participation statement issued in December 2021.
Conclusão no 1º semestre de 2019. Colação de grau em 22 de outubro de 2019. Cópia do certificado com identificadores pessoais omitidos.|Completed in the first half of 2019. Degree conferred on October 22, 2019. Certificate copy with personal identifiers redacted.
Ampliar comprovante:|Enlarge credential:
Comprovante de ${c.title} de Vinícius Vieira da Silva|Credential for ${c.title} held by Vinícius Vieira da Silva
Abrir certificado da graduação|Open degree certificate
Conferir na fonte|View original source
DEZ. 2021|DEC. 2021
Animar|Animate
VARREDURA|SCAN
COR|COLOR
P&B|B&W
Atuação com Azure desde 2019 e certificação Microsoft Certified: Azure Fundamentals (AZ-900).|Working with Azure since 2019; Microsoft Certified: Azure Fundamentals (AZ-900).
Desenvolvimento de APIs e serviços .NET na Reply desde 2019.|Developing .NET APIs and services at Reply since 2019.
Interfaces React e uso de hooks na atuação full stack.|React interfaces and hooks in fullstack development.
Desenvolvimento de interfaces Vue.js e Nuxt.|Developing Vue.js and Nuxt interfaces.
Desenvolvimento backend com Node.js na atuação sênior.|Backend development with Node.js in my senior role.
NestJS declarado no conjunto de competências; profundidade a confirmar em conversa técnica.|NestJS is a declared skill; depth to be discussed in a technical interview.
Desenvolvimento e integração de APIs e serviços entre aplicações.|Developing and integrating APIs and services across applications.
Experiência declarada em arquitetura orientada a eventos e mensageria com Kafka.|Declared experience in event-driven architecture and Kafka messaging.
Desenvolvimento de webhooks para integração de sistemas.|Developing webhooks for system integration.
Trajetória com SQL Server desde 2016 e experiência com PostgreSQL e Oracle.|Working with SQL Server since 2016, with PostgreSQL and Oracle experience.
Uso de Claude Code e Codex no desenvolvimento orientado por especificações, com revisão e validação.|Using Claude Code and Codex for specification-driven development, including review and validation.
OpenSpec: proposal, delta specs, design, tasks e verificação dos cenários de aceitação.|OpenSpec: proposals, delta specs, design, tasks and acceptance scenario verification.
Angular integra a experiência frontend declarada.|Angular is part of my declared frontend experience.
Inglês avançado declarado no currículo.|Advanced English proficiency declared in the resume.
Experiência declarada com AWS: Lambda, S3 e SQS. Curso preparatório comprovado; escopo de uso a detalhar em entrevista.|Declared AWS experience: Lambda, S3 and SQS. Preparatory course documented; scope of use to be discussed in an interview.
Sem evidência detalhada no currículo atual; confirmar em entrevista.|No detailed evidence in the current resume; confirm in an interview.
Curso preparatório de AWS comprovado; atuação em produção a confirmar.|Documented AWS preparatory course; production experience to be confirmed.
Integrações|Integrations
Kafka / Eventos|Kafka / Events
SQL / Dados|SQL / Data
IA & SDD|AI & SDD
Inglês|English
Comunicação|Communication
Liderança formal|Formal leadership
AWS em produção|AWS in production
Alta|High
Média|Medium
A confirmar|To confirm
Inclua requisitos ou tecnologias na descrição para visualizar a aderência.|Enter requirements or technologies in the description to see the fit.
Aguardando requisitos reconhecidos.|Waiting for recognized requirements.
Aderência estimada: ${score} de 100|Estimated fit: ${score} out of 100
● ADERÊNCIA ESTIMADA|● ESTIMATED FIT
Bom alinhamento para uma conversa técnica|Good alignment for a technical conversation
Alinhamento parcial com a vaga|Partial alignment with the role
Explorar os requisitos em entrevista|Explore the requirements in an interview
EVIDÊNCIA ALTA EM ${high} DE ${results.length} REQUISITOS|HIGH CONFIDENCE IN ${high} OF ${results.length} REQUIREMENTS
Destaques:|Highlights:
COBERTURA POR ÁREA|COVERAGE BY AREA
Requisito|Requirement
Nível|Level
Evidência|Evidence
Confiança|Confidence
DESEJÁVEL|DESIRABLE
REQUISITO|REQUIREMENT
PESO|WEIGHT
% de cobertura estimada|% estimated coverage
Domínio|Expertise
Forte|Strong
Parcial|Partial
Ver evidência|View evidence
Nota = média ponderada da cobertura declarada. Azure recebe peso 3 por atuação desde 2019 e certificação; .NET, REST e Kafka recebem peso 2. Requisitos desejáveis têm metade do peso. Outros requisitos não reconhecidos precisam de avaliação humana.|Score = weighted average of declared coverage. Azure has weight 3 for experience since 2019 and certification; .NET, REST and Kafka have weight 2. Desirable requirements carry half the weight. Unrecognized requirements need human assessment.
requisitos reconhecidos|recognized requirements
principais|core
desejáveis|desirable
Comparados com experiência e comprovantes|Compared with experience and credentials
Nota ponderada atualizada em tempo real|Weighted score updated in real time
Desenvolvedor Sênior Full Stack com foco em Azure|Senior Fullstack Developer focused on Azure
Buscamos experiência em Microsoft Azure, C# e .NET, APIs REST, React ou Vue e SQL Server. Integrações orientadas a eventos com Kafka e webhooks. Desenvolvimento com IA usando Claude Code e Codex, SDD e OpenSpec.|We are looking for experience with Microsoft Azure, C# and .NET, REST APIs, React or Vue and SQL Server. Event-driven integrations with Kafka and webhooks. AI-assisted development using Claude Code and Codex, SDD and OpenSpec.
Desejável: Kubernetes em produção.|Desirable: Kubernetes in production.
''')
pattern=re.compile('|'.join(re.escape(k) for k in sorted(pairs,key=len,reverse=True)))
def translate(s):return pattern.sub(lambda m:pairs[m.group()],s)
p=root/'dist/index.html';pt=p.read_text(encoding='utf-8')
if 'language-switch' not in pt:
 pt=pt.replace('<a class="button dark header-cv"','<div class="language-switch" role="group" aria-label="Idioma"><a href="?lang=pt" lang="pt-BR" aria-current="true">PT</a><a href="en/?lang=en" lang="en" aria-label="Switch to English">EN</a></div>\n  <a class="button dark header-cv"',1)
 pt=pt.replace('<meta charset="UTF-8">','<meta charset="UTF-8">\n  <script>if(new URLSearchParams(location.search).get("lang")==="en")location.replace("en/"+location.search+location.hash);</script>',1)
 p.write_text(pt,encoding='utf-8')
en=translate(pt).replace('lang="pt-BR"','lang="en"',1)
en=re.sub(r'  <script>if\(new URLSearchParams.*?</script>\n','',en)
en=en.replace('href="?lang=pt" lang="pt-BR" aria-current="true"','href="../?lang=pt" lang="pt-BR"').replace('href="en/?lang=en" lang="en"','href="?lang=en" lang="en" aria-current="true"').replace('aria-label="Idioma"','aria-label="Language"')
en=en.replace('Vinicius_Vieira_CV.pdf','Vinicius_Vieira_CV_EN.pdf')
en=en.replace('href="styles.css"','href="../styles.css"').replace('href="assets/','href="../assets/').replace('src="assets/','src="../assets/').replace('href="docs/','href="../docs/').replace('src="orb.js"','src="../orb.js"')
en=en.replace('https://viniciuzvieira.github.io/">','https://viniciuzvieira.github.io/en/">')
en=en.replace('Vinícius Vieira — Senior Developer · .NET · Events · IA','Vinícius Vieira — Senior Fullstack Developer · .NET · Events · AI')
en=en.replace('Vinícius Vieira, desenvolvedor sênior full stack. .NET, React, Vue, arquitetura orientada a eventos, Kafka, webhooks e desenvolvimento com IA e SDD.','Vinícius Vieira, Senior Fullstack Developer. .NET, React, Vue, event-driven architecture, Kafka, webhooks and AI-assisted development with SDD.').replace('Software, integrações e IA orientada por especificações. Conheça minha trajetória e minhas certificações.','Software, integrations and specification-guided AI. Explore my career and credentials.')
(root/'dist/en').mkdir(exist_ok=True)
(root/'dist/en/index.html').write_text(en,encoding='utf-8')
for name in ['app.js','fit.js','portrait.js']:
 s=(root/'dist'/name).read_text(encoding='utf-8')
 # Translate string literals without touching code, regexes, URLs or DOM selectors.
 def literal(m):
  if m.group(1) is not None:
   value=ast.literal_eval(m.group());translated=translate(value)
   return json.dumps(translated,ensure_ascii=False) if translated!=value else m.group()
  return '`'+translate(m.group(2))+'`'
 s=re.sub(r"'((?:\\.|[^'\\])*)'|`((?:\\.|[^`\\])*)`",literal,s)
 s=s.replace("'assets/","'../assets/").replace('"assets/','"../assets/').replace("'docs/","'../docs/").replace('"docs/','"../docs/')
 if name=='fit.js':
  s=s.replace('desejavel|diferencial|opcional|nice.to.have','desejavel|diferencial|opcional|nice.to.have|desirable|preferred|optional')
  s=s.replace('eventos?|event.driven','eventos?|events?|event.driven').replace('especificacoes','especificacoes|specifications').replace('lideranca|tech lead','lideranca|leadership|tech lead')
 (root/'dist/en'/name).write_text(s,encoding='utf-8')
print('English page and dynamic modules generated')
