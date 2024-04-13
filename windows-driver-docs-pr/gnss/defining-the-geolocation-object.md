---
title: Defining the Geolocation Sensor as an Object
description: The sensors geolocation driver sample treats its simulated geolocation-sensor as an object.
ms.date: 03/21/2023
---

# Defining the geolocation sensor as an object

> [!IMPORTANT]
> This documentation and the geolocation driver sample for Windows 8.1 has been deprecated.

The sensors geolocation driver sample treats its simulated geolocation-sensor as an object. This object is declared in the header file named geolocation.h. For a description of the header file and the other driver sample files refer to [The sample driver file list](the-sample-driver-file-list.md) section.

The header file contains a data structure that defines the properties supported by the pseudo sensor. In addition, the header file contains the definitions of the methods that do the following:

- [Initialize the geolocation object](initializing-the-geolocation-object.md)

- Set or retrieve the geolocation properties

The definitions of the corresponding methods are found in a source file named: geolocation.cpp.

To extend this sample to support hardware, create similar header and source files that declare and define the corresponding objects for your device. For more information about extending this sample, see [Adding support for actual hardware](adding-support-for-actual-hardware.md).

## Related topics

[Adding support for actual hardware](adding-support-for-actual-hardware.md)  

[Initialize the geolocation object](initializing-the-geolocation-object.md)  

[The sample driver file list](the-sample-driver-file-list.md)  
