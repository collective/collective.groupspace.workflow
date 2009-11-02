Introduction
============

Implements a placeful workflow policy needed for the GroupSpace content type that makes sure that, unless otherwise defined, all content types use the default workflow as defined by the placeful workflow policy.

collective.groupspace.workflow Installation
-------------------------------------------

To install collective.groupspace.workflow into the global Python environment (or a workingenv),
using a traditional Zope 2 instance, you can do this:

* When you're reading this you have probably already run 
  ``easy_install collective.groupspace.workflow``. Find out how to install setuptools
  (and EasyInstall) here:
  http://peak.telecommunity.com/DevCenter/EasyInstall

* Create a file called ``collective.groupspace.workflow-configure.zcml`` in the
  ``/path/to/instance/etc/package-includes`` directory.  The file
  should only contain this::

    <include package="collective.groupspace.workflow" />


Alternatively, if you are using zc.buildout and the plone.recipe.zope2instance
recipe to manage your project, you can do this:

* Add ``collective.groupspace.workflow`` to the list of eggs to install, e.g.:

    [buildout]
    ...
    eggs =
        ...
        collective.groupspace.workflow
       
* Tell the plone.recipe.zope2instance recipe to install a ZCML slug:

    [instance]
    recipe = plone.recipe.zope2instance
    ...
    zcml =
        collective.groupspace.workflow
      
* Re-run buildout, e.g. with:

    $ ./bin/buildout
        
You can skip the ZCML slug if you are going to explicitly include the package
from another package's configure.zcml file.
