// Check if the iframe already exists
if (!document.getElementById("sliding-iframe")) {
    // Create container div
    let container = document.createElement("div");
    container.id = "sliding-container";
  
    // Create iframe
    let iframe = document.createElement("iframe");
    iframe.id = "sliding-iframe";
    iframe.src = "https://example.com"; // Change this to your desired webpage
  
    // Create close button
    let closeButton = document.createElement("button");
    closeButton.innerText = "×";
    closeButton.id = "close-sliding";
    closeButton.onclick = () => {
      container.style.right = "-100%"; // Moves it out of view
      setTimeout(() => container.remove(), 300);
    };
  
    // Append elements
    container.appendChild(closeButton);
    container.appendChild(iframe);
    document.body.appendChild(container);
  
    // Slide in effect
    setTimeout(() => {
      container.style.right = "0";
    }, 100);
  }
  