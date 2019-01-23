---
title: Join the RAPIDS Team | RAPIDS
og_title: "Join the RAPIDS Team!"
og_description: "RAPIDS is looking to hire new developers to the team. Apply today to become a part of the RAPIDS team!"
brand_name: "JOB BOARD"
brand_tagline: "Join the RAPIDS team!"
layout: short
---

## Latest Job Posts

<div class="features-row">
  <ul>
  {% for category in site.categories %}
    {% if category[0] == "job" %}
      {% for post in category[1] %}
        <li>
          <h3><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h3>
          <p>{{ post.date | date_to_string }}</p>
          <p>{{ post.excerpt }}</p>
          <p><a href="{{ site.baseurl }}{{ post.url }}">Learn more...</a></p>
        </li>
        {% assign mod = forloop.index | modulo: 3 %}
        {% if mod == 0 %}
          </ul></div><div class="features-row"><ul>
        {% endif %}
      {% endfor %}
    {% endif %}
  {% endfor %}
  </ul>
</div>
