class Example {
    button: HTMLButtonElement;
    constructor() {
        this.button = document.createElement("button");
        this.button.textContent = "Click";
        this.button.addEventListener("click", this.onClick.bind(this));
        document.body.appendChild(this.button);
    }

    onClick() {
        if (this.button.textContent === "Click") {
            this.button.textContent = "Clicked!";
            alert("Button is Clicked and it is rendering by Typescript.")
        } else {
            this.button.textContent = "Click";
        }
    }
}

window.addEventListener("load", () => {
    new Example();
});

