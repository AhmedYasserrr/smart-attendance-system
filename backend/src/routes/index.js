const express = require("express");
const router = express.Router();

router.use("/", require("./home"));
router.use("/instructor", require("./instructor"));
router.use("/student", require("./student"));

module.exports = router;
