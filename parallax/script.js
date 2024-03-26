// script.js
document.addEventListener('DOMContentLoaded', () => {
    const sections = document.querySelectorAll('.section');
    let currentSectionIndex = 0;
    let isThrottled = false;

    const navigateSections = (direction) => {
        if (isThrottled) return;
        isThrottled = true;
        // Adjust the timing here to match the CSS transition duration
        setTimeout(() => { isThrottled = false; }, 1500); 

        const potentialIndex = currentSectionIndex + (direction === 'down' ? 1 : -1);
        if (potentialIndex >= 0 && potentialIndex < sections.length) {
            sections[currentSectionIndex].style.opacity = '0';
            currentSectionIndex = potentialIndex;
            sections[currentSectionIndex].style.opacity = '1';
        }
    };

    document.addEventListener('wheel', (event) => {
        const direction = event.deltaY > 0 ? 'down' : 'up';
        navigateSections(direction);
    });

    document.addEventListener('keydown', (event) => {
        if (event.key === 'ArrowDown') {
            navigateSections('down');
        } else if (event.key === 'ArrowUp') {
            navigateSections('up');
        }
    });
});
