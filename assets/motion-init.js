/* Instant Server — motion layer.

   Two jobs:
     1. scroll-reveal every [data-reveal] element (staggered, once)
     2. lazy-start the promo reels on click (preload="none" keeps the page light)

   Everything degrades: if Motion fails to load, or the visitor prefers reduced
   motion, the content is simply visible with no animation.

   Why IntersectionObserver and not Motion's inView: Motion's inView never fired
   on this page (verified live — the element was on screen with ratio 0.88 and the
   callback stayed silent, while a plain IntersectionObserver on the same node
   fired immediately). Motion is still used for the animation itself; only the
   trigger is native, so a library quirk cannot leave the page invisible. */

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

  const animate = (window.Motion && window.Motion.animate) || null;

  const reveal = (el) => {
    if (el.classList.contains('is-in')) return;
    el.classList.add('is-in');
    const dy = Number(el.getAttribute('data-reveal-y') || 28);

    if (!animate) {
      el.style.opacity = '1';
      el.style.transform = 'none';
      return;
    }

    animate(
      el,
      { opacity: [0, 1], transform: [`translateY(${dy}px)`, 'translateY(0px)'] },
      { duration: 0.75, ease: [0.22, 1, 0.36, 1] }
    );
    el.style.opacity = '1';
    el.style.transform = 'translateY(0px)';
  };

  if (reduced || !('IntersectionObserver' in window)) {
    root.classList.add('no-motion');
    items.forEach(reveal);
    return;
  }

  // start displaced
  items.forEach((el) => {
    el.style.opacity = '0';
    el.style.transform = `translateY(${Number(el.getAttribute('data-reveal-y') || 28)}px)`;
  });

  const io = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        reveal(entry.target);
        io.unobserve(entry.target);   // once, then stop watching
      }
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -8% 0px' });

  items.forEach((el) => io.observe(el));

  // Anything already on screen at load must not wait for a scroll event.
  requestAnimationFrame(() => {
    items.forEach((el) => {
      const r = el.getBoundingClientRect();
      if (r.top < window.innerHeight * 0.95 && r.bottom > 0) {
        reveal(el);
        io.unobserve(el);
      }
    });
  });

  // Safety net: nothing may stay invisible. An element the visitor has already
  // scrolled PAST (top above the viewport bottom) must be shown too — a fast
  // scroll can outrun the observer, and a permanently invisible caption reads as
  // a broken page.
  const catchUp = () => {
    items.forEach((el) => {
      if (el.classList.contains('is-in')) return;
      const r = el.getBoundingClientRect();
      if (r.top < window.innerHeight) reveal(el);
    });
  };
  setTimeout(catchUp, 1800);
  window.addEventListener('scroll', () => {
    if (window.__catchUpQueued) return;
    window.__catchUpQueued = true;
    requestAnimationFrame(() => { window.__catchUpQueued = false; catchUp(); });
  }, { passive: true });

  /* ---------- product card stagger ---------- */
  const grid = document.getElementById('grid-vps');
  if (grid && animate) {
    let done = false;
    const cards = grid.querySelectorAll('.card');
    const revealCards = () => {
      if (done) return;
      done = true;
      animate(cards,
        { opacity: [0, 1], transform: ['translateY(26px)', 'translateY(0px)'] },
        { duration: 0.6, delay: window.Motion.stagger(0.06), ease: [0.22, 1, 0.36, 1] });
      cards.forEach((c) => { c.style.opacity = '1'; });
    };

    const gio = new IntersectionObserver((entries) => {
      entries.forEach((e) => {
        if (e.isIntersecting) { revealCards(); gio.disconnect(); }
      });
    }, { threshold: 0.1 });
    gio.observe(grid);
    setTimeout(revealCards, 2600);
  }
})();
