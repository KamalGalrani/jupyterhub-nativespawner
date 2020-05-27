# Copyright (c) Kamal Galrani.
# Distributed under the terms of the Modified BSD License.
import os
import sys

from traitlets import Unicode
from jupyterhub.spawner import LocalProcessSpawner


class NativeSpawner(LocalProcessSpawner):

    storage = Unicode(
        '/opt/jupyterhub/users',
        help="""
        The directory in which user notebooks are stored
        """,
    ).tag(config=True)

    def user_env(self, env):
        """Augment environment of spawned process with user specific env variables."""
        import pwd

        env['USER'] = self.user.name
        home = self.storage + '/' + self.user.name
        shell = '/bin/bash'
        # These will be empty if undefined,
        # in which case don't set the env:
        if home:
            env['HOME'] = home
        if shell:
            env['SHELL'] = shell
        return env

    async def move_certs(self, paths):
        """Disables move and sets ownership for cert paths

        Arguments:
            paths (dict): a list of paths for key, cert, and CA

        Returns:
            dict: a list (potentially altered) of paths for key, cert,
            and CA
        """
        return paths

    def make_preexec_fn(self, name):
        """
        Return a function that can be used to change directory to home directory of user with name `name`

        This function can be safely passed to `preexec_fn` of `Popen`
        """

        def preexec():
            """chdir to the user's home directory.
            """

            home = self.storage + '/' + name

            if not os.path.isdir(home):
                os.makedirs(home)

            os.chdir(home)

        return preexec
