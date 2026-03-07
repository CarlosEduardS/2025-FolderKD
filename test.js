document.addEventListener("DOMContentLoaded", function () {
  const botao = document.getElementById("mbt");
  const sidebar = document.getElementById("sidebar");
  const closeSidebar = document.getElementById("closeSidebar");

  // Botão do menu lateral 'Projetos'
  const projetosBtn = sidebar.querySelectorAll("ul li")[1];
  const projetosDiv = document.getElementById("projetos");
  const projetosTitulo = document.getElementById("projetosTitulo");

  botao.addEventListener("click", function () {
    sidebar.classList.add("active");
  });

  closeSidebar.addEventListener("click", function () {
    sidebar.classList.remove("active");
  });

  projetosBtn.addEventListener("click", function () {
    sidebar.classList.remove("active");
    window.open("projetos3v3.html", "_blank");
  });
});
