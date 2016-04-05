---
title: Obtaining Information About an I/O Request
description: Obtaining Information About an I/O Request
ms.assetid: a686ea00-6987-480a-a4ce-892e1efbed87
keywords: ["request processing WDK KMDF , obtaining information about", "I/O requests WDK KMDF , obtaining information about", "status information WDK KMDF", "status information WDK KMDF , I/O requests"]
---

# Obtaining Information About an I/O Request


Before processing an I/O request, a driver must determine the request type. When a framework-based driver [creates I/O queues](creating-i-o-queues.md) for a device, it typically sets up the I/O queues and request handlers so that each queue or request handler receives requests of a particular type (read, write, or device I/O control).

After determining the request type, the driver must obtain the request's input and output buffers, if they are needed. For information about obtaining a request's buffers, see [Accessing Data Buffers in Framework-Based Drivers](https://msdn.microsoft.com/library/windows/hardware/ff540701).

To provide additional information about an I/O request that a driver has received, the framework request object defines the following methods:

-   [**WdfRequestGetIoQueue**](https://msdn.microsoft.com/library/windows/hardware/ff549968), which returns a handle to the I/O queue from which the I/O request was delivered.

-   [**WdfRequestGetRequestorMode**](https://msdn.microsoft.com/library/windows/hardware/ff549971), which returns the processor access mode (user or kernel) of the request's originator.

-   [**WdfRequestGetFileObject**](https://msdn.microsoft.com/library/windows/hardware/ff549963), which returns a handle to the framework file object that is associated with the request.

-   [**WdfRequestWdmGetIrp**](https://msdn.microsoft.com/library/windows/hardware/ff550037), which returns the WDM [**IRP**](https://msdn.microsoft.com/library/windows/hardware/ff550694) structure that is associated with the request.

-   [**WdfRequestGetParameters**](https://msdn.microsoft.com/library/windows/hardware/ff549969), which retrieves non-IRP request parameters in WDM format.

After a driver completes an I/O request, other drivers in the driver stack can call additional request object methods to obtain request completion information. For more information about these additional methods, see [Completing I/O Requests](completing-i-o-requests.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Obtaining%20Information%20About%20an%20I/O%20Request%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




