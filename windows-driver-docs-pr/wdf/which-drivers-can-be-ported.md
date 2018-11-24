---
title: Which Drivers Can Be Ported and Where
description: This topic describes which WDM drivers can be ported to Windows Driver Frameworks (WDF), and how to decide whether to port to Kernel-Mode Driver Framework (KMDF) or User-Mode Driver Framework (UMDF).
ms.assetid: 53E34B9C-8C0A-4F15-951B-7AB133DE0C5A
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Which Drivers Can Be Ported and Where


This topic describes which WDM drivers can be ported to Windows Driver Frameworks (WDF), and how to decide whether to port to Kernel-Mode Driver Framework (KMDF) or User-Mode Driver Framework (UMDF).

## Which WDM drivers can I port to WDF?


Whether a particular driver can be ported to WDF depends on the following criteria:

-   The operating system versions on which the driver runs
-   The type of device that the driver supports
-   The driver model that the driver uses

In general, you can use KMDF or UMDF to write drivers that conform to WDM, supply entry points for the major I/O dispatch routines, and handle IRPs.

For some device types, system-supplied device class and port drivers provide driver dispatch functions and call a vendor-supplied miniport driver to handle specific I/O details. These miniport drivers are essentially callback libraries and are not supported by WDF. In addition, WDF does not support device types that use Windows Image Acquisition (WIA).

You can use KMDF to create drivers that run on Windows 2000 and later. You can use UMDF version 1 to write drivers that run on Windows XP and later, and UMDF version 2 to target Windows 8.1 and later.

For information about device and driver types that UMDF and KMDF support, see [Choosing a Driver Model](https://msdn.microsoft.com/library/windows/hardware/ff554652).

## Which framework should I port my WDM driver to, KMDF or UMDF 2?


1.  Review the list of KMDF-only functionality in [Comparing UMDF 2.0 Functionality to KMDF](comparing-umdf-2-0-functionality-to-kmdf.md). If your driver does not require any of these features, and you are targeting Windows 8.1 or later, open a new UMDF 2 driver template in Visual Studio.

    If you realize later that you need a KMDF-only feature, it's straightforward to convert your UMDF 2 driver to KMDF, as described in [How to convert a KMDF driver to a UMDF 2.0 driver (and vice-versa)](how-to-generate-a-umdf-driver-from-a-kmdf-driver.md).

2.  You can also write a *mode-agnostic* driver, meaning one that can be compiled using either KMDF or UMDF. To write a mode-agnostic driver, start with a UMDF 2 template. Use the DDI versioning info listed in [Summary of WDF Callbacks and Methods](https://msdn.microsoft.com/library/windows/hardware/dn265591) to ensure that you only call methods that are available in both KMDF and UMDF 2. Conditionally tag any header references with the preprocessor macros described in [How to convert a KMDF driver to a UMDF 2.0 driver (and vice-versa)](how-to-generate-a-umdf-driver-from-a-kmdf-driver.md). To switch your driver, you would create an empty driver project using a Visual Studio template for the target framework, and copy your source code over.

## Related topics


[Getting Started with UMDF](https://msdn.microsoft.com/library/windows/hardware/dn384105)

[KMDF Version History](kmdf-version-history.md)

[UMDF Version History](umdf-version-history.md)

[User-Mode Driver Framework Frequently Asked Questions](user-mode-driver-framework-frequently-asked-questions.md)

 

 






