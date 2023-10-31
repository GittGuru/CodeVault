# CodeVault
# Workout Manager (wger)
![wger Logo](https://raw.githubusercontent.com/wger-project/wger/master/wger/core/static/images/logos/logo.png)

Welcome to wger, your free and open-source workout management tool. wger enables you to keep track of your workouts, weight, diet plans, and can even serve as a straightforward gym management solution. Plus, it offers a robust REST API for easy integration with various projects and tools.

For a live, fully functional system, visit the [wger project website](https://wger.de/).

![Workout Plan](https://raw.githubusercontent.com/wger-project/wger/master/wger/software/static/images/workout.png)

## Mobile App
- [Get it on Google Play](https://play.google.com/store/apps/details?id=de.wger.flutter)
- [Get it on F-Droid](https://f-droid.org/packages/de.wger.flutter/)

## Installation

Here are the basic steps to install and run the application locally on a Linux system. More detailed instructions, deployment options, and an administration guide are available at [wger.readthedocs.io](https://wger.readthedocs.io) or in the [docs repository](https://github.com/wger-project/docs).

Please consult the commands' help for additional information and available parameters.

### Production

If you intend to host your own instance, consider using the provided Docker Compose file. This configuration will persist your database and uploaded images: [Docker Compose for Production](https://github.com/wger-project/docker).

### Demo

For a quick trial:

```shell script
docker run -ti --name wger.demo --publish 8000:80 wger/demo
