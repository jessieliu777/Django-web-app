// scope is something everyone can talk to
app.controller('MainController', function ($scope, $http, $log, MainService) {
    var va = this;
    va.greeting = "Welcome!";
    va.products = [];
    va.categories = [];
    va.tags = [];
    va.page = 1;
    va.page_size = 100;
    va.newProduct = {};
//    $scope.newCategory = {};

    va.errors = {};
    va.query = {};
    va.keyword = '';

    va.getProducts = getProducts;
    va.getCategories = getCategories;
    va.getTags = getTags;
    va.postProduct = postProduct;
    va.searchProducts = searchProducts;
    va.filterProducts = filterProducts;

    function getProducts() {
        MainService.get('/api/products/' + '?page=' + va.page + '&page_size=' + va.page_size)
        .then(function(res){
          va.products = res;
        },function(err) {
          console.error('Error while getting products');
        });
    };

    function getCategories() {
        MainService.get('/api/categories/').then(function(res){
          va.categories = res;
        });
    };

    function getTags() {
        MainService.get('/api/tags/').then(function(res){
          va.tags = res;
        });
    };

    va.getProducts();
    va.getCategories();
    va.getTags();

    function postProduct() {
        MainService.post('/api/products/', va.newProduct, $scope.errors)
        .then(function(res){
          va.newProduct = {};
        }, function(err) {
            console.error('Error while posting product');
        });
    };

//    $scope.postCategory = function() {
//        MainService.post('/api/categories/', $scope.newCategory, $scope.errors).then(function(res){
//          $scope.newCategory = {};
//        }, function(err) {
//            console.error('Error while posting category');
//        });
//    };


   function searchProducts(product) {
        if (!product) return;
        if (!product.name || !product.category) return;
        // the following wouldn't break since empty string can still be converted to lower case
        searchName = product.name.toLowerCase().includes(va.keyword.toLowerCase());
        searchCategory = product.category.name.toLowerCase().includes(va.keyword.toLowerCase());
        searchTag = false;
        for (let i = 0; i < product.tag.length; i++) {
            searchTag = searchTag || (product.tag[i].name.toLowerCase().includes(va.keyword.toLowerCase()));
            // if none of the product tags contains query tag, then the product doesn't contain it
            if (searchTag) break;
        }
        return searchName || searchCategory || searchTag;
    };

    function filterProducts(product) {
        if (!product) return;
        if (!product.name || !product.category) return;
        filterName = true;
        filterCategory = true;
        filterTag = true;
        if (va.query.name){
            filterName = product.name.toLowerCase().includes(va.query.name.toLowerCase());
        }
        if (va.query.category){
            filterCategory = product.category.id === va.query.category.id;
        }
        if (va.query.tag){
            for (let i = 0; i < va.query.tag.length; i++) {
                ithFilter = false;
                // as long as one product tag contains the query tag, then the product contains the query tag
                for (let j = 0; j < product.tag.length; j++){
                    ithFilter = ithFilter || (product.tag[j].id == va.query.tag[i].id);
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