function dibuja(datos) {
	let filas="";
	for (i of datos) {
		filas+=`<tr><td>${i[0]}</td><td>${i[1]}</td></tr>`;
	}
	document.querySelector("table").innerHTML=filas;
}
function insertar(evt) {
	if (document.querySelector('form').checkValidity()) {
		document.querySelector(".alert").hidden=true;
	const data = new FormData(document.querySelector('form'));
	fetch('insert', {
		method: 'POST',
		body: data
	})
	.then(function(response) {
		if(response.ok) {
			console.log(response);
			return response.statusText;
		} else {
			throw "Error en la llamada Ajax";
		}
	})
	.then(function(texto) {
		console.log(texto);
	})
	.catch(function(err) {
		console.log(err);
	});
} else {
	document.querySelector(".alert").hidden=false;
}
}
function cargar(evt) {
	fetch('datos')
	.then(response => response.json())
	.then(data => dibuja(data));
}
window.addEventListener('DOMContentLoaded', () => {
	document.querySelector(".ver").addEventListener("click", (evt)=>cargar(evt));
	document.querySelector(".insertar").addEventListener("click", (evt)=>insertar(evt));
});
