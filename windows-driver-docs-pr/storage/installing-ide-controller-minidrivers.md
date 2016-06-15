---
title: Installing IDE Controller Minidrivers
author: windows-driver-content
description: Installing IDE Controller Minidrivers
ms.assetid: c1b41f89-150d-47e9-9bed-04f5796f69bd
keywords: ["IDE controller minidrivers WDK storage , installing", "storage IDE controller minidrivers WDK , installing"]
---

# Installing IDE Controller Minidrivers


## <span id="ddk_installing_ide_controller_minidrivers_kg"></span><span id="DDK_INSTALLING_IDE_CONTROLLER_MINIDRIVERS_KG"></span>


This section provides installation information that is specific to IDE controller drivers and controller minidrivers in Microsoft Windows 2000 and later operating systems.

Vendors supplying their own controller minidriver should make that driver a member of the Hard Disk Controllers (HDC) setup class in the [**INF Version Section**](https://msdn.microsoft.com/library/windows/hardware/ff547502) of the driver's INF file. For example:

```
[version]
Signature="$WINDOWS NT$"
Class=hdc
ClassGuid={4D36E96A-E325-11CE-BFC1-08002BE10318}
```

There are no other special requirements associated with installing IDE controller minidrivers.

For more installation information, including a list of controller hardware supported in Windows 2000 and later operating systems, see the system-supplied INF file for hard disk controllers, *mshdc.inf*.

For general information about device installation in Windows 2000 and later operating systems, see [Requirements for Vendor-Supplied IDE Controller Minidrivers](requirements-for-vendor-supplied-ide-controller-minidrivers.md) and [Device Installation Overview](https://msdn.microsoft.com/library/windows/hardware/ff549455).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Installing%20IDE%20Controller%20Minidrivers%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


