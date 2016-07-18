---
title: Completing an Isochronous Data Transfer
author: windows-driver-content
description: Completing an Isochronous Data Transfer
MS-HAID:
- '1394-isoch\_d58d7460-a333-40db-b13f-fef81239324b.xml'
- 'IEEE.completing\_an\_isochronous\_data\_transfer'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 1fc98e1b-4dd5-4358-aa23-86fcbbf33967
keywords: ["isochronous I/O WDK IEEE 1394 bus , completing transfers"]
---

# Completing an Isochronous Data Transfer


## <a href="" id="ddk-completing-an-isochronous-data-transfer-kg"></a>


Once a device no longer needs to transfer data, the driver must inform the bus that the operation is complete, and then deallocate the isochronous resources it allocated when setting up.

Drivers must follow these steps to clean up:

1.  If the driver has begun an isochronous operation through the [**REQUEST\_ISOCH\_LISTEN**](https://msdn.microsoft.com/library/windows/hardware/ff537655) or [**REQUEST\_ISOCH\_TALK**](https://msdn.microsoft.com/library/windows/hardware/ff537660) bus requests, it must issue the [**REQUEST\_ISOCH\_STOP**](https://msdn.microsoft.com/library/windows/hardware/ff537659) request to signal the bus driver to stop the isochronous operation.

2.  Any buffers that remain attached to a resource handle must be detached by using the [**REQUEST\_ISOCH\_DETACH\_BUFFERS**](https://msdn.microsoft.com/library/windows/hardware/ff537651) request.

3.  If the driver has allocated a resource handle, it must deallocate it through the [**REQUEST\_ISOCH\_FREE\_RESOURCES**](https://msdn.microsoft.com/library/windows/hardware/ff537654) request.

4.  If the driver has a channel allocated, it must deallocate it through the [**REQUEST\_ISOCH\_FREE\_CHANNEL**](https://msdn.microsoft.com/library/windows/hardware/ff537653) request.

5.  The driver must deallocate any bandwidth it has allocated by using the [**REQUEST\_ISOCH\_FREE\_BANDWIDTH**](https://msdn.microsoft.com/library/windows/hardware/ff537652) request.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5BIEEE\buses%5D:%20Completing%20an%20Isochronous%20Data%20Transfer%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


