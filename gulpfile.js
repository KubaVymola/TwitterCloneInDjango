gulp = require('gulp');
gulpIf = require('gulp-if');
inlineSource = require('gulp-inline-source');
rename = require('gulp-rename');


gulp.task('media', function() { 
	imagemin = require('gulp-imagemin');

	return gulp.src('./src/images/*')
		.pipe(imagemin())
		.pipe(gulp.dest('./dist/images/'));

});


gulp.task('js', function() {
	const babel = require('gulp-babel');
	const uglify = require('gulp-uglify');
	const concat = require('gulp-concat');

	return gulp.src('./src/js/*.js')
		.pipe(concat('main.js', { newLine: '\r\n' }))
		.pipe(babel( { presets: ['@babel/env'] } ))
		.pipe(uglify())
		.pipe(gulp.dest('./dist/js/'));
});


/* 
  TODO: Supported browsers to autoprefixer
  TODO: Compile css from sass
*/
gulp.task('css', function() {
	const concat = require('gulp-concat');
	const autoprefixer = require('gulp-autoprefixer');
	const sourcemaps = require('gulp-sourcemaps');
	// const sass = require('gulp-sass');
	const cleancss = require('gulp-clean-css');
	const postcss = require('gulp-postcss');

	return gulp.src('./src/style/*.css')
		.pipe(sourcemaps.init())
		.pipe(autoprefixer())
		.pipe(concat('style.css'))
		.pipe(cleancss( { compatibility: 'ie10' } ))
		.pipe(sourcemaps.write('.'))
		.pipe(gulp.dest('./dist/style/'));

});


gulp.task('default', gulp.parallel('media', 'js', 'css'));
