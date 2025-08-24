module.exports.getHome = (req, res) => {
  // res.status(200).send("Welcome to Smart Attendance");
  res.status(200).render("home");
};
