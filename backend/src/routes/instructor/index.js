const express = require("express");
const router = express.Router();

router.use("/students", require("./students"));
router.use("/auth", require("./auth"));
router.use("/dashboard", require("./dashboard"));
router.use("/attendance", require("./attendance"));

module.exports = router;
