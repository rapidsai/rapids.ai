---
layout: default
title: Join the RAPIDS Team | RAPIDS
---

## Latest Job Posts

{% for category in site.categories %}
{% if category[0] == "job" %}
  <ul>
    {% for post in category[1] %}
      <li><h2><a href="{{ site.root }}{{ post.url }}">{{ post.title }}</a></h2>
      <p>{{ post.excerpt }}</p></li>
    {% endfor %}
  </ul>
{% endif %}
{% endfor %}
