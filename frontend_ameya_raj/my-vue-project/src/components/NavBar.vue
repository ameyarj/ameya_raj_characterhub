<template>
    <nav class="bg-gray-900 fixed w-full z-50">
      <div class="container mx-auto px-4">
        <div class="flex items-center justify-between h-16">
          <div class="flex items-center">
            <span class="text-white font-bold text-2xl">TMDB</span>
          </div>
          
          <div class="hidden md:flex items-center space-x-8">
            <a href="#" class="text-gray-300 hover:text-white">Movies</a>
            <a href="#" class="text-gray-300 hover:text-white">TV Shows</a>
            <a href="#" class="text-gray-300 hover:text-white">People</a>
          </div>
          
          <button @click="toggleMenu" class="md:hidden text-gray-300">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16m-7 6h7" />
            </svg>
          </button>
        </div>
      </div>
      
      <div v-if="isMenuOpen" class="md:hidden bg-gray-800">
        <a href="#" class="block px-4 py-2 text-gray-300 hover:text-white">Movies</a>
        <a href="#" class="block px-4 py-2 text-gray-300 hover:text-white">TV Shows</a>
        <a href="#" class="block px-4 py-2 text-gray-300 hover:text-white">People</a>
      </div>
    </nav>
</template>

<script>
export default {
  data() {
    return {
      isMenuOpen: false
    }
  },
  methods: {
    toggleMenu() {
      this.isMenuOpen = !this.isMenuOpen
    }
  }
}
</script>

<style>
nav {
  transition: background-color 0.3s;
}
</style>
