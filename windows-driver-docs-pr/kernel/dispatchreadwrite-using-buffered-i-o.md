---
title: DispatchReadWrite Using Buffered I/O
author: windows-driver-content
description: DispatchReadWrite Using Buffered I/O
ms.assetid: bb8ce47d-5722-4050-9492-bec154744597
keywords: ["DispatchReadWrite routine", "dispatch routines WDK kernel , DispatchReadWrite routine", "read/write dispatch routines WDK kernel", "IRP_MJ_WRITE I/O function codes", "IRP_MJ_READ I/O function codes", "data transfers WDK kernel , read/write dispatch routines", "transferring data WDK kernel , read/write dispatch routines", "buffered I/O WDK kernel", "I/O WDK kernel , buffered"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# DispatchReadWrite Using Buffered I/O


## <a href="" id="ddk-dispatchreadwrite-using-buffered-i-o-kg"></a>


Any lowest-level device driver that sets up its device objects for buffered I/O satisfies a read request by returning data transferred from its device into a locked down system-space buffer at **Irp-&gt;AssociatedIrp.SystemBuffer**. It satisfies a write request by transferring data from the same buffer out to its device.

Consequently, the *DispatchReadWrite* routine of such a device driver usually does the following on receipt of a transfer request:

1.  Calls [**IoGetCurrentIrpStackLocation**](https://msdn.microsoft.com/library/windows/hardware/ff549174) and determines the direction of the transfer request.

2.  Checks the validity of the parameters for the request.

    -   For a read request, the routine usually checks the driver's *IoStackLocation*-&gt;**Parameters.Read.Length** value to determine whether the buffer is large enough to receive data transferred from the device.

        For example, the system keyboard class driver processes read requests that come only from the Win32 user input thread. This driver defines a structure, KEYBOARD\_INPUT\_DATA, in which to store keystrokes from the device and, at any given moment, holds some number of these structures in an internal ring buffer in order to satisfy read requests as they come in.

    -   For a write request, the routine usually checks the value at **Parameters.Write.Length**, and checks the data at **Irp-&gt;AssociatedIrp.SystemBuffer** for validity if necessary: that is, if its device accepts only structured data packets containing members with defined value ranges.

3.  If any parameters are invalid, the *DispatchReadWrite* routine completes the IRP immediately, as already described in [Completing IRPs](completing-irps.md). Otherwise, the routine passes the IRP on for further processing by other driver routines, as described in [Passing IRPs down the Driver Stack](passing-irps-down-the-driver-stack.md).

Lowest-level device drivers that use buffered I/O usually must satisfy a transfer request by reading or writing data of a size specified by that the originator of the request. Such a driver is likely to define a structure for data coming in from or being sent to its device and is likely to buffer structured data internally, as the system keyboard class driver does.

Drivers that buffer data internally should support [**IRP\_MJ\_FLUSH\_BUFFERS**](https://msdn.microsoft.com/library/windows/hardware/ff550760) requests, and can also support [**IRP\_MJ\_SHUTDOWN**](https://msdn.microsoft.com/library/windows/hardware/ff550807) requests.

The highest-level driver in a chain is usually responsible for checking the input IRP's parameters before passing a read/write request on to lower drivers. Consequently, many lower-level drivers can assume that their I/O stack locations in a read/write IRP have valid parameters. If a lowest-level driver in a chain is aware of device-specific constraints on data transfers, that driver is required to check the validity of the parameters in its I/O stack location.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20DispatchReadWrite%20Using%20Buffered%20I/O%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


