---
title: Opening and Using a Parallel Device
author: windows-driver-content
description: Opening and Using a Parallel Device
MS-HAID:
- 'vspd\_65f06290-197a-4f32-8e23-512157432be4.xml'
- 'parports.opening\_and\_using\_a\_parallel\_device'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: ca58b1c3-9ecf-4ebe-8f08-a2f78ae17921
keywords: ["parallel devices WDK , opening", "parallel devices WDK , sharing"]
---

# Opening and Using a Parallel Device


## <a href="" id="ddk-opening-and-using-a-parallel-device-kg"></a>


The system-supplied bus driver for parallel ports enforces exclusive access to a parallel device attached to a parallel port. If a parallel device is open, the parallel port bus driver fails any subsequent [**IRP\_MJ\_CREATE**](https://msdn.microsoft.com/library/windows/hardware/ff544131) requests for the device until the device has been closed. A client must open a parallel device before it sends other I/O requests to the device or calls the [parallel device callback routines](https://msdn.microsoft.com/library/windows/hardware/ff544275). A client must not attempt to communicate with a parallel device after the client has closed its file on a device. A client must close a device to allow other clients to access the device.

A client usually does the following:

-   Opens a parallel device

-   Connects to a parallel device − see [Connecting to a Parallel Device](connecting-to-a-parallel-device.md)

-   Obtains information about the parallel device − see [Obtaining Information about a Parallel Device](obtaining-information-about-a-parallel-device.md)

-   Locks the device − see [Locking and Unlocking a Parallel Port for Use by a Parallel Device](locking-and-unlocking-a-parallel-port-for-use-by-a-parallel-device.md)

-   Does a sequence of operations on the device

-   Disconnects from a parallel device − see [Connecting to a Parallel Device](connecting-to-a-parallel-device.md)

-   Unlocks the device − see [Locking and Unlocking a Parallel Port for Use by a Parallel Device](locking-and-unlocking-a-parallel-port-for-use-by-a-parallel-device.md)

-   Closes the device

Note that in a Plug and Play environment, a device can be removed or added whenever there are no open files on it. In general, every time a parallel device is added, Plug and Play assigns a different location and resources.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bparports\parports%5D:%20Opening%20and%20Using%20a%20Parallel%20Device%20%20RELEASE:%20%287/25/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


