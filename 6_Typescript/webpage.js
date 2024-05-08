var Example = /** @class */ (function () {
    function Example() {
        this.button = document.createElement("button");
        this.button.textContent = "Click";
        this.button.style.margin = "auto";
        this.button.addEventListener("click", this.onClick.bind(this));
        document.body.appendChild(this.button);
    }
    Example.prototype.onClick = function () {
        if (this.button.textContent === "Click") {
            this.button.textContent = "Clicked!";
            alert("Button is Clicked and it is rendering by Typescript.");
        }
        else {
            this.button.textContent = "Click";
        }
    };
    return Example;
}());
window.addEventListener("load", function () {
    new Example();
});
