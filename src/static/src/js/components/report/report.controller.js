goog.module('dmb.components.report.controller');

const BreakpointService = goog.require('glue.ng.common.Breakpoint');
const PaginationModel = goog.require('glue.ng.pagination.Model');

const surveyEndpoint = '/api/report/company/';
const industryEndpoint = '/api/report/industry/';
const locationSidRegex = /reports\/(\w+)[#\/].*$/;


/**
 * Report class controller
 */
class ReportController {
  /**
   * Report controller
   *
   * @param {!angular.Scope} $scope
   * @param {!angular.$http} $http
   * @param {!angular.$location} $location
   * @param {!glue.ng.state.StateService} glueState
   * @param {!angular.$timeout} $timeout
   * @param {!Object} reportService
   * @param {!Function} floorDmbFactory
   * @param {!Object} dimensionHeaders
   * @param {!Object} glueBreakpoint
   *
   * @ngInject
   */
  constructor(
      $scope,
      $http,
      $location,
      glueState,
      $timeout,
      reportService,
      floorDmbFactory,
      dimensionHeaders,
      glueBreakpoint) {
    const sidMatches = $location.absUrl().match(locationSidRegex);
    const surveyId = sidMatches ? sidMatches[1] : null;

    /** @private {!glue.ng.state.StateService} */
    this.glueState_ = glueState;

    /** @private {!angular.$timeout} */
    this.ngTimeout_ = $timeout;

    /**
     * Survey object.
     * @type {Object}
     * @export
     */
    this.survey = null;

    /**
     * Survey result object.
     * @type {Object}
     * @export
     */
    this.result = null;

    /**
     * Floored dmb.
     * @type {?number}
     * @export
     */
    this.floorDmb = null;

    /**
     *  Show dimensions tab (instead of the zippy).
     * @type {!bool}
     * @export
     */
    this.showTabs = this.showTabs_(glueBreakpoint.getBreakpointSize());

    /**
     * Floored dmb.
     * @type {!object}
     * @export
     */
    this.dimensionHeaders = dimensionHeaders;

    /**
     * @export
     * @type {Array.<string>}
     */
    this.dimensions = [
      'attribution',
      'ads',
      'audience',
      'access',
      'automation',
      'organization',
    ];

       /**
     * @type {glue.ng.pagination.Model}
     * @export
     */
    this.model = new PaginationModel({
      'activeEl': this.dimensions[0],
    });

    /**
     * Industry result object.
     * @type {Object}
     * @export
     */
    this.industryResult = null;

    // We're saving the results in a service since it's not possible to
    // directly pass them to the directive throught the bindings since
    // the tab component messes up the scopes. We use a service instead.
    $http.get(`${surveyEndpoint}${surveyId}`).then((res)=> {
      this.survey = res.data;
      this.result = this.survey['last_survey_result'];

      // DRF returns decimal fields as strings. We should probably look into this
      // on the BE but until we do let's fix this on the FE.
      this.result.dmb = parseFloat(this.result['dmb']);

      this.floorDmb = floorDmbFactory(this.result.dmb);

      reportService.dmb_d = this.result['dmb_d'];

      $http.get(`${industryEndpoint}${this.survey['industry']}`).then((res) => {
        this.industryResult = res.data;
        reportService.industryDmb_d = this.industryResult['dmb_d'];
        reportService.industryDmb_d_bp = this.industryResult['dmb_d_bp'];
      });
    });

    $scope.$on(BreakpointService.service.BREAK_POINT_UPDATE_EVENT, (e, size) => {
      this.showTabs= this.showTabs_(size);
      $scope.$apply();
    });
  }

  /**
   *  @param {string} size
   *  @return {bool}
   *  @private
   */
  showTabs_(size) {
    const bpTabsEnabled = [
      'large',
      'x-large',
      'xx-large',
      'medium-large',
      'medium',
    ];

    return bpTabsEnabled.indexOf(size) > -1;
  }

    /**
   * Opens a specific tab if state is enabled. This is expected to be used with
   * something like ngClick.
   *
   * @param {string} tabsetId The unique state id for the tabset.
   * @param {string} elementId The unique id of the tab to open.
   * @export
   */
  selectTab(tabsetId, elementId) {
    this.ngTimeout_(() => {
      this.glueState_.setState(tabsetId, {
        'activeEl': elementId,
      });
    }, 0, true);
  }
}


/** @const {string} */
ReportController.CONTROLLER_NAME = 'ReportCtrl';


/** @const {string} */
ReportController.CONTROLLER_AS_NAME = 'reportCtrl';


exports = {
  main: ReportController,
  CONTROLLER_NAME: ReportController.CONTROLLER_NAME,
  CONTROLLER_AS_NAME: ReportController.CONTROLLER_AS_NAME,
};