goog.module('dmb.tableCustomSort');

const configureAdditionalSortTypes = function (glueTableSortServiceProvider) {
  glueTableSortServiceProvider.setSortType('datetime-custom', function (a, b) {
    const dateA = Date.parse(a.split('utc=')[1]);
    const dateB = Date.parse(b.split('utc=')[1]);

    return dateB < dateA ? 1 : -1;
  });

  glueTableSortServiceProvider.setDefaultSortTypes();
};

exports = configureAdditionalSortTypes;