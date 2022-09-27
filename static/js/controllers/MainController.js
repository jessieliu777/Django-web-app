// scope is something everyone can talk to
app.controller('MainController', function($scope, $http, $log, MainService) {
    var va = this;
    $scope.greeting = "Welcome!";
    $scope.products = [];
    $scope.page = 0;
    $scope.page_size = 10;
    $scope.get = function() {
        MainService.get('/api/products/' + '?page=' + $scope.page + '&page_size=' + $scope.page_size)
        .then(function(res){
          $scope.products = res;
        },function(err) {
          console.error('Error while getting data');
        });
    };

    $scope.getCategories = function() {
        MainService.get('/api/categories/').then(function(res){
          $scope.categories = res;
        });
    };

    $scope.getTags= function() {
        MainService.get('/api/tags/').then(function(res){
          $scope.tags = res;
        });
    };

    $scope.get();
    $scope.getCategories();
    $scope.getTags();

    $scope.newProduct = {};
    $scope.newCategory = {};
    $scope.newTags = {};

    $scope.errors = {};

    $scope.post = function() {
        MainService.post('/api/products/', $scope.newProduct, $scope.errors)
        .then(function(res){
          $scope.newProduct = {};
        }, function(err) {
            console.error('Error while posting product');
        });
    };

    $scope.postCategory = function() {
        MainService.post('/api/categories/', $scope.newCategory, $scope.errors).then(function(res){
          $scope.newCategory = {};
        }, function(err) {
            console.error('Error while posting category');
        });
    };

    $scope.query = {};
    $scope.keyword = '';

    $scope.searchProducts = function(product) {
        searchName = product.name.toLowerCase().includes($scope.keyword.toLowerCase());
        searchCategory = product.category.name.toLowerCase().includes($scope.keyword.toLowerCase());
        searchTag = false;
        for (let i = 0; i < product.tag.length; i++) {
            searchTag = searchTag || (product.tag[i].name.toLowerCase().includes($scope.keyword.toLowerCase()));
            // if none of the product tags contains query tag, then the product doesn't contain it
            if (searchTag) break;
        }
        return searchName || searchCategory || searchTag;
    };

    $scope.filterProducts = function(product) {
        filterName = true;
        filterCategory = true;
        filterTag = true;
        if ($scope.query.name){
            filterName = product.name.toLowerCase().includes($scope.query.name.toLowerCase());
        }
        if ($scope.query.category){
            filterCategory = product.category.id === $scope.query.category.id;
        }
        if ($scope.query.tag){
            for (let i = 0; i < $scope.query.tag.length; i++) {
                ithFilter = false;
                // as long as one product tag contains the query tag, then the product contains the query tag
                for (let j = 0; j < product.tag.length; j++){
                    ithFilter = ithFilter || (product.tag[j].id == $scope.query.tag[i].id);
                    if (ithFilter) break;
                }
                filterTag = filterTag && ithFilter;
                // if none of the product tags contains query tag, then the product doesn't contain it
                if (!filterTag) break;
            }
        }
        return filterName && filterCategory && filterTag;
      };
    });

app.config(['$httpProvider', function ($httpProvider) {
        $httpProvider.defaults.headers.post['Content-Type'] = 'application/json';
}]);