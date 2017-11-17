
Skip to content
This repository

    Pull requests
    Issues
    Marketplace
    Explore

    @Austin0077

0
1

    3

Austin0077/moviemango-pwa forked from jfkm69/moviemango-pwa
Code
Pull requests 0
Projects 0
Wiki
Insights
Settings
moviemango-pwa/service-worker.js
e25d56c 5 minutes ago
@jfkm69 jfkm69 Added service worker and manifest
42 lines (37 sloc) 1004 Bytes
var cacheName = 'moviemango';
var filesToCache = [
	'/moviemango/index.html',
	'/moviemango/scripts/app.js',
	'/moviemango/css/style.css',
];

self.addEventListener('install', function(e){
	console.log('[ServiceWorker] Install');
	e.waitUntil(
		caches.open(cacheName).then(function(cache){
			console.log('[ServiceWorker] caching app shell');
			return cache.addAll(filesToCache);
		})
	);
});

self.addEventListener('activate', function(e) {

  console.log('[ServiceWorker] Activate');

  e.waitUntil(
  	caches.keys().then(function(keyList) {
  		return Promise.all(keyList.map(function(key) {
  			if (key !== cacheName) {
  				console.log('[ServiceWorker] Removing old cache', key);
  				return caches.delete(key);
  			}
  		}));
  	})
  );
  return self.clients.claim();
});

self.addEventListener('fetch', function(e) {
	console.log('[ServiceWorker] Fetch', e.request.url);
	e.respondWith(
		caches.match(e.request).then(function(response) {
			return response || fetch(e.request);
		})
	);
});

    © 2017 GitHub, Inc.
    Terms
    Privacy
    Security
    Status
    Help

    Contact GitHub
    API
    Training
    Shop
    Blog
    About

