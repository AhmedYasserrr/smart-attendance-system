const express = require("express");
const attendanceController = require("../../controllers/instructor/attendanceController");
const router = express.Router();

router.post("/start", attendanceController.startAttendance);

router.post("/end", attendanceController.endAttendance);

module.exports = router;
