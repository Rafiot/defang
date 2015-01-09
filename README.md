defang
======

Defangs and refangs malicious URLs

Usage
-----

- As a script: use the `defang` command to defang or "refang"
  content, supporting
  both stdin/stdout streams as well as to/from files on disk::

        $ echo http://evil.example.com/malicious.php | defang
        hXXp://evil.example[.]com/malicious.php

- As a library::

        >>> from defang import defang
        >>> url = "http://evil.example.com/malicious.php"
        >>> defang(url)
        'hXXp://evil.example[.]com/malicious.php'
