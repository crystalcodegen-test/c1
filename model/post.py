#
# post model
# @author Chris Tate <crystal@test.com>
#

from django.db import models

class post(models.Model):
	content = models.text()
	created = models.created()
	deleted = models.deleted()
	id = models.id()
	name = models.string()
	status = models.select()
	title = models.string()
	updated = models.updated()
