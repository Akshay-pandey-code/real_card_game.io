const express=require("express")
const app=express()
app.use(express.json())
app.get("/",(req,res)=>{
    res.send("server conect")
})
app.listen(2000,()=>{
    console.log("alredy conecting");
})