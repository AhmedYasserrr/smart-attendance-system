const express = require("express");
const attendanceController = require("../../controllers/student/attendanceController");
const router = express.Router();

router
  .route("/")
  .get(attendanceController.getAttendance)
  .post(attendanceController.postAttendance);

module.exports = router;
