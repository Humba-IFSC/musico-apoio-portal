/* ==========================================================================
   MAIN.JS — Acessibilidade (eMAG 3.1 / WCAG 2.2 AA), Navegação,
   Estúdio Rítmico (sem autoplay) e Carregamento Sob Demanda de Vídeo
   ========================================================================== */

(function () {
  'use strict';

  const ROOT = document.documentElement;
  const STORAGE_CONTRAST = 'ma_ifsc_high_contrast';
  const STORAGE_FONT = 'ma_ifsc_font_scale';
  const STORAGE_MOTION = 'ma_ifsc_reduce_motion';

  let fontScale = parseFloat(localStorage.getItem(STORAGE_FONT) || '1');
  fontScale = Math.min(1.25, Math.max(0.85, isNaN(fontScale) ? 1 : fontScale));

  function applyFontScale(scale) {
    fontScale = Math.round(Math.min(1.25, Math.max(0.85, scale)) * 100) / 100;
    ROOT.style.setProperty('--font-scale', String(fontScale));
    localStorage.setItem(STORAGE_FONT, String(fontScale));
  }

  function applyContrast(enabled) {
    ROOT.classList.toggle('high-contrast', enabled);
    localStorage.setItem(STORAGE_CONTRAST, enabled ? '1' : '0');
    const btn = document.getElementById('btn-contrast');
    if (btn) btn.setAttribute('aria-pressed', enabled ? 'true' : 'false');
  }

  function applyReduceMotion(enabled) {
    ROOT.classList.toggle('reduce-motion', enabled);
    localStorage.setItem(STORAGE_MOTION, enabled ? '1' : '0');
    const btn = document.getElementById('btn-motion');
    if (btn) btn.setAttribute('aria-pressed', enabled ? 'true' : 'false');
  }

  // Inicializa preferências salvas
  applyFontScale(fontScale);
  applyContrast(localStorage.getItem(STORAGE_CONTRAST) === '1');
  applyReduceMotion(localStorage.getItem(STORAGE_MOTION) === '1');

  // Controles da Barra de Acessibilidade
  const btnInc = document.getElementById('btn-font-inc');
  const btnDec = document.getElementById('btn-font-dec');
  const btnReset = document.getElementById('btn-font-reset');
  const btnContrast = document.getElementById('btn-contrast');
  const btnMotion = document.getElementById('btn-motion');

  if (btnInc) btnInc.addEventListener('click', () => applyFontScale(fontScale + 0.08));
  if (btnDec) btnDec.addEventListener('click', () => applyFontScale(fontScale - 0.08));
  if (btnReset) btnReset.addEventListener('click', () => applyFontScale(1));
  if (btnContrast) btnContrast.addEventListener('click', () => applyContrast(!ROOT.classList.contains('high-contrast')));
  if (btnMotion) btnMotion.addEventListener('click', () => applyReduceMotion(!ROOT.classList.contains('reduce-motion')));

  // Menu Responsivo Mobile + Dropdowns Acessíveis (Mouse, Clique e Teclado)
  const navToggle = document.getElementById('nav-toggle');
  const mainNav = document.getElementById('menu-principal');
  const dropdownItems = Array.from(document.querySelectorAll('.nav-item--has-sub'));

  function closeAllDropdowns(exceptItem = null) {
    dropdownItems.forEach((item) => {
      if (item !== exceptItem) {
        item.classList.remove('open');
        const btn = item.querySelector('.nav-caret-btn');
        if (btn) btn.setAttribute('aria-expanded', 'false');
      }
    });
  }

  dropdownItems.forEach((item) => {
    const caret = item.querySelector('.nav-caret-btn');
    if (caret) {
      caret.addEventListener('click', (e) => {
        e.preventDefault();
        e.stopPropagation();
        const willOpen = !item.classList.contains('open');
        closeAllDropdowns(item);
        item.classList.toggle('open', willOpen);
        caret.setAttribute('aria-expanded', willOpen ? 'true' : 'false');
      });
    }
  });

  document.addEventListener('click', (e) => {
    if (!e.target.closest('.nav-item--has-sub')) {
      closeAllDropdowns();
    }
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      closeAllDropdowns();
      if (mainNav && mainNav.classList.contains('open')) {
        mainNav.classList.remove('open');
        if (navToggle) navToggle.setAttribute('aria-expanded', 'false');
      }
    }
  });

  if (navToggle && mainNav) {
    navToggle.addEventListener('click', () => {
      const open = mainNav.classList.toggle('open');
      navToggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      if (!open) closeAllDropdowns();
    });
    mainNav.querySelectorAll('a').forEach((link) => {
      link.addEventListener('click', () => {
        mainNav.classList.remove('open');
        navToggle.setAttribute('aria-expanded', 'false');
        closeAllDropdowns();
      });
    });
  }

  // Busca / Filtro Rápido (Alt + 4)
  const searchTrigger = document.getElementById('trigger-search');
  const searchDrawer = document.getElementById('search-drawer');
  const searchInput = document.getElementById('site-search-input');
  const searchCount = document.getElementById('search-results-count');
  const searchClose = document.getElementById('search-close');

  function toggleSearch(forceOpen) {
    if (!searchDrawer) return;
    const shouldOpen = typeof forceOpen === 'boolean' ? forceOpen : searchDrawer.hidden;
    searchDrawer.hidden = !shouldOpen;
    if (shouldOpen && searchInput) {
      searchInput.focus();
    } else if (!shouldOpen && searchInput) {
      searchInput.value = '';
      filterContent('');
    }
  }

  function filterContent(query) {
    const q = query.trim().toLowerCase();
    const cards = document.querySelectorAll('[data-searchable]');
    let visible = 0;
    cards.forEach((el) => {
      const match = !q || el.textContent.toLowerCase().includes(q);
      el.classList.toggle('search-hidden', !match);
      if (match) visible++;
    });
    if (searchCount) {
      searchCount.textContent = q
        ? `${visible} bloco(s) encontrado(s) para "${query.trim()}"`
        : 'Digite para filtrar conteúdos, eventos ou documentos';
    }
  }

  if (searchTrigger) {
    searchTrigger.addEventListener('click', (e) => {
      e.preventDefault();
      toggleSearch(true);
    });
  }
  if (searchClose) searchClose.addEventListener('click', () => toggleSearch(false));
  if (searchInput) searchInput.addEventListener('input', (e) => filterContent(e.target.value));

  // Destaca automaticamente a página atual e o menu pai quando em subpágina
  const currentFile = (window.location.pathname.split('/').pop() || 'index.html').toLowerCase();
  document.querySelectorAll('.nav-link, .dropdown-link').forEach((link) => {
    const href = (link.getAttribute('href') || '').toLowerCase();
    const isCurrent = href === currentFile || (currentFile === '' && href === 'index.html');
    link.classList.toggle('active', isCurrent);
    if (isCurrent) {
      link.setAttribute('aria-current', 'page');
      const parentItem = link.closest('.nav-item--has-sub');
      if (parentItem) {
        const parentLink = parentItem.querySelector(':scope > .nav-link');
        if (parentLink) parentLink.classList.add('active');
      }
    } else {
      link.removeAttribute('aria-current');
    }
  });

  // Carregamento sob demanda do YouTube (Respeito Sensorial TEA: SEM autoplay)
  document.querySelectorAll('[data-yt-load]').forEach((btn) => {
    btn.addEventListener('click', () => {
      const videoId = btn.getAttribute('data-yt-load');
      const container = btn.closest('.video-facade');
      if (!container || !videoId) return;
      const iframe = document.createElement('iframe');
      iframe.src = `https://www.youtube-nocookie.com/embed/${videoId}?rel=0&mute=1`;
      iframe.title = btn.getAttribute('data-yt-title') || 'Vídeo oficial do Projeto Músico de Apoio';
      iframe.allow = 'accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture';
      iframe.allowFullscreen = true;
      container.innerHTML = '';
      container.appendChild(iframe);
    });
  });

  // =========================================================================
  // MOTOR WEB AUDIO COMPARTILHADO (Acionado SOMENTE por clique do usuário)
  // =========================================================================
  let audioCtx = null;
  let activeOsc = null;
  let toneTimer = null;

  function getAudioCtx() {
    if (!audioCtx) {
      const AudioContextCtor = window.AudioContext || window.webkitAudioContext;
      audioCtx = new AudioContextCtor();
    }
    if (audioCtx.state === 'suspended') {
      audioCtx.resume();
    }
    return audioCtx;
  }

  function stopTone() {
    if (activeOsc) {
      try { activeOsc.stop(); } catch (_) {}
      activeOsc.disconnect();
      activeOsc = null;
    }
    if (toneTimer) {
      clearTimeout(toneTimer);
      toneTimer = null;
    }
    const status = document.getElementById('audio-live-status');
    if (status) status.textContent = 'Áudio silenciado (nenhum som em execução).';
  }

  function playTone(freq, label, durationSec = 2.0) {
    stopTone();
    const ctx = getAudioCtx();
    const osc = ctx.createOscillator();
    const gain = ctx.createGain();
    const waveEl = document.getElementById('tone-waveform');

    osc.type = waveEl ? waveEl.value : 'triangle';
    osc.frequency.setValueAtTime(freq, ctx.currentTime);

    gain.gain.setValueAtTime(0.001, ctx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.22, ctx.currentTime + 0.05);
    gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + durationSec);

    osc.connect(gain);
    gain.connect(ctx.destination);
    osc.start();
    osc.stop(ctx.currentTime + durationSec);
    activeOsc = osc;

    const status = document.getElementById('audio-live-status');
    if (status) {
      status.textContent = `Reproduzindo sob demanda: ${label} (${freq.toFixed(2).replace('.', ',')} Hz).`;
    }
    toneTimer = setTimeout(() => {
      activeOsc = null;
      if (status) status.textContent = 'Áudio concluído.';
    }, durationSec * 1000);
  }

  // Exposto para a calculadora acústica usar o mesmo motor seguro
  window.MusicoAudio = { playTone, stopTone };

  // Botões de Diapasão / Cordas
  document.querySelectorAll('[data-tone-freq]').forEach((btn) => {
    btn.addEventListener('click', () => {
      const f = parseFloat(btn.getAttribute('data-tone-freq'));
      const lbl = btn.getAttribute('data-tone-label') || `${f} Hz`;
      if (!isNaN(f)) playTone(f, lbl, 2.2);
    });
  });

  const btnMuteAll = document.getElementById('btn-mute-all');
  if (btnMuteAll) {
    btnMuteAll.addEventListener('click', () => {
      stopTone();
      if (metroRunning) toggleMetronome();
    });
  }

  // Metrônomo Digital (Estúdio Músico de Apoio — inicia sempre PARADO)
  let metroRunning = false;
  let metroBpm = 90;
  let metroBeats = 4;
  let metroStep = 0;
  let metroTimer = null;

  const bpmDisplay = document.getElementById('bpm-display');
  const bpmSlider = document.getElementById('bpm-slider');
  const beatBar = document.getElementById('beat-bar');
  const metroToggle = document.getElementById('metro-toggle');
  const metroSelect = document.getElementById('metro-beats');

  function renderBeatDots() {
    if (!beatBar) return;
    beatBar.innerHTML = '';
    for (let i = 0; i < metroBeats; i++) {
      const dot = document.createElement('span');
      dot.className = 'beat-dot';
      dot.id = `beat-dot-${i}`;
      dot.setAttribute('aria-hidden', 'true');
      beatBar.appendChild(dot);
    }
  }

  function updateBpm(val) {
    metroBpm = Math.max(40, Math.min(200, parseInt(val, 10) || 90));
    if (bpmDisplay) bpmDisplay.textContent = String(metroBpm);
    if (bpmSlider) bpmSlider.value = String(metroBpm);
    if (metroRunning) restartMetronome();
  }

  function clickBeat() {
    const ctx = getAudioCtx();
    const isStrong = metroStep === 0;
    const osc = ctx.createOscillator();
    const gain = ctx.createGain();
    osc.type = 'triangle';
    osc.frequency.setValueAtTime(isStrong ? 980 : 660, ctx.currentTime);
    gain.gain.setValueAtTime(0.24, ctx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.045);
    osc.connect(gain);
    gain.connect(ctx.destination);
    osc.start();
    osc.stop(ctx.currentTime + 0.05);

    for (let i = 0; i < metroBeats; i++) {
      const dot = document.getElementById(`beat-dot-${i}`);
      if (dot) {
        dot.classList.remove('strong', 'weak');
        if (i === metroStep) dot.classList.add(isStrong ? 'strong' : 'weak');
      }
    }
    metroStep = (metroStep + 1) % metroBeats;
  }

  function restartMetronome() {
    if (metroTimer) clearInterval(metroTimer);
    clickBeat();
    metroTimer = setInterval(clickBeat, (60 / metroBpm) * 1000);
  }

  function toggleMetronome() {
    metroRunning = !metroRunning;
    if (metroRunning) {
      metroStep = 0;
      restartMetronome();
      if (metroToggle) {
        metroToggle.textContent = '⏹ Parar Metrônomo';
        metroToggle.setAttribute('aria-pressed', 'true');
        metroToggle.classList.replace('btn-primary', 'btn-accent');
      }
    } else {
      if (metroTimer) clearInterval(metroTimer);
      metroTimer = null;
      for (let i = 0; i < metroBeats; i++) {
        const dot = document.getElementById(`beat-dot-${i}`);
        if (dot) dot.classList.remove('strong', 'weak');
      }
      if (metroToggle) {
        metroToggle.textContent = '▶ Iniciar Metrônomo';
        metroToggle.setAttribute('aria-pressed', 'false');
        metroToggle.classList.replace('btn-accent', 'btn-primary');
      }
    }
  }

  if (bpmSlider) bpmSlider.addEventListener('input', (e) => updateBpm(e.target.value));
  if (metroToggle) metroToggle.addEventListener('click', toggleMetronome);
  if (metroSelect) {
    metroSelect.addEventListener('change', (e) => {
      metroBeats = parseInt(e.target.value, 10) || 4;
      metroStep = 0;
      renderBeatDots();
      if (metroRunning) restartMetronome();
    });
  }
  document.querySelectorAll('[data-bpm-delta]').forEach((b) => {
    b.addEventListener('click', () => updateBpm(metroBpm + parseInt(b.getAttribute('data-bpm-delta'), 10)));
  });
  document.querySelectorAll('[data-bpm-preset]').forEach((b) => {
    b.addEventListener('click', () => updateBpm(parseInt(b.getAttribute('data-bpm-preset'), 10)));
  });

  renderBeatDots();
})();

