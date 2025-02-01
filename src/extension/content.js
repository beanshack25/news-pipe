// Define tree structure
const treeData = {
    title: "Root",
    image: "image_root.jpg",
    description: "This is the root box",
    date: "January 31, 2025",
    children: [
        {
            title: "Child 1",
            image: "image1.jpg",
            description: "Description for Box 1",
            date: "February 1, 2025",
            children: [
                {
                    title: "Child 1.1",
                    image: "image1_1.jpg",
                    description: "Description for Box 1.1",
                    date: "February 2, 2025",
                    children: []
                },
                {
                    title: "Child 1.2",
                    image: "image1_2.jpg",
                    description: "Description for Box 1.2",
                    date: "February 3, 2025",
                    children: []
                }
            ]
        },
        {
            title: "Child 2",
            image: "image2.jpg",
            description: "Description for Box 2",
            date: "February 4, 2025",
            children: []
        }
    ]
};

// Create the sliding popup container
if (!document.getElementById("sliding-popup-container")) {
    let container = document.createElement("div");
    container.id = "sliding-popup-container";

    // Load popup content inside the container
    fetch(chrome.runtime.getURL("popup.html"))
        .then(response => response.text())
        .then(html => {
            container.innerHTML = html;
            document.body.appendChild(container);

            // Create a container for the tree
            let treeContainer = document.createElement("div");
            treeContainer.id = "tree-container";
            container.appendChild(treeContainer);

            // Generate the tree inside the sliding popup
            createBox(treeData);

            // Slide in effect by default
            container.style.right = "0";

            // Add close functionality
            document.getElementById("close-btn").addEventListener("click", () => {
                container.style.right = "-100vw"; // Slide out
                setTimeout(() => container.remove(), 300);
            });
        });
}

// Function to create and append the tree structure
function createBox(node, parentElement = null, depth = 0, index = 0) {
    let box = document.createElement("div");
    box.classList.add("expandable-box");
    box.style.left = `${(4 - depth) * 250}px`; // Adjusts position based on depth
    box.dataset.depth = depth;
    box.dataset.index = index;

    box.innerHTML = `
        <div class="box-title">${node.title}</div>
        <div class="box-content">
            <img src="${node.image}" alt="${node.title}">
            <p>${node.description}</p>
            <span class="date">${node.date}</span>
        </div>
    `;

    // Append to the tree container
    document.getElementById("tree-container").appendChild(box);

    // Create connecting line
    if (parentElement) {
        let line = document.createElement("div");
        line.classList.add("connection-line");
        document.getElementById("tree-container").appendChild(line);
        updateLine(box, parentElement, line);
    }

    // Recursively create children
    node.children.forEach((child, childIndex) => {
        createBox(child, box, depth + 1, childIndex);
    });

    // Expand and collapse logic
    box.addEventListener("mouseover", () => {
        let content = box.querySelector(".box-content");
        content.style.maxHeight = "300px";
        content.style.opacity = "1";
        updateAllLines();
    });

    box.addEventListener("mouseleave", () => {
        let content = box.querySelector(".box-content");
        content.style.maxHeight = "0";
        content.style.opacity = "0";
        updateAllLines();
    });

    return box;
}

// Update connection lines dynamically
function updateLine(box, parent, line) {
    let boxRect = box.getBoundingClientRect();
    let parentRect = parent.getBoundingClientRect();
    line.style.left = `${parentRect.left + parentRect.width / 2}px`;
    line.style.top = `${parentRect.top + parentRect.height}px`;
    line.style.width = `${Math.abs(boxRect.left - parentRect.left)}px`;
    line.style.transform = `rotate(${boxRect.top > parentRect.top ? 30 : -30}deg)`;
}

// Update all lines when boxes expand/collapse
function updateAllLines() {
    document.querySelectorAll(".connection-line").forEach(line => {
        let childBox = document.querySelector(`[data-depth='${line.dataset.childDepth}'][data-index='${line.dataset.childIndex}']`);
        let parentBox = document.querySelector(`[data-depth='${line.dataset.parentDepth}'][data-index='${line.dataset.parentIndex}']`);
        if (childBox && parentBox) updateLine(childBox, parentBox, line);
    });
}