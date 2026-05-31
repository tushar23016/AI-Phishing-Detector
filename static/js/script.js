
// ===============================
// PHISHGUARD AI
// script.js
// ===============================

// Page Loaded

document.addEventListener("DOMContentLoaded", () => {

    console.log("PhishGuard AI Loaded");

    initializeAnimations();
    initializeCounters();
    initializeTextareaCounter();

});

// ===============================
// CARD HOVER EFFECT
// ===============================

function initializeAnimations() {

    const cards = document.querySelectorAll(
        ".feature-card, .info-card, .dashboard-card, .category-card, .stat-card"
    );

    cards.forEach(card => {

        card.addEventListener("mousemove", (e) => {

            const rect = card.getBoundingClientRect();

            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;

            card.style.background =
                `radial-gradient(circle at ${x}px ${y}px,
                rgba(0,245,255,0.12),
                rgba(255,255,255,0.05))`;

        });

        card.addEventListener("mouseleave", () => {

            card.style.background =
                "rgba(255,255,255,0.05)";

        });

    });

}

// ===============================
// ANIMATED COUNTERS
// ===============================

function initializeCounters() {

    const counters = document.querySelectorAll(
        ".stat-card h3, .dashboard-card h2"
    );

    counters.forEach(counter => {

        const text = counter.innerText;

        const target =
            parseFloat(text.replace(/[^\d.]/g, ""));

        if (isNaN(target)) return;

        let count = 0;

        const increment = target / 80;

        const updateCounter = () => {

            if (count < target) {

                count += increment;

                if (text.includes("%")) {

                    counter.innerText =
                        count.toFixed(1) + "%";

                } else {

                    counter.innerText =
                        Math.floor(count);

                }

                requestAnimationFrame(updateCounter);

            } else {

                counter.innerText = text;

            }

        };

        updateCounter();

    });

}

// ===============================
// TEXTAREA CHARACTER COUNTER
// ===============================

function initializeTextareaCounter() {

    const textarea =
        document.querySelector(
            "textarea[name='email_text']"
        );

    if (!textarea) return;

    const counter =
        document.createElement("div");

    counter.style.marginTop = "10px";
    counter.style.color = "#00f5ff";
    counter.style.fontSize = "14px";

    textarea.parentNode.appendChild(counter);

    textarea.addEventListener("input", () => {

        const length = textarea.value.length;

        counter.innerText =
            `Characters: ${length}`;

    });

}

// ===============================
// FORM VALIDATION
// ===============================

const form = document.querySelector("form");

if (form) {

    form.addEventListener("submit", function(e) {

        const textarea =
            document.querySelector(
                "textarea[name='email_text']"
            );

        if (
            textarea &&
            textarea.value.trim().length < 20
        ) {

            e.preventDefault();

            alert(
                "Please enter a valid email content before analysis."
            );

        }

    });

}

// ===============================
// COPY SAMPLE EMAIL
// ===============================

function copySampleEmail() {

    const sample =
`Dear Customer,

Your account has been suspended.

Please verify your account immediately:

http://secure-account-verify.xyz

Failure to comply within 24 hours
will result in account closure.

Regards,
Security Team`;

    navigator.clipboard.writeText(sample)
        .then(() => {

            alert(
                "Sample email copied to clipboard."
            );

        });

}

// ===============================
// SCROLL TO TOP BUTTON
// ===============================

const topButton =
    document.createElement("button");

topButton.innerHTML = "↑";

topButton.id = "topButton";

document.body.appendChild(topButton);

topButton.style.position = "fixed";
topButton.style.bottom = "25px";
topButton.style.right = "25px";
topButton.style.width = "50px";
topButton.style.height = "50px";
topButton.style.border = "none";
topButton.style.borderRadius = "50%";
topButton.style.cursor = "pointer";
topButton.style.fontSize = "20px";
topButton.style.display = "none";
topButton.style.zIndex = "999";
topButton.style.background = "#00f5ff";
topButton.style.color = "#000";

window.addEventListener("scroll", () => {

    if (window.scrollY > 300) {

        topButton.style.display = "block";

    } else {

        topButton.style.display = "none";

    }

});

topButton.addEventListener("click", () => {

    window.scrollTo({

        top: 0,
        behavior: "smooth"

    });

});

// ===============================
// LOADING BUTTON EFFECT
// ===============================

const analyzeButton =
    document.querySelector(".analyze-btn");

if (analyzeButton) {

    analyzeButton.addEventListener("click", () => {

        analyzeButton.innerHTML =
            '<i class="fas fa-spinner fa-spin"></i> Analyzing...';

    });

}

