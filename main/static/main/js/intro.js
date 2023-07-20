function changeService() {
    const services = ["Mechanical Solutions", "Auto Electrical Solutions"];
    const highlightedServiceElement = document.getElementById("intro");
    let currentServiceIndex = 0;

    setInterval(() => {

        const currentService = services[currentServiceIndex];

        highlightedServiceElement.textContent = "";

        for (let i = 0; i < currentService.length; i++) {
            setTimeout(() => {
                highlightedServiceElement.textContent += currentService.charAt(i);
            }, i * 100);
        }

        currentServiceIndex = (currentServiceIndex + 1) % services.length;
    }, 4000);
}

changeService();