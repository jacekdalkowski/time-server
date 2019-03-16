'use strict';

import moment from 'moment';
import restifyErrors from 'restify-errors';

module.exports = class TimeController {

  constructor() {
    this.time = new Date();  
    this.getTime = this.getTime.bind(this);
    this.setTime = this.setTime.bind(this);
  }

  getTime(req, res, next) {
    res.json({
      time: moment(this.time).format()
    });
  }

  setTime(req, res, next) {
    const inputTimeString = req.body.time;
    if (moment(inputTimeString, moment.ISO_8601).isValid()) {
      this.time = moment.utc(inputTimeString);
      res.json({
        time: moment(this.time).format()
      });
    } else {
      next(new restifyErrors.BadRequestError('Time parameter string has to be provided in ISO 8601 format.'));
    }
  }
}

