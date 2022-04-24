LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
    },
    'filters': {
        'admin_user': {
            '()': 'users.logging.AdminFilter'
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
            'filters': ['require_debug_true']
        },
        'users_file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': 'users.log',
            'filters': ['admin_user']
        },
        'emails_file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'emails.log',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
        }
    },
    'loggers': {
        'users': {
            'handlers': ['users_file', 'console', 'mail_admins'],
            'level': 'WARNING',
            'propagate': False,
        },
        'users.views': {
            'handlers': ['users_file'],
            'level': 'WARNING',
            'propagate': False,
        },
        'emails': {
            'handlers': ['emails_file', 'console'],
            'level': 'INFO'
        },
        'emails.views': {
            'handlers': ['emails_file'],
            'level': 'INFO',
            'propagate': False,
        },

    }
}
