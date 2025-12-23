// -----------------
// Navigation Logic
// -----------------
document.querySelectorAll(".nav-title, .menu-btn, .cta-btn").forEach(link => {
    link.addEventListener("click", e => {
        e.preventDefault();
        const page = link.dataset.page;

        if (page === "homepage") {
            window.location.href = "/";
            return;
        }

        if (page === "about") {
            window.location.href = "/about";
            return;
        }

        if (page === "module") {
            window.location.href = "/module";
            return;
        }

        if (page === "practice") {
            window.location.href = "/practice";
            return;
        }
    });
});

// --------------
// Scroll Header
// --------------
window.addEventListener("scroll", () => {
    const header = document.querySelector(".navbar");
    const hero = document.querySelector(".hero");

    if (window.scrollY > (hero.offsetHeight - 100)) {
        header.classList.add("scrolled");
    } else {
        header.classList.remove("scrolled");
    }
});