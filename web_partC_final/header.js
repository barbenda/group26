         function toggleMenu() {
            const menu = document.getElementById('menu');
            menu.style.display = menu.style.display === 'block' ? 'none' : 'block';
        }

        function toggleAccountMenu() {
            const accountMenu = document.getElementById('accountMenu');
            accountMenu.style.display = accountMenu.style.display === 'block' ? 'none' : 'block';
        }

        document.addEventListener('click', function(event) {
            const menu = document.getElementById('menu');
            const menuIcon = document.querySelector('.menu-icon');
            const accountMenu = document.getElementById('accountMenu');
            const accountIcon = document.querySelector('.account-icon');

            // Close menu if clicked outside
            if (!menuIcon.contains(event.target) && !menu.contains(event.target)) {
                menu.style.display = 'none';
            }

            // Close account menu if clicked outside
            if (!accountIcon.contains(event.target) && !accountMenu.contains(event.target)) {
                accountMenu.style.display = 'none';
            }
        });

        function toggleAccountMenu() {
            const accountMenu = document.getElementById('accountMenu');
            accountMenu.style.display = accountMenu.style.display === 'block' ? 'none' : 'block';
        }
        document.addEventListener('click', function(event) {
            const accountMenu = document.getElementById('accountMenu');
            const accountIcon = document.querySelector('.account-icon');

            if (!accountIcon.contains(event.target) && !accountMenu.contains(event.target)) {
                accountMenu.style.display = 'none';
            }
        });


        function showPopup(popupId) {
            document.getElementById('overlay').style.display = 'block';
            document.getElementById(popupId).style.display = 'block';
        }

        function closePopup() {
            document.getElementById('overlay').style.display = 'none';
            document.querySelectorAll('.popup').forEach(popup => popup.style.display = 'none');
        }

        function setupSearch() {
            const searchInput = document.getElementById('searchInput');

            searchInput.addEventListener('keydown', (event) => {
                if (event.key === 'Enter') {
                    searchProducts();
                }
            });
        }

        async function searchProducts() {
            const query = document.getElementById('searchInput').value.toLowerCase();

            if (!query) {
                alert('Please enter a search term!');
                return;
            }

            window.location.href = `search_results.html?query=${encodeURIComponent(query)}`;
        }

        document.addEventListener('DOMContentLoaded', setupSearch);


// קריאה לפונקציה בעת טעינת הדף
document.addEventListener('DOMContentLoaded', updateCartCount);

// עדכון המונה כאשר יש שינוי ב-localStorage
window.addEventListener('storage', updateCartCount);
document.addEventListener("DOMContentLoaded", function () {
    // טוען את קובץ ה-HTML של הכותרת
    fetch("header.html")
        .then(response => response.text())
        .then(data => {
            // מחדיר את התוכן של הכותרת ל-DOM
            document.getElementById("header-container").innerHTML = data;

            // טוען ומבצע את הקוד של header.js
            const script = document.createElement("script");
            script.src = "header.js";
            script.type = "text/javascript";
            document.body.appendChild(script);

            // קורא לפונקציה לעדכון מספר הפריטים בעגלה
            updateCartCount();
        })
        .catch(error => console.error("Error loading header:", error));
});

// פונקציית עדכון מונה הפריטים
function updateCartCount() {
    const cart = JSON.parse(localStorage.getItem("cart")) || [];
    const cartCountElement = document.getElementById("cart-count");

    const totalItems = cart.reduce((sum, item) => sum + (item.quantity || 1), 0);

    if (cartCountElement) {
        if (totalItems > 0) {
            cartCountElement.textContent = totalItems;
            cartCountElement.style.display = "block";
        } else {
            cartCountElement.textContent = "0";
            cartCountElement.style.display = "none";
        }
    }
}
