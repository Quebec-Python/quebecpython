module.exports = function(grunt) {

  // Project configuration.
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    less: {
      development: {
        options: {
          compress: true,
          cleancss: true
        },
        files: {
          "css/main.min.css": "css/src/main.less"
        }
      }
    },
    watch: {
        less: {
          files: "css/src/*.less",
          tasks: ["less"]
        }
    }
  });

  grunt.loadNpmTasks('grunt-contrib-less');
  grunt.loadNpmTasks('grunt-contrib-watch');

  // Default task(s).
  grunt.registerTask('default', ['less', 'watch']);
};