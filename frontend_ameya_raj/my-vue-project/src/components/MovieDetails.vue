<template>
    <div>
      <NavBar />
      <div v-if="movie" class="min-h-screen bg-gray-900">
        <div class="relative pt-16"> 
          <div class="absolute inset-0">
            <img :src="movie.Poster" class="w-full h-full object-cover opacity-40 fixed" />
            <div class="absolute inset-0 bg-gradient-to-r from-black/80 to-black/50"></div>
          </div>
          
          <div class="container mx-auto px-4 relative z-10 py-8">
            <div class="flex flex-col md:flex-row gap-8">
              <div class="w-64 flex-shrink-0 transform hover:scale-105 transition-all duration-300">
                <img :src="movie.Poster" class="rounded-lg shadow-2xl w-full" />
              </div>
              <div class="text-white">
                <h1 class="text-4xl md:text-5xl font-bold mb-4 bg-clip-text text-transparent bg-gradient-to-r from-white to-gray-300">
                  {{ movie.Title }}
                </h1>
                <div class="text-gray-300 mb-6 flex flex-wrap gap-2 items-center">
                  <span>{{ movie.Released }}</span>
                  <span class="w-2 h-2 rounded-full bg-gray-500"></span>
                  <span>{{ movie.Runtime }}</span>
                  <span class="w-2 h-2 rounded-full bg-gray-500"></span>
                  <span class="px-2 py-1 rounded bg-gray-800">{{ movie.Rated }}</span>
                </div>
                <div class="flex gap-6 mb-8">
                  <div class="bg-gray-800/80 backdrop-blur rounded-xl p-4 transform hover:scale-105 transition-all">
                    <div class="text-center">
                      <div class="font-bold text-2xl">{{ movie.imdbRating }}</div>
                      <div class="text-sm text-gray-400">IMDb Rating</div>
                    </div>
                  </div>
                  <button class="bg-gray-800/80 backdrop-blur rounded-xl px-6 flex items-center gap-2 hover:bg-gray-700 transition-colors">
                    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z" />
                    </svg>
                    Like
                  </button>
                </div>
                <div class="mb-8 max-w-2xl">
                  <h3 class="text-2xl font-semibold mb-4">Overview</h3>
                  <p class="text-gray-300 leading-relaxed">{{ movie.Plot }}</p>
                </div>
                <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                  <div class="backdrop-blur bg-gray-800/30 p-4 rounded-lg">
                    <div class="font-semibold mb-2">Director</div>
                    <div class="text-gray-300">{{ movie.Director }}</div>
                  </div>
                  <div class="backdrop-blur bg-gray-800/30 p-4 rounded-lg">
                    <div class="font-semibold mb-2">Writers</div>
                    <div class="text-gray-300">{{ movie.Writer }}</div>
                  </div>
                  <div class="backdrop-blur bg-gray-800/30 p-4 rounded-lg">
                    <div class="font-semibold mb-2">Stars</div>
                    <div class="text-gray-300">{{ movie.Actors }}</div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import NavBar from './NavBar.vue';
  
  export default {
    name: 'MovieDetails',
    components: {
      NavBar
    },
    data() {
      return {
        movie: null
      };
    },
    async created() {
      try {
        const response = await fetch('http://www.omdbapi.com/?i=tt3896198&apikey=d2132124');
        this.movie = await response.json();
      } catch (error) {
        console.error('Error fetching movie data:', error);
      }
    }
  };
  </script>
  
  <style>
  ::-webkit-scrollbar {
    width: 8px;
  }
  
  ::-webkit-scrollbar-track {
    background: rgba(255, 255, 255, 0.1);
  }
  
  ::-webkit-scrollbar-thumb {
    background: rgba(255, 255, 255, 0.5);
    border-radius: 4px;
  }
  
  ::-webkit-scrollbar-thumb:hover {
    background: rgba(255, 255, 255, 0.7);
  }
  </style>