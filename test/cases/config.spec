{
  "env": {
      "format": "string ['production', 'local']",
      "env": "NODE_ENV"
  },
  "URL": "https://browserid.org",
  "use_minified_resources": true,
  "var_path": "/home/browserid/var",
  "database": {
    "driver": "mysql",
    "user": 'browserid',
    "create_schema": true,
    "may_write": false
  },
  "statsd": {
    "enabled": true
  },
  "bcrypt_work_factor": 12,
  "authentication_duration": "2 weeks",
  "certificate_validity": "1 day",
  "min_time_between_emails": "1 minute",
  "max_compute_duration": "10 seconds",
  "disable_primary_support": false,
  // code_version is a property in the session_context response...  When
  // enabled it causes frontend code to employ cache busting logic.  issue #226
  "enable_code_version": false,
  "default_lang": [ 'en-US' ],
  "supported_languages": [ 'en-US' ],
  // Contains po files
  "locale_directory": "locale",
  "express_log_format": "default"
}
