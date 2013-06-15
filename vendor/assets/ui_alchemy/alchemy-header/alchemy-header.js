angular.module("alch-templates").run(["$templateCache", function($templateCache) {

  $templateCache.put("component/templates/dropdown.html",
    "<ul class=\"dropdown\"\n" +
    "    ng-class=\"{ 'dropdown-right' : isRight(dropdown.direction), 'dropdown-active' : dropdown.show }\">\n" +
    "  <li class=\"dropdown-item\"\n" +
    "      ng-repeat=\"item in dropdown\"\n" +
    "      ng-mouseenter=\"setHover(item, true)\"\n" +
    "      ng-mouseleave=\"setHover(item, false)\">\n" +
    "\n" +
    "    <a class=\"dropdown-item-link\"\n" +
    "       href=\"{{ item.url }}\"\n" +
    "       ng-class=\"{'menu-anchor' : item.type, 'dropdown-item-link-active' : item.active }\">\n" +
    "      <span class=\"fl\">{{ item.display }}</span>\n" +
    "      <i class=\"icon-caret-right flyout-indicator\" ng-show=\"item.type=='flyout'\"></i>\n" +
    "    </a>\n" +
    "    <ul alch-flyout=\"item.items\"\n" +
    "        ng-show=\"flyout.show\"\n" +
    "        ng-class=\"{ 'dropdown-active' : dropdown.show }\">\n" +
    "    </ul>\n" +
    "  </li>\n" +
    "</ul>\n"
  );

  $templateCache.put("component/templates/flyout.html",
    "<ul class=\"flyout\">\n" +
    "  <li class=\"flyout-item\"\n" +
    "      ng-repeat=\"item in flyout\"\n" +
    "      ng-class=\"{ 'dropdown-highlight' : item.active }\"\n" +
    "      ng-mouseenter=\"setHover(item, true)\"\n" +
    "      ng-mouseleave=\"setHover(item, false)\">\n" +
    "  \n" +
    "    <a class=\"flyout-item-link\" href=\"{{ item.url }}\">{{ item.display }}</a>\n" +
    "  </li>\n" +
    "</ul>\n"
  );

  $templateCache.put("component/templates/menu.html",
    "<nav ng-class=\"menu.location\">\n" +
    "  <ul class=\"menu-container\">\n" +
    "\n" +
    "    <li class=\"menu-item\"\n" +
    "        ng-repeat=\"item in menu.items\"\n" +
    "        ng-mouseenter=\"handleHover(item, true)\"\n" +
    "        ng-mouseleave=\"handleHover(item, false)\">\n" +
    "\n" +
    "        <a href=\"{{ item.url }}\"\n" +
    "           ng-class=\"{ 'active-item' : item.active, 'menu-anchor' : item.type }\"\n" +
    "           class=\"menu-item-link\"> \n" +
    "          <span ng-bind-html-unsafe=\"item.display\"></span>\n" +
    "         <i class=\"icon-caret-down\" ng-show=\"item.type == 'dropdown'\"></i>\n" +
    "        </a>\n" +
    "        <ul alch-dropdown=\"item.items\"></ul>\n" +
    "    </li>\n" +
    "  </ul>\n" +
    "</nav>\n"
  );

}]);

'use strict';

angular.module('alchemy').directive('alchDropdown', function(){
    return {
        restrict: 'EA',
        transclude: true,
        replace: true,
        scope: {
            'dropdown' : '=alchDropdown'
        },
        templateUrl: 'component/templates/dropdown.html',

        controller: ['$scope', function($scope) {
            $scope.setHover = function(item, mousein) {
                if (mousein) {
                    item.active = true;

                    if (item.type === 'flyout') {
                        $scope.flyout = item.items;
                        $scope.flyout.show = true;
                    }
                } else {
                    if ($scope.flyout) {
                        $scope.flyout.show = false;
                    }
                    item.active = false;
                }
            };

            $scope.isRight = function(direction) {
                return direction === 'right';
            };
        }]
    };
});

'use strict';

angular.module('alchemy').directive('alchFlyout', function(){
    return {
        restrict: 'EA',
        transclude: true,
        replace: true,
        scope: {
            'flyout' : '=alchFlyout'
        },
        templateUrl: 'component/templates/flyout.html',

        controller: ['$scope', function($scope) {
            $scope.setHover = function(item, mousein) {
                if (mousein) {
                    item.active = true;
                } else {
                    item.active = false;
                }
            };
        }]
    };
});

'use strict';

angular.module('alchemy').directive('alchMenu', ['$window', function($window){
    return {
        restrict: 'EA',
        transclude: true,
        replace: true,
        scope: {
            'menu': '=alchMenu',
            'compact' : '@'
        },
        templateUrl: 'component/templates/menu.html',
        controller: ['$scope', function($scope) {
            $scope.dropdown = {};

            $scope.handleHover = function(item, mousein) {
                if (item.type === 'dropdown' && mousein) {
                    item.active = true;
                    $scope.dropdown = item.items;
                    $scope.dropdown.show = true;
                    $scope.dropdown.direction = $scope.menu.location;
                } else {
                    $scope.dropdown.show = false;

                    if (item !== $scope.menu.activeItem) {
                        item.active = false;
                    }
                }
            };

        }],
        link: function(scope, element, attrs) {
            var elementOriginalOffset;

            if (attrs.compact !== undefined) {
                elementOriginalOffset = $(element).offset().top;

                angular.element($window).bind('scroll', function() {
                    var windowScrollTop = $($window).scrollTop();

                    if (windowScrollTop > elementOriginalOffset + 2) {
                        element.parent().addClass('compact');
                    } else if (windowScrollTop < elementOriginalOffset) {
                        element.parent().removeClass('compact');
                    }
                 });
            }
        }
    };
}]);
