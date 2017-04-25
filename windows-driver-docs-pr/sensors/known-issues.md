---
title: Known issues
author: windows-driver-content
description: This topic identifies known issues in the tool outupt.
ms.assetid: 77714A7F-3C7B-43B3-A540-00E0B0E04DE4
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Known issues


This topic identifies known issues in the tool outupt.

## <a href="" id="sensor-property-device-id"></a>SENSOR\_PROPERTY\_DEVICE\_ID


The **SENSOR\_PROPERTY\_DEVICE\_ID** property, which the tool displays in the property list, corresponds to **SENSOR\_PROPERTY\_DEVICE\_PATH** property which is defined in the header file sensors.h.

## Ambient Light Sensor (ALR) Curve


The tool returns ALR curve values as \[Offset, LUX\] pairs (rather than \[LUX, Offset\] pairs).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors\sensors%5D:%20Known%20issues%20%20RELEASE:%20%281/12/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


