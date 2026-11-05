'use strict';
const certificates = [
 {id:'azure',category:'cloud',issuer:'MICROSOFT',year:'JUL. 2022',type:'Certificação profissional',title:'Azure Fundamentals',description:'Microsoft Certified · AZ-900. Fundamentos de serviços, arquitetura e recursos do Microsoft Azure.',image:'assets/azure-fundamentals.png',url:'https://www.credly.com/badges/eb3c4c9d-fefa-4d54-8015-ee4c4fc6cfbf'},
 {id:'fiap',category:'ia',issuer:'FIAP',year:'JAN. 2022',type:'Curso · 80 horas',title:'Inteligência Artificial e Computacional',description:'Nano Course de Inteligência Artificial e Computacional. Concluído em 4 de janeiro de 2022.',image:'assets/fiap-ia.png',url:'https://on.fiap.com.br/pluginfile.php/1/local_nanocourses/certificado_nanocourse/36987/65b13cdd8247f8f136aef5a73ac76e29/certificado.png'},
 {id:'edx',category:'dados',issuer:'MICROSOFT / EDX',year:'JUN. 2018',type:'Curso com certificado verificado',title:'Data Access in C# and .NET Core',description:'DEV258x · Curso Microsoft na edX. Certificado emitido em 21 de junho de 2018.',image:'assets/edx-csharp.jpg',url:'https://courses.edx.org/certificates/e2994fd1796e4d0490be2d85a069e93e'},
 {id:'aws',category:'cloud',issuer:'UDEMY / BACKSPACE ACADEMY',year:'DEZ. 2021',type:'Curso preparatório · 46 horas',title:'Amazon Web Services (AWS)',description:'AWS Certified 2021 – 4 Certifications! Conclusão de curso preparatório na Udemy, em 21 de dezembro de 2021.',image:'assets/udemy-aws.jpg',url:'https://www.udemy.com/certificate/UC-dec44fde-0438-456b-8ddf-2f050d90f591/'},
 {id:'ebac',category:'dados',issuer:'EBAC',year:'DEZ. 2021',type:'Workshop · 6 horas',title:'Desmistificando a modelagem dimensional',description:'Workshop online ministrado por Luiz Filipe Santos. Declaração de participação emitida em dezembro de 2021.',image:'assets/ebac-modelagem.png',url:'https://static.lms.ebaconline.com.br/certs/7152c019-4bca-42eb-a20d-1c522cd311ef.pdf'},
 {id:'senac',category:'formacao',issuer:'CENTRO UNIVERSITÁRIO SENAC',year:'2019',type:'Graduação · Tecnólogo',title:'Análise e Desenvolvimento de Sistemas',description:'Conclusão no 1º semestre de 2019. Colação de grau em 22 de outubro de 2019. Cópia do certificado com identificadores pessoais omitidos.',image:'assets/senac-tads.png',url:'docs/senac-tads.pdf'}
];
const grid = document.querySelector('#cert-grid');
certificates.forEach(c=>{
 const article=document.createElement('article');article.className='cert';article.dataset.category=c.category;
 const preview=document.createElement('button');preview.className='cert-preview';preview.type='button';preview.setAttribute('aria-label',`Ampliar comprovante: ${c.title}`);
 const img=document.createElement('img');img.src=c.image;img.alt=`Comprovante de ${c.title} de Vinícius Vieira da Silva`;img.loading='lazy';img.width=1200;img.height=850;
 const zoom=document.createElement('span');zoom.className='zoom-icon';zoom.textContent='↗';zoom.setAttribute('aria-hidden','true');preview.append(img,zoom);preview.addEventListener('click',()=>openCertificate(c));
 const info=document.createElement('div');info.className='cert-info';
 const meta=document.createElement('div');meta.className='cert-meta';const issuer=document.createElement('span');issuer.textContent=c.issuer;const year=document.createElement('span');year.textContent=c.year;meta.append(issuer,year);
 const title=document.createElement('h3');title.textContent=c.title;const desc=document.createElement('p');desc.className='cert-description';desc.textContent=`${c.type}. ${c.description}`;
 const link=document.createElement('a');link.className='cert-link';link.href=c.url;link.target='_blank';link.rel='noopener noreferrer';link.textContent=c.id==='senac'?'Abrir certificado da graduação ↗':'Conferir na fonte ↗';
 info.append(meta,title,desc,link);article.append(preview,info);grid.append(article);
});
const dialog=document.querySelector('#cert-dialog');
function openCertificate(c){document.querySelector('#dialog-title').textContent=c.title;document.querySelector('#dialog-type').textContent=`${c.issuer} · ${c.type}`;document.querySelector('#dialog-image').src=c.image;document.querySelector('#dialog-image').alt=`Comprovante de ${c.title} de Vinícius Vieira da Silva`;document.querySelector('#dialog-description').textContent=c.description;document.querySelector('#dialog-link').href=c.url;dialog.showModal();}
document.querySelector('#close-dialog').addEventListener('click',()=>dialog.close());
dialog.addEventListener('click',e=>{if(e.target===dialog){const r=dialog.getBoundingClientRect();if(e.clientX<r.left||e.clientX>r.right||e.clientY<r.top||e.clientY>r.bottom)dialog.close();}});
document.querySelectorAll('[data-filter]').forEach(button=>button.addEventListener('click',()=>{document.querySelectorAll('[data-filter]').forEach(b=>b.setAttribute('aria-pressed',String(b===button)));document.querySelectorAll('.cert').forEach(c=>c.hidden=button.dataset.filter!=='all'&&c.dataset.category!==button.dataset.filter);}));
const menu=document.querySelector('.menu'),nav=document.querySelector('#nav');
menu.addEventListener('click',()=>{const expanded=menu.getAttribute('aria-expanded')!=='true';menu.setAttribute('aria-expanded',String(expanded));menu.setAttribute('aria-label',expanded?'Fechar menu':'Abrir menu');nav.classList.toggle('open',expanded);});
nav.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>{nav.classList.remove('open');menu.setAttribute('aria-expanded','false');menu.setAttribute('aria-label','Abrir menu');}));
document.querySelector('.brand').addEventListener('click',()=>{nav.classList.remove('open');menu.setAttribute('aria-expanded','false');menu.setAttribute('aria-label','Abrir menu');});
document.addEventListener('keydown',e=>{if(e.key==='Escape'){nav.classList.remove('open');menu.setAttribute('aria-expanded','false');menu.setAttribute('aria-label','Abrir menu');}});
document.querySelector('#year').textContent=String(new Date().getFullYear());
