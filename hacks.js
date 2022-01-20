const head = document.getElementsByTagName('head')[0];

// Save the original method
var insertBefore = head.insertBefore;

// Replace it!
async function hackroboto(){
    head.insertBefore = function (newElement, referenceElement) {

        if (newElement.href && newElement.href.indexOf("https://fonts.googleapis.com/css?family=Roboto") === 0) {
            return;
        }

        insertBefore.call(head, newElement, referenceElement);
    };
}

hackroboto();
