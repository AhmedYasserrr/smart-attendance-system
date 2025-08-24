module.exports.getDashboard = (req, res) => {
  const instructorCode = "INST123"; // replace with real code from DB
  const message = req.query.message || null; // flag from redirect
  res.render("instructor/dashboard", { instructorCode, message });
};
