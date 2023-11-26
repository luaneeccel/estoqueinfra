var modalBtns = document.querySelectorAll(".modal-target");
var closeBtns = document.querySelectorAll('.delete');

modalBtns.forEach(function (btn) {
	btn.onclick = function () {
		id = btn.getAttribute('data-bulma-modal');
		document.getElementById(id).style.display = "block";
	};
});

closeBtns.forEach(function (btn) {
   	btn.onclick = function () {
       	var moda = (btn.closest(".modal").style.display = "none");
   	};
});

/* close modal on click background */
window.onclick = function(event) {
	if (event.target.className == 'modal-background') {
		closeBtns.forEach(function (btn) {
			var moda = (btn.closest(".modal").style.display = "none");
		});
	}
};

function geraPdf(imprimir, form) {
	var formulario = document.getElementById(form);
	document.getElementById('imprimir').value = imprimir;
	if (imprimir =='pdf'){
		formulario.setAttribute("target", "_blank");
	} else {
		formulario.setAttribute("target", "_self");
	}
	formulario.submit();
};

