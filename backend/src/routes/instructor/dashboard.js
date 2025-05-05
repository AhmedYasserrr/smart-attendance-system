const express = require("express");
const dashboardController = require("../../controllers/instructor/dashboardController");
const router = express.Router();

router.get("/", dashboardController.getDashboard);

module.exports = router;
