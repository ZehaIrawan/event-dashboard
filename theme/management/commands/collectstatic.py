{
  "name": "dashboard-event",
  "version": "1.0.0",
  "description": "Dummy package.json to point the Heroku buildpack at the correct one.",
  "scripts": {
    "postinstall": "cd theme/static_src && npm install"
  },
  "cacheDirectories": [
    "theme/static_src/node_modules"
  ]
}