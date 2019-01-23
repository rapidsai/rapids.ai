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
### {{ post.title }}
{{ post.excerpt }}

[Learn more...]({{site.repo-name}}{{ post.url }})
</div>
{% endfor %}
{% endif %}
{% endfor %}
</div>
