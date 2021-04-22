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

	function printRational(arr) {
		var strs = getStringRational(arr);
		var res = `<div class="res_rational-nom">${strs[0]}</div>
						<div class="res_rational-denom">${strs[1]}</div>`;
		$('.rational_res').html(res); 
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

	$('.tab:first').click();

	$('.popup-container').on('click', function(event){
		if (event.target == this) {
			authors();
		}
	});

	/******** NATURAL ********/

	$('#N-1').on('click', function(){
		var N1, N2;

		N1 = getNatural($('#natural_1')[0].value);
		N2 = getNatural($('#natural_2')[0].value);

		eel.N_1(N1, N2)(function(ret){
			document.getElementById('natural_res').innerHTML = getStringNat(ret);
		});
	});

	$('#N-2').on('click', function(){
		var N1, N2;

		N1 = getNatural($('#natural_1')[0].value);
		N2 = getNatural($('#natural_2')[0].value);

		eel.N_2(N1, N2)(function(ret){
			document.getElementById('natural_res').innerHTML = getStringNat(ret);
		});
	});

	$('#N-3').on('click', function(){
		var N1, N2;

		N1 = getNatural($('#natural_1')[0].value);
		N2 = getNatural($('#natural_2')[0].value);

		eel.N_3(N1, N2)(function(ret){
			document.getElementById('natural_res').innerHTML = getStringNat(ret);
		});
	});

	$('#N-4').on('click', function(){
		var N1, N2;

		N1 = getNatural($('#natural_1')[0].value);
		N2 = getNatural($('#natural_2')[0].value);

		eel.N_4(N1, N2)(function(ret){
			document.getElementById('natural_res').innerHTML = getStringNat(ret);
		});
	});

	$('#N-5').on('click', function(){
		var N1, N2;

		N1 = getNatural($('#natural_1')[0].value);
		N2 = getNatural($('#natural_2')[0].value);

		eel.N_5(N1, N2)(function(ret){
			document.getElementById('natural_res').innerHTML = getStringNat(ret);
		});
	});

	$('#N-6').on('click', function(){
		var N1, N2;

		N1 = getNatural($('#natural_1')[0].value);
		N2 = getNatural($('#natural_2')[0].value);

		eel.N_6(N1, N2)(function(ret){
			document.getElementById('natural_res').innerHTML = getStringNat(ret);
		});
	});

	$('#N-7').on('click', function(){
		var N1, N2;

		N1 = getNatural($('#natural_1')[0].value);
		N2 = getNatural($('#natural_2')[0].value);

		eel.N_7(N1, N2)(function(ret){
			document.getElementById('natural_res').innerHTML = getStringNat(ret);
		});
	});

	/******** INTEGER ********/

	$('#I-1').on('click', function(){
		var I1, I2;

		I1 = getInteger($('#integer_1')[0].value);
		I2 = getInteger($('#integer_2')[0].value);

		eel.I_1(I1, I2)(function(ret){
			document.getElementById('integer_res').innerHTML = getStringInt(ret);
		});
	});

	$('#I-2').on('click', function(){
		var I1, I2;

		I1 = getInteger($('#integer_1')[0].value);
		I2 = getInteger($('#integer_2')[0].value);

		eel.I_2(I1, I2)(function(ret){
			document.getElementById('integer_res').innerHTML = getStringInt(ret);
		});
	});

	$('#I-3').on('click', function(){
		var I1, I2;

		I1 = getInteger($('#integer_1')[0].value);
		I2 = getInteger($('#integer_2')[0].value);

		eel.I_3(I1, I2)(function(ret){
			document.getElementById('integer_res').innerHTML = getStringInt(ret);
		});
	});

	$('#I-4').on('click', function(){
		var I1, I2;

		I1 = getInteger($('#integer_1')[0].value);
		I2 = getInteger($('#integer_2')[0].value);

		eel.I_4(I1, I2)(function(ret){
			document.getElementById('integer_res').innerHTML = getStringInt(ret);
		});
	});

	$('#I-5').on('click', function(){
		var I1, I2;

		I1 = getInteger($('#integer_1')[0].value);
		I2 = getInteger($('#integer_2')[0].value);

		eel.I_5(I1, I2)(function(ret){
			document.getElementById('integer_res').innerHTML = getStringInt(ret);
		});
	});


	/******** RATIONAL ********/

	$('#Q-1').on('click', function(){
		var Q1;

		Q1 = getRational($('#rational-nom_1')[0].value, $('#rational-denom_1')[0].value);

		eel.Q_1(Q1)(function(ret){
			printRational(ret);
		});
	});

	$('#Q-2').on('click', function(){
		var Q1, Q2;

		Q1 = getRational($('#rational-nom_1')[0].value, $('#rational-denom_1')[0].value);
		Q2 = getRational($('#rational-nom_2')[0].value, $('#rational-denom_2')[0].value);

		eel.Q_2(Q1, Q2)(function(ret){
			printRational(ret);
		});
	});

	$('#Q-3').on('click', function(){
		var Q1, Q2;

		Q1 = getRational($('#rational-nom_1')[0].value, $('#rational-denom_1')[0].value);
		Q2 = getRational($('#rational-nom_2')[0].value, $('#rational-denom_2')[0].value);

		eel.Q_3(Q1, Q2)(function(ret){
			printRational(ret);
		});
	});

	$('#Q-4').on('click', function(){
		var Q1, Q2;

		Q1 = getRational($('#rational-nom_1')[0].value, $('#rational-denom_1')[0].value);
		Q2 = getRational($('#rational-nom_2')[0].value, $('#rational-denom_2')[0].value);

		eel.Q_4(Q1, Q2)(function(ret){
			printRational(ret);
		});
	});

	$('#Q-5').on('click', function(){
		var Q1, Q2;

		Q1 = getRational($('#rational-nom_1')[0].value, $('#rational-denom_1')[0].value);
		Q2 = getRational($('#rational-nom_2')[0].value, $('#rational-denom_2')[0].value);

		eel.Q_5(Q1, Q2)(function(ret){
			printRational(ret);
		});
	});

	$('#P-1').on('click', function(){
		var P1, P2;

		P1 = getPolynome(1);
		P2 = getPolynome(2);

		eel.P_5(P1, P2)(function(ret){
			printPolynome(ret);
		});
	});

	$('#P-2').on('click', function(){
		var P1, P2;

		P1 = getPolynome(1);
		P2 = getPolynome(2);

		eel.P_2(P1, P2)(function(ret){
			printPolynome(ret);
		});
	});

	$('#P-3').on('click', function(){
		var P1, P2;

		P1 = getPolynome(1);
		P2 = getPolynome(2);

		eel.P_3(P1, P2)(function(ret){
			printPolynome(ret);
		});
	});

	$('#P-4').on('click', function(){
		var P1, P2;

		P1 = getPolynome(1);
		P2 = getPolynome(2);

		eel.P_4(P1, P2)(function(ret){
			printPolynome(ret);
		});
	});

	$('#P-5').on('click', function(){
		var P1, P2;

		P1 = getPolynome(1);
		P2 = getPolynome(2);

		eel.P_5(P1, P2)(function(ret){
			printPolynome(ret);
		});
	});

	$('#P-6').on('click', function(){
		var P1, P2;

		P1 = getPolynome(1);
		P2 = getPolynome(2);

		eel.P_6(P1, P2)(function(ret){
			printPolynome(ret);
		});
	});

	$('#P-7').on('click', function(){
		var P1, P2;

		P1 = getPolynome(1);

		eel.P_7(P1)(function(ret){
			printPolynome(ret);
		});
	});

	$('#P-8').on('click', function(){
		var P1, P2;

		P1 = getPolynome(1);
		P2 = getPolynome(2);

		eel.P_8(P1, P2)(function(ret){
			printPolynome(ret);
		});
	});


});
