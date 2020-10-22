<xsl:stylesheet version="1.0"
xmlns:xsl="{% block urlParcel %}{% endblock %}">
<xsl:template match="/">
  <html>
  <head>
  </head>
    <h1>
      {% block content %}{% endblock %}
    </h1>
  </html>
</xsl:template>
</xsl:stylesheet>
