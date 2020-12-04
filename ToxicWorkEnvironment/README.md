# Python: A toxic work environment (tox & poetry)

This code contains the examples outlined in my Medium blog post titled "Python: A toxic work environment (tox & poetry)."  These examples are longform compared to the versions in the blog post (like splitting classes into their own files).

## Notes

These examples are based on Python 3.7 and Python 3.8 and use `poetry` to manage the environment.  To run, install `poetry` first, then from this folder run `tox`.  This will cause the same dependencies to be installed twice and the same unit test to run twice: once against Python 3.7 and once against Python 3.8.
