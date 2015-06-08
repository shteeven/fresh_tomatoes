//TEST PURPOSE ONLY
/**
 * Created by Shtav on 5/25/15.
 */
app.factory('movieDataFactory', function($http){

  function Movie(title, story_line, poster_image, trailer_youtube_url, imdb, itunes, amazon) {
    this.title = title;
    this.story_line = story_line;
    this.poster_image_url = poster_image;
    this.trailer_youtube_url = trailer_youtube_url;
    this.imdb = imdb;
    this.itunes = itunes;
    this.amazon = amazon;
  }

  toy_story = new Movie('Toy Story',
    'A story of a boy and his toys that come to life',
    'http://www.rotoscopers.com/wp-content/uploads/2013/10/Toy-Story-Poster.jpg',
    'https://youtu.be/KYz2wyBy3kc',
    'http://www.imdb.com/title/tt0114709/',
    '',
    '');

  the_great_dictator = new Movie('The Great Dictator',
    'A Jewish Barber is mistaken for the dictator that has been terrorizing the world.',
    'http://shelleysdavies.com/wp-content/uploads/2012/11/olly-moss-the-great-dictator.jpg',
    'https://www.youtube.com/watch?v=4sfJxdytYn4',
    'http://www.imdb.com/title/tt0032553/',
    '',
    '');

  manos = new Movie('Manos: The Hands of Fate',
    'A family gets lost on the road and stumbles upon a hidden, underground, devil-worshiping cult led by the fearsome Master and his servant Torgo.',
    'http://ia.media-imdb.com/images/M/MV5BMTI1NTg1MTE3MF5BMl5BanBnXkFtZTcwNzA4NDgyMQ@@._V1_SX640_SY720_.jpg',
    'https://www.youtube.com/watch?v=tRcGukCdr3c',
    'http://www.imdb.com/title/tt0060666/',
    '',
    'http://www.amazon.com/Manos-Hands-Fate-Bettie-Burns/dp/B0000AGWMF');

  gigli = new Movie('Gigli',
    'The violent story about how a criminal lesbian, a tough-guy hit-man with a heart of gold, and a mentally challenged man came to be best friends through a hostage.',
    'http://ia.media-imdb.com/images/M/MV5BMTE5MTYxMDg5NV5BMl5BanBnXkFtZTYwNjc5MzQ3._V1_SX640_SY720_.jpg',
    'https://www.youtube.com/watch?v=8UhCCHFZugE',
    'http://www.imdb.com/title/tt0299930/',
    '',
    '');

  the_danish_poet = new Movie('The Danish Poet',
    'A woman ponders over the strange coincidences that made her forefathers and -mothers meet and create the premises for her becoming the person that she is.',
    'https://image.tmdb.org/t/p/w500/sB9uqoD1GxCPLXzZyKMvw7ulGzH.jpg',
    'https://www.youtube.com/watch?v=mREkFAWiaLA',
    'http://www.imdb.com/title/tt0933357/',
    '',
    '');

  avatar = new Movie('Avatar',
    'A man is sent to live with alien creatures through an avatar',
    'http://cafmp.com/wp-content/uploads/2012/11/French-Avatar-Poster',
    'https://youtu.be/5PSNL1qE6VY',
    'http://www.imdb.com/title/tt0499549/',
    '',
    '');



  //return [the_great_dictator, avatar, toy_story, manos, gigli, the_danish_poet];




  return $http.get('movies/processed_data.json');

});