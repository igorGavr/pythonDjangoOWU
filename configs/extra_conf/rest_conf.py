REST_FRAMEWORK = {
  'DEFAULT_AUTHENTICATION_CLASSES': (
    'rest_framework_simplejwt.authentication.JWTAuthentication',
  ),
  'DEFAULT_PERMISSION_CLASSES': (
    'rest_framework.permissions.IsAuthenticated',
  ),
  'DEFAULT_RENDERER_CLASSES': (
    'rest_framework.renderers.JSONRenderer',
  ),
  'EXCEPTION_HANDLER': 'core.handlers.error_handlers.custom_error_handler',

  'DEFAULT_FILTER_BACKENDS': (
    'django_filters.rest_framework.DjangoFilterBackend',
  ),
}



# DEFAULT_PERMISSION_CLASSES': (
#     'rest_framework.permissions.IsAuthenticated', --->  в такому випадку
#     доступ до всіх в"юшок по дефолту буде можливий тільки залогованим юзерам

#'PAGE_SIZE': 10  -- стандартна пагінація