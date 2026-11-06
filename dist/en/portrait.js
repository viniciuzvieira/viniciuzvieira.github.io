'use strict';
(()=>{
 const canvas=document.querySelector('#portrait-canvas'),ctx=canvas.getContext('2d'),host=canvas.parentElement,img=new Image();
 const source=document.createElement('canvas'),gray=document.createElement('canvas'),dots=document.createElement('canvas');
 const sctx=source.getContext('2d',{willReadFrequently:true}),gctx=gray.getContext('2d'),dctx=dots.getContext('2d');
 const preference=matchMedia('(prefers-reduced-motion: reduce)'),button=document.querySelector('#motion');
 let width=320,height=430,hover=null,paused=preference.matches,time=0,last=0,ready=false;
 const duration=3200,secondStart=3600,secondEnd=6800;
 function resize(){
  width=Math.max(1,host.clientWidth);height=Math.max(1,host.clientHeight);canvas.width=width*2;canvas.height=height*2;ctx.setTransform(2,0,0,2,0,0);
  source.width=gray.width=dots.width=Math.ceil(width*2);source.height=gray.height=dots.height=Math.ceil(height*2);
  const scale=Math.min(source.width/850,(source.height-16)/1120),w=850*scale,h=1120*scale;
  sctx.clearRect(0,0,source.width,source.height);sctx.imageSmoothingQuality='high';sctx.drawImage(img,160,0,850,1120,(source.width-w)/2,source.height-h,w,h);
  const frame=sctx.getImageData(0,0,source.width,source.height),pixels=frame.data;dctx.clearRect(0,0,dots.width,dots.height);dctx.fillStyle='#222629';
  for(let y=2;y<dots.height;y+=7)for(let x=2;x<dots.width;x+=7){const i=(y*dots.width+x)*4;if(pixels[i+3]<60)continue;const luminance=(pixels[i]*.2126+pixels[i+1]*.7152+pixels[i+2]*.0722)/255;dctx.beginPath();dctx.arc(x,y,(1-luminance)*3.1+.3,0,Math.PI*2);dctx.fill();}
  dctx.globalCompositeOperation='destination-in';dctx.drawImage(source,0,0);dctx.globalCompositeOperation='source-over';
  for(let i=0;i<pixels.length;i+=4){const l=pixels[i]*.2126+pixels[i+1]*.7152+pixels[i+2]*.0722;pixels[i]=pixels[i+1]=pixels[i+2]=l;}gctx.putImageData(frame,0,0);draw();
 }
 function paint(layer,from=0,to=height){if(to<=from)return;ctx.save();ctx.beginPath();ctx.rect(0,from,width,to-from);ctx.clip();ctx.clearRect(0,from,width,to-from);ctx.drawImage(layer,0,0,width,height);ctx.restore();}
 function draw(){
  if(!ready)return;ctx.clearRect(0,0,width,height);const t=preference.matches?secondEnd+1:time;let y=null;
  if(t<duration){paint(dots);y=height*t/duration;paint(gray,0,y);}
  else if(t<secondStart)paint(gray);
  else if(t<secondEnd){paint(gray);y=height*(t-secondStart)/duration;paint(source,0,y);}
  else{paint(source);if(!preference.matches){y=((t-secondEnd)%6500)/6500*(height+65)-30;paint(dots,Math.max(0,y-24),Math.min(height,y));}}
  canvas.dataset.phase=t<duration?'halftone-to-monochrome':t<secondStart?'monochrome':t<secondEnd?'monochrome-to-color':'color';
  if(y!==null&&y>=0&&y<=height){ctx.strokeStyle='#0b514b';ctx.lineWidth=.9;ctx.beginPath();ctx.moveTo(0,y);ctx.lineTo(width,y);ctx.stroke();if(y<height-15){ctx.fillStyle='#0b514b';ctx.font='8px monospace';ctx.fillText(t<secondStart?"SCAN 01 · B&W":t<secondEnd?"SCAN 02 · COLOR":"SCAN",4,y+12);}}
  if(hover){const{x,y}=hover,r=38,zoom=1.8;ctx.save();ctx.beginPath();ctx.arc(x,y,r,0,Math.PI*2);ctx.clip();ctx.fillStyle='#f7f4ec';ctx.fillRect(x-r,y-r,r*2,r*2);ctx.drawImage(dots,x*(1-zoom),y*(1-zoom),width*zoom,height*zoom);ctx.restore();ctx.strokeStyle='#292d2d';ctx.lineWidth=1;ctx.beginPath();ctx.arc(x,y,r,0,Math.PI*2);ctx.stroke();ctx.strokeStyle='#0b514b';for(const[dx,dy]of[[-1,0],[1,0],[0,-1],[0,1]]){ctx.beginPath();ctx.moveTo(x+dx*r,y+dy*r);ctx.lineTo(x+dx*(r+6),y+dy*(r+6));ctx.stroke();}ctx.fillStyle='#0b514b';ctx.font='8px monospace';ctx.fillText('DET. A',Math.min(width-39,x+r+8),Math.max(9,y-r));}
 }
 function frame(now){if(!last)last=now;if(!paused&&!document.hidden)time+=Math.min(now-last,60);last=now;draw();requestAnimationFrame(frame);}
 host.addEventListener('pointermove',e=>{if(e.pointerType==='touch')return;const r=canvas.getBoundingClientRect();hover={x:e.clientX-r.left,y:e.clientY-r.top};draw();});host.addEventListener('pointerleave',()=>{hover=null;draw();});
 function sync(){button.setAttribute('aria-pressed',String(paused));button.textContent=paused?"▷ Animate":"Ⅱ Pause";document.querySelectorAll('.wires').forEach(s=>paused?s.pauseAnimations():s.unpauseAnimations());}
 button.addEventListener('click',()=>{paused=!paused;sync();draw();});preference.addEventListener('change',e=>{paused=e.matches;sync();draw();});
 img.onload=()=>{ready=true;resize();new ResizeObserver(resize).observe(host);sync();requestAnimationFrame(frame);};img.src='../assets/vinicius-transparent.png';
})();
