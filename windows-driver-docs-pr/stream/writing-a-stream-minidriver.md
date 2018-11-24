---
title: Writing a Stream Minidriver
description: Writing a Stream Minidriver
ms.assetid: 83540dff-3774-4197-8ba1-d28e12b4e366
keywords:
- Stream.sys class driver WDK Windows 2000 Kernel , writing
- streaming minidrivers WDK Windows 2000 Kernel , writing
- minidrivers WDK Windows 2000 Kernel Streaming , writing
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Writing a Stream Minidriver





The main design goal of the stream class driver is to handle the work both of handling the operating system, which includes the intricacies of supporting multiprocessor machines, and of supporting kernel streaming semantics. It requires the minidriver to handle only the device-specific portion of any operation it must perform. The class driver allocates memory for the minidriver, performs bookkeeping for any NT kernel resources the minidriver may require, and (optionally) handles all synchronization issues.

The class driver communicates to the minidriver through a set of minidriver-provided callbacks. Most of the work of writing a streaming minidriver occurs in writing these callbacks.

In this documentation, we refer to each type of minidriver-provided routines as **StrMiniXxx**. The minidriver may have to provide one or more versions of each routine, depending on how many different functions the underlying hardware is capable of performing.

A streaming driver typically can support several different streams of data. For example, a DVD player produces both an audio and a video stream. Within the context of kernel streaming, each stream of data is represented by a [pin](ks-pins.md).

The stream class driver keeps track of each pin on the minidriver. In the terminology of the class driver, each pin type is a *stream*. Streams, like pin types, may have multiple instances. Since streams can receive I/O requests, the driver must provide callbacks for each stream.

The following are the routines the minidriver may have to provide. They are documented more fully below and in the reference guide.

**Routines every minidriver provides**

[*StrMiniCancelPacket*](https://msdn.microsoft.com/library/windows/hardware/ff568448)

[*StrMiniReceiveDevicePacket*](https://msdn.microsoft.com/library/windows/hardware/ff568463)

[*StrMiniRequestTimeout*](https://msdn.microsoft.com/library/windows/hardware/ff568473)

[*StrMiniEvent*](https://msdn.microsoft.com/library/windows/hardware/ff568457)

[*StrMiniInterrupt*](https://msdn.microsoft.com/library/windows/hardware/ff568459)

**Routines the minidriver provides for each individual stream**

[*StrMiniReceiveStreamDataPacket*](https://msdn.microsoft.com/library/windows/hardware/ff568470)

[**StrMiniReceiveStreamControlPacket**](https://msdn.microsoft.com/library/windows/hardware/ff568467)

[*StrMiniEvent*](https://msdn.microsoft.com/library/windows/hardware/ff568457)

[*StrMiniClock*](https://msdn.microsoft.com/library/windows/hardware/ff568452)

It is possible for the minidriver to use the same callback for several different streams. The callback can determine the stream on whose behalf it was called from its parameters.

The minidriver must, like all WDM drivers, also provide a **DriverEntry** routine. The main task of the **DriverEntry** routine of a minidriver is to register the minidriver with the class driver.

The class driver receives all I/O requests on behalf of the minidriver. To obtain the information it needs to complete the request, the class driver builds a stream request block (SRB) and passes it to one of the **StrMini*XXX*Packet** routines. The class driver dispatches I/O requests to the device as a whole to the [*StrMiniReceiveDevicePacket*](https://msdn.microsoft.com/library/windows/hardware/ff568463) routine. It passes requests to individual streams to the [*StrMiniReceiveStreamDataPacket*](https://msdn.microsoft.com/library/windows/hardware/ff568470) (for kernel streaming read and write requests) or [**StrMiniReceiveStreamControlPacket**](https://msdn.microsoft.com/library/windows/hardware/ff568467) (for other requests).

Normally, the class driver queues its requests, and passes them one at a time to the minidriver. The minidriver may optionally do its own synchronization; the minidriver is then responsible for queuing requests it cannot immediately handle. See [Minidriver Synchronization](minidriver-synchronization.md) for details.

The minidriver must provide two additional routines for manipulating stream request blocks. The class driver calls [*StrMiniCancelPacket*](https://msdn.microsoft.com/library/windows/hardware/ff568448) when it receives a cancel IRP, and needs to tell the minidriver to cancel a specific packet. The class driver also keeps track of how long the minidriver takes to complete its handling of a stream request block. If the minidriver takes too long, the class driver times out the request, and calls the minidriver's [*StrMiniRequestTimeout*](https://msdn.microsoft.com/library/windows/hardware/ff568473) routine.

When a hardware interrupt occurs, the operating system signals the class driver, which then calls the minidriver's [*StrMiniInterrupt*](https://msdn.microsoft.com/library/windows/hardware/ff568459) routine to handle the interrupt.

 

 




