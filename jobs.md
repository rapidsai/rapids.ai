---
layout: default
title: Join the RAPIDS Team | RAPIDS
---
<h1>Latest Job Posts</h1>

{% for category in site.categories %}
{% if category == "job" %}
  <ul>
    {% for post in category[1] %}
      <li><h2><a href="{{ post.url }}">{{ post.title }}</a></h2>
      <p>{{ post.excerpt }}</p></li>
    {% endfor %}
  </ul>
{% endif %}
{% endfor %}

<ul>
  {% for post in site.posts %}
    <li>
      <h2><a href="{{ post.url }}">{{ post.title }}</a></h2>
      <p>{{ post.excerpt }}</p>
    </li>
  {% endfor %}
</ul>
