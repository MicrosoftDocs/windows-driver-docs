---
title: Updating Your Package-Aware Driver's INF
description: Updating Your Package-Aware Driver's INF
ms.date: 01/31/2023
---

# Updating Your Package-Aware Driver's INF

[!include[Print Support Apps](../includes/print-support-apps.md)]

After you bundle the core driver with your package-aware driver, the next step is to update your package-aware driver's INF file.

The INF file for your package-aware driver needs to reference the updated core driver package. To do this, identify the core driver package with a core model GUID, as discussed in [Writing Core Drivers](writing-core-drivers.md). In addition to identifying the core driver package, you will need to make the following two changes to the INF file.

First, specify the minimum acceptable version of the core driver so that only the updated version will be used. Specifying a minimum version eliminates the possibility of your package-aware driver being installed with an older, incompatible version of the core driver package. To specify the minimum version, use the INF InboxVersionRequired directive, as shown in the following example:

```inf
[PrinterPackageInstallation.x86]
PackageAware=TRUE
CoreDriverDependencies={D20EA372-DD35-4950-9ED8-A6335AFE79F0}
InboxVersionRequired=<version of the updated core driver>
```

In the preceding example, replace the text in italics with the appropriate driver version information.

Second, use the [**INF CopyINF directive**](../install/inf-copyinf-directive.md) to copy the updated core driver package to the driver store. This directive was updated in Windows Vista to support copying to the driver store.

After completing these steps, the driver should be ready to test. During PnP installation, the installer will discover the new package-aware driver and read the associated INF file. The CopyINF directive will force the updated core driver package to be loaded into the driver store, and the rest of the package-aware driver installation will proceed.
