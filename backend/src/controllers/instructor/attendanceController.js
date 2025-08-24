module.exports.startAttendance = (req, res) => {
    res.redirect("/instructor/dashboard?message=Attendance%20started!");
};

module.exports.endAttendance = (req, res) => {
    res.redirect("/instructor/dashboard?message=Attendance%20ended!");
};
