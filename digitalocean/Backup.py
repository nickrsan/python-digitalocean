from .baseapi import BaseAPI, Error, GET, POST, DELETE

class Backup(BaseAPI):

    def __init__(self, *args, **kwargs):
        if "id" in kwargs.keys():
            self.id = kwargs['id']
        else:
            self.id = None

        self.name = None

        if self.id:  # if we have an ID to load, try to load!
            self.load()

        if "droplet" in kwargs.keys():
            self.set_droplet(kwargs["droplet"])
        else:
            self.droplet = None

        super(Backup, self).__init__(*args, **kwargs)

    def set_droplet(self, droplet):
        self.droplet = droplet  # reference the parent droplet
        self.token = droplet.token

    def load(self):
        backups = self.get_data("droplets/%s/backups" % self.id)  # this is roundabout and inefficient, making a request per backup instead of a single request. Could do this from a control function instead, or
        print backups[0]
        pass