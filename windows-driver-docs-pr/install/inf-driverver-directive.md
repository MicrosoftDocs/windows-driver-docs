---
title: INF DriverVer Directive
description: A DriverVer directive specifies version information for drivers installed by this INF.
keywords:
- INF DriverVer Directive Device and Driver Installation
topic_type:
- apiref
ms.topic: reference
api_name:
- INF DriverVer Directive
api_type:
- NA
ms.date: 03/23/2023
---

# INF DriverVer directive

A **DriverVer** directive specifies date and version information for drivers installed by this INF.

```inf
[Version] |
[DDInstall]
 
DriverVer=mm/dd/yyyy,w.x.y.z 
```

## Entries

*mm/dd/yyyy*  
This value specifies the date of the [driver package](driver-packages.md), which includes the driver files and the INF. This date must be the most recent date of any file in the driver package.

The date must be specified in month/day/year order. The month and day must contain two digits, and the year must contain four digits. A hyphen (-) can be used as the date field separator instead of the slash (/).

*w.x.y.z*  
This value specifies a version number.

Each of *w*, *x*, *y*, and *z* must be an integer that is greater than or equal to zero and less than 65535.

For Windows XP SP1, Windows Server 2003 and later versions of Windows, this value is also used by Setup, in combination with the driver rank and date, to select a driver for a device. For more information, see [How Windows Selects Drivers](./how-windows-selects-a-driver-for-a-device.md).

The following point applies to this value for Windows 2000, and Windows XP:

- You should consider this value to be required for input drivers (such as mouse or keyboard drivers). If you do not include the version value, input drivers might not update programmatically. Typically, you should specify version information in all [driver packages](driver-packages.md) because the operating system uses version information as a criteria to determine the newest driver.

> [!CAUTION]
> A *w.x.y.z* value of 0.0.0.0 is not valid.
>
> Whenever anything in the driver package is changed, including changes to binary files and not just changes in the INF, it is recommended that both the date and the version number is updated. See [Best practices for naming and versioning your INF file](./general-guidelines-for-inf-files.md#best-practices-for-naming-and-versioning-your-inf-file) for more information.

## Remarks

Starting with Windows 2000, INF files must have a **DriverVer** directive in their [**INF Version sections**](inf-version-section.md) to provide version information for the whole INF. Individual [**INF *DDInstall* sections**](inf-ddinstall-section.md) can also contain **DriverVer** directives to provide version information for individual drivers. **DriverVer** directives in the *DDInstall* sections are more specific and take precedence over the global **DriverVer** directive in the **Version** section.

When the operating system searches for drivers, it selects a driver that has a more recent **DriverVer** date over a driver that has an earlier date. If an INF has no **DriverVer** directive or contains an invalid date specification, the operating system applies the default date of 00/00/0000. For Windows 2000 only, unsigned drivers are also assigned a date of 00/00/0000.

## Examples

```inf
[Version]
...
DriverVer=09/28/1999,5.00.2136.1
```

## See also

[***DDInstall***](inf-ddinstall-section.md)

[**Version**](inf-version-section.md)
