---
title: Defining the geolocation sensor as an object
author: windows-driver-content
description: The sensors geolocation driver sample treats its simulated geolocation-sensor as an object.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: CDAA93A1-9B20-4602-9A8A-A2C7CF52B576
---

# Defining the geolocation sensor as an object


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

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors\sensors%5D:%20Defining%20the%20geolocation%20sensor%20as%20an%20object%20%20RELEASE:%20%281/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


