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
  cursor: pointer;
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
.lightbox {
  position: fixed;
  z-index: 1000;
  left: 0; top: 0; width: 100vw; height: 100vh;
  background: rgba(0,0,0,0.8);
  display: none; align-items: center; justify-content: center;
}
.lightbox.active {
  display: flex;
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
.lightbox-arrow {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  font-size: 4rem;
  color: #fff;
  background: rgba(0,0,0,0.2);
  border: none;
  cursor: pointer;
  z-index: 1001;
  user-select: none;
  padding: 0 16px;
  border-radius: 8px;
}
.lightbox-arrow.left { left: 32px; }
.lightbox-arrow.right { right: 32px; }
</style>

<div id="lightbox" class="lightbox">
  <button class="lightbox-arrow left" onclick="prevLightbox(event)">&#8592;</button>
  <img id="lightbox-img" src="" alt="Großes Bild">
  <button class="lightbox-arrow right" onclick="nextLightbox(event)">&#8594;</button>
  <span class="lightbox-close" onclick="closeLightbox()">&times;</span>
</div>

<div class="gallery">
  {% assign portrait_images = "IMG_20250918_132650.jpg,IMG_20250918_185043.jpg" | split: "," %}
  {% assign gallery_files = site.static_files | where_exp: "file", "file.path contains '/gallery/'" %}
  {% for file in gallery_files %}
    {% assign filename = file.path | split: "/" | last %}
    <div class="gallery-item{% if portrait_images contains filename %} portrait{% endif %}">
      <img src="{{ file.path }}" alt="img" data-index="{{ forloop.index0 }}" onclick="openLightbox({{ forloop.index0 }})">
    </div>
  {% endfor %}
</div>

<script>
const galleryImages = [
  {% for file in gallery_files %}
    "{{ file.path }}"{% unless forloop.last %},{% endunless %}
  {% endfor %}
];
let currentIndex = 0;

function openLightbox(index) {
  currentIndex = index;
  document.getElementById('lightbox-img').src = galleryImages[currentIndex];
  document.getElementById('lightbox').classList.add('active');
}
function closeLightbox() {
  document.getElementById('lightbox').classList.remove('active');
  document.getElementById('lightbox-img').src = '';
}
function prevLightbox(event) {
  event.stopPropagation();
  currentIndex = (currentIndex - 1 + galleryImages.length) % galleryImages.length;
  document.getElementById('lightbox-img').src = galleryImages[currentIndex];
}
function nextLightbox(event) {
  event.stopPropagation();
  currentIndex = (currentIndex + 1) % galleryImages.length;
  document.getElementById('lightbox-img').src = galleryImages[currentIndex];
}
// Schließen bei Klick auf Hintergrund
document.addEventListener('DOMContentLoaded', function() {
  document.getElementById('lightbox').addEventListener('click', function(e) {
    if (e.target === this) closeLightbox();
  });
  // Tastatursteuerung
  document.addEventListener('keydown', function(e) {
    if (!document.getElementById('lightbox').classList.contains('active')) return;
    if (e.key === 'ArrowLeft') prevLightbox(e);
    if (e.key === 'ArrowRight') nextLightbox(e);
    if (e.key === 'Escape') closeLightbox();
  });
});
</script>