document.addEventListener("DOMContentLoaded", function() {
    const sections = document.querySelectorAll(".section");

    const revealOnScroll = () => {
        sections.forEach(section => {
            const sectionTop = section.getBoundingClientRect().top;
            if (sectionTop < window.innerHeight - 100) {
                section.classList.add("visible");
            }
        });
    };

    window.addEventListener("scroll", revealOnScroll);
    revealOnScroll();
});
