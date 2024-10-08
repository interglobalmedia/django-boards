Element.prototype.getLink = function () {
  let link = document.createElement("a");
  link.href = this.getUrl();
  link.innerText = this.innerText;
  return link;
};

Element.prototype.getUrl = function () {
  return new URL(window.location.origin + window.location.pathname + '#' + this.id);
};

Clipboard.prototype.writeHTML = function (html, text) {
  let textContent = text || html.innerText;
  let htmlContent = "";
  if (typeof (html) == "string") htmlContent = html;
  else if (html instanceof Element) htmlContent = html.outerHTML;
  else htmlContent = html.toString();

  if (ClipboardItem) //bug in firefox : https://developer.mozilla.org/en-US/docs/Web/API/ClipboardItem
  {
    let content = [
      new ClipboardItem({
        "text/html": new Blob([htmlContent], { type: "text/html" }), //this can be interpreted by applications like teams or office word
        "text/plain": new Blob([textContent], { type: "text/plain" }) //while this is required for other apps, like plain text editors
      })
    ];
    return this.write(content);
  }
  else {
    return this.writeText(textContent);
  }
};

let header = document.getElementById("copy-header");
let button = document.getElementById("copy-button");
let feedback = document.getElementById("feedback");
button.addEventListener("click", function () {
  navigator.clipboard
    .writeHTML(header.getLink(), header.getUrl())
    .then(function () {
      feedback.innerText = "copied!";
      setTimeout(function () {
        document.getElementById("feedback").innerHTML = "";
      }, 1000);
    })
    .catch((error) => {
      feedback.innerText = `Oops... that shouldn't have happened. ${error}`;
    });
});