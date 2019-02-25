---
title: Minidriver Synchronization
description: Minidriver Synchronization
ms.assetid: 2f560e7a-4717-4b3f-9513-e34fcb2b5e6c
keywords:
- Stream.sys class driver WDK Windows 2000 Kernel , synchronization
- streaming minidrivers WDK Windows 2000 Kernel , synchronization
- minidrivers WDK Windows 2000 Kernel Streaming , synchronization
- synchronization WDK streaming minidriver
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Minidriver Synchronization





Streaming minidriver developers have the option of allowing the class driver to handle synchronization. When minidrivers register themselves with the class driver, they can opt for class-driver-provided synchronization by setting the **TurnOffSynchronization** member of [**HW\_INITIALIZATION\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff559682) to **FALSE**.

When the class driver handles synchronization, it ensures that two pieces of the minidriver code are never executed simultaneously. The class driver queues all stream requests, and passes them to the minidriver one at a time.

One purpose of this synchronization is to spare the minidriver writer from having to deal with all the details of driver synchronization and request queuing in a multitasking, reentrant, multiprocessor environment. However, some minidrivers should not use it. Two examples are provided in the [Synchronization Examples](synchronization-examples.md) topic that illustrate what a minidriver needs to do concerning synchronization.

Turning stream class synchronization off means that all requests are immediately and asynchronously called down to the minidriver in the context of the submitting thread at PASSIVE\_LEVEL. Exceptions to the preceding rule are HwCancelPacket, TimeoutHandler, and Timer routines. These are called at DISPATCH\_LEVEL. A final exception is the interrupt handler, which is called at DIRQL.

When synchronization is off, the minidriver is responsible for performing synchronization in compliance with the WDM model. If a minidriver is called back at PASSIVE\_LEVEL, it can then be preempted by any higher IRQL events such as DPCs or interrupts. Similarly, if a minidriver is called back at DISPATCH\_LEVEL, it can subsequently be preempted by interrupts. Minidriver functions that manipulate shared resources must synchronize the accesses.

Multiple requests can be simultaneously issued to the same or different streams when stream class synchronization is off. The minidriver must queue its own requests and handle any hardware synchronization with other threads and the ISR. Spin locks, mutexes, and [**KeSynchronizeExecution**](https://msdn.microsoft.com/library/windows/hardware/ff553302) are some of the synchronization objects available to stream minidrivers running without stream class synchronization.

 

 




