---
title: Sensors ACPI entries
description: This topic describes the advanced configuration and power management interface (ACPI) entries that are specific to sensors in Windows 10.
ms.assetid: DFDD5603-18F5-4F6C-8D09-D6905587F3CE
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Sensors ACPI entries


This topic describes the advanced configuration and power management interface (ACPI) entries that are specific to sensors in Windows 10 Mobile. These entries are to be added to the ACPI source language (ASL) file.

## ROTM


A rotation matrix (ROTM) is a matrix that is used to describe the relationship between the sensor's X, Y, and Z axes and the X, Y, and Z axes of the mobile device (as defined by an OEM).

Each row represents the transformation applied to the X, Y and Z axis respectively. Each entry is a decimal number between -1 and 1, with each number having a maximum of 3 decimal places.

For example, in the following **Method**, the matrix indicates that the X, Y, and Z axes of the sensor hardware are along the Y, -X, and -Z axes of the mobile device, respectively.

```cpp
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

```cpp
Method(PRIM, 0x0, NotSerialized) {
                Name(RBUF, Buffer(){1})
                    Return (RBUF)
            }
```

>[!NOTE]
> If there are multiple sensors of the same kind on the mobile device (for example, multiple accelerometers), then one of them must be marked as primary using the **PRIM** keyword. The primary sensor will be used by the WinRT API when the sensor's GetDefault method is invoked. The primary sensor will also be used by any operating system features that are dependent on that sensor type.








