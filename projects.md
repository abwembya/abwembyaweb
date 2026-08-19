---
layout: default
title: Projects
description: Selected projects in sensing, scientific modelling, artificial intelligence and sustainable technology.
permalink: /projects/
sidebar_compact: true
---
<h1>Projects</h1>
<p class="page-intro">A selection of technical work spanning sensor calibration, scientific modelling, AI-assisted diagnostics, and sustainability.</p>

<div class="filter-bar d-print-none" aria-label="Filter projects">
  <button class="filter-button active" data-filter="all">All</button>
  <button class="filter-button" data-filter="sensing">Sensing</button>
  <button class="filter-button" data-filter="modelling">Modelling</button>
  <button class="filter-button" data-filter="ai">AI & Data</button>
  <button class="filter-button" data-filter="impact">Impact</button>
</div>

<div class="visual-strip" aria-label="Art inspired by radio timing and distributed sensor arrays">
  <img src="{{ site.baseurl }}/assets/images/timing-array-yellow.webp" alt="Abstract artwork inspired by timing stations and radio signals">
  <img src="{{ site.baseurl }}/assets/images/timing-array-blue.webp" alt="Abstract artwork inspired by a distributed antenna array">
</div>
<p class="visual-note">Visual studies inspired by distributed timing, antennas, and coherent signals.</p>

<div class="card-grid">
{% for project in site.data.data.projects.assignments %}
  <article class="content-card" data-category="{{ project.category }}">
    <h3>{{ project.title }}</h3>
    <p>{{ project.tagline }}</p>
    <span class="tag">{{ project.category | upcase }}</span>
    {% if project.title == "Radio Interferometry for Cosmic-Ray Detection" %}<p class="project-status"><i class="fas fa-check-circle"></i> Production research workflow.</p>{% endif %}
    {% if project.title == "Precision Timing and Phase Calibration" %}<p class="project-status"><i class="fas fa-check-circle"></i> Validated research workflow.</p>{% endif %}
    {% if project.title == "AI-Assisted RFI Classification" %}<p class="project-status"><i class="fas fa-flask"></i> Research concept in development - not yet deployed.</p>{% endif %}
  </article>
{% endfor %}
</div>

<section class="section ml-case-study">
  <h2 class="section-title"><span class="section-icon" aria-hidden="true"><i class="fas fa-brain"></i></span>Machine-Learning Case Study</h2>
  <div class="case-study-grid">
    <div><strong>Problem</strong><p>Radio-frequency interference can corrupt calibration and astronomical measurements, while simple threshold flagging discards useful data.</p></div>
    <div><strong>Approach</strong><p>Concept design using spectral, temporal and modulation features with supervised classification, calibrated probabilities and anomaly detection.</p></div>
    <div><strong>Evaluation plan</strong><p>Benchmark precision, recall and calibration residuals against established flagging methods, then test probabilistic weighting in the calibration pipeline.</p></div>
    <div><strong>Maturity</strong><p>Research concept and prototype plan. No deployment or performance metric is claimed yet.</p></div>
  </div>
</section>

<section class="section" style="margin-top:2rem">
  <h2 class="section-title"><span class="section-icon" aria-hidden="true"><i class="fas fa-code-branch"></i></span>Working Principles</h2>
  <div class="card-grid">
    <article class="content-card"><h3>Traceable</h3><p>Explicit assumptions, versioned inputs, reproducible pipelines, and clear provenance from raw data to result.</p></article>
    <article class="content-card"><h3>Uncertainty-aware</h3><p>Calibration errors, model limitations, and confidence are treated as part of the result—not as afterthoughts.</p></article>
    <article class="content-card"><h3>Operational</h3><p>Diagnostics and visualisations are designed to help people detect failure modes and make better decisions.</p></article>
    <article class="content-card"><h3>Responsible</h3><p>Models should be explainable, appropriately validated, and used with attention to scientific and societal consequences.</p></article>
  </div>
</section>
