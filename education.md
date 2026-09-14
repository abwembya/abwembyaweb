---
layout: default
title: Education
description: Academic education and selected technical training in physics, scientific computing, radio astronomy and instrumentation.
permalink: /education/
---
<style>
  .education-page-intro {
    font-size: 1.16rem !important;
    line-height: 1.7 !important;
  }
  .education-training-grid {
    gap: 1.35rem !important;
  }
  .education-training-grid .content-card {
    padding: 1.55rem 1.6rem !important;
    min-height: 190px;
  }
  .education-training-grid .content-card h3 {
    font-size: 1.72rem !important;
  }
  .education-training-grid .content-card p {
    font-size: 1.07rem !important;
    line-height: 1.7 !important;
  }
  .education-foundation .section-title {
    font-size: 2rem !important;
  }
  .education-foundation .tag-list {
    gap: .72rem !important;
    margin-top: 1.1rem !important;
  }
  .education-foundation .tag {
    padding: .7rem 1.05rem !important;
    font-size: 1.12rem !important;
    line-height: 1.3 !important;
  }
  @media (max-width: 600px) {
    .education-training-grid .content-card {
      min-height: 0;
      padding: 1.3rem !important;
    }
    .education-foundation .tag {
      padding: .62rem .9rem !important;
      font-size: 1.02rem !important;
    }
  }
</style>

<h1>Education & Training</h1>
<p class="page-intro education-page-intro">A physics foundation extending from fundamental theory to computation, instrumentation, radiation measurement, radio detection, and machine learning.</p>

{% assign education = site.data.data.education %}
{% if education %}
<section class="section educations-section">
  <h2 class="section-title">
    <span class="section-icon" aria-hidden="true"><i class="fas fa-graduation-cap"></i></span>
    {{ education.title }}
  </h2>

  {% for graduation in education.info %}
  <div class="item">
    <div class="meta">
      <h3 class="degree">{{ graduation.degree }}</h3>
      <div class="university">{{ graduation.university }}</div>
    </div>
    {% if graduation.details %}
    <div class="details">
      {{ graduation.details | markdownify }}
    </div>
    {% endif %}
  </div>
  {% endfor %}
</section>
{% endif %}

<section class="section">
  <h2 class="section-title"><span class="section-icon" aria-hidden="true"><i class="fas fa-certificate"></i></span>Selected Training</h2>
  <div class="card-grid education-training-grid">
    <article class="content-card"><h3>Development in Africa with Radio Astronomy</h3><p>Training in radio astronomy, radio detection techniques, data analysis, and large-scale scientific instrumentation.</p></article>
    <article class="content-card"><h3>Machine Learning in Physics</h3><p>Machine-learning methods and their application to particle physics and astrophysical datasets.</p></article>
    <article class="content-card"><h3>LiDAR and Optical Instrumentation</h3><p>ICTP-linked training and practical exposure to LiDAR operations, optics, calibration, and atmospheric measurements.</p></article>
    <article class="content-card"><h3>Computing Foundations</h3><p>Formal computer training in operating systems, Microsoft Office applications, databases, software installation, typing, and internet skills.</p></article>
  </div>
</section>

<section class="section education-foundation">
  <h2 class="section-title"><span class="section-icon" aria-hidden="true"><i class="fas fa-book"></i></span>Physics Foundation</h2>
  <div class="tag-list">
    <span class="tag">Classical mechanics</span><span class="tag">Electromagnetism</span>
    <span class="tag">Quantum mechanics</span><span class="tag">Statistical physics</span>
    <span class="tag">Thermodynamics</span><span class="tag">Optics</span>
    <span class="tag">Analogue electronics</span><span class="tag">Digital electronics</span>
    <span class="tag">Solid-state physics</span><span class="tag">Computational physics</span>
    <span class="tag">Nuclear physics</span><span class="tag">Renewable energy</span>
  </div>
</section>
