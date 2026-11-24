/* Şevket — ortak davranışlar: üst çubuk, açık/kapalı, görünürken açılma, büyütme, giriş fotoğrafları */
(function(){
var d=document,h=d.documentElement,en=h.lang==='en';
var ust=d.querySelector('.ust');
function kay(){if(ust)ust.classList.toggle('kaydi',window.scrollY>8);}
kay();window.addEventListener('scroll',kay,{passive:true});
/* açık mı: her gün 10.30–23.00, İstanbul saati */
var dm=d.querySelector('[data-durum]');
if(dm){try{var p=new Intl.DateTimeFormat('en-GB',{timeZone:'Europe/Istanbul',hour:'2-digit',minute:'2-digit',hour12:false}).format(new Date()).split(':'),m=(+p[0])*60+(+p[1]),acik=m>=630&&m<1380;
dm.textContent=acik?(en?'Open now':'Şu an açık'):(en?'Closed now':'Şu an kapalı');dm.classList.add(acik?'acik':'kapali');dm.hidden=false;}catch(e){}}
/* görünürken açılma */
var az=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
var ac=d.querySelectorAll('[data-ac]');
if(!az&&'IntersectionObserver' in window){h.classList.add('js-ac');
var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('gorundu');io.unobserve(e.target);}});},{rootMargin:'0px 0px -8% 0px',threshold:.08});
ac.forEach(function(e){io.observe(e);});}
/* giriş fotoğrafları */
var kare=d.querySelectorAll('.giris-foto img');
if(kare.length>1&&!az){var i=0;setInterval(function(){kare[i].classList.remove('on');i=(i+1)%kare.length;kare[i].classList.add('on');},5200);}
/* büyütme */
var liste=[].slice.call(d.querySelectorAll('[data-buyut]')),kutu=d.getElementById('buyut');
if(kutu&&liste.length){var gi=kutu.querySelector('img'),gy=kutu.querySelector('p'),n=0;
function goster(k){n=(k+liste.length)%liste.length;var s=liste[n];gi.src=s.currentSrc||s.src;gi.alt=s.alt;gy.textContent=s.getAttribute('data-buyut')||s.alt;}
liste.forEach(function(s,k){var b=s.closest('button');if(b)b.addEventListener('click',function(){goster(k);kutu.showModal();});});
kutu.querySelector('.kapat').addEventListener('click',function(){kutu.close();});
kutu.querySelector('.once').addEventListener('click',function(){goster(n-1);});
kutu.querySelector('.sonra').addEventListener('click',function(){goster(n+1);});
kutu.addEventListener('click',function(e){if(e.target===kutu)kutu.close();});
kutu.addEventListener('keydown',function(e){if(e.key==='ArrowLeft')goster(n-1);if(e.key==='ArrowRight')goster(n+1);});}
})();
