---
title: Sensors ACPI entries
author: windows-driver-content
description: This topic describes the advanced configuration and power management interface (ACPI) entries that are specific to sensors in Windows 10.
ms.assetid: DFDD5603-18F5-4F6C-8D09-D6905587F3CE
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Sensors ACPI entries


This topic describes the advanced configuration and power management interface (ACPI) entries that are specific to sensors in Windows 10 Mobile. These entries are to be added to the ACPI source language (ASL) file.

## ROTM


A rotation matrix (ROTM) is a matrix that is used to describe the relationship between the sensor's X, Y, and Z axes and the X, Y, and Z axes of the mobile device (as defined by an OEM).

Each row represents the transformation applied to the X, Y and Z axis respectively. Each entry is a decimal number between -1 and 1, with each number having a maximum of 3 decimal places.

For example, in the following **Method**, the matrix indicates that the X, Y, and Z axes of the sensor hardware are along the Y, -X, and -Z axes of the mobile device, respectively.

``` syntax
Method(ROTM, 0x0, NotSerialized) {
                Name(RBUF, Package(){
                    "0 1 0",
                    "-1 0 0",
                    "0 0 -1"
                })
                Return (RBUF)
            }
```

## PRIM


The following **Method** marks a sensor as primary.

``` syntax
Method(PRIM, 0x0, NotSerialized) {        
                Name(RBUF, Buffer(){1})       
                    Return (RBUF)             
            }
```

**Note:** If there are multiple sensors of the same kind on the mobile device (for example, multiple accelerometers), then one of them must be marked as primary using the **PRIM** keyword. The primary sensor will be used by the WinRT API when the sensor's GetDefault method is invoked. The primary sensor will also be used by any operating system features that are dependent on that sensor type.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors\sensors%5D:%20Sensors%20ACPI%20entries%20%20RELEASE:%20%281/12/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


