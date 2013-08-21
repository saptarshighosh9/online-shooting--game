import cgi
from google.appengine.api import users
import webapp2




MAIN_PAGE_FOOTER_TEMPLATE= """\
<!DOCTYPE html>
<html lang="en">
	<head>
	
		<meta charset="utf-8">
		<title>Shooting Game</title>
		
	</head>
	<body bgcolor="#000000">
<script>
var canvas = document.createElement("canvas");
var ctx = canvas.getContext("2d");
canvas.width = 1000;
canvas.height = 550;
document.body.appendChild(canvas);




var bgImage = new Image();
bgImage.src = "http://whistler5on5.com/wp-content/uploads/2012/10/Grass-Stripe1.jpeg";

var heroImage = new Image();
heroImage.src = "images/gb.gif";

var dImage = new Image();
dImage.src = "images/gbb.gif";

var ddImage = new Image();
ddImage.src = "images/gbbb.gif";

var monsterImage = new Image();
monsterImage.src = "images/fire.png";


var mi = new Image();
mi.src = "images/monster.png";

var m ={};
var score=0;
var scrr=0;
var hero = {
	speed: 256 
};
var monster = {};
var d = {};
var monstersCaught = 0;
var p=40;
var keysDown = {};

addEventListener("keydown", function (e) {
	keysDown[e.keyCode] = true;
}, false);

addEventListener("keyup", function (e) {
	delete keysDown[e.keyCode];
}, false);

var reset = function () {
	hero.x = canvas.width / 2;
	hero.y = canvas.height / 2;
	
	
};
var k=0;
var update = function (modifier) {
	if (38 in keysDown) { 
		hero.y -= hero.speed * modifier;

	}
	if (40 in keysDown) { // Player holding down
	      
		hero.y += hero.speed * modifier;
	}
	if (37 in keysDown) { // Player holding left
	        
		hero.x -= hero.speed * modifier;
	}
	if (39 in keysDown) { // Player holding right
	       
		hero.x += hero.speed * modifier;
	}


	
	if (hero.x >970)
	  {
	   hero.x=970;
	  }
	  
	if (hero.x <20)
	  {
	   hero.x=20;
	  }  
	  
	if (hero.y >520)
	  {
	   hero.y=520;
	  }  
	if (hero.y <10)
	  {
	   hero.y=10;
	  }   
	
         
                 
        
  
	k=k+10
        if (k >1000) {
          m.x=	 (Math.random() * (canvas.width - 64));
           m.y =  (Math.random() * (canvas.height - 64)); 
           k=0;
           }
	
	if (13 in keysDown) {
	  scrr=1;
	  }
	  
	if (scrr>0) {
scrr=scrr+1;
}
	        
	
};

var scrng = function () {
if (scrr>0){
if (m.x > d.x-30 && m.x < d.x +30) {
    if (m.y >d.y-30 && m.y<d.y +30){
score=score +1;  
}
}  
  }

}


var render = function () {

        ctx.drawImage(bgImage,0,0)
        if (38 in keysDown) { 
		
            ctx.drawImage(ddImage, hero.x, hero.y);
            p=38;
	}
	else if (40 in keysDown) { // Player holding down
	      
		ctx.drawImage(heroImage, hero.x, hero.y);
		p=40;
	}
	
	else {
	      if(p==38) {
	        ctx.drawImage(ddImage, hero.x, hero.y);
	        }
	      else if(p==40) {
	        ctx.drawImage(heroImage, hero.x, hero.y); 
	        }
	}
	};
	
	
var renderr = function () {	

    if (32 in keysDown) {
          
          if (38 in keysDown) {       
     
	     d.x = hero.x;
             jj=200 ;       
	for (var i=0;i<jj;i++)
       { 
         d.y = hero.y-i-25;
         ctx.drawImage(monsterImage, d.x, d.y);
         scrng()
        
        }
	}
	
	
	
	if (40 in keysDown) {       
     
	     d.x = hero.x;
             jj=200 ;       
	for (var i=0;i<jj;i++)
       { 
         d.y = hero.y+i+25;
         ctx.drawImage(monsterImage, d.x, d.y);
         scrng()
        }
	}
	
	if (39 in keysDown) {
	 jj=200 ; 
	  d.y = hero.y;
	for (var i=0;i<jj;i++)
       {  
         d.x= hero.x+i+25;
         ctx.drawImage(monsterImage, d.x, d.y);
         scrng()
        }
        }
	
	
	if (37 in keysDown) {
	 jj=200 ; 
	  d.y = hero.y;
	for (var i=0;i<jj;i++)
       {  
         d.x= hero.x-i;
         ctx.drawImage(monsterImage, d.x, d.y);
         scrng()
        }
        }
	
	
	}
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	if (17 in keysDown) {       
             
             jj=200 ;       
	for (var i=0;i<jj;i++)
       { 
         d.y = hero.y-i;
         d.x= hero.x-i;
         ctx.drawImage(monsterImage, d.x, d.y);
         scrng()
        }
        
        for (var i=0;i<jj;i++)
       { 
         d.y = hero.y+i;
         d.x= hero.x+i;
         ctx.drawImage(monsterImage, d.x, d.y);
         scrng()
        }
	}
	
	
	
	
	if (190 in keysDown) {       
        
             jj=200 ;       
	for (var i=0;i<jj;i++)
       { 
         d.y = hero.y+i;
         d.x= hero.x-i;
         ctx.drawImage(monsterImage, d.x, d.y);
         scrng()
        }
        
        for (var i=0;i<jj;i++)
        { 
         d.y = hero.y+i+25;
         d.x= hero.x+i+25;
         ctx.drawImage(monsterImage, d.x, d.y);
         scrng()
        }
        
	}
	
	
	
	ctx.drawImage(mi, m.x, m.y);
	
	
	
	ctx.fillStyle = "rgb(250, 250, 250)";
	ctx.font = "24px Helvetica";
	ctx.textAlign = "left";
	ctx.textBaseline = "top";
	ctx.fillText("Score : " + score, 332, 32);
        var h=10000-scrr;	
	ctx.fillText("Time  : " + h , 332, 50);
	
	
};

var main = function () {
	var now = Date.now();
	var delta = now - then;
        if (scrr<10000){
	update(delta / 1000);
	render();
        renderr();
        }
        else{
         if(score>=25000){
        ctx.fillStyle = "rgb(250, 250, 250)";
	ctx.font = "24px Helvetica";
	ctx.textAlign = "left";
	ctx.textBaseline = "top";
	ctx.fillText("You won.You can submit your score via the link below", 250, 232);         
}
         else{
            ctx.fillStyle = "rgb(250, 250, 250)";
	ctx.font = "24px Helvetica";
	ctx.textAlign = "left";
	ctx.textBaseline = "top";
	ctx.fillText("Game over.You can submit your score via the link below", 250, 232);          
         }
         
        }
	then = now;
};

reset();
var then = Date.now();
setInterval(main, 2); 
		
		</script>
		
<div style="position:absolute; color:#FF0000 ;left : 1100px;top:0px;">
<p style="font-size:36px"> <strong>Game Instructions</strong> </p>
</div>
<div style="position:absolute; color:#F8F8FF ;left : 1100px;top:120px;">
<p style="font-size:16px"> 1.Shoot the devil to score points </p>
<p style="font-size:16px"> 2.Maximum time=10000 unit </p>
<p style="font-size:16px"> 3.Score more than 25,000 points to win </p>
<p style="font-size:16px"> 4.Hit for a longer time will ensure more points </p>
<p style="font-size:16px"> 5.Use up down right left arrow for moving  </p>
<p style="font-size:16px"> 6.up/down/left/right arrow+space bar shoots </p>
<p style="font-size:16px"> 7.Cntrl and '<' button can shoot at angles </p>
<p style="font-size:16px"> 8.Refresh the page to restart</p>
</div>
<div style="position:absolute; color:#FF0000 ;left : 1100px;top:500px;">
<p style="font-size:36px"> <strong>Press Enter to START</strong> </p>
</div>		
<div style="position:absolute; color:#00CC00;left : 1100px;top:460px;">
<p style="font-size:24px"> Please wait till the entire page loads </p>
</div>	
<div style="position:absolute; color:#FFFF66 ;left : 0px;top:570px;">
<p style="font-size:12px"> Game developed with Google App Engine,JAVAscript CANVAS element,HTML,Python 2.7 </p>
 <p style="font-size:12px">Developed by gooblu </p>
 <a href="https://github.com/saptarshighosh9/online-shooting--game">Source code is available here </a>
</div>	
<div style="position:absolute; color:#FFFF66 ;left : 600px;top:570px;">
<a href='http://s9051855845.appspot.com'> 
<img src="/images/mm.png">
</a>
</div>
	</body>
</html>

"""



















