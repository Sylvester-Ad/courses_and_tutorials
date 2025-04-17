document.addEventListener('DOMContentLoaded', () => {
    let menu = document.querySelector('#menu-bars');
    let navbar = document.querySelector('.navbar');
    let section = document.querySelectorAll('section');
    let navLinks = document.querySelectorAll('header .navbar a');

    menu.onclick = () => {
        menu.classList.toggle('fa-times');
        navbar.classList.toggle('active');
    };


    window.onscroll = () => {
        menu.classList.remove('fa-times');
        navbar.classList.remove('active');

        section.forEach(sec => {
            let top = window.scrollY;
            let offset = sec.offsetTop - 150;
            let height = sec.offsetHeight;
            let id = sec.getAttribute('id');

            if (top >= offset && top < offset + height) {
                navLinks.forEach(link => {
                    link.classList.remove('active');
                    document.querySelector('header .navbar a[href*=' + id + ']').classList.add('active');
                });
            }
        }
        );
    };

    document.querySelector('#search-icon').onclick = () => {
        document.querySelector('#search-form').classList.toggle('active');
    };

    document.querySelector('#close').onclick = () => {
        console.log('close button clicked');	
        document.querySelector('#search-form').classList.remove('active');
    };

    var swiper = new Swiper(".home-slider", {
        spaceBetween: 30,
        centeredSlides: true,
        autoplay: {
            delay: 2500,
            disableOnInteraction: false,
        },
        pagination: {
            el: ".swiper-pagination",
            clickable: true,
        },
        loop: true, // Enable looping
    });

    var swiper = new Swiper(".review-slider", {
        spaceBetween: 20,
        centeredSlides: true, // Ensure slides are centered
        autoplay: {
            delay: 2500,
            disableOnInteraction: false,
        },
        loop: true, // Enable looping
        slidesPerView: 1, // Default to 1 slide per view
        breakpoints: {
            640: {
                slidesPerView: 1, // Keep 1 slide per view for smaller screens
            },
            768: {
                slidesPerView: 2, // Show 2 slides per view for medium screens
            },
            1024: {
                slidesPerView: 3, // Show 3 slides per view for larger screens
            },
        },
    });

    function loader() {
        document.querySelector('.loader-container').classList.add('fade-out');
    }
    function fadeOut() {
        setInterval(loader, 3000);
    }
    window.onload = fadeOut;

    const themeToggle = document.getElementById('theme-toggle');
    const currentTheme = localStorage.getItem('theme');

    if (currentTheme === 'dark') {
        document.body.classList.add('dark-theme');
    }

    themeToggle.addEventListener('click', () => {
        document.body.classList.toggle('dark-theme');
        const theme = document.body.classList.contains('dark-theme') ? 'dark' : 'light';
        localStorage.setItem('theme', theme);
    });
});