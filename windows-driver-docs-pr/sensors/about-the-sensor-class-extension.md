---
title: About the Sensor Class Extension
description: About the Sensor Class Extension
ms.date: 07/20/2018
ms.localizationpriority: medium
---

# About the Sensor Class Extension


To make it easier to write a device driver that exposes a sensor to Windows (and to the sensor and location platform in particular), Windows includes a sensor driver class extension, [ISensorClassExtension](/windows-hardware/drivers/ddi/sensorsclassextension/nn-sensorsclassextension-isensorclassextension) interface. A required component for sensor device drivers, this COM object provides a simple set of interfaces that enable programmers to implement a sensor driver without writing lots of boilerplate code. Additionally, this class extension provides the following benefits:

-   Helps to ensure that user privacy is well protected because the class extension enforces appropriate access control restrictions for sensors that handle personal information.

-   Provides a standard way to retrieve data from the driver and to raise event notifications through the API layers.

 

