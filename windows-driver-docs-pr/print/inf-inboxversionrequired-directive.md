---
title: INF InboxVersionRequired Directive
author: windows-driver-content
description: INF InboxVersionRequired Directive
ms.assetid: 75a07ca7-d279-4815-b644-10b58753f885
---

# INF InboxVersionRequired Directive


For package-aware drivers, you can use the **InboxVersionRequired** INF directive to specify a minimum acceptable version for all core drivers that the INF references. You can use the **UseDriverVer** keyword to specify the minimum version. This minimum version applies to all referenced core drivers in the INF.

The following example package-aware-driver section shows how you insert the **InboxVersionRequired** INF directive:

```
[PrinterPackageInstallation.amd64]
PackageAware=TRUE
CoreDriverDependencies={D20EA372-DD35-4950-9ED8-A6335AFE79F0},{D20EA372-DD35-4950-9ED8-A6335AFE79F3}
InboxVersionRequired=UseDriverVer
```

If the **UseDriverVer** keyword is used as the value for **InboxVersionRequired**, **UseDriverVer** informs the class installer to use the **DriverVer** directive version string from the INF that is being parsed as the minimum acceptable version of any core drivers. You must be careful when you service drivers that use the **UseDriverVer** keyword. All core drivers that are referenced by an INF must be the same or higher version for installation to be successful.

You can also specify specific version strings as the value for **InboxVersionRequired**. These version strings follow the same formatting as the **DriverVer** string that is specified in the [**INF Version Section**](https://msdn.microsoft.com/library/windows/hardware/ff547502). For more information about the **DriverVer** string format, see [**INF DriverVer Directive**](https://msdn.microsoft.com/library/windows/hardware/ff547394).

The following example shows how you set **InboxVersionRequired** to a specific version string:

```
InboxVersionRequired=09/28/1999,5.00.2136.1
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20INF%20InboxVersionRequired%20Directive%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


