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

	function win() {
		if ($('body').hasClass('disable-scroll')) {
			resurrectScroll();
			$('.popup-container').fadeOut();
			$('.win').fadeOut();
			$('body').css('background', 'linear-gradient(90deg, rgba(255,166,0,.8) 0%, rgba(253,45,45,.8) 100%)');
		} else {
			killScroll();
			$('.popup-container').fadeIn();
			$('.win').fadeIn();
			$('.win').css('display', 'flex');
			$('body').css('background', 'orange');
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

	function lose() {
		$('.lock__try').css({'color' : 'red', 'border-color': 'red'});
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

	$('.hints__help').on('click', function(){
		$(this).siblings('.hints__hint').slideToggle();
		$(this).toggleClass('hints__help_active');
	});

	$('.main__rules-button').on('click', function(){
		$('.main__rules').slideToggle();
		$(this).toggleClass('rules-button__active');
	});

	$('.tab').on('click', function(e){
		e.preventDefault();

		$('.tab').removeClass('tab_active');
		$('.hints__item').removeClass('hints__item_active');

		$(this).addClass('tab_active');
		$($(this).attr('href')).addClass('hints__item_active');
	});

	$('.main__authors').on('click', authors);

	$('.tab:first').click();

	$('.popup-container').on('click', function(event){
		if (event.target == this) {
			authors();
		}
	});

	$('.lock__try').on('click', trying);

	init();

	$('.main__reset').on('click', init);

});


// Получает код от польщователя, сравнивает с правильным паролем [red, green, blue]

//checker(tryRed, tryGreen, tryBlue) сравнивает с [red, green, blue] (ПРОВЕРКА tryColor На число!!!!) Возвращает 1 или true, если все совпало и пользователь угадал

//Генератор случайной подсказки от 100 до 100000 ПРОВЕРКА, ЧТО ХОТЬ ОДНО ЧИСЛО больше 3

//Генератор случайного зеленого числа. Получает подсказку возвращает индекс случайного элемента ПРОВЕРКА НА ТО ЧТО > 3

// init() => вернет случайное число от 100 до 100000 и индекс случайный. запуск игры

//red(hint) => считает количество нулей в записи подсказки в системе счисления, равной количеству цифр в подсказке. Возвращает КРАСНЫЙ пароль
 
//green(hint, indx) => берет 23.(01) и переводит из системы == hint[indx] в 10 систему и суммирует первые чертыре знака после запятой. Возвращает ЗЕЛЕНЫЙ пароль

//blue(hint) => переворачивает hint и испольщуя функцию fibonacci(hint) => переводит в систему Фибоначчи, далее считает количество едениц в записи. Возвращает СИНИЙ пароль
