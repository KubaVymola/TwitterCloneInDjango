const gulp = require('gulp');
const gulpIf = require('gulp-if');
const inlineSource = require('gulp-inline-source');
const rename = require('gulp-rename');
const shell = require('gulp-shell');

const appName = 'twitter';
const destinationDir = './dist/';


gulp.task('images', function() { 
	imagemin = require('gulp-imagemin');

	return gulp.src('./src/images/*')
		.pipe(imagemin())
		.pipe(gulp.dest(`${ destinationDir }images/`));

});


gulp.task('js', function() {
	const babel = require('gulp-babel');
	const uglify = require('gulp-uglify');
	const concat = require('gulp-concat');

	return gulp.src('./src/js/*.js')
		.pipe(concat('main.js', { newLine: '\r\n' }))
		.pipe(babel( { presets: ['@babel/env'] } ))
		.pipe(uglify())
		.pipe(gulp.dest(`${ destinationDir }js/`));

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
		.pipe(concat('style.css'))
		.pipe(autoprefixer())
		.pipe(cleancss( { compatibility: 'ie10' } ))
		.pipe(sourcemaps.write('.'))
		.pipe(gulp.dest(`${ destinationDir }style/`));
});


gulp.task('default', gulp.parallel('images', 'js', 'css'));


gulp.task('watch', function() {
	browserSync = require('browser-sync')

	browserSync.init({
        notify: false,
		proxy: "localhost:8000"
	});
	
	gulp.watch('src/js/*.js', gulp.series('js'));
	gulp.watch('src/style/*.css', gulp.series('css'));

	gulp.watch(['./dist/**/*.{css,html,js,py}']).on('change', browserSync.reload);
	gulp.watch(['./src/**/*.{html,py}']).on('change', browserSync.reload);
});