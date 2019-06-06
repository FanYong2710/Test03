onload = function () {
    document.getElementsByTagName('button')[0].onclick = function () {
        test();
    }
}
function test() {
    alert("这是js");
}