const express = require("express");
const router = express.Router();

router.use("/attendance", require("./attendance"));

module.exports = router;
