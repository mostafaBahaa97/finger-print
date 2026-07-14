const CACHE_NAME = 'basmaty-v1';
const ASSETS_TO_CACHE = [
  './',
  './index.html',
  './manifest.json',
  './mostafa.ico',
  './watermarked_img_6559831621308037342.png'
];

// تثبيت الـ Service Worker وتخزين الملفات الأساسية في الكاش
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.addAll(ASSETS_TO_CACHE);
    })
  );
});

// تفعيل وتحسين إدارة الكاش عند التحديث
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) => {
      return Promise.all(
        keys.map((key) => {
          if (key !== CACHE_NAME) {
            return caches.delete(key);
          }
        })
      );
    })
  );
});

// استراتيجية جلب البيانات (Network-first لطلبات الـ API، و Cache-first للملفات الثابتة)
self.addEventListener('fetch', (event) => {
  // عدم تخزين طلبات Google Sheets (POST/GET API) في الكاش لضمان تحديث البيانات دائماً
  if (event.request.url.includes('script.google.com')) {
    return;
  }

  event.respondWith(
    caches.match(event.request).then((cachedResponse) => {
      return cachedResponse || fetch(event.request);
    })
  );
});