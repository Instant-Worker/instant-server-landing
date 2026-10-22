/* Instant Server — motion layer.

   Two jobs:
     1. scroll-reveal every [data-reveal] element (staggered, once)
     2. lazy-start the promo reels on click (preload="none" keeps the page light)

   Everything degrades: if Motion fails to load, or the visitor prefers reduced
   motion, the content is simply visible with no animation. */

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

    // clicking the video toggles pause/resume once it is running
    video.addEventListener('click', () => {
      if (video.paused) start();
      else video.pause();
    });

    // put the play button back when the reel is paused by the visitor
    video.addEventListener('pause', () => {
      if (button && video.currentTime > 0) button.hidden = false;
    });
    video.addEventListener('play', () => {
      if (button) button.hidden = true;
    });

    // pause when scrolled away — no background decode cost
    if ('IntersectionObserver' in window) {
      const io = new IntersectionObserver((entries) => {
        entries.forEach((e) => {
          if (!e.isIntersecting && !video.paused) video.pause();
        });
      }, { threshold: 0.15 });
      io.observe(video);
    }
  }

  const heroVideo = document.getElementById('reel-vps');
  const heroBtn = document.getElementById('reel-play');
  wirePlayer(heroVideo, heroBtn);

  document.querySelectorAll('[data-play]').forEach((btn) => {
    const v = document.getElementById(btn.getAttribute('data-play'));
    wirePlayer(v, btn);
  });

  /* ---------- reveals ---------- */
  const items = Array.from(document.querySelectorAll('[data-reveal]'));
  if (!items.length) return;

  if (reduced || !window.Motion || !window.Motion.animate) {
    root.classList.add('no-motion');
    items.forEach((el) => el.classList.add('is-in'));
    return;
  }

  const { animate, inView, stagger } = window.Motion;

  // Start each element displaced and transparent, then let inView animate it in.
  items.forEach((el) => {
    const dy = Number(el.getAttribute('data-reveal-y') || 28);
    el.style.transform = `translateY(${dy}px)`;
  });

  const stop = inView(items, (el) => {
    const dy = Number(el.getAttribute('data-reveal-y') || 28);
    animate(
      el,
      { opacity: [0, 1], transform: [`translateY(${dy}px)`, 'translateY(0px)'] },
      { duration: 0.75, ease: [0.22, 1, 0.36, 1] }
    );
    el.classList.add('is-in');
    el.style.transform = 'translateY(0px)';
  }, { amount: 0.15 });

  // Hero reel gets a slightly longer, softer entrance.
  if (heroVideo) {
    const card = heroVideo.closest('.reel-hero');
    if (card) {
      animate(card, { opacity: [0, 1], transform: ['translateY(34px) scale(.985)', 'translateY(0px) scale(1)'] },
        { duration: 1.0, delay: 0.15, ease: [0.22, 1, 0.36, 1] });
      card.style.opacity = '1';
      card.style.transform = 'none';
      card.classList.add('is-in');
    }
  }

  // Stagger the product cards inside the visible grid the first time it appears.
  const grid = document.getElementById('grid-vps');
  if (grid) {
    let done = false;
    inView(grid, () => {
      if (done) return;
      done = true;
      animate(grid.querySelectorAll('.card'),
        { opacity: [0, 1], transform: ['translateY(26px)', 'translateY(0px)'] },
        { duration: 0.6, delay: stagger(0.06), ease: [0.22, 1, 0.36, 1] });
    }, { amount: 0.1 });
  }
})();
