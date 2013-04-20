angular.module("alch-templates").run(["$templateCache", function($templateCache) {
  $templateCache.put("component/templates/table.html",
    "<thead>" +
    "  <tr>" +
    "    <th class=\"table-selection-row\" " +
    "        colspan=\"{{ table.data.columns.length +1 }}\" " +
    "        ng-show=\"table.more_results()\">" +
    "" +
    "        All {{ table.offset }} results shown are currently selected.  " +
    "        <a href=\"\">Select all {{ table.total }} results.</a>" +
    "    </th>" +
    "  </tr>" +
    "  <tr>" +
    "    <th ng-show=\"rowSelect\">" +
    "      <input class=\"select_all\" " +
    "             type=\"checkbox\" " +
    "             name=\"select_all\" " +
    "             ng-model=\"table.all_selected\" " +
    "             ng-change=\"table.select_all()\">" +
    "    </th>" +
    "    <th ng-click=\"table.sort(header)\" " +
    "        ng-show=\"header.show\" " +
    "        ng-repeat=\"header in table.data.columns\" " +
    "        ng-class=\"{ 'active-column' : header.active }\">" +
    "" +
    "        {{ header.display }}" +
    "    </th>" +
    "  </tr>" +
    "</thead>" +
    "<tbody infinite-scroll=\"table.next_page()\" " +
    "       infinite-scroll-disable=\"table.loading_more\" " +
    "       infinite-scroll-distance=\"table.scroll_distance\">" +
    "  <tr ng-class=\"{active : row.selected }\" " +
    "      ng-repeat=\"row in table.data.rows\" " +
    "      ng-show=\"show_row(row)\">" +
    "    <td ng-show=\"rowSelect\">" +
    "      <input ng-model=\"row.selected\" " +
    "             type=\"checkbox\" name=\"{{ row.id }}\" " +
    "             value=\"{{ row.id }}\" " +
    "             ng-change=\"adjust_num_selected(row.selected)\">" +
    "    </td>" +
    "    <td ng-show=\"show_cell(cell)\" " +
    "        ng-repeat=\"cell in row.cells\">" +
    "      " +
    "        {{ cell.display }}" +
    "    </td>" +
    "  </tr>" +
    "</tbody>" +
    "");
}]);

angular.module("alch-templates").run(["$templateCache", function($templateCache) {
  $templateCache.put("component/templates/tool_bar.html",
    "<div ng-model=\"table.data.columns\" class=\"form table-toolbar\">" +
    "  <div class=\"fl\">" +
    "    <input type=\"text\" " +
    "           class=\"input\" " +
    "           placeholder=\"Search...\" " +
    "           ng-model=\"table.search_string\" " +
    "           on-enter=\"table.search(table.search_string)\"" +
    "    />" +
    "    Showing {{ table.start }}-{{ table.offset }} of {{ table.total }} {{ table.model }}" +
    "  </div>" +
    "  <div class=\"fr deselect\" ng-show=\"table.num_selected\">" +
    "    <span ng-model=\"table.num_selected\">{{ table.num_selected }} Selected</span>" +
    "    <a ng-click=\"deselect_all()\" href=\"\">Deselect All</a>" +
    "  </div>" +
    "</div>" +
    "");
}]);

'use strict';

angular.module('alchemy').directive('alchTable', function(){
    return {
        restrict: 'A',
        scope: {
            'table' : '=alchTable',
            'rowSelect' : '@'
        },
        templateUrl: 'component/templates/table.html',

        controller: ['$scope', function($scope){
            if (!$scope.table.scroll_distance) {
                $scope.table.scroll_distance = 0;
            }

            $scope.show_cell = function(cell){
                var to_show;

                angular.forEach($scope.table.data.columns, function(header){
                    if( header.id === cell.column_id ){
                        to_show = header.show;
                    }
                });

                return to_show;
            };

            $scope.show_row = function(row){
                return row.show;
            };

            $scope.adjust_num_selected = function(selected){
                $scope.table.num_selected += selected ? 1 : -1;
            };

            $scope.table.select_all = function(selected){
                var table = $scope.table;

                if( selected !== undefined ){
                    table.all_selected = selected;
                }

                table.num_selected = table.all_selected ? table.data.rows.length : 0;

                angular.forEach(table.data.rows, function(row){
                    row.selected = table.all_selected;
                });
            };

            $scope.table.more_results = function(){
                var more = $scope.table.total > $scope.table.offset;

                more = more && $scope.table.all_selected;
                return more;
            };
        }]
    };
});

angular.module('alchemy').directive('alchTableToolbar', function(){
    return {
        restrict: 'A',
        transclude: true,
        scope: {
            'table' : '=alchTableToolbar'
        },
        templateUrl: 'component/templates/tool_bar.html',

        controller: ['$scope', function($scope){
            $scope.deselect_all = function(){
                $scope.table.select_all(false);
            };
        }]
    };
});
