#
# comment model
# @author Chris Tate <crystal@test.com>
#

from django.db import models

class comment(models.Model):
	approved = models.bool()
	author = models.string()
	author_email = models.string()
	author_ip = models.string()
	author_url = models.string()
	content = models.text()
	created = models.created()
	deleted = models.deleted()
	id = models.id()
	post = models.model()
	updated = models.updated()
	user = models.model()
