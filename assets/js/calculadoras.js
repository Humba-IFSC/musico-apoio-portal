/* ==========================================================================
   CALCULADORAS.JS — Sinfonia da Permanência (Client-Side Vanilla JS)
   Módulo A: Tubofones de PVC (Equação de Helmholtz: L = v/(2f) - 1,22*r)
   Módulo B: Domo Geodésico 2V (Euler V-A+F=1 · Cordas LA=0,6180R, LB=0,5465R)
   ========================================================================== */

(function () {
  'use strict';

  const NOTES = [
    { nome: 'Dó', cifra: 'C', semi: -9, natural: true },
    { nome: 'Dó# / Réb', cifra: 'C#', semi: -8, natural: false },
    { nome: 'Ré', cifra: 'D', semi: -7, natural: true },
    { nome: 'Ré# / Mib', cifra: 'D#', semi: -6, natural: false },
    { nome: 'Mi', cifra: 'E', semi: -5, natural: true },
    { nome: 'Fá', cifra: 'F', semi: -4, natural: true },
    { nome: 'Fá# / Solb', cifra: 'F#', semi: -3, natural: false },
    { nome: 'Sol', cifra: 'G', semi: -2, natural: true },
    { nome: 'Sol# / Láb', cifra: 'G#', semi: -1, natural: false },
    { nome: 'Lá', cifra: 'A', semi: 0, natural: true },
    { nome: 'Lá# / Sib', cifra: 'A#', semi: 1, natural: false },
    { nome: 'Si', cifra: 'B', semi: 2, natural: true },
    { nome: 'Dó (8ª acima)', cifra: 'C+', semi: 3, natural: true }
  ];

  const fmt = (n, dec = 2) => n.toFixed(dec).replace('.', ',');

  // Abas acessíveis entre Módulo A e Módulo B
  const tabBtns = document.querySelectorAll('.calc-tab-btn');
  const tabPanels = document.querySelectorAll('.calc-panel');

  tabBtns.forEach((btn) => {
    btn.addEventListener('click', () => {
      const targetId = btn.getAttribute('aria-controls');
      tabBtns.forEach((b) => b.setAttribute('aria-selected', b === btn ? 'true' : 'false'));
      tabPanels.forEach((p) => { p.hidden = p.id !== targetId; });
    });
  });

  // =========================================================================
  // MÓDULO A — CALCULADORA ACÚSTICA DE TUBOFONES DE PVC
  // =========================================================================
  const elTemp = document.getElementById('pvc-temp');
  const elDiam = document.getElementById('pvc-diameter');
  const elOctave = document.getElementById('pvc-octave');
  const elFilterNat = document.getElementById('pvc-only-natural');
  const elSpeed = document.getElementById('pvc-speed-out');
  const elCorr = document.getElementById('pvc-corr-out');
  const elTbody = document.getElementById('pvc-tbody');

  // Cálculo rápido de frequência personalizada
  const elCustomFreq = document.getElementById('pvc-custom-freq');
  const elCustomOut = document.getElementById('pvc-custom-out');

  function updatePvcCalculator() {
    if (!elTbody) return;
    const temp = parseFloat(elTemp ? elTemp.value : '20') || 20;
    const diamMm = parseFloat(elDiam ? elDiam.value : '46.4') || 46.4;
    const octave = parseInt(elOctave ? elOctave.value : '4', 10) || 4;
    const onlyNatural = elFilterNat ? elFilterNat.checked : false;

    // Velocidade do som: v = 331,4 + 0,6 * T (para T=20°C -> 343,4 m/s)
    const v = 331.4 + 0.6 * temp;
    const r = (diamMm / 1000) / 2;
    const corrM = 1.22 * r; // 2 * 0,61 * r (tubo aberto nas 2 extremidades)

    if (elSpeed) elSpeed.textContent = `v = ${fmt(v, 2)} m/s (${temp} °C)`;
    if (elCorr) elCorr.textContent = `Correção 1,22·r = ${fmt(corrM * 100, 2)} cm (${Math.round(corrM * 1000)} mm)`;

    // Atualiza cálculo livre por frequência (Hz)
    if (elCustomFreq && elCustomOut) {
      const fCustom = parseFloat(elCustomFreq.value);
      if (fCustom && fCustom >= 50 && fCustom <= 2000) {
        const lCut = Math.max(0.02, v / (2 * fCustom) - corrM);
        elCustomOut.textContent = `Corte exato para ${fmt(fCustom, 1)} Hz: ${fmt(lCut * 100, 2)} cm (${Math.round(lCut * 1000)} mm)`;
      } else {
        elCustomOut.textContent = 'Informe uma frequência entre 50 Hz e 2000 Hz.';
      }
    }

    const octShift = octave - 4;
    const rowsData = NOTES.filter((n) => !onlyNatural || n.natural).map((n) => {
      const semi = n.semi + octShift * 12;
      const freq = 440 * Math.pow(2, semi / 12);
      const lTheo = v / (2 * freq);
      const lCut = Math.max(0.02, lTheo - corrM);
      const label = n.cifra === 'C+' ? `C${octave + 1}` : `${n.cifra}${octave}`;
      return { ...n, freq, lTheo, lCut, label };
    });

    const maxLen = rowsData.length ? Math.max(...rowsData.map((rItem) => rItem.lCut)) : 1;

    elTbody.innerHTML = '';
    rowsData.forEach((item) => {
      const pct = Math.max(12, Math.round((item.lCut / maxLen) * 100));
      const tr = document.createElement('tr');
      tr.innerHTML = `
        <td><strong>${item.nome}</strong> <span class="mono">(${item.label})</span></td>
        <td>${item.natural ? 'Natural (Diatônica)' : 'Acidente (#/b)'}</td>
        <td class="mono">${fmt(item.freq, 2)} Hz</td>
        <td class="mono">${fmt(item.lTheo * 100, 2)} cm</td>
        <td class="cut-highlight">${fmt(item.lCut * 100, 2)} cm <small style="font-weight:500;color:var(--text-muted)">(${Math.round(item.lCut * 1000)} mm)</small></td>
        <td aria-hidden="true"><div class="tube-bar-visual" style="width:${pct}%"></div></td>
        <td>
          <button type="button" class="btn btn-secondary btn-sm" data-play-note="${item.freq.toFixed(2)}" data-play-label="${item.nome} (${item.label})">
            ▶ Ouvir
          </button>
        </td>
      `;
      elTbody.appendChild(tr);
    });

    elTbody.querySelectorAll('[data-play-note]').forEach((b) => {
      b.addEventListener('click', () => {
        const f = parseFloat(b.getAttribute('data-play-note'));
        const lbl = b.getAttribute('data-play-label');
        if (window.MusicoAudio) window.MusicoAudio.playTone(f, `Tubofone ${lbl}`, 1.8);
      });
    });
  }

  [elTemp, elDiam, elOctave, elFilterNat, elCustomFreq].forEach((el) => {
    if (el) el.addEventListener('input', updatePvcCalculator);
    if (el) el.addEventListener('change', updatePvcCalculator);
  });

  // =========================================================================
  // MÓDULO B — CALCULADORA DO DOMO GEODÉSICO 2V
  // =========================================================================
  const elRadius = document.getElementById('dome-radius');

  function updateDomeCalculator() {
    if (!elRadius) return;
    const R = Math.max(0.5, Math.min(8.0, parseFloat(elRadius.value) || 2.0));
    const la = 0.6180 * R;
    const lb = 0.5465 * R;
    const totalA = 35 * la;
    const totalB = 30 * lb;
    const totalLinear = totalA + totalB;
    const area = Math.PI * R * R;

    const setText = (id, value) => {
      const node = document.getElementById(id);
      if (node) node.textContent = value;
    };

    setText('dome-out-diam', `${fmt(2 * R, 2)} m`);
    setText('dome-out-height', `${fmt(R, 2)} m`);
    setText('dome-out-area', `${fmt(area, 2)} m²`);
    setText('dome-out-la', `${fmt(la, 3)} m (${fmt(la * 100, 1)} cm)`);
    setText('dome-out-lb', `${fmt(lb, 3)} m (${fmt(lb * 100, 1)} cm)`);
    setText('dome-out-tot-a', `${fmt(totalA, 2)} m (35 un.)`);
    setText('dome-out-tot-b', `${fmt(totalB, 2)} m (30 un.)`);
    setText('dome-out-linear', `${fmt(totalLinear, 2)} m totais de tubos/barras`);

    // Cotas verticais dos 3 estratos simbólicos de permanência ecológica
    setText('stratum-cota-3', `${fmt(R, 2)} m`);
    setText('stratum-cota-2', `${fmt(0.5 * R, 2)} m`);
    setText('stratum-cota-1', `${fmt(0.05 * R, 2)} m`);

    // Atualiza rótulos no diagrama SVG do Domo 2V
    setText('svg-dome-r', `R = ${fmt(R, 2)} m · Diâmetro = ${fmt(2 * R, 2)} m`);
    setText('svg-cota-3', `Ápice: ${fmt(R, 2)} m (400–4.000 anos)`);
    setText('svg-cota-2', `Médio: ${fmt(0.5 * R, 2)} m (50–500 anos)`);
    setText('svg-cota-1', `Base: ${fmt(0.05 * R, 2)} m (Semanas–Meses)`);
  }

  if (elRadius) {
    elRadius.addEventListener('input', updateDomeCalculator);
    elRadius.addEventListener('change', updateDomeCalculator);
  }

  document.querySelectorAll('[data-dome-preset]').forEach((btn) => {
    btn.addEventListener('click', () => {
      if (elRadius) {
        elRadius.value = btn.getAttribute('data-dome-preset');
        updateDomeCalculator();
      }
    });
  });

  const btnPrintCut = document.getElementById('btn-print-plan');
  if (btnPrintCut) btnPrintCut.addEventListener('click', () => window.print());

  // Inicialização
  updatePvcCalculator();
  updateDomeCalculator();
})();

