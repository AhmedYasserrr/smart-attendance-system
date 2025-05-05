const express = require("express");
const studentsController = require("../../controllers/instructor/studentsController");
const router = express.Router();

router
  .route("/")
  .get(studentsController.getAllStudents)
  .post(studentsController.createStudent);

router
  .route("/:id")
  .get(studentsController.getStudentById)
  .put(studentsController.updateStudentById)
  .delete(studentsController.deleteStudentById);

module.exports = router;
