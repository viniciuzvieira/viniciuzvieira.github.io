'use strict';
// Adapted from the user's CollectionOrbView for a static page.
(()=>{
 const canvas=document.querySelector('#brand-orb'),context=canvas.getContext('2d');if(!context)return;
 const scale=Math.max(3,Math.min(devicePixelRatio||1,4));canvas.width=48*scale;canvas.height=40*scale;context.scale(scale,scale);context.lineCap='round';context.lineWidth=.8;
 const reducedMotion=matchMedia('(prefers-reduced-motion: reduce)'),turn=Math.PI*2,radius=16,tilt=.3;let animation=0,lastFrame=null,angle=.5;
 const point=(latitude,longitude)=>{const x=Math.cos(latitude)*Math.sin(longitude+angle),y=Math.sin(latitude),z=Math.cos(latitude)*Math.cos(longitude+angle);return{x:24+x*radius,y:20+(y*Math.cos(tilt)-z*Math.sin(tilt))*radius,z:z*Math.cos(tilt)+y*Math.sin(tilt)};};
 function draw(){
  context.clearRect(0,0,48,40);context.strokeStyle='rgba(44,100,80,.5)';context.beginPath();context.arc(24,20,radius,0,turn);context.stroke();
  for(let band=1;band<6;band++){const latitude=-Math.PI/2+band*Math.PI/6,r=radius*Math.cos(latitude);context.beginPath();context.ellipse(24,20+radius*Math.sin(latitude)*Math.cos(tilt),r,r*Math.sin(tilt),0,0,turn);context.stroke();}
  for(let meridian=0;meridian<10;meridian++){const longitude=meridian*turn/10,depth=(Math.cos(longitude+angle)+1)/2,opacity=.15+.7*depth*depth*(3-2*depth);context.strokeStyle=meridian===0?`rgba(172,60,23,${opacity})`:`rgba(44,100,80,${opacity})`;context.beginPath();for(let step=0;step<=48;step++){const vertex=point(-Math.PI/2+step*Math.PI/48,longitude);if(!step)context.moveTo(vertex.x,vertex.y);else context.lineTo(vertex.x,vertex.y);}context.stroke();}
  const marker=point(0,0);context.fillStyle=`rgba(172,60,23,${.18+.82*(marker.z+1)/2})`;context.beginPath();context.arc(marker.x,marker.y,1.25,0,turn);context.fill();
 }
 function tick(time){if(lastFrame!==null)angle=(angle+(time-lastFrame)*turn/6000)%turn;lastFrame=time;draw();animation=requestAnimationFrame(tick);}
 function sync(){cancelAnimationFrame(animation);lastFrame=null;draw();if(!reducedMotion.matches&&!document.hidden)animation=requestAnimationFrame(tick);}
 reducedMotion.addEventListener('change',sync);document.addEventListener('visibilitychange',sync);sync();
})();
