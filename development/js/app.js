/**
 * Created by Shtav on 5/16/15.
 */

app = angular.module('myApp', ['ui.bootstrap']);

app.controller('MainCtrl', ['$scope', '$interval', '$modal', '$http', function($scope, $interval, $modal, $http) {

  /* processed movie data*/
  /*delete begin*/$http.get('data/movies.json').success(function(data) { $scope.movies = data; });/*delete end*/

  $scope.moviesRevealed = -1;
  function revealMovie(){
    $scope.moviesRevealed++;
    if ($scope.moviesRevealed > 6) {
      $interval.cancel(revealMovieInterval);
    }
  }
  var revealMovieInterval = $interval(revealMovie, 300);



  function openModal(movie) {
    var modalInstance = $modal.open({
      templateUrl: 'templates/modal.html',
      controller: 'ModalInstanceCtrl',
      resolve: { movie: function () { return movie; } },
      size: 'lg'
    });
  }
  $scope.openModal = openModal;
}]);

app.controller('ModalInstanceCtrl', function ($scope, $modalInstance, movie, $sce, $window) {

  $scope.movie = movie;
  $scope.url = $sce.trustAsResourceUrl('http://www.youtube.com/embed/' + movie.trailer_youtube_id + '?autoplay=1&html5=1');

  $scope.ok = function () { $modalInstance.close(); };

  $scope.cancel = function () { $modalInstance.dismiss('cancel'); };

  $scope.redirectTo = function(url){
    if (url !== '') {
      $window.open(url, '_blank');
    }
  };

});

