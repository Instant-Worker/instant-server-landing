/* Instant Server — motion layer.

   Two jobs:
     1. scroll-reveal every [data-reveal] element (staggered, once)
     2. lazy-start the promo reels on click (preload="none" keeps the page light)

   Everything degrades: if Motion fails to load, or the visitor prefers reduced
   motion, the content is simply visible with no animation.

   API note: Motion's inView signature is inView(target, onStart, options) where
   onStart receives {target}. Passing the callback as the second argument (the
   "element, callback" habit) silently returns an observer that never calls
   anything — which looks exactly like "the reveal never fired". */

(function () {
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const root = document.documentElement;

  /* ---------- video players ---------- */
  function wirePlayer(video, button) {
    if (!video) return;

    const start = () => {
      // preload="none" means the first play() triggers the download
      video.preload = 'auto';
      const p = video.play();
      if (p && p.catch) p.catch(() => { /* autoplay policy: leave the poster */ });
      if (button) button.hidden = true;
    };

    if (button) button.addEventListener('click', start);

    video.addEventListener('click', () => {
      if (video.paused) start();
      else video.pause();
    });

    video.addEventListener('pause', () => {
      if (button && video.currentTime > 0) button.hidden = false;
    });
    video.addEventListener('play', () => {
      if (button) button.hidden = true;
    });

    if ('IntersectionObserver' in window) {
      const io = new IntersectionObserver((entries) => {
        entries.forEach((e) => {
          if (!e.isIntersecting && !video.paused) video.pause();
        });
      }, { threshold: 0.15 });
      io.observe(video);
    }
  }

  wirePlayer(document.getElementById('reel-vps'), document.getElementById('reel-play'));
  document.querySelectorAll('[data-play]').forEach((btn) => {
    wirePlayer(document.getElementById(btn.getAttribute('data-play')), btn);
  });

  /* ---------- reveals ---------- */
  const items = Array.from(document.querySelectorAll('[data-reveal]'));
  if (!items.length) return;

  const showAll = () => {
    root.classList.add('no-motion');
    items.forEach((el) => {
      el.classList.add('is-in');
      el.style.opacity = '1';
      el.style.transform = 'none';
    });
  };

  if (reduced || !window.Motion || typeof window.Motion.inView !== 'function') {
    showAll();
    return;
  }

  const { animate, inView, stagger } = window.Motion;

  // start displaced
  items.forEach((el) => {
    el.style.opacity = '0';
    el.style.transform = `translateY(${Number(el.getAttribute('data-reveal-y') || 28)}px)`;
  });

  const reveal = (el) => {
    if (el.classList.contains('is-in')) return;
    el.classList.add('is-in');
    const dy = Number(el.getAttribute('data-reveal-y') || 28);
    animate(
      el,
      { opacity: [0, 1], transform: [`translateY(${dy}px)`, 'translateY(0px)'] },
      { duration: 0.75, ease: [0.22, 1, 0.36, 1] }
    );
    el.style.opacity = '1';
    el.style.transform = 'translateY(0px)';
  };

  // inView(target, onStart, options) — the callback is the SECOND argument and
  // receives {target}; it fires when the element enters the viewport.
  inView(items, (entry) => reveal(entry.target), { amount: 0.15 });

  // Anything already on screen at load (the hero) must not wait for a scroll.
  requestAnimationFrame(() => {
    items.forEach((el) => {
      const r = el.getBoundingClientRect();
      if (r.top < window.innerHeight * 0.92 && r.bottom > 0) reveal(el);
    });
  });

  // Safety net: if a reveal never fired (odd viewport, observer quirk), make
  // sure nothing stays invisible after a few seconds.
  setTimeout(() => {
    items.forEach((el) => {
      const r = el.getBoundingClientRect();
      if (r.top < window.innerHeight && r.bottom > 0 && !el.classList.contains('is-in')) reveal(el);
    });
  }, 2600);

  // Stagger the product cards the first time the grid appears.
  const grid = document.getElementById('grid-vps');
  if (grid) {
    let done = false;
    inView(grid, () => {
      if (done) return;
      done = true;
      animate(grid.querySelectorAll('.card'),
        { opacity: [0, 1], transform: ['translateY(26px)', 'translateY(0px)'] },
        { duration: 0.6, delay: stagger(0.06), ease: [0.22, 1, 0.36, 1] });
      grid.querySelectorAll('.card').forEach((c) => { c.style.opacity = '1'; });
    }, { amount: 0.1 });
  }
})();
