const path = require('path');
const express = require("express");
const logger = require("morgan");

const routes = require("./routes");

const app = express();

app.set("views", path.join(__dirname, "views")); 
app.set("view engine", "ejs");
app.use(express.urlencoded({ extended: true }));
app.use(logger("dev"));

app.use(routes);
module.exports = app;
