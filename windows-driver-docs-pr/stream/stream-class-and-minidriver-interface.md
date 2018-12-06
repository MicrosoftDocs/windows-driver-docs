---
title: Stream Class and Minidriver Interface
description: Stream Class and Minidriver Interface
ms.assetid: d85510e6-1fd7-442a-bd88-f32b6c13ff75
keywords:
- Stream.sys class driver WDK Windows 2000 Kernel , stream class interface
- streaming minidrivers WDK Windows 2000 Kernel , stream class interface
- minidrivers WDK Windows 2000 Kernel Streaming , stream class interface
- stream class interface WDK streaming minidriver
- SRBs WDK streaming minidriver
- ISRs WDK streaming minidriver
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Stream Class and Minidriver Interface





The stream class interface is primarily a set of function calls between the class driver and the minidriver. The class driver controls the request flow, calling the adapter minidriver when access to the adapter hardware is necessary. The class driver is responsible for multiprocessor and interrupt synchronization. After both the class driver and the minidriver are initialized, the minidriver is passive and is called only by the class driver. Most of the function calls from the minidriver to the class driver are low-level service requests.

The basic mechanism controlling commands and information to the minidriver is the *stream request block* (SRB). A set of SRBs is provided for each minidriver to access particular capabilities of a driver and are usually specific for each data stream supported by the device. This information is passed to the device through an operating-system-controlled DMA in a large circular buffer.

An SRB comprises a command and data associated with that command. A [**HW\_STREAM\_REQUEST\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff559702) structure contains all information relating to a specific SRB. This structure, often referred to simply as an SRB, contains additional parameters to supplement the command.

The following illustration shows the interaction between the stream class and the minidriver during initialization.

![diagram illustrating the interaction between the stream class and the minidriver during initialization](images/stclassi.png)

All streaming minidriver functions are optionally synchronized with the minidriver's interrupt service routine (ISR), making the minidrivers nonreentrant. In other words, when a thread is executing in the minidriver, no calls will be made to any other function within the minidriver, including the ISR. This nonreentrant condition holds true even on multiprocessor Windows NT/Windows 2000 systems, making the minidrivers easier to write. The stream class driver achieves this nonreentrant condition by masking off the IRQ of the streaming minidriver (and all lower priority IRQs) using **KeSynchronizeExecution** when code is executing in any of the minidriver's routines. For more information about synchronization, see [Minidriver Synchronization](minidriver-synchronization.md).

The streaming minidriver can call WDM system services as necessary. However, the minidriver does not allocate a device object but uses the class driver's device object to make system calls. Most minidrivers do not need to make WDM system calls, because all necessary functionality is available from the class driver.

Minidrivers must be aware that all minidriver entry points are called at IRQL &gt; DISPATCH\_LEVEL when making WDM system service calls, except for the [**StreamClassCallAtNewPriority**](https://msdn.microsoft.com/library/windows/hardware/ff568230) routine. This function allows service calls at IRQL = DISPATCH\_LEVEL or PASSIVE\_LEVEL, depending on the priority specified. This limitation on IRQL can be overridden by setting the **TurnOffSynchronization** Boolean in the [**HW\_INITIALIZATION\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff559682) structure to **TRUE**.

 

 