MAIN_PAGE_FOOTER_TEMPLATEE= """\
   <!DOCTYPE html>
<html>
 <title>fUn_Key</title>
    
 <head>
     
  </head>
<body >

<div style="position: absolute; left: 0px; top:0px;">
<img  src="http://imagesci.com/img/2013/12/abstract-blue-3090-hd-wallpapers.jpg" width=1365.2 height=662.7></a>
</div>
<div style="position:absolute; color:#F8F8FF ;left : 500px;top:420px;">
<p style="font-size:20px">Click Here</p>
</div>
<div style="position:absolute; color:#F8F8FF ;left : 480px;top:220px;">
<p style="font-size:72px">fU </p>
</div>
<div style="position:absolute; color:#FF0000	 ;left : 560px;top:220px;">
<p style="font-size:60px">   n_K </p>
</div>
<div style="position:absolute; color:#F8F8FF ;left : 670px;top:220px;">
<p style="font-size:72px">   eY </p>
</div>
<div style="position: absolute; left: 610px; top:420px;">
<a  href='/sign' >
<img  src="http://cdn.redmondpie.com/wp-content/uploads/2011/07/Google-G-Logo-psd64498.png" width=50 height=50></a>
</div>
<div style="position: absolute; left: 430px; top:20px;">
<img  src="http://www.photoshopstar.com/tutorials/09/07.jpg" width=390 height=220></a>
</div>
<div style="position: absolute; left: 30px; top:20px;">
<img  src="/images/pic1.jpg" width=370 height=220></a>
</div>
<div style="position: absolute; left: 860px; top:20px;">
<img  src="http://images2.layoutsparks.com/1/168839/cartoon-reaper-red-design.jpg" width=370 height=220></a>
</div>
<div style="position: absolute; left: 30px; top:260px;">
<img  src="http://wallpapers77.com/thumbs/smile_trollface_yellow_cartoon_hd_wallpaper-t2.jpg" width=370 height=220></a>
</div>
<div style="position: absolute; left: 860px; top:260px;">
<img  src="/images/pic.jpg" width=370 height=220></a>
</div>
<div style="position: absolute; left: 640px; top:560px;">
<img  src="http://techgearz.com/wp-content/uploads/2011/06/google-app-engine-logo.png" width=50 height=50></a>
</div>
<div style="position:absolute; color:#F8F8FF ;left : 540px;top:570px;">
<p style="font-size:18px"> Powered by </p>
</div>
http://techgearz.com/wp-content/uploads/2011/06/google-app-engine-logo.png
<div style="position:absolute; color:#F8F8FF ;left : 420px;top:600px;">
<p style="font-size:12px">  App developed by gooblu.Developed with Google App Engine    Image source:Internet </p>
</div>
</html>
"""






class MainPage(webapp2.RequestHandler):

    def get(self):
    	    
           self.response.write(MAIN_PAGE_FOOTER_TEMPLATEE)
      
        
class test(webapp2.RequestHandler):

    def get(self):
    	self.response.write(MAIN_PAGE_FOOTER_TEMPLATE)
        	



application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/sign',test),
    
], debug=True)
