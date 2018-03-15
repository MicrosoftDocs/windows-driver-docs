---
title: About the Sensor Class Extension
author: windows-driver-content
description: About the Sensor Class Extension
ms.assetid: 4b55e5fe-2947-4511-ba2d-479d5fd83ebe
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# About the Sensor Class Extension


To make it easier to write a device driver that exposes a sensor to Windows (and to the sensor and location platform in particular), Windows includes a sensor driver class extension. A required component for sensor device drivers, this COM object provides a simple set of interfaces that enable programmers to implement a sensor driver without writing lots of boilerplate code. Additionally, this class extension provides the following benefits:

-   Helps to ensure that user privacy is well protected because the class extension enforces appropriate access control restrictions for sensors that handle personal information.

-   Provides a standard way to retrieve data from the driver and to raise event notifications through the API layers.

 

 




