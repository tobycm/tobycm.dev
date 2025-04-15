/**
 * Sets the theme of the page. If no theme is provided, it will toggle between light and dark.
 *
 * @param {string | undefined} theme The theme to set.
 *
 * @returns {void}
 */
function setTheme(theme) {
  /** @type {HTMLLinkElement} */
  const css = document.getElementById("theme");

  if (!theme) theme = css.href.endsWith("light.css") ? "dark.css" : "light.css";

  css.href = theme;

  localStorage.setItem("theme", theme);

  document.getElementById("themeButton").textContent = theme === "light.css" ? "🔆" : "🌙";
}

let theme = localStorage.getItem("theme");

const prefersDarkScheme = window.matchMedia("(prefers-color-scheme: dark)");

if (!theme && prefersDarkScheme.matches) theme = "dark.css";

setTheme(theme);
