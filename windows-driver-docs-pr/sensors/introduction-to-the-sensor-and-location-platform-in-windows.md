---
title: Introduction to the Sensor and Location Platform in Windows
description: Introduction to the Sensor and Location Platform in Windows
ms.assetid: 62e945e5-78a1-4eb6-ad59-b30cf5e3d5ad
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Introduction to the Sensor and Location Platform in Windows


The Windows operating system provides native support for sensor devices. This support includes location sensors such as GPS devices. As part of this support, the platform provides a standard way for device manufacturers to expose sensor devices to software developers and consumers. At the same time, the platform gives developers a standardized API and device driver interface (DDI) to work with sensors and sensor data. This section summarizes the Windows sensor and location platform, discusses the various parts of the platform, and describes how the pieces work together to provide a comprehensive system for working with sensors.

### Sensor Device Overview

Sensors come in many configurations and, from a certain perspective, almost anything that provides data about physical phenomena can be called a sensor. Although we typically think of sensors as hardware devices, logical sensors can also provide information through emulation of sensor functionality in software or firmware. Also, a single hardware device can contain multiple sensors.

The sensor and location platform organizes sensors into **categories**, which represent broad classes of sensor devices, and **types**, which represent specific kinds of sensors. For example, a sensor in a video game controller that detects the position and movement of a player's hand (perhaps for a video bowling game) would be categorized as an Orientation sensor, but its type would be 3-D Accelerometer. In code, Windows represents categories and types by using globally unique identifiers (GUIDs), many of which are predefined. Device manufacturers can create new categories and types by defining and publishing new GUIDs, when it is required.

Location devices comprise one especially interesting category. By now, most people are familiar with global positioning systems (GPS). In Windows, a GPS is a kind of sensor that is part of the Location category. The Location category could include other sensor types. Some of these sensor types are software based, such as an IP resolver that provides location information based on an Internet address, a cellular phone tower triangulator that determines location based on nearby towers, or a sensor that determines location from the presence of Wi-Fi networks.

### About the Platform

The Windows sensor and location platform consists of the following developer and user components:

-   The DDI. Windows provides a standard way for sensor devices to connect to the computer and to provide data to other subsystems.

-   The Windows Sensor API provides a set of methods, properties, and events to work with connected sensors and sensor data.

-   The Windows Location API, which is built on the Windows Sensor API, provides a set of programming objects. These objects include scripting objects, for working with location information.

-   The Control Panel gives computer users control over location settings.

The following sections describe each of these components.

### Device Driver Interface

Sensor manufacturers can create device drivers to connect sensors with Windows. Sensor device drivers are implemented by using the Windows Portable Devices (WPD) driver model, which is based on the Windows User Mode Driver Framework (UMDF).Many device drivers have been written by using these frameworks. Because these technologies are established, experienced device driver programmers will find writing a sensor driver to be a familiar task. The sensor DDI uses specific UMDF and WPD data types and interfaces, and also defines sensor-specific WPD commands and parameters, where it is required.

To help make it easier to write a device driver that exposes a sensor to Windows (and to the sensor and location platform in particular), the operating system includes a driver class extension. A required component for sensor device drivers, this COM object provides a simple set of interfaces that enable programmers to implement a sensor driver without writing lots of boilerplate code. The class extension can also reduce, or even eliminate, the need to manage WPD calls. This documentation contains detailed information about the sensor DDI and class extension object.

### Sensor API

The Windows Sensor API enables C++ developers to create sensor-based programs by using a set of COM interfaces. The API defines interfaces to perform common sensor programming tasks that include managing sensors by category, type, or ID, managing sensor events, working with individual sensors and sensor collections, and working with sensor data. The Windows SDK includes header files, documentation, samples, and tools to help guide software developers on how to use sensors in Windows programs.

### Location API

Built on the sensor platform, the Location API provides an easy way to retrieve data about geographic location while protecting user privacy. The Location API provides its functionality through a set of COM interfaces that represent objects. These objects can be used by programmers who understand how to use COM through the C++ programming language, or in scripting languages, such as JScript. Scripting support gives easy access to location data for projects that run in the Local Computer zone, such as gadgets. The Windows SDK includes header files, documentation (including scripting reference documentation), samples, and tools to help guide Web and software developers on how to use location information in their programs.

### User Control Panel

Windows includes a control panel that allows computer users to enable or disable location settings. Because thesesettings can expose sensitive data, this user interface gives users control over whether programs have access to their location.

 

 




