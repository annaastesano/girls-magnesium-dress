goog.module('dmb.components.progressTable.directive');

const progTableCtrl = goog.require('dmb.components.progressTable.controller');
const progressTableTemplate = goog.require('dmb.components.progressTable.template');

/**
 * Side panel directive.
 * @ngInject
 * @return {Object} Config for the directive
 */
function ReportDirective() {
  return {
    restrict: 'E',
    scope: {
      'companyName': '@',
      'industryAvg': '<',
      'industryBest': '<',
      'ratingMain': '<',
    },
    controller: progTableCtrl.main,
    controllerAs: progTableCtrl.CONTROLLER_AS_NAME,
    template: progressTableTemplate,
  };
}


/** @const {string} */
ReportDirective.DIRECTIVE_NAME = 'dmbProgressTable';


exports = {
  main: ReportDirective,
  DIRECTIVE_NAME: ReportDirective.DIRECTIVE_NAME,
};

/*
EXAMPLE HTML

<dmb-progress-table
  data-rating-main="reportCtrl.result.dmb"
  data-industry-avg="reportCtrl.industryResult.dmb"
  data-industry-best="reportCtrl.industryResult.dmb_bp"
  data-company-name="{[reportCtrl.survey.company_name]}">
</dmb-progress-table>

*/
