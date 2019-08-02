---
title: "Blog"
description: "Read the Latest News and Announcements on Our RAPIDS Blog"
tagline: "Read Our Latest News"
layout: short
---
{% include tag-list-sorted.html %}

<section class="blog-container container-padding">
{% for category in site.categories %}
  {% if category[0] == "blog" %}
    {% for post in category[1] %}
      <div class="blog-preview-item">
          <h1><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h1>
          <div class="post-excerpt">{{ post.excerpt }}</div>
          <a class="post-read-more" href="{{ site.baseurl }}{{ post.url }}">Read More <i class="fas fa-angle-double-right"></i></a>
          <div class="posts-date"> <i class="far fa-calendar"></i> {{ post.date | date_to_string }} </div>
          <div class="posts-author">
            {% assign authorlist = post.author | split: ", " %}
            {% for person in authorlist %}
              {% assign author = site.authors | where: 'short_name', person | first %}
              {% if author %}
                 <i class="fas fa-pen"></i> <a href="{{ site.baseurl }}{{ author.url }}">{{ author.name }}</a> &nbsp;
              {% else %}
                <i class="fas fa-pen"></i> {{ person }} &nbsp;
              {% endif %}
            {% endfor %}
          </div>
      </div>
    {% endfor %}
  {% endif %}
{% endfor %}
</section>

{% include tag-list.html %}