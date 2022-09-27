app.factory('MainService', function($http, $log) {
    var MainService = {
        get: function(url, query){
            return $http.get(url).then(function(res) {
                return res.data;
            })
        },

        post: function(url, obj, errs){
            return $http.post(url, obj, errs)
            .then(function(res) {
            });
        }
    };
    return MainService;
});