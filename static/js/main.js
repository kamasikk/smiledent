/**
 * SmileDent — main.js
 * Handles: mobile navigation, scroll-reveal animations, FAQ accordion,
 * service category filtering, and lightweight client-side form UX.
 */
(function () {
  'use strict';

  /* ---- Mobile navigation ------------------------------------------------ */
  const burger = document.querySelector('[data-burger]');
  const mobileNav = document.querySelector('[data-mobile-nav]');

  if (burger && mobileNav) {
    burger.addEventListener('click', function () {
      const isOpen = mobileNav.classList.toggle('is-open');
      burger.classList.toggle('is-open', isOpen);
      burger.setAttribute('aria-expanded', String(isOpen));
    });

    mobileNav.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        mobileNav.classList.remove('is-open');
        burger.classList.remove('is-open');
        burger.setAttribute('aria-expanded', 'false');
      });
    });
  }

  /* ---- Header shadow on scroll ------------------------------------------ */
  const header = document.querySelector('[data-site-header]');
  if (header) {
    const toggleHeaderShadow = function () {
      header.style.boxShadow = window.scrollY > 12
        ? '0 8px 30px -18px rgba(15,43,38,0.4)'
        : 'none';
    };
    toggleHeaderShadow();
    window.addEventListener('scroll', toggleHeaderShadow, { passive: true });
  }

  /* ---- Scroll-reveal animations ------------------------------------------ */
  const revealTargets = document.querySelectorAll('[data-reveal]');
  if (revealTargets.length) {
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (prefersReducedMotion) {
      revealTargets.forEach(function (el) { el.classList.add('is-visible'); });
    } else if ('IntersectionObserver' in window) {
      const observer = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-visible');
            observer.unobserve(entry.target);
          }
        });
      }, { threshold: 0.15, rootMargin: '0px 0px -60px 0px' });
      revealTargets.forEach(function (el) { observer.observe(el); });
    } else {
      revealTargets.forEach(function (el) { el.classList.add('is-visible'); });
    }
  }

  /* ---- FAQ accordion ------------------------------------------------------ */
  document.querySelectorAll('.faq-item').forEach(function (item) {
    const question = item.querySelector('.faq-item__q');
    if (!question) return;
    question.addEventListener('click', function () {
      const isOpen = item.classList.contains('is-open');
      item.closest('.faq-list').querySelectorAll('.faq-item').forEach(function (el) {
        el.classList.remove('is-open');
        const q = el.querySelector('.faq-item__q');
        if (q) q.setAttribute('aria-expanded', 'false');
      });
      if (!isOpen) {
        item.classList.add('is-open');
        question.setAttribute('aria-expanded', 'true');
      }
    });
  });

  /* ---- Service category filter (services list page) ----------------------- */
  const filterChips = document.querySelectorAll('[data-filter-chip]');
  const filterCards = document.querySelectorAll('[data-service-card]');
  if (filterChips.length && filterCards.length) {
    filterChips.forEach(function (chip) {
      chip.addEventListener('click', function () {
        filterChips.forEach(function (c) { c.classList.remove('is-active'); });
        chip.classList.add('is-active');
        const category = chip.getAttribute('data-filter-chip');
        filterCards.forEach(function (card) {
          const match = category === 'all' || card.getAttribute('data-service-card') === category;
          card.style.display = match ? '' : 'none';
        });
      });
    });
  }

  /* ---- Basic client-side required-field feedback (native validation aid) --- */
  document.querySelectorAll('form[data-validate]').forEach(function (form) {
    form.addEventListener('submit', function (event) {
      const invalid = form.querySelector(':invalid');
      if (invalid) {
        event.preventDefault();
        invalid.focus();
        invalid.reportValidity();
      }
    });
  });

  /* ---- Auto-dismiss alerts -------------------------------------------------- */
  document.querySelectorAll('.alert').forEach(function (alert) {
    setTimeout(function () {
      alert.style.transition = 'opacity .4s ease, transform .4s ease';
      alert.style.opacity = '0';
      alert.style.transform = 'translateX(24px)';
      setTimeout(function () { alert.remove(); }, 400);
    }, 6000);
  });
})();
