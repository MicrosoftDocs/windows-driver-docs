---
title: Updating Your Package-Aware Driver's INF
author: windows-driver-content
description: Updating Your Package-Aware Driver's INF
ms.assetid: d0bf489d-d084-40df-b5aa-69cdf679993f
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Updating Your Package-Aware Driver's INF


After you bundle the core driver with your package-aware driver, the next step is to update your package-aware driver's INF file.

The INF file for your package-aware driver needs to reference the updated core driver package. To do this, identify the core driver package with a core model GUID, as discussed in [Writing Core Drivers](writing-core-drivers.md). In addition to identifying the core driver package, you will need to make the following two changes to the INF file.

First, specify the minimum acceptable version of the core driver so that only the updated version will be used. Specifying a minimum version eliminates the possibility of your package-aware driver being installed with an older, incompatible version of the core driver package. To specify the minimum version, use the INF InboxVersionRequired directive, as shown in the following example:

```
[PrinterPackageInstallation.x86]
PackageAware=TRUE
CoreDriverDependencies={D20EA372-DD35-4950-9ED8-A6335AFE79F0}
InboxVersionRequired=<version of the updated core driver>
```

In the preceding example, replace the text in italics with the appropriate driver version information.

Second, use the [**INF CopyINF directive**](https://msdn.microsoft.com/library/windows/hardware/ff547317) to copy the updated core driver package to the driver store. This directive was updated in Windows Vista to support copying to the driver store.

After completing these steps, the driver should be ready to test. During PnP installation, the installer will discover the new package-aware driver and read the associated INF file. The CopyINF directive will force the updated core driver package to be loaded into the driver store, and the rest of the package-aware driver installation will proceed.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Updating%20Your%20Package-Aware%20Driver's%20INF%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


