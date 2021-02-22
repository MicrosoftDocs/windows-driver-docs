---
title: Installing IDE Controller Minidrivers
description: Installing IDE Controller Minidrivers
keywords:
- IDE controller minidrivers WDK storage , installing
- storage IDE controller minidrivers WDK , installing
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Installing IDE Controller Minidrivers


## <span id="ddk_installing_ide_controller_minidrivers_kg"></span><span id="DDK_INSTALLING_IDE_CONTROLLER_MINIDRIVERS_KG"></span>


This section provides installation information that is specific to IDE controller drivers and controller minidrivers in Microsoft Windows 2000 and later operating systems.

Vendors supplying their own controller minidriver should make that driver a member of the Hard Disk Controllers (HDC) setup class in the [**INF Version Section**](../install/inf-version-section.md) of the driver's INF file. For example:

```cpp
[version]
Signature="$WINDOWS NT$"
Class=hdc
ClassGuid={4D36E96A-E325-11CE-BFC1-08002BE10318}
```

There are no other special requirements associated with installing IDE controller minidrivers.

For more installation information, including a list of controller hardware supported in Windows 2000 and later operating systems, see the system-supplied INF file for hard disk controllers, *mshdc.inf*.

For general information about device installation in Windows 2000 and later operating systems, see [Requirements for Vendor-Supplied IDE Controller Minidrivers](requirements-for-vendor-supplied-ide-controller-minidrivers.md) and [Device Installation Overview](../install/overview-of-device-and-driver-installation.md).

 

