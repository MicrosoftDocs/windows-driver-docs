---
title: Writing a Stream Minidriver
author: windows-driver-content
description: Writing a Stream Minidriver
MS-HAID:
- 'strmini-design\_b704f365-0320-4a14-bb8d-5197a476b85b.xml'
- 'stream.writing\_a\_stream\_minidriver'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 83540dff-3774-4197-8ba1-d28e12b4e366
keywords: ["Stream.sys class driver WDK Windows 2000 Kernel , writing", "streaming minidrivers WDK Windows 2000 Kernel , writing", "minidrivers WDK Windows 2000 Kernel Streaming , writing"]
---

# Writing a Stream Minidriver


## <a href="" id="ddk-writing-a-stream-minidriver-ksg"></a>


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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Writing%20a%20Stream%20Minidriver%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


