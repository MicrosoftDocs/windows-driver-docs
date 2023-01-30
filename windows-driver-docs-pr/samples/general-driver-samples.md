---
title: General driver samples
description: The samples in this directory provide a starting point for writing a custom driver for your device.
ms.date: 12/03/2019
---

# General driver samples

The samples in this directory provide a starting point for writing a custom driver for your device.

| Sample | Description |
| --- | --- |
| [Cancel Safe IRP Queue](/samples/microsoft/windows-driver-samples/cancel-safe-irp-queue-sample) | Demonstrates the use of the cancel-safe queue routines IoCsqInitialize, IoCsqInsertIrp, IoCsqRemoveIrp, IoCsqRemoveNextIrp. By using these routines, driver developers do not have to worry about IRP cancellation race conditions. |
| [KMDF Echo](/samples/microsoft/windows-driver-samples/kmdf-echo-sample) | Demonstrates how to use a sequential queue to serialize read and write requests presented to the driver. |
| [UMDF1 Echo](../wdf/user-mode-driver-framework-design-guide.md) | Demonstrates how to use UMDF 1 to write a driver and to employ best practices. |
| [UMDF2 Echo](/samples/microsoft/windows-driver-samples/echo-sample-umdf-version-2) | Demonstrates how to use UMDF 2 to write a driver and to employ best practices. |
| [UMDF SocketEcho Sample (UMDF Version 1)](../wdf/user-mode-driver-framework-design-guide.md) | Demonstrates how to use the UMDF to write a driver and demonstrates best practices. |
| [Hardware Event](/samples/microsoft/windows-driver-samples/hardware-event-sample)| Demonstrates two different ways a kernel-mode driver can notify an application about a hardware event. One way uses an event-based method, and the other uses an IRP-based method. The sample driver uses a timer DPC to simulate hardware events. |
| [File History](/samples/microsoft/windows-driver-samples/file-history-sample)| A console application that starts the file history service, if it is stopped, and schedules regular backups. |
| [Non-PnP Driver Sample](/samples/microsoft/windows-driver-samples/non-pnp-driver-sample)| Demonstrates how to write a non-PnP driver using the Kernel Mode Driver Framework. |
| [IOCTL](/samples/microsoft/windows-driver-samples/ioctl)| Demonstrates the usage of four different types of IOCTLs (METHOD\_IN\_DIRECT, METHOD\_OUT\_DIRECT, METHOD\_NEITHER, and METHOD\_BUFFERED). |
| [ObCallback](/samples/microsoft/windows-driver-samples/obcallback-callback-registration-driver) | Demonstrates the use of registered callbacks for process protection. The driver registers control callbacks which are called at process creation. |
| [PCIDRV](/samples/microsoft/windows-driver-samples/pcidrv---wdf-driver-for-pci-device) | This sample demonstrates how to write a KMDF driver for a PCI device. The sample works with the Intel 82557/82558 based PCI Ethernet Adapter (10/100) and Intel compatibles. |
| [Kernel Counter](/samples/microsoft/windows-driver-samples/kernel-counter-sample-kcs) | Demonstrates the use of the kernel-mode performance library. The driver does not control any hardware, it simply provides counters. The code contains comments to explain what each function does. |
| [PLX9x5x PCI Driver](/samples/microsoft/windows-driver-samples/plx9x5x-pci-driver) | Demonstrates how to write driver for a generic PCI device using Windows Driver Frameworks (WDF). The target hardware for this driver is PLX9656/9653RDK-LITE board. |
| [RegFltr](/samples/microsoft/windows-driver-samples/regfltr-sample-driver) | Shows how to write a registry filter driver. |
| [Simple Media Source](/samples/microsoft/windows-driver-samples/simplemediasource-sample) | Demonstrates how to write a custom media source and driver package. |
| [System DMA](/samples/microsoft/windows-driver-samples/system-dma) | Demonstrates the usage of V3 System DMA. It shows how a driver could use a system DMA controller supported by Windows to write data to a hardware location using DMA. |
| [Toaster Sample Driver](/samples/microsoft/windows-driver-samples/toaster-sample-driver) | An iterative series of samples that demonstrate fundamental aspects of Windows driver development for both Kernel-Mode Driver Framework (KMDF) and User-Mode Driver Framework (UMDF) version 1. |
| [Toaster Package Sample](/samples/microsoft/windows-driver-samples/toaster-package-sample-driver) | Simulates hardware-first and software-first installation of the toaster sample driver. |
| [Toaster Sample (UMDF Version 2)](/samples/microsoft/windows-driver-samples/toaster-sample-umdf-version-2) | An iterative series of samples that demonstrate fundamental aspects of Windows driver development using User-Mode Driver Framework (UMDF) version 2. |
| [EventDrv](/samples/microsoft/windows-driver-samples/eventdrv) | A kernel-mode trace provider and driver. The driver does not control any hardware; it simply generates trace events. It is designed to demonstrate the use of the Event Tracing for Windows (ETW) API in a driver. |
| [System Trace Control](/samples/microsoft/windows-driver-samples/systemtraceprovider) | Demonstrates how to use event tracing control APIs to collect events from the system trace provider. |
| [Tracedrv](/samples/microsoft/windows-driver-samples/tracedrv) | A sample driver instrumented for software tracing.|
| [UMDF Driver Skeleton](../wdf/user-mode-driver-framework-design-guide.md) | Demonstrates how to use the User-Mode Driver Framework to write a minimal driver and shows best practices. |
| [Driver package installation toolkit for universal drivers](/samples/microsoft/windows-driver-samples/driver-package-installation-toolkit-for-universal-drivers) | Illustrates DCHU principles of universal driver design. |
| [WinHEC 2017 Lab](/samples/microsoft/windows-driver-samples/winhec-2017-lab) | Toaster samples from the WinHEC 2017 Lab: Toaster Driver, PlugInToaster, and Toaster Support App. |
