function startCountdown() {
  //
  let count = 15; // tiempo inicial en segundos
  const countdownElement = document.getElementById("countdown-btn");
  const RedirectElement = document.getElementById("exit");
  const RedirectElement0 = document.getElementById("suger");

  countdownElement.innerHTML = `${count}`; // Se inserta el contador como texto

  const countdownInterval = setInterval(() => {
    //Se actualiza el contador cada intervalo de tiempo
    count--;
    countdownElement.innerHTML = `${count}`;

    if (count === 0) {
      // Si contador llega a 0 :
      clearInterval(countdownInterval);
      RedirectElement.setAttribute("title", "Salir");
      RedirectElement.setAttribute("href", "?exit"); // activar el enlace de redireccionamiento
      RedirectElement0.setAttribute("href", "poppu.html");

      const newButton = document.createElement("button"); //  Se crea un Boton
      newButton.type = "button"; //  que remplaze el anterior y se le grega la imagen
      newButton.id = "countdown-btn"; //  y sus estilos
      const newImg = document.createElement("img");
      newImg.src = "https://cdn-icons-png.flaticon.com/512/8472/8472186.png";
      newImg.alt = "flaticon";
      newButton.appendChild(newImg);

      RedirectElement.replaceChild(newButton, countdownElement);
    }
  }, 1000);
}
