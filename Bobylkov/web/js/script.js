$(function(){

	function killScroll() {
		let pagePosition = window.scrollY;
		$('body').addClass('disable-scroll');
		document.body.dataset.position = pagePosition;
		document.body.style.top = -pagePosition + 'px';
	}

	function resurrectScroll() {
		let pagePosition = parseInt(document.body.dataset.position, 10);
		document.body.style.top = 'auto';
		$('body').removeClass('disable-scroll');
		window.scroll({top: pagePosition, left: 0});
		document.body.removeAttribute('data-position');
	}

	function authors() {
		if ($(this).hasClass('popuped')) {
			$('.win').fadeOut();
			$('.authors').fadeIn();
		} else {
			if ($('body').hasClass('disable-scroll')) {
				resurrectScroll();
				$('.popup-container').fadeOut();
				$('.authors').fadeOut();
				$('body').css('background', 'linear-gradient(90deg, rgba(255,166,0,.8) 0%, rgba(253,45,45,.8) 100%)');
			} else {
				killScroll();
				$('.popup-container').fadeIn();
				$('.authors').fadeIn();
				$('body').css('background', 'orange');
			}
		}
	}


	function trying() {
		let tryRed = document.getElementById('input-red').value,
				tryGreen = document.getElementById('input-green').value,
				tryBlue = document.getElementById('input-blue').value;
				
		eel.checker(tryRed, tryGreen, tryBlue)(function(ret){
			console.log(ret == 1);
			if (ret == 1) {
				win();
				$('.lock__try').css({'color': 'white', 'border-color': '-internal-light-dark(rgb(118, 118, 118), rgb(133, 133, 133));'});
			} else {
				lose();
			}
		});
	}


	function init() {
		let Arr, number, green;
		Arr = eel.init()(function(ret){
			console.log(ret);
			let number = String(ret[0]),
					green = ret[1];
			let element = document.querySelector('.main__number');
				num1 = number.slice(0, green);
				num2 = number.slice(green + 1);
				res = num1 + '<span>' + number[green] + '</span>' + num2;
				element.innerHTML = res;
		});
		// Запрашиваем у Python число подсказку
		// let green = getRandomInt(number.length); // Запрашиваем у Python случайное число
	}

	function getNatural(str) {
		var res = [str.length, []];
		if (isFinite(str)) {

			for (var i = 0; i < str.length; i++) {

				res[1].push(Number(str[i]));
			}
		}
		else res = false;
		return res;
	}

	function getInteger(str) {
		var res;

		if (str[0] == '-') {
		 	res = getNatural(str.slice(1));
		 	res.unshift(1);
		} else {
			res = getNatural(str);
			res.unshift(0);
		}

		return res;
	}

	function answer(id, str) {
		document.getElementById(id).innerHTML = str;
	}

	function getStringNat(arr) {
		var res = '';

		for (var i = 0; i < arr[0]; i++) {
			res += arr[1][i];
		}

		return res;
	} 

	function getStringInt(arr) {
		res = getStringNat(arr.slice(1));
		if (arr[0] == 1) res = '-' + res;

		return res;
	}

	function getRational(str1, str2) {
		var res;

		res = [getInteger(str1), getNatural(str2)];

		return res;
	}

	function getStringRational(arr) {
		var res;

		res = [getStringInt(arr[0]), getStringNat(arr[1])];

		return res;
	}

	function addPower(str) {
		var len;
		var adder;
		if (str == 'more__1') {
			len = $('.polynom__1').children('.polynom__inputs').children().length;
			adder = `
				<div class="rational_num polynom__input--${len}">
					<div class="polynom__x">
						x
						<span class="x__power">${len}</span>
					</div>
					<input type="text" class="num_input">
					<input type="text" class="num_input">
				</div>
			`;
			$('.polynom__1').children('.polynom__inputs').children().last().after(adder);


		} else {
			len = $('.polynom__2').children('.polynom__inputs').children().length;
			adder = `
				<div class="rational_num polynom__input--${len}">
				<div class="polynom__x">
					x
					<span class="x__power">${len}</span>
				</div>
					<input type="text" class="num_input">
					<input type="text" class="num_input">
				</div>
			`;
			$('.polynom__2').children('.polynom__inputs').children().last().after(adder);
		}
	}

	function deletePower(str) {
		var len;
		if (str == 'less__1') {
			len = $('.polynom__1').children('.polynom__inputs').children().length;

			if (len > 1) $('.polynom__1').find(`.polynom__input--${len-1}`).remove();
		} else {
			len = $('.polynom__2').children('.polynom__inputs').children().length;
			if (len > 1) $('.polynom__2').find(`.polynom__input--${len-1}`).remove();
		}
	}

	function getPolynome(n){
		var len = $(`.polynom__${n}`).children('.polynom__inputs').children().length;
		var poly = [len-1, []];

		for (var i = 0; i < len; i++) {
			str1 = $(`.polynom__${n}`).find(`.polynom__input--${i}`).find('.num_input')[0].value;
			str2 = $(`.polynom__${n}`).find(`.polynom__input--${i}`).find('.num_input')[1].value;
			poly[1].push(getRational(str1, str2));
		}

		return poly;
	}

	function printPolynome(arr) {
		var res = '';
		var coefs = [];
		var curHTML;

		for (var i = 0; i < arr[1].length; i++) {
			coefs.push(getStringRational(arr[1][i]));
		}

		for (var i = 0; i < coefs.length; i++) {
			curHTML = `
				<div class="rational_coef">
							<div class="res_rational-nom">${coefs[i][0]}</div>
							<div class="res_rational-denom">${coefs[i][1]}</div>
							<div class="polynom__x">
								x
								<span class="x__power">${i}</span>
							</div>
						</div>
			`
			res += curHTML;
		}

		$('.polynom_res').html(res);

	}

	$("#P-1").on('click', function() {
		printPolynome(getPolynome(1));
		console.log(getPolynome(2));
	})

	$('.tab').on('click', function(e){
		e.preventDefault();

		$('.tab').removeClass('tab_active');
		$('.options__item').removeClass('options__item_active');

		$(this).addClass('tab_active');
		$($(this).attr('href')).addClass('options__item_active');
	});

	$('.main__authors').on('click', authors);

	$('.control__more').on('click', function(e){
		addPower($(e.target)[0].classList[1]);
	});

	$('.control__less').on('click', function(e){
		deletePower($(e.target)[0].classList[1]);
	});

	$('.tab:last').click();

	$('.popup-container').on('click', function(event){
		if (event.target == this) {
			authors();
		}
	});
	console.log(getStringNat(getNatural('98765432')));
	console.log(getStringInt(getInteger('-123')));
	console.log(getRational('-12345', '123'));
	document.getElementById('natural_res').innerHTML = '123';


});
