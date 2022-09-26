app.factory('MainService', function($http, $log) {
    var MainService = {
        get: function(url, query){
            return $http.get(url).then(function(res) {
                return res.data;
            }, function(err) {
                console.error('Error while getting data');
            });
        },

        post: function(url, obj, errs){
            return $http.post(url, obj, errs)
            .then(function(res) {
            }, function(err) {
                console.error('Error while posting data');
            });
        }
    };
    return MainService;
});