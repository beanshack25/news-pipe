// Check if the overlay already exists
if (!document.getElementById("customOverlay")) {
    // Create the overlay div
    let overlay = document.createElement("div");
    overlay.id = "customOverlay";
    
    // Add overlay content
    overlay.innerHTML = `
        <div id="overlayContent">
            <span id="closeOverlay">&times;</span>
            <h2>Overlay Panel</h2>
            <p>This is a smooth overlay that slides in from the right.</p>
        </div>
    `;

    // Inject styles
    let style = document.createElement("link");
    style.rel = "stylesheet";
    style.href = chrome.runtime.getURL("styles.css");
    document.head.appendChild(style);

    // Append overlay to body
    document.body.appendChild(overlay);

    // Delay to trigger smooth animation
    setTimeout(() => overlay.classList.add("visible"), 100);

    // Close button functionality
    document.getElementById("closeOverlay").addEventListener("click", function () {
        overlay.classList.remove("visible"); // Slide out
        setTimeout(() => overlay.remove(), 500); // Remove from DOM after animation
    });
}
