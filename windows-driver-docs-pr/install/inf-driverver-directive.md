---
title: INF DriverVer Directive
description: A DriverVer directive specifies version information for drivers installed by this INF.
ms.assetid: b8c17839-a027-4fb6-b017-8e9a3fd0d694
keywords: ["INF DriverVer Directive Device and Driver Installation"]
topic_type:
- apiref
api_name:
- INF DriverVer Directive
api_type:
- NA
---

# INF DriverVer Directive


A **DriverVer** directive specifies version information for drivers installed by this INF.

``` syntax
[Version] |
[DDInstall]
 
DriverVer=mm/dd/yyyy[,w.x.y.z] 
```

## Entries


<a href="" id="mm-dd-yyyy"></a>*mm/dd/yyyy*  
This value specifies the date of the "[driver package](driver-packages.md)", which includes the driver files and the INF. This date must be the most recent date of any file in the driver package.

The date must be specified in month/day/year order. The month and day must contain two digits, and the year must contain four digits. A hyphen (-) can be used as the date field separator instead of the slash (/).

<a href="" id="w-x-y-z"></a>*w.x.y.z*  
This value specifies an optional version number. If a value is specified, *w* is required but *x*, *y*, *z*, and their preceding period characters are optional.

If specified, *w*, *x*, *y*, and *z* must each be an integer that is greater than or equal to zero and less than 65535.

For Windows XP SP1, Windows Server 2003 and later versions of Windows, this value is also *used* by Setup, in combination with the driver rank and date, to select a driver for a device. For more information, see [How Windows Selects Drivers](how-setup-selects-drivers.md).

The following points apply to this value for Windows 2000, and Windows XP:

-   This value is used for display purposes only (for example, in Device Manager) and not used to select a driver for a device.
-   You should consider this value to be required for input drivers (such as mouse or keyboard drivers). If you do not include the version value, input drivers might not update programmatically. Typically, you should specify version information in all [driver packages](driver-packages.md) because the operating system uses version information as a criteria to determine the newest driver.

Remarks
-------

Starting with Windows 2000, INF files must have a **DriverVer** directive in their [**INF Version sections**](inf-version-section.md) to provide version information for the whole INF. Individual [**INF *DDInstall* sections**](inf-ddinstall-section.md) can also contain **DriverVer** directives to provide version information for individual drivers. **DriverVer** directives in the *DDInstall* sections are more specific and take precedence over the global **DriverVer** directive in the **Version** section.

When the operating system searches for drivers, it selects a driver that has a more recent **DriverVer** date over a driver that has an earlier date. If an INF has no **DriverVer** directive or contains an invalid date specification, the operating system applies the default date of 00/00/0000. For Windows 2000 only, unsigned drivers are also assigned a date of 00/00/0000.

Examples
--------

```
[Version]
...
DriverVer=09/28/1999,5.00.2136.1
```

## See also


[***DDInstall***](inf-ddinstall-section.md)

[**Version**](inf-version-section.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20INF%20DriverVer%20Directive%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





