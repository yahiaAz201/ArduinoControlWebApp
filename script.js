var el = document.getElementById("serc"),
st = window.getComputedStyle(el, null),
tr = st.getPropertyValue("transform");
console.log(tr);


setInterval(function(){
  
    $.get( "http://127.0.0.1:5000", function( data ) {
        var ok = data;
        document.getElementById('result').innerHTML =  ok.potValue  ;serc
        document.getElementById('bar').style.width =  ok.potValue +""  ;
        document.getElementById('serc').style.transform =  'rotate('+ok.potValue +""+')'  ;
        
        
  
 });
        
    
 },250);

 