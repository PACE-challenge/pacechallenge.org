---
layout: page 
title: "PACE 2025 - Gallery"
---

<style>
.gallery {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 16px;
  align-items: stretch;
}
.gallery-item img {
  width: 100%;
  height: auto;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  display: block;
}
.gallery-item.portrait {
  grid-row: span 2;
}
@media (max-width: 600px) {
  .gallery {
    grid-template-columns: 1fr;
  }
  .gallery-item.portrait {
    grid-row: span 1;
  }
}
</style>

<!-- ...existing code... -->

<div id="lightbox" class="lightbox" style="display:none;">
  <span class="lightbox-close" onclick="closeLightbox()">&times;</span>
  <img id="lightbox-img" src="" alt="Großes Bild">
</div>

<style>
/* ...existing styles... */
.lightbox {
  position: fixed;
  z-index: 1000;
  left: 0; top: 0; width: 100vw; height: 100vh;
  background: rgba(0,0,0,0.8);
  display: flex; align-items: center; justify-content: center;
}
.lightbox img {
  max-width: 90vw;
  max-height: 90vh;
  border-radius: 10px;
  box-shadow: 0 4px 32px rgba(0,0,0,0.5);
}
.lightbox-close {
  position: absolute;
  top: 32px; right: 48px;
  font-size: 3rem;
  color: #fff;
  cursor: pointer;
  z-index: 1001;
  user-select: none;
}
</style>

<script>
function openLightbox(src) {
  document.getElementById('lightbox-img').src = src;
  document.getElementById('lightbox').style.display = 'flex';
}
function closeLightbox() {
  document.getElementById('lightbox').style.display = 'none';
  document.getElementById('lightbox-img').src = '';
}
// Schließen bei Klick auf Hintergrund
document.addEventListener('DOMContentLoaded', function() {
  document.getElementById('lightbox').addEventListener('click', function(e) {
    if (e.target === this) closeLightbox();
  });
});
</script>

<!-- Passe die img-Tags in der Galerie an: -->
<div class="gallery">
  {% assign portrait_images = "IMG_20250918_132650.jpg,IMG_20250918_185043.jpg" | split: "," %}
  {% for file in site.static_files %}
    {% if file.path contains '/gallery/' %}
      {% assign filename = file.path | split: "/" | last %}
      <div class="gallery-item{% if portrait_images contains filename %} portrait{% endif %}">
        <img src="{{ file.path }}" alt="img" onclick="openLightbox(this.src)">
      </div>
    {% endif %}
  {% endfor %}
</div>