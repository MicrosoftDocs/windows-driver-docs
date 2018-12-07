---
title: Differences in WDM Versions
description: Differences in WDM Versions
ms.assetid: 735b01c4-4eff-4c8e-ab60-3813d1830112
keywords: ["WDM drivers WDK kernel , versions", "versions WDK WDM", "compatibility WDK WDM", "cross-system compatibility WDK WDM", "Plug and Play WDK WDM", "driver support routines WDK WDM", "power management WDK WDM"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Differences in WDM Versions





The simplest way to ensure cross-system compatibility is to write a driver that uses only features that are supported by the lowest-numbered version of WDM. However, this is not always possible. Sometimes, drivers require additional code to take advantage of the features that are available in later versions of WDM, or to compensate for differences between Windows operating systems.

### WDM Differences in Driver Support Routines

The Windows Driver Kit (WDK) reference page for each [driver support routine](https://msdn.microsoft.com/library/windows/hardware/ff544200) indicates if the routine is restricted to specific versions of WDM, or if its behavior is different on different operating system versions. Before using any driver support routine in a cross-system driver, be sure to understand any version-specific restrictions or behaviors.

### WDM Differences in Plug and Play

The following Plug and Play I/O request packet (IRP) is supported only in Windows 2000 and later versions of the NT-based operating system (WDM version 1.10 and later):

[**IRP\_MN\_SURPRISE\_REMOVAL**](https://msdn.microsoft.com/library/windows/hardware/ff551760)

In addition, the following IRPs work differently on Windows 98/Me from how they work on the NT-based operating system:

[**IRP\_MN\_STOP\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551755) and [**IRP\_MN\_REMOVE\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551738)

[**IRP\_MN\_QUERY\_REMOVE\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551705)

### WDM Differences in Power Management

The following power management functions and I/O requests differ in operation between the Windows 98/Me operating system and the NT-based operating system:

[**PoSetPowerState**](https://msdn.microsoft.com/library/windows/hardware/ff559765)

[**PoRequestPowerIrp**](https://msdn.microsoft.com/library/windows/hardware/ff559734)

[**PoRegisterDeviceForIdleDetection**](https://msdn.microsoft.com/library/windows/hardware/ff559721)

[**IRP\_MN\_QUERY\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551699)

[**IRP\_MN\_SET\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551744)

When completing power IRPs, drivers on Windows 98/Me must complete power IRPs at IRQL = PASSIVE\_LEVEL, while drivers on the NT-based operating system can complete such IRPs at IRQL = PASSIVE\_LEVEL or IRQL = DISPATCH\_LEVEL.

The DO\_POWER\_PAGABLE flag in the [**DEVICE\_OBJECT**](https://msdn.microsoft.com/library/windows/hardware/ff543147) structure is used differently on the Windows 98/Me operating system than on the NT-based operating system.

### WDM Differences in Kernel-Mode Driver Operation

Kernel-mode WDM drivers for Windows 98/Me must follow certain guidelines for using floating-point operations, MMX, 3DNOW!, or Intel's SSE extensions. For more information, see [Using Floating Point or MMX in a WDM Driver](using-floating-point-or-mmx-in-a-wdm-driver.md).

Windows 98/Me provides a fixed number of worker threads that might not be adequate for some drivers.

 

 




