var toggle = document.getElementById('theme-toggle');
var dark = document.body.classList.contains('dark-mode');
toggle.setAttribute('aria-pressed', dark);

toggle.addEventListener('click', function() {
    dark = document.body.classList.toggle('dark-mode');
    this.setAttribute('aria-pressed', dark);
    try {
        localStorage.setItem('theme', dark ? 'dark' : 'light');
    } catch (e) {}
});
