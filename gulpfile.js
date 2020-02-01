const gulp = require('gulp');
const gulpIf = require('gulp-if');
const inlineSource = require('gulp-inline-source');
const rename = require('gulp-rename');
const exec = require('child_process').exec;

const appName = 'twitter';


gulp.task('images', function() { 
	imagemin = require('gulp-imagemin');

	return gulp.src('./src/images/*')
		.pipe(imagemin())
		.pipe(gulp.dest(`./src/${ appName }/static/images/`));

});


gulp.task('js', function() {
	const babel = require('gulp-babel');
	const uglify = require('gulp-uglify');
	const concat = require('gulp-concat');

	return gulp.src('./src/js/*.js')
		.pipe(concat('main.js', { newLine: '\r\n' }))
		.pipe(babel( { presets: ['@babel/env'] } ))
		.pipe(uglify())
		.pipe(gulp.dest(`./src/${ appName }/static/js/`));
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
		.pipe(gulp.dest(`./src/${ appName }/static/style/`));
});


gulp.task('default', gulp.parallel('images', 'js', 'css'));


/*gulp.task('update', function(cb) {
	exec(`python src/${ appName}/manage.py collectstatic --noinput`);
});

gulp.task('runserver', function(cb) {
	console.log('Starting python server');

	var proc = exec(`python src/${ appName }/manage.py runserver &`);
});

gulp.task('sync', function() {
	browserSync.init( {
		notify: true,
		port: 8000,
		proxy: 'localhost:8000'
	});

	// console.log('Server is running...');
}); */

gulp.task('watch', function() {
	gulp.watch('src/js/*.js', gulp.series('js'));
	gulp.watch('src/style/*.css', gulp.series('css'));

	return;
});