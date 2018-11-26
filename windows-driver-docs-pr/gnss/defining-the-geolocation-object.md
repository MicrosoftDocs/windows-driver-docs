---
title: Defining the geolocation sensor as an object
description: The sensors geolocation driver sample treats its simulated geolocation-sensor as an object.
ms.assetid: CDAA93A1-9B20-4602-9A8A-A2C7CF52B576
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Defining the geolocation sensor as an object

> [!IMPORTANT] 
> This documentation and the geolocation driver sample for Windows 8.1 has been deprecated.

The sensors geolocation driver sample treats its simulated geolocation-sensor as an object. This object is declared in the header file named geolocation.h. (For a description of the header file and the other driver sample files refer to [The sample driver file list](the-sample-driver-file-list.md) section.)

The header file contains a data structure that defines the properties supported by the pseudo sensor. In addition, the header file contains the definitions of the methods that do the following:

-   [Initialize the geolocation object](initializing-the-geolocation-object.md)
-   Set or retrieve the geolocation properties

The definitions of the corresponding methods are found in a source file named: geolocation.cpp.

To extend this sample to support hardware, create similar header and source files that declare and define the corresponding objects for your device. For more information about extending this sample, see [Adding support for actual hardware](adding-support-for-actual-hardware.md).

## Related topics
[Adding support for actual hardware](adding-support-for-actual-hardware.md)  
[Initialize the geolocation object](initializing-the-geolocation-object.md)  
[The sample driver file list](the-sample-driver-file-list.md)  



