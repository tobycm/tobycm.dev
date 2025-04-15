const as = document.querySelectorAll("a");
as.forEach((a) => {
  if (a.classList.contains("exclude")) return;
  if (a.href.startsWith("https://")) {
    a.target = "_blank";
    a.rel = "noopener noreferrer";
  }
});
