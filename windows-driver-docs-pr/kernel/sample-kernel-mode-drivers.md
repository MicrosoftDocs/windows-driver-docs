---
title: Sample Kernel-Mode Drivers
description: Sample Kernel-Mode Drivers
ms.assetid: 09d08e07-e991-458f-aedf-018a0dd20af5
keywords: ["kernel-mode drivers WDK , samples", "sample drivers WDK kernel-mode"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Sample Kernel-Mode Drivers

The WDK provides various sample kernel-mode drivers. After you have installed the WDK, the src\\general subdirectory contains sample driver code that is applicable to all kernel-mode drivers. The samples are also maintained online. These samples include the following:

[**toaster**](https://github.com/Microsoft/Windows-driver-samples/tree/master/general/toaster/toastpkg)  
Provides sample code for a set of drivers that conform to the [Windows Driver Model](windows-driver-model.md) (WDM). This sample also includes sample installation software.

[KMDF filter driver for a HID device (ioctl sample)](https://github.com/Microsoft/Windows-driver-samples/tree/master/hid/firefly)  
Demonstrates how drivers should support I/O control codes.

[**event**](https://github.com/Microsoft/Windows-driver-samples/tree/master/general/event)  
Demonstrates techniques that kernel-mode drivers can use to notify applications of hardware events, if the application requests notification. One technique uses [event objects](event-objects.md) and the other relies on [queuing](queuing-and-dequeuing-irps.md) the notification request until an event occurs.

[**cancel**](https://github.com/Microsoft/Windows-driver-samples/tree/master/general/cancel)  
Demonstrates the use of [cancel-safe IRP queues](cancel-safe-irp-queues.md).

[**tracedrv**](https://github.com/Microsoft/Windows-driver-samples/tree/master/general/tracing/tracedriver)  
Shows how to use [WPP software tracing](https://msdn.microsoft.com/library/windows/hardware/ff556204).

Other subdirectories of [the \\src directory](https://github.com/Microsoft/Windows-driver-samples) contain sample code for kernel-mode drivers for various types of hardware.

## See also

[Microsoft Windows driver samples](https://github.com/Microsoft/Windows-driver-samples) on GitHub
