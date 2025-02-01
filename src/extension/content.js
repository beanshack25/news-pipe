// Check if the popup is already open
if (!document.getElementById("sliding-popup-container")) {
    // Create container div
    let container = document.createElement("div");
    container.id = "sliding-popup-container";

    // Fetch and insert popup.html content
    fetch(chrome.runtime.getURL("popup.html"))
        .then(response => response.text())
        .then(html => {
            container.innerHTML = html;
            document.body.appendChild(container);

            // Slide in effect
            setTimeout(() => {
                container.style.right = "0";
            }, 100);

            // Add close functionality
            document.getElementById("close-btn").addEventListener("click", () => {
                container.style.right = "-100vw"; // Slide out
                setTimeout(() => container.remove(), 300);
            });
        });
}
