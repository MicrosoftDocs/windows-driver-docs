---
title: Getting an Adapter Object
description: Getting an Adapter Object
ms.assetid: 2af4ac28-b3c0-4e46-afb1-9c6897c67f03
keywords: ["adapter objects WDK kernel , getting", "DEVICE_DESCRIPTION", "DMA_OPERATIONS", "DMA transfers WDK kernel , adapter objects"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Getting an Adapter Object





At device start-up, a driver that uses system or bus-master DMA calls [**IoGetDmaAdapter**](https://msdn.microsoft.com/library/windows/hardware/ff549220) to get a pointer to an adapter object and to determine the maximum number of map registers available for each transfer operation. When a driver calls **IoGetDmaAdapter**, the I/O manager, in turn, calls the HAL to get the necessary platform-specific information.

A driver must supply certain information in a system-defined [**DEVICE\_DESCRIPTION**](https://msdn.microsoft.com/library/windows/hardware/ff543107) structure in its call to **IoGetDmaAdapter**. Drivers must use [**RtlZeroMemory**](https://msdn.microsoft.com/library/windows/hardware/ff563610) to initialize the **DEVICE\_DESCRIPTION** structure with zeros before setting values in it.

The required data includes information about the features of the driver's device, such as whether the device is a bus master, if it has scatter/gather capabilities, and how many bytes of data the device can transfer at a time (**MaximumLength**).

The required device description data also includes platform-specific information, such as the platform-specific and system-assigned number of the bus that a driver of a bus-master device controls. A driver can obtain this information by calling [**IoGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff549203).

The **DEVICE\_DESCRIPTION** structure includes some fields that might be irrelevant to some DMA devices or drivers. For example, the **BusNumber** field is not used in WDM drivers. Each driver should supply values for the relevant structure members and should set the values for all other members to zero.

The driver of a subordinate device should not pass **TRUE** in the **ScatterGather** field unless the device is capable of waiting for the system DMA controller to be reprogrammed when a request must be broken up into two or more DMA operations.

**IoGetDmaAdapter** returns both a pointer to an adapter object and a platform-specific or device-specific value indicating how many map registers are available with the adapter object for each DMA transfer operation.

The returned adapter object contains three fields that are accessible to drivers:

-   Version number (**Version**)

-   Size (**Size**)

-   Pointer to a [**DMA\_OPERATIONS**](https://msdn.microsoft.com/library/windows/hardware/ff544071) structure (**DmaOperations**)

The **DMA\_OPERATIONS** structure comprises a table of pointers to functions the driver must use to perform DMA operations on its device. The functions are accessible only through the pointers in this data structure; a driver cannot call them directly by name. (Note that these routines replace **Hal*Xxx*** routines supported in previous versions of Windows NT. To ensure compatibility for legacy drivers, the Wdm.h and Ntddk.h header files supply macros with the obsolete names, but new drivers should always call the functions through the data structure.)

The number of map registers can vary from device to device and from platform to platform. Generally, the HAL assigns a number of map registers according to the following criteria:

-   If possible, the HAL returns a value that is one more than the number of map registers needed to transfer **MaximumLength** bytes, as specified in the driver's call to **IoGetDmaAdapter**.

-   Otherwise, the HAL returns a lesser value that is as large as possible for the particular platform.

In other words, the HAL usually gives each driver enough map registers to maximize DMA throughput for its device, but the HAL can return a lesser value on some Windows platforms. There is no guarantee that a driver will get the number of map registers it requests, so drivers should always check the returned value.

Any DMA device driver must provide storage for the adapter object pointer and *NumberOfMapRegisters* value returned by **IoGetDmaAdapter**. This pointer is a required parameter to the system-supplied support routines used for DMA. Because many of these support routines must be called at IRQL = DISPATCH\_LEVEL, the driver-allocated storage must be resident. Most DMA drivers provide the necessary storage in a [device extension](device-extensions.md). However, the storage can be in a controller extension if the driver also uses a [controller object](using-controller-objects.md) or in nonpaged pool that is allocated by the driver. See [Allocating System-Space Memory](allocating-system-space-memory.md) and [Managing Hardware Priorities](managing-hardware-priorities.md) for more information.

When the driver has completed all DMA operations, it calls [**PutDmaAdapter**](https://msdn.microsoft.com/library/windows/hardware/ff559965) to free the adapter object.

The following sections ([Using System DMA](using-system-dma.md) and [Using Bus-Master DMA](using-bus-master-dma.md)) describe how monolithic drivers of DMA devices use support routines to satisfy transfer requests. These sections assume that the driver has the following:

-   A standard [*StartIo*](https://msdn.microsoft.com/library/windows/hardware/ff563858) routine, rather than setting up and managing an internal queue of IRPs

-   An internal routine to split transfer requests for which an insufficient number of map registers is available

-   No device-specific DMA constraints

In other words, these sections describe the simplest possible technique for drivers' DMA operations, but individual drivers do not necessarily use exactly the same techniques. For any driver of a DMA device, which driver routines should split up large DMA transfer requests depends on the driver model (class/port or monolithic), on the device's features, and on any device-specific DMA constraints that driver must handle.

 

 




