html_pwa_content = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>بصمتي | إدارة أوقات العمل</title>
    
    <!-- ميزات تحويل الصفحة لتطبيق موبايل (PWA / iOS Web App) -->
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    <meta name="apple-mobile-web-app-title" content="بصمتي">
    <meta name="mobile-web-app-capable" content="yes">
    
    <!-- Tailwind CSS & SweetAlert2 & Fonts -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700&display=swap" rel="stylesheet">
    
    <style>
        body { 
            font-family: 'Tajawal', sans-serif; 
            background-color: #f1f5f9; 
            -webkit-tap-highlight-color: transparent;
        }
        .glass-card { 
            background: rgba(255, 255, 255, 0.98); 
            backdrop-filter: blur(20px); 
        }
        .tab-active {
            background-color: #2563eb;
            color: #ffffff;
            box-shadow: 0 4px 12px rgba(37, 99, 235, 0.2);
        }
        .dir-ltr { direction: ltr; text-align: left; }
        .dir-rtl { direction: rtl; text-align: right; }
    </style>
</head>
<body class="text-slate-800 antialiased min-h-screen flex flex-col items-center p-4 pb-12 select-none">

    <div class="w-full max-w-md space-y-5 mt-4">
        
        <!-- الهيدر -->
        <div class="text-center space-y-1">
            <div class="inline-flex items-center justify-center w-14 h-14 rounded-2xl bg-blue-600 text-white mb-2 shadow-lg shadow-blue-600/30">
                <svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 11c0 3.517-1.009 6.799-2.753 9.571m-3.44-2.04l.054-.09A13.916 13.916 0 009 11V7a4 4 0 00-8 0v4c0 2.503-.664 4.846-1.847 6.88kM19.233 13.514l-.078-.112A14.018 14.018 0 0017 11V7a5 5 0 10-10 0v4c0 .691-.048 1.371-.141 2.036M15 11h.01M19 21l-4-4m0 0l4-4m-4 4h6"></path>
                </svg>
            </div>
            <h1 class="text-xl font-bold text-slate-900">تطبيق بصمتي الشخصي</h1>
            <p class="text-xs text-slate-500">مزامنة مباشرة مع Google Sheets</p>
        </div>

        <!-- أزرار التنقل بين التابات -->
        <div class="grid grid-cols-2 gap-2 bg-slate-200/80 p-1 rounded-xl text-sm font-medium">
            <button id="tabQuickBtn" onclick="switchTab('quick')" class="py-2.5 rounded-lg text-center transition-all tab-active">
                تسجيل سريع (اليوم)
            </button>
            <button id="tabManualBtn" onclick="switchTab('manual')" class="py-2.5 rounded-lg text-center text-slate-600 transition-all">
                إدخال يدوي / تاريخ قديم
            </button>
        </div>

        <!-- تاب 1: التسجيل السريع -->
        <div id="quickTab" class="glass-card rounded-2xl p-5 border border-slate-100 shadow-sm space-y-4">
            <p class="text-xs text-slate-400 text-center">يقوم بالتسجيل بناءً على اللحظة الحالية فوراً</p>
            <div class="grid grid-cols-2 gap-4">
                <button onclick="sendQuickStamp('checkIn')" class="bg-emerald-600 hover:bg-emerald-700 active:scale-95 text-white p-5 rounded-xl transition-all shadow-md flex flex-col items-center justify-center gap-2">
                    <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 16l-4-4m0 0l4-4m-4 4h14m-5 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h7a3 3 0 013 3v1"></path>
                    </svg>
                    <span class="font-bold text-sm">بصمة دخول الآن</span>
                </button>
                <button onclick="sendQuickStamp('checkOut')" class="bg-rose-600 hover:bg-rose-700 active:scale-95 text-white p-5 rounded-xl transition-all shadow-md flex flex-col items-center justify-center gap-2">
                    <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"></path>
                    </svg>
                    <span class="font-bold text-sm">بصمة خروج الآن</span>
                </button>
            </div>
        </div>

        <!-- تاب 2: الإدخال اليدوي والتاريخ القديم -->
        <div id="manualTab" class="glass-card rounded-2xl p-5 border border-slate-100 shadow-sm hidden">
            <form id="manualForm" class="space-y-4">
                <div>
                    <label class="block text-xs font-medium text-slate-600 mb-1">التاريخ</label>
                    <input type="date" id="mDate" required class="w-full px-3 py-2.5 rounded-lg bg-slate-50 border border-slate-200 focus:border-blue-500 outline-none text-sm font-medium">
                </div>
                <div class="grid grid-cols-2 gap-3">
                    <div>
                        <label class="block text-xs font-medium text-slate-600 mb-1">وقت الدخول</label>
                        <input type="time" id="mCheckIn" required class="w-full px-3 py-2.5 rounded-lg bg-slate-50 border border-slate-200 focus:border-blue-500 outline-none text-sm font-medium">
                    </div>
                    <div>
                        <label class="block text-xs font-medium text-slate-600 mb-1">وقت الخروج</label>
                        <input type="time" id="mCheckOut" required class="w-full px-3 py-2.5 rounded-lg bg-slate-50 border border-slate-200 focus:border-blue-500 outline-none text-sm font-medium">
                    </div>
                </div>
                <button type="submit" id="mSubmitBtn" class="w-full bg-blue-600 hover:bg-blue-700 text-white text-sm font-bold py-3 rounded-lg transition-all shadow-md mt-2">
                    حفظ اليوم بالكامل
                </button>
            </form>
        </div>

        <!-- كارت الرصيد التراكمي -->
        <div class="glass-card rounded-2xl p-4 border border-slate-100 shadow-sm flex justify-between items-center hidden" id="balanceCard">
            <div class="flex items-center gap-2">
                <span class="p-2 rounded-lg bg-indigo-50 text-indigo-600">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"></path>
                    </svg>
                </span>
                <span class="text-xs font-bold text-slate-700">الرصيد التراكمي العام:</span>
            </div>
            <span id="globalBalance" class="text-base font-bold tracking-wide">0.00 س</span>
        </div>

    </div>

    <script>
        const SCRIPT_URL = "https://script.google.com/macros/s/AKfycbwmxw-JqLtkwUzQH4y_OtO2r5Q0vPnuPCcgDyFuj0RrFT2n7_Cn1AxLtr41bArp3C7E0A/exec";

        function switchTab(tab) {
            const quickTab = document.getElementById('quickTab');
            const manualTab = document.getElementById('manualTab');
            const quickBtn = document.getElementById('tabQuickBtn');
            const manualBtn = document.getElementById('tabManualBtn');

            if(tab === 'quick') {
                quickTab.classList.remove('hidden');
                manualTab.classList.add('hidden');
                quickBtn.classList.add('tab-active');
                manualBtn.classList.remove('tab-active');
                manualBtn.classList.add('text-slate-600');
            } else {
                manualTab.classList.remove('hidden');
                quickTab.classList.add('hidden');
                manualBtn.classList.add('tab-active');
                quickBtn.classList.remove('tab-active');
                quickBtn.classList.add('text-slate-600');
                
                // تعيين الافتراضيات لليدوي (11 AM لـ 7 PM)
                document.getElementById('mDate').value = new Date().toISOString().split('T')[0];
                document.getElementById('mCheckIn').value = "11:00";
                document.getElementById('mCheckOut').value = "19:00";
            }
        }

        async function fetchGlobalStats() {
            try {
                const res = await fetch(SCRIPT_URL);
                const data = await res.json();
                if(data.status === 'success') {
                    const card = document.getElementById('balanceCard');
                    const text = document.getElementById('globalBalance');
                    card.classList.remove('hidden');
                    const bal = parseFloat(data.overallBalance);
                    
                    if(bal > 0) {
                        text.innerText = `+${bal.toFixed(2)} س`;
                        text.className = "text-base font-bold text-emerald-600 dir-ltr";
                    } else if(bal < 0) {
                        text.innerText = `${bal.toFixed(2)} س`;
                        text.className = "text-base font-bold text-rose-600 dir-ltr";
                    } else {
                        text.innerText = `${bal.toFixed(2)} س`;
                        text.className = "text-base font-bold text-slate-600 dir-ltr";
                    }
                }
            } catch(e) { console.error(e); }
        }

        async function sendRequest(payload) {
            Swal.fire({
                title: 'جاري الحفظ...',
                allowOutsideClick: false,
                didOpen: () => { Swal.showLoading(); }
            });

            try {
                const response = await fetch(SCRIPT_URL, {
                    method: 'POST',
                    headers: { "Content-Type": "text/plain;charset=utf-8" },
                    redirect: "follow",
                    body: JSON.stringify(payload)
                });
                const result = await response.json();
                
                if(result.status === 'success') {
                    let msg = result.message;
                    if(result.totalHours) {
                        msg += `<br><span class='text-xs text-slate-500'>ساعات اليوم: ${result.totalHours} س (الرصيد: ${result.balance > 0 ? '+'+result.balance : result.balance})</span>`;
                    }
                    Swal.fire({
                        icon: 'success',
                        title: 'تم بنجاح!',
                        html: msg,
                        confirmButtonColor: '#2563eb',
                        confirmButtonText: 'ممتاز'
                    });
                    fetchGlobalStats();
                } else {
                    throw new Error(result.message);
                }
            } catch(e) {
                Swal.fire({ icon: 'error', title: 'فشلت العملية', text: 'حدث خطأ أثناء الاتصال بالسيرفر.' });
            }
        }

        function sendQuickStamp(actionType) {
            const now = new Date();
            const dateStr = now.toISOString().split('T')[0];
            const hours = String(now.getHours()).padStart(2, '0');
            const mins = String(now.getMinutes()).padStart(2, '0');
            const timeStr = `${hours}:${mins}`;

            sendRequest({
                type: actionType,
                date: dateStr,
                time: timeStr
            });
        }

        document.getElementById('manualForm').addEventListener('submit', (e) => {
            e.preventDefault();
            sendRequest({
                type: 'historical',
                date: document.getElementById('mDate').value,
                checkIn: document.getElementById('mCheckIn').value,
                checkOut: document.getElementById('mCheckOut').value
            });
        });

        window.onload = fetchGlobalStats;
    </script>
</body>
</html>"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_pwa_content)

print("[file-tag: index.html]")