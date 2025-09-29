**Notice:** While JavaScript is not essential for this website, your interaction with the content will be limited. Please turn JavaScript on for the full experience. 
[Skip to content](https://www.python.org/#content "Skip to content")
[ ▼ Close ](https://www.python.org/#python-network)
  * [Python](https://www.python.org/ "The Python Programming Language")
  * [PSF](https://www.python.org/psf/ "The Python Software Foundation")
  * [Docs](https://docs.python.org "Python Documentation")
  * [PyPI](https://pypi.org/ "Python Package Index")
  * [Jobs](https://www.python.org/jobs/ "Python Job Board")
  * [Community](https://www.python.org/community/)

[ ▲ The Python Network ](https://www.python.org/#top)
#  [![python™](https://www.python.org/static/img/python-logo.png)](https://www.python.org/)
[Donate](https://psfmember.org/civicrm/contribute/transact?reset=1&id=2)
[≡ Menu](https://www.python.org/#site-map) Search This Site GO 
  * [**A A**](https://www.python.org/)
    * [Smaller](javascript:; "Make Text Smaller")
    * [Larger](javascript:; "Make Text Larger")
    * [Reset](javascript:; "Reset any font size changes I have made")


  * [Socialize](https://www.python.org/)
    * [](https://www.linkedin.com/company/python-software-foundation/)
    * [](https://fosstodon.org/@ThePSF)
    * [](https://www.python.org/community/irc/)
    * [](https://twitter.com/ThePSF)


  * [Sign In](https://www.python.org/accounts/login/ "Sign Up or Sign In to Python.org")
    * [Sign Up / Register](https://www.python.org/accounts/signup/)
    * [Sign In](https://www.python.org/accounts/login/)


  * [About](https://www.python.org/about/)
    * [Applications](https://www.python.org/about/apps/)
    * [Quotes](https://www.python.org/about/quotes/)
    * [Getting Started](https://www.python.org/about/gettingstarted/)
    * [Help](https://www.python.org/about/help/)
    * [Python Brochure](http://brochure.getpython.info/)
  * [Downloads](https://www.python.org/downloads/)
    * [All releases](https://www.python.org/downloads/)
    * [Source code](https://www.python.org/downloads/source/)
    * [Windows](https://www.python.org/downloads/windows/)
    * [macOS](https://www.python.org/downloads/macos/)
    * [Android](https://www.python.org/downloads/android/)
    * [Other Platforms](https://www.python.org/download/other/)
    * [License](https://docs.python.org/3/license.html)
    * [Alternative Implementations](https://www.python.org/download/alternatives)
  * [Documentation](https://www.python.org/doc/)
    * [Docs](https://www.python.org/doc/)
    * [Audio/Visual Talks](https://www.python.org/doc/av)
    * [Beginner's Guide](https://wiki.python.org/moin/BeginnersGuide)
    * [Developer's Guide](https://devguide.python.org/)
    * [FAQ](https://docs.python.org/faq/)
    * [Non-English Docs](http://wiki.python.org/moin/Languages)
    * [PEP Index](https://peps.python.org)
    * [Python Books](https://wiki.python.org/moin/PythonBooks)
    * [Python Essays](https://www.python.org/doc/essays/)
  * [Community](https://www.python.org/community/)
    * [Diversity](https://www.python.org/community/diversity/)
    * [Mailing Lists](https://www.python.org/community/lists/)
    * [IRC](https://www.python.org/community/irc/)
    * [Forums](https://www.python.org/community/forums/)
    * [PSF Annual Impact Report](https://www.python.org/psf/annual-report/2024/)
    * [Python Conferences](https://www.python.org/community/workshops/)
    * [Special Interest Groups](https://www.python.org/community/sigs/)
    * [Python Logo](https://www.python.org/community/logos/)
    * [Python Wiki](https://wiki.python.org/moin/)
    * [Code of Conduct](https://www.python.org/psf/conduct/)
    * [Community Awards](https://www.python.org/community/awards)
    * [Get Involved](https://www.python.org/psf/get-involved/)
    * [Shared Stories](https://www.python.org/psf/community-stories/)
  * [Success Stories](https://www.python.org/success-stories/ "success-stories")
    * [Arts](https://www.python.org/success-stories/category/arts/)
    * [Business](https://www.python.org/success-stories/category/business/)
    * [Education](https://www.python.org/success-stories/category/education/)
    * [Engineering](https://www.python.org/success-stories/category/engineering/)
    * [Government](https://www.python.org/success-stories/category/government/)
    * [Scientific](https://www.python.org/success-stories/category/scientific/)
    * [Software Development](https://www.python.org/success-stories/category/software-development/)
  * [News](https://www.python.org/blogs/ "News from around the Python world")
    * [Python News](https://www.python.org/blogs/ "Python Insider Blog Posts")
    * [PSF Newsletter](https://www.python.org/psf/newsletter/ "Python Software Foundation Newsletter")
    * [PSF News](http://pyfound.blogspot.com/ "PSF Blog")
    * [PyCon US News](http://pycon.blogspot.com/ "PyCon Blog")
    * [News from the Community](http://planetpython.org/ "Planet Python")
  * [Events](https://www.python.org/events/)
    * [Python Events](https://www.python.org/events/python-events/)
    * [User Group Events](https://www.python.org/events/python-user-group/)
    * [Python Events Archive](https://www.python.org/events/python-events/past/)
    * [User Group Events Archive](https://www.python.org/events/python-user-group/past/)
    * [Submit an Event](https://wiki.python.org/moin/PythonEventsCalendar#Submitting_an_Event)


  * [>_ Launch Interactive Shell ](https://www.python.org/shell/)


  * ```
# Python 3: Fibonacci series up to n
>>> def fib(n):
>>>     a, b = 0, 1
>>>     while a < n:
>>>         print(a, end=' ')
>>>         a, b = b, a+b
>>>     print()
>>> fib(1000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
```

# Functions Defined
The core of extensible programming is defining functions. Python allows mandatory and optional arguments, keyword arguments, and even arbitrary argument lists. [More about defining functions in Python 3](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
  * ```
# Python 3: List comprehensions
>>> fruits = ['Banana', 'Apple', 'Lime']
>>> loud_fruits = [fruit.upper() for fruit in fruits]
>>> print(loud_fruits)
['BANANA', 'APPLE', 'LIME']

# List and the enumerate function
>>> list(enumerate(fruits))
[(0, 'Banana'), (1, 'Apple'), (2, 'Lime')]
```

# Compound Data Types
Lists (known as arrays in other languages) are one of the compound data types that Python understands. Lists can be indexed, sliced and manipulated with other built-in functions. [More about lists in Python 3](https://docs.python.org/3/tutorial/introduction.html#lists)
  * ```
# Python 3: Simple arithmetic
>>> 1 / 2
0.5
>>> 2 ** 3
8
>>> 17 / 3  # classic division returns a float
5.666666666666667
>>> 17 // 3  # floor division
5
```

# Intuitive Interpretation
Calculations are simple with Python, and expression syntax is straightforward: the operators `+`, `-`, `*` and `/` work as expected; parentheses `()` can be used for grouping. [More about simple math functions in Python 3](http://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator).
  * ```
# For loop on a list
>>> numbers = [2, 4, 6, 8]
>>> product = 1
>>> for number in numbers:
...    product = product * number
... 
>>> print('The product is:', product)
The product is: 384
```

# All the Flow You’d Expect
Python knows the usual control flow statements that other languages speak — `if`, `for`, `while` and `range` — with some of its own twists, of course. [More control flow tools in Python 3](https://docs.python.org/3/tutorial/controlflow.html)
  * ```
# Simple output (with Unicode)
>>> print("Hello, I'm Python!")
Hello, I'm Python!
# Input, assignment
>>> name = input('What is your name?\n')
What is your name?
Python
>>> print(f'Hi, {name}.')
Hi, Python.

```

# Quick & Easy to Learn
Experienced programmers in any other language can pick up Python very quickly, and beginners find the clean syntax and indentation structure easy to learn. [Whet your appetite](https://docs.python.org/3/tutorial/) with our Python 3 overview.


  1. 1
  2. 2
  3. 3
  4. 4
  5. 5


Python is a programming language that lets you work quickly [Learn More](https://www.python.org/doc/)
Whether you're new to programming or an experienced developer, it's easy to learn and use Python.
[Start with our Beginner’s Guide](https://www.python.org/about/gettingstarted/)
Python source code and installers are available for download for all versions!
Latest: [Python 3.13.7](https://www.python.org/downloads/release/python-3137/)
Documentation for Python's standard library, along with tutorials and guides, are available online.
[docs.python.org](https://docs.python.org)
Looking for work or have a Python related position that you're trying to hire for? Our **relaunched community-run job board** is the place to go.
[jobs.python.org](https://jobs.python.org)
[More](https://blog.python.org "More News")
  * 2025-08-26 [pypistats.org is now operated by the Python Software Foundation](https://pyfound.blogspot.com/2025/08/pypistats-org-is-now-operated-by-the-psf.html)
  * 2025-08-18 [The 2024 Python Developer Survey Results are here!](https://pyfound.blogspot.com/2025/08/the-2024-python-developer-survey.html)
  * 2025-08-14 [Python 3.14.0rc2 and 3.13.7 are go!](https://pythoninsider.blogspot.com/2025/08/python-3140rc2-and-3137-are-go.html)
  * 2025-08-14 [Announcing the PSF Board Candidates for 2025!](https://pyfound.blogspot.com/2025/08/announcing-psf-board-candidates-for-2025.html)
  * 2025-08-08 [Announcing Python Software Foundation Fellow Members for Q2 2025! 🎉](https://pyfound.blogspot.com/2025/08/announcing-python-software-foundation.html)


[More](https://www.python.org/events/calendars/ "More Events")
  * 2025-09-04 [Python Leiden User Group](https://www.python.org/events/python-user-group/2085/)
  * 2025-09-06 [PyCon Taiwan](https://www.python.org/events/python-events/1991/)
  * 2025-09-09 [Workshop: Creating Python Communities](https://www.python.org/events/python-user-group/2097/)
  * 2025-09-09 [PyCon Israel 2025](https://www.python.org/events/python-events/2021/)
  * 2025-09-10 [Python Meeting Düsseldorf](https://www.python.org/events/python-user-group/2030/)


[More](https://www.python.org/success-stories/ "More Success Stories")
> [Python programmability on Algorand makes the entire development lifecycle easier and means more affordable and efficient maintenance and upgrades going forward.](https://www.python.org/success-stories/using-python-to-build-a-solution-for-instant-tokenized-real-estate-redemptions/)
[Using Python to build a solution for instant tokenized real estate redemptions](https://www.python.org/success-stories/using-python-to-build-a-solution-for-instant-tokenized-real-estate-redemptions/) _by Brian Whippo, Head of Developer Relations, Algorand Foundation_  
---  
[More](https://www.python.org/about/apps "More Applications")
  * **Web Development** : [Django](http://www.djangoproject.com/), [Pyramid](http://www.pylonsproject.org/), [Bottle](http://bottlepy.org), [Tornado](http://tornadoweb.org), [Flask](http://flask.pocoo.org/), [web2py](http://www.web2py.com/)
  * **GUI Development** : [tkInter](http://wiki.python.org/moin/TkInter), [PyGObject](https://wiki.gnome.org/Projects/PyGObject), [PyQt](http://www.riverbankcomputing.co.uk/software/pyqt/intro), [PySide](https://wiki.qt.io/PySide), [Kivy](https://kivy.org/), [wxPython](http://www.wxpython.org/), [DearPyGui](https://dearpygui.readthedocs.io/en/latest/)
  * **Scientific and Numeric** :  [SciPy](http://www.scipy.org), [Pandas](http://pandas.pydata.org/), [IPython](http://ipython.org)
  * **Software Development** : [Buildbot](http://buildbot.net/), [Trac](http://trac.edgewall.org/), [Roundup](http://roundup.sourceforge.net/)
  * **System Administration** : [Ansible](http://www.ansible.com), [Salt](https://saltproject.io), [OpenStack](https://www.openstack.org), [xonsh](https://xon.sh)


##  >>> [Python Software Foundation](https://www.python.org/psf/)
The mission of the Python Software Foundation is to promote, protect, and advance the Python programming language, and to support and facilitate the growth of a diverse and international community of Python programmers. [Learn more](https://www.python.org/psf/)
[Become a Member](https://www.python.org/psf/membership/) [Donate to the PSF](https://www.python.org/psf/donations/)
[▲ Back to Top](https://www.python.org/#python-network)
  * [About](https://www.python.org/about/)
    * [Applications](https://www.python.org/about/apps/)
    * [Quotes](https://www.python.org/about/quotes/)
    * [Getting Started](https://www.python.org/about/gettingstarted/)
    * [Help](https://www.python.org/about/help/)
    * [Python Brochure](http://brochure.getpython.info/)
  * [Downloads](https://www.python.org/downloads/)
    * [All releases](https://www.python.org/downloads/)
    * [Source code](https://www.python.org/downloads/source/)
    * [Windows](https://www.python.org/downloads/windows/)
    * [macOS](https://www.python.org/downloads/macos/)
    * [Android](https://www.python.org/downloads/android/)
    * [Other Platforms](https://www.python.org/download/other/)
    * [License](https://docs.python.org/3/license.html)
    * [Alternative Implementations](https://www.python.org/download/alternatives)
  * [Documentation](https://www.python.org/doc/)
    * [Docs](https://www.python.org/doc/)
    * [Audio/Visual Talks](https://www.python.org/doc/av)
    * [Beginner's Guide](https://wiki.python.org/moin/BeginnersGuide)
    * [Developer's Guide](https://devguide.python.org/)
    * [FAQ](https://docs.python.org/faq/)
    * [Non-English Docs](http://wiki.python.org/moin/Languages)
    * [PEP Index](https://peps.python.org)
    * [Python Books](https://wiki.python.org/moin/PythonBooks)
    * [Python Essays](https://www.python.org/doc/essays/)
  * [Community](https://www.python.org/community/)
    * [Diversity](https://www.python.org/community/diversity/)
    * [Mailing Lists](https://www.python.org/community/lists/)
    * [IRC](https://www.python.org/community/irc/)
    * [Forums](https://www.python.org/community/forums/)
    * [PSF Annual Impact Report](https://www.python.org/psf/annual-report/2024/)
    * [Python Conferences](https://www.python.org/community/workshops/)
    * [Special Interest Groups](https://www.python.org/community/sigs/)
    * [Python Logo](https://www.python.org/community/logos/)
    * [Python Wiki](https://wiki.python.org/moin/)
    * [Code of Conduct](https://www.python.org/psf/conduct/)
    * [Community Awards](https://www.python.org/community/awards)
    * [Get Involved](https://www.python.org/psf/get-involved/)
    * [Shared Stories](https://www.python.org/psf/community-stories/)
  * [Success Stories](https://www.python.org/success-stories/ "success-stories")
    * [Arts](https://www.python.org/success-stories/category/arts/)
    * [Business](https://www.python.org/success-stories/category/business/)
    * [Education](https://www.python.org/success-stories/category/education/)
    * [Engineering](https://www.python.org/success-stories/category/engineering/)
    * [Government](https://www.python.org/success-stories/category/government/)
    * [Scientific](https://www.python.org/success-stories/category/scientific/)
    * [Software Development](https://www.python.org/success-stories/category/software-development/)
  * [News](https://www.python.org/blogs/ "News from around the Python world")
    * [Python News](https://www.python.org/blogs/ "Python Insider Blog Posts")
    * [PSF Newsletter](https://www.python.org/psf/newsletter/ "Python Software Foundation Newsletter")
    * [PSF News](http://pyfound.blogspot.com/ "PSF Blog")
    * [PyCon US News](http://pycon.blogspot.com/ "PyCon Blog")
    * [News from the Community](http://planetpython.org/ "Planet Python")
  * [Events](https://www.python.org/events/)
    * [Python Events](https://www.python.org/events/python-events/)
    * [User Group Events](https://www.python.org/events/python-user-group/)
    * [Python Events Archive](https://www.python.org/events/python-events/past/)
    * [User Group Events Archive](https://www.python.org/events/python-user-group/past/)
    * [Submit an Event](https://wiki.python.org/moin/PythonEventsCalendar#Submitting_an_Event)
  * [Contributing](https://www.python.org/dev/)
    * [Developer's Guide](https://devguide.python.org/)
    * [Issue Tracker](https://github.com/python/cpython/issues)
    * [python-dev list](https://mail.python.org/mailman/listinfo/python-dev)
    * [Core Mentorship](https://www.python.org/dev/core-mentorship/)
    * [Report a Security Issue](https://www.python.org/dev/security/)

[▲ Back to Top](https://www.python.org/#python-network)
  * [Help & General Contact](https://www.python.org/about/help/)
  * [Diversity Initiatives](https://www.python.org/community/diversity/)
  * [Submit Website Bug](https://github.com/python/pythondotorg/issues)
  * [Status ](https://status.python.org/)


Copyright ©2001-2025. [Python Software Foundation](https://www.python.org/psf-landing/) [Legal Statements](https://www.python.org/about/legal/) [Privacy Notice](https://policies.python.org/python.org/Privacy-Notice/)
