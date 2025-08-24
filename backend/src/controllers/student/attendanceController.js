module.exports.getAttendance = (req, res) => {
  res.status(200).render("student/attendance"); 
};
module.exports.postAttendance = (req, res) => {
    const { name, email, instructorCode } = req.body;
    console.log({ name, email, instructorCode });
    res.send("Attendance submitted successfully!");
};
