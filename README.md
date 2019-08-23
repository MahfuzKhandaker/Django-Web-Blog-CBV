# Django-Web-Blog-CBV
Django class bases views blog application

# Generic Class-Based Views
The generic class-based-views was introduced to address the common use cases in a Web application, such as creating new objects, form handling, list views, pagination, archive views and so on. They come in the Django core, and you can implement them from the module django.views.generic. They are great and can speed up the development process.

Class-based views provide an alternative way to implement views as Python objects instead of functions. They do not replace function-based views, but have certain differences and advantages when compared to function-based views.

Pros:
> Code reuseability — In CBV, a view class can be inherited by another view class and modified for a different use case.
> DRY — Using CBVs help to reduce code duplication.
> Code extendability — CBV can be extended to include more functionalities using Mixins.
> Code structuring — In CBVs A class based view helps you respond to different http request with different class instance methods instead of conditional branching statements inside a single function based view.
Built-in generic class-based views.

Cons:
> Harder to read.
> Implicit code flow.
> Use of view decorators require extra import, or method override.



