var done = false;
var camstate = 0;
var armcamstate = false;
var armcamnum = 1;


function camset(){
		let result = document.querySelector('#cam_test');
		if(result.innerText == "on"){
			var time = new Date().getTime();
				result.innerHTML = "off";
				camstate = 0;
			}
		else if(result.innerText == "off"){
				result.innerHTML = "on";
				camstate = 1;
			}
	}

function onloadcam(num){
	var time = new Date().getTime();
	
	if(done && armcamstate && num == 1){
			document.getElementById("cam" + num).src="/video_feed/" + armcamnum + "/" + camstate + "?time" + time;
		}
	else if(done){
			document.getElementById("cam" + num).src="/video_feed/" + num + "/" + camstate + "?time" + time;
		}
  }

$(function(){
	onloadcam(0);
	$('.select-area select').on('change', function(){
		onloadcam($(this).val();
		$('.select-area'). val(src = "/video_feed/" + num + "/" + camstate + "?time" + time);
	});
});

$(function(){
	onloadcam(1);
	$('.select-area select').on('change', function(){
		onloadcam($(this).val();
		$('.select-area'). val(src = "/motor/" + num + "/" + camstate + "?time" + time);
	});
});

$(function(){
	onloadcam(2);
	$('.select-area select').on('change', function(){
		onloadcam($(this).val();
		$('.select-area'). val(src = "/servo/" + num + "/" + camstate + "?time" + time);
	});
});



window.addEventListener("keydown", (e) => {
	if(servo_keys.includes(e.key.toLowerCase())){
		armcamstate = true;
	}
	else{
		armcamstate =false;
	}
});
    
