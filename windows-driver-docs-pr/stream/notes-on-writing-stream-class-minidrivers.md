---
title: Notes on Writing Stream Class Minidrivers
description: Notes on Writing Stream Class Minidrivers
ms.assetid: dc966b47-4ffe-4122-847d-118a465bf5f5
keywords:
- Stream.sys class driver WDK Windows 2000 Kernel , writing
- streaming minidrivers WDK Windows 2000 Kernel , writing
- minidrivers WDK Windows 2000 Kernel Streaming , writing
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Notes on Writing Stream Class Minidrivers





-   Minidrivers must run on both Intel and non-Intel x86 processors, and therefore must be written in C (or other high-level language). Minidrivers should not contain assembly language source code.

-   Some hardware requires firmware to be loaded before it will function. Minidrivers should embed firmware in the data segment of the minidriver. Optionally, the minidriver can dynamically load its firmware by calling the appropriate WDM file I/O functions, if, for example, the minidriver uses several versions of firmware that would make embedding it impractical.

-   Turn off synchronization (by setting the **TurnOffSynchronization** member in the [**HW\_INITIALIZATION\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff559682) structure to **TRUE**) if the minidriver needs to go to PASSIVE\_LEVEL (low priority) for most requests. See the [Minidriver Synchronization](minidriver-synchronization.md) section For more information about synchronization.

-   Hardware resources (port or memory addresses) should be accessed through the macros found in *wdm.h*. For example, to write to a word port, the macro WRITE\_PORT\_USHORT should be used. To write a buffer to a port, WRITE\_PORT\_BUFFER\_USHORT should be used.

-   Minidrivers should not have unprotected spin loops. If the minidriver needs to spin while waiting for the value of a port to change, the loop must be protected by a loop counter.

-   Minidrivers that need to synchronously wait for a small period of time should use [**KeStallExecutionProcessor**](https://msdn.microsoft.com/library/windows/hardware/ff553295). This routine should be used sparingly so system performance is not degraded.

-   Minidrivers that need to wait a long period of time (more than a few microseconds) for an operation to complete should either be interrupt-driven or use the [**StreamClassScheduleTimer**](https://msdn.microsoft.com/library/windows/hardware/ff568264) function to schedule a timed callback. Minidrivers should not spin for more than a few microseconds waiting for a status change, since it degrades overall system performance.

-   Devices that use bus-master DMA need only to use the scatter/gather DMA list supplied in the stream request block structure ([**HW\_STREAM\_REQUEST\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff559702)). No locking or mapping of the DMA buffers is necessary. See the **HW\_STREAM\_REQUEST\_BLOCK** structure for more information. Additionally, if minidrivers need to break up DMA requests, the [**StreamClassGetPhysicalAddress**](https://msdn.microsoft.com/library/windows/hardware/ff568247) function can be used to get the physical address of the offset within the virtual buffer pointers.

 

 




