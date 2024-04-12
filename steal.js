const fs= require("fs");
fetch("https://www.delhisldc.org/Redirect.aspx?Loc=0804").then(k=>k.text()).then(data=>{
    fs.writeFile("data.html",data,()=>{
        console.log("done");
    });
});