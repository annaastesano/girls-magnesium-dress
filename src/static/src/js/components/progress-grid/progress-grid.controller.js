goog.module('dmb.components.progressGrid.controller');

/**
 * ProgressGrid class controller.
 */
class ProgressGridController {
  /**
   * ProgressGrid controller
   *
   * @param {function (*): number|null} floorDmbFactory
   * @param {!Object} tenantConf
   *
   * @ngInject
   */
  constructor(
    floorDmbFactory,
    tenantConf) {
    /**
     * @type {function (*): number|null}
     * @private
     */
    this.floorDmbFactory_ = floorDmbFactory;

    /**
     * @export
     * type {Object}
     */
    this.levels = tenantConf.levels;

    /**
     * @export
     * type {Object}
     */
    this.levelsTotal = Object.keys(this.levels).length;

    /**
     * @export
     * type {boolean}
     */
    this.verticalOverflow = null;

    /**
     * @export
     * type {boolean}
     */
    this.horizontalOverflow = null;
  }

  /**
   * Function to get a rounded level value from a value
   * @param {number} value
   * @return {string}
   * @export
   */
  getLevel(value) {
    return Math.min(Math.floor(value), (this.levelsTotal - 1));
  }

  /**
   * Function to get the level name from the value
   * @param {number} value
   * @return {string}
   * @export
   */
  getLevelName(value) {
    const level = this.getLevel(value);
    return this.levels[level];
  }

  /**
   * Function to get the progressw width/height for the horizontal and vertical bars
   * @param {number} value
   * @return {string}
   * @export
   */
  getProgress(value) {
    const prog = value * 100;
    this.verticalOverflow = this.verticalOverflow || value > 3.2;
    this.horizontalOverflow = this.horizontalOverflow || value > 3.83;
    return `${prog}%`;
  }
}


/** @const {string} */
ProgressGridController.CONTROLLER_NAME = 'ProgressGridCtrl';


/** @const {string} */
ProgressGridController.CONTROLLER_AS_NAME = 'progressGridCtrl';


exports = {
  main: ProgressGridController,
  CONTROLLER_NAME: ProgressGridController.CONTROLLER_NAME,
  CONTROLLER_AS_NAME: ProgressGridController.CONTROLLER_AS_NAME,
};
