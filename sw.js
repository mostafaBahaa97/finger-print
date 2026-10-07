const CACHE_NAME = 'basmaty-v3';
const ASSETS_TO_CACHE = [
  './',
  './index.html',
  './manifest.json',
  './mostafa.ico',
  './watermarked_img_6559831621308037342.png'
];

// تثبيت: بنخزّن كل ملف لوحده، فلو ملف ناقص التثبيت مبيفشلش كله
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) =>
      Promise.all(ASSETS_TO_CACHE.map((a) => cache.add(a).catch(() => {})))
    )
  );
  self.skipWaiting(); // النسخة الجديدة تشتغل فورًا
});

// تفعيل: مسح أي كاش قديم والسيطرة على الصفحات المفتوحة
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(keys.filter((k) => k !== CACHE_NAME).map((k) => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

// Network-first: الصفحة دايمًا أحدث نسخة من النت، والكاش للأوفلاين بس
// طلبات السيرفر (script.google.com) وملفات الـ CDN مبنلمسهاش
self.addEventListener('fetch', (event) => {
  const req = event.request;
  if (req.method !== 'GET' || new URL(req.url).origin !== self.location.origin) return;
  event.respondWith(
    fetch(req, { cache: 'no-cache' })
      .then((res) => {
        if (res.ok) { const copy = res.clone(); caches.open(CACHE_NAME).then((c) => c.put(req, copy)); }
        return res;
      })
      .catch(() => caches.match(req).then((m) => m || caches.match('./index.html')))
  );
});