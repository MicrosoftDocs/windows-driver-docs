---
title: Using Direct I/O
author: windows-driver-content
description: Using Direct I/O
MS-HAID:
- 'ioproguser\_30be904a-89e3-4c81-85cb-7832413b67b0.xml'
- 'kernel.using\_direct\_i\_o'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: e40b4657-833f-404c-8472-2e33564129a5
keywords: ["direct I/O WDK kernel", "buffers WDK I/O , direct I/O", "data buffers WDK I/O , direct I/O", "I/O WDK kernel , direct I/O"]
---

# Using Direct I/O


## <a href="" id="ddk-using-direct-i-o-kg"></a>


Drivers for devices that can transfer large amounts of data at a time should use direct I/O for those transfers. Using direct I/O for large transfers improves a driver's performance, both by reducing its interrupt overhead and by eliminating the memory allocation and copying operations inherent in buffered I/O.

Generally, mass-storage device drivers request direct I/O for transfer requests, including lowest-level drivers that use direct memory access (DMA) or programmed I/O (PIO), as well as any intermediate drivers chained above them.

The I/O manager determines that an I/O operation is using direct I/O as follows:

-   For [**IRP\_MJ\_READ**](https://msdn.microsoft.com/library/windows/hardware/ff550794) and [**IRP\_MJ\_WRITE**](https://msdn.microsoft.com/library/windows/hardware/ff550819) requests, DO\_DIRECT\_IO is set in the **Flags** member of the [**DEVICE\_OBJECT**](https://msdn.microsoft.com/library/windows/hardware/ff543147) structure. For more information, see [Initializing a Device Object](initializing-a-device-object.md).

-   For [**IRP\_MJ\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550744) and [**IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550766) requests, the IOCTL code's value contains METHOD\_IN\_DIRECT or METHOD\_OUT\_DIRECT as the *TransferType* value in the IOCTL value. For more information, see [Defining I/O Control Codes](defining-i-o-control-codes.md).

Drivers that use direct I/O will sometimes also use buffered I/O to handle some IRPs. In particular, drivers typically use buffered I/O for some I/O control codes for **IRP\_MJ\_DEVICE\_CONTROL** requests that require data transfers, regardless of whether the driver uses direct I/O for read and write operations.

Setting up a direct I/O transfer varies slightly, depending on whether DMA or PIO is being used. For more information, see:

[Using Direct I/O with DMA](using-direct-i-o-with-dma.md)

[Using Direct I/O with PIO](using-direct-i-o-with-pio.md)

Drivers must take steps to maintain cache coherency during DMA and PIO transfers. For more information, see [Maintaining Cache Coherency](maintaining-cache-coherency.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Using%20Direct%20I/O%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


