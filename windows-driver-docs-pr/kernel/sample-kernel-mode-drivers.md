---
title: Sample Kernel-Mode Drivers
description: Sample Kernel-Mode Drivers
keywords: ["kernel-mode drivers WDK , samples", "sample drivers WDK kernel-mode"]
ms.date: 06/16/2017
---

# Sample Kernel-Mode Drivers

The WDK provides various sample kernel-mode drivers. After you have installed the WDK, the `src\general` subdirectory contains sample driver code that is applicable to all kernel-mode drivers. The samples are also maintained online. These samples include the following:

[**DCHU**](https://github.com/Microsoft/Windows-driver-samples/tree/main/general/DCHU)

Applies the DCH [design principles](../develop/getting-started-with-windows-drivers.md) (Declarative, Componentized, and Hardware Support Apps [HSA]).  You can use it as a model for your own Windows Driver package.

[**PLX9x5x**](https://github.com/Microsoft/Windows-driver-samples/tree/main/general/PLX9x5x)

This sample demonstrates how to write driver for a generic PCI device using Windows Driver Framework.

[**SimpleMediaSource**](https://github.com/Microsoft/Windows-driver-samples/tree/main/general/SimpleMediaSource)

This sample demonstrates how to create a custom media source and driver package that can be installed as a Camera and produce frames.

[**SystemDma/wdm**](https://github.com/Microsoft/Windows-driver-samples/tree/main/general/SystemDma/wdm)

This sample demonstrates the usage of V3 System DMA. It shows how a driver could use a system DMA controller supported by Windows to write data to a hardware location using DMA.

[**WinHEC 2017 Lab**](https://github.com/Microsoft/Windows-driver-samples/tree/main/general/WinHEC%202017%20Lab)

[**WinHEC 2017/Optimizing Windows Performance**](https://github.com/Microsoft/Windows-driver-samples/tree/main/general/WinHEC%202017/Optimizing%20Windows%20Performance)

[**cancel**](https://github.com/Microsoft/Windows-driver-samples/tree/main/general/cancel)  

Demonstrates the use of [cancel-safe IRP queues](cancel-safe-irp-queues.md).

[**echo**](https://github.com/Microsoft/Windows-driver-samples/tree/main/general/echo)

[**event**](https://github.com/Microsoft/Windows-driver-samples/tree/main/general/event)  

Demonstrates techniques that kernel-mode drivers can use to notify applications of hardware events, if the application requests notification. One technique uses [event objects](event-objects.md) and the other relies on [queuing](queuing-and-dequeuing-irps.md) the notification request until an event occurs.

[**filehistory**](https://github.com/Microsoft/Windows-driver-samples/tree/main/general/filehistory)

The FileHistory sample is a console application that starts the file history service, if it is stopped, and schedules regular backups. The application requires, as a command-line parameter, the path name of a storage device to use as the default backup target.

[**IOCTL sample**](https://github.com/Microsoft/Windows-driver-samples/tree/main/general/ioctl)

Demonstrates how drivers should support I/O control codes.

[**obcallback**](https://github.com/Microsoft/Windows-driver-samples/tree/main/general/obcallback)

The ObCallback sample driver demonstrates the use of registered callbacks for process protection. The driver registers control callbacks which are called at process creation.

[**pcidrv**](https://github.com/Microsoft/Windows-driver-samples/tree/main/general/pcidrv)

This sample demonstrates how to write a KMDF driver for a PCI device. The sample works with the Intel 82557/82558 based PCI Ethernet Adapter (10/100) and Intel compatibles.

[**perfcounters/kcs**](https://github.com/Microsoft/Windows-driver-samples/tree/main/general/perfcounters/kcs)

The Kcs sample driver demonstrates the use of the kernel-mode performance library.

[**registry/regfltr**](https://github.com/Microsoft/Windows-driver-samples/tree/main/general/registry/regfltr)

The RegFltr sample shows how to write a registry filter driver.

[**toaster**](https://github.com/Microsoft/Windows-driver-samples/tree/main/general/toaster)  

Provides sample code for a set of drivers that conform to the [Windows Driver Model](introduction-to-wdm.md) (WDM). This sample also includes sample installation software.

[**tracedrv**](https://github.com/Microsoft/Windows-driver-samples/tree/main/general/tracing/tracedriver)  

Shows how to use [WPP software tracing](../devtest/wpp-software-tracing.md).

[**UMDF Driver Skeleton Sample**](https://github.com/Microsoft/Windows-driver-samples/tree/main/general/umdfSkeleton)

This sample demonstrates how to use version 1 of the User-Mode Driver Framework to write a minimal driver.

[**Firefly KMDF filter driver for a HID device**](https://github.com/Microsoft/Windows-driver-samples/tree/main/hid/firefly)
Along with illustrating how to write a filter driver, this sample shows how to use remote I/O target interfaces to open a HID collection in kernel-mode and send IOCTL requests to set and get feature reports, as well as how an application can use WMI interfaces to send commands to a filter driver.

Other subdirectories of the `\src` directory contain sample code for kernel-mode drivers for various types of hardware.

## See also

[Microsoft Windows driver samples](https://github.com/Microsoft/Windows-driver-samples) on GitHub
