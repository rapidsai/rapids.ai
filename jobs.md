---
layout: default
title: Join the RAPIDS Team | RAPIDS
---

## Latest Job Posts

<div class="footer-help-section">
  {% for category in site.categories %}
  {% if category[0] == "job" %}
  {% for post in category[1] %}
  <div "footer-help-box">
    <h3>{{ post.title }}</h3>
    <p>{{ post.excerpt }}</p>
    <p><a href="{{ site.baseurl }}{{ post.url }}">Learn more...</a></p>
  </div>
  {% endfor %}
  {% endif %}
  {% endfor %}
</div>
