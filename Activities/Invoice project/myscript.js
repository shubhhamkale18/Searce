


    
    function add() {
      var x = parseInt(document.getElementById("rate").value);
      var y = parseInt(document.getElementById("quantity").value)
      var amount = document.getElementById("amount").value = x * y;
      var subtotal = 0;
      var subtotal = subtotal + amount;
      var subtotal = document.getElementById("subtotal").value = subtotal;
      
      
    
    }
    
    function tax12(){
        var x = parseInt(document.getElementById("subtotal").value);
        var y = parseInt(document.getElementById("taxes").value);
        var taxdis = (x * y)/100;
        var taxdis = document.getElementById("taxdis").value = taxdis;
        
    }

    function total(){
        var x = parseInt(document.getElementById("taxdis").value);
        var y = parseInt(document.getElementById("subtotal").value);
        var total = x+y;
        var total = document.getElementById("finaltotal").value = total;

    }


    function generatePDF() {
        html2canvas(document.getElementById("printPDF")).then(function (canvas) {
            var imgdata = canvas.toDataURL('image/png', 1.0)
            var doc = new jsPDF("1", "mm", "a4")
            // imagedata, format, x, y, width, height
            doc.addImage(imgdata, 'PNG', 10, 10, 190, 230)
            doc.save("sample.pdf")
        })
    }