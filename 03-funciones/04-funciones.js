var obj = {
    init: function () {
        var m = new Matrix(2);
        m.showDlg();
        var b = document.createElement("input");
        b.type = "button";
        b.value = "print";
        document.body.appendChild(b);
        b.onclick = function () {
        };
    }
};
