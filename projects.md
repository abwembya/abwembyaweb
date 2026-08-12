---
layout: default
title: Projects
description: Selected projects in sensing, scientific modelling, artificial intelligence and sustainable technology.
permalink: /projects/
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

<div class="card-grid">
{% for project in site.data.data.projects.assignments %}
  <article class="content-card" data-category="{{ project.category }}">
    <h3>{{ project.title }}</h3>
    <p>{{ project.tagline }}</p>
    <span class="tag">{{ project.category | upcase }}</span>
  </article>
{% endfor %}
</div>

<section class="section" style="margin-top:2rem">
  <h2 class="section-title"><span class="fa-stack fa-xs"><i class="fas fa-circle fa-stack-2x"></i><i class="fas fa-code-branch fa-stack-1x fa-inverse"></i></span>Working Principles</h2>
  <div class="card-grid">
    <article class="content-card"><h3>Traceable</h3><p>Explicit assumptions, versioned inputs, reproducible pipelines, and clear provenance from raw data to result.</p></article>
    <article class="content-card"><h3>Uncertainty-aware</h3><p>Calibration errors, model limitations, and confidence are treated as part of the result—not as afterthoughts.</p></article>
    <article class="content-card"><h3>Operational</h3><p>Diagnostics and visualisations are designed to help people detect failure modes and make better decisions.</p></article>
    <article class="content-card"><h3>Responsible</h3><p>Models should be explainable, appropriately validated, and used with attention to scientific and societal consequences.</p></article>
  </div>
</section>
