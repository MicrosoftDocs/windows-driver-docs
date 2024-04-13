---
title: INF InboxVersionRequired Directive
description: INF InboxVersionRequired Directive
ms.date: 01/27/2023
---

# INF InboxVersionRequired Directive

[!include[Print Support Apps](../includes/print-support-apps.md)]

For package-aware drivers, you can use the **InboxVersionRequired** INF directive to specify a minimum acceptable version for all core drivers that the INF references. You can use the **UseDriverVer** keyword to specify the minimum version. This minimum version applies to all referenced core drivers in the INF.

The following example package-aware-driver section shows how you insert the **InboxVersionRequired** INF directive:

```inf
[PrinterPackageInstallation.amd64]
PackageAware=TRUE
CoreDriverDependencies={D20EA372-DD35-4950-9ED8-A6335AFE79F0},{D20EA372-DD35-4950-9ED8-A6335AFE79F3}
InboxVersionRequired=UseDriverVer
```

If the **UseDriverVer** keyword is used as the value for **InboxVersionRequired**, **UseDriverVer** informs the class installer to use the **DriverVer** directive version string from the INF that is being parsed as the minimum acceptable version of any core drivers. You must be careful when you service drivers that use the **UseDriverVer** keyword. All core drivers that are referenced by an INF must be the same or higher version for installation to be successful.

You can also specify specific version strings as the value for **InboxVersionRequired**. These version strings follow the same formatting as the **DriverVer** string that is specified in the [**INF Version Section**](../install/inf-version-section.md). For more information about the **DriverVer** string format, see [**INF DriverVer Directive**](../install/inf-driverver-directive.md).

The following example shows how you set **InboxVersionRequired** to a specific version string:

```inf
InboxVersionRequired=09/28/1999,5.00.2136.1
```
