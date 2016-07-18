---
title: Isochronous I/O for IEEE 1394 Devices
author: windows-driver-content
description: Isochronous I/O for IEEE 1394 Devices
MS-HAID:
- '1394-isoch\_0d86dc4e-5b5c-4e02-9d22-9a17ac7f579b.xml'
- 'IEEE.isochronous\_i\_o\_for\_ieee\_1394\_devices'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: fc544776-af45-40e2-9699-7dcc50275d1e
keywords: ["IEEE 1394 WDK buses , isochronous I/O", "1394 WDK buses , isochronous I/O", "I/O WDK IEEE 1394 bus", "I/O request packets WDK IEEE 1394 bus", "IRPs WDK IEEE 1394 bus", "isochronous I/O WDK IEEE 1394 bus", "guaranteed bandwidth WDK IEEE 1394 bus", "bandwidth WDK IEEE 1394 bus", "isochronous I/O WDK IEEE 1394 bus , about isochronous I/O", "transferring data WDK IEEE 1394 bus"]
---

# Isochronous I/O for IEEE 1394 Devices


## <a href="" id="ddk-isochronous-i-o-for-ieee-1394-devices-kg"></a>


Real-time multimedia devices such as digital cameras need large amounts of bandwidth to send data in a steady stream, but do not require guaranteed delivery. (For example, a dropped frame from a digital camera would degrade the quality of the signal, but it would not destroy its meaning.) For such devices, IEEE 1394 provides *isochronous* transfer, which provides guaranteed bandwidth, but does not guarantee delivery.

This section includes:

[Setting Up Isochronous Transfer for IEEE 1394 Devices](https://msdn.microsoft.com/library/windows/hardware/ff538108)

[Buffering Isochronous DMA Transfers for IEEE 1394 Devices](https://msdn.microsoft.com/library/windows/hardware/ff537014)

[Isochronous Listen Options for IEEE 1394 Devices](https://msdn.microsoft.com/library/windows/hardware/ff537377)

[Isochronous Talk Options for IEEE 1394 Devices](https://msdn.microsoft.com/library/windows/hardware/ff537380)

[Isochronous Synchronization Options for IEEE 1394 Devices](https://msdn.microsoft.com/library/windows/hardware/ff537379)

[Completing an Isochronous Data Transfer](https://msdn.microsoft.com/library/windows/hardware/ff537058)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5BIEEE\buses%5D:%20Isochronous%20I/O%20for%20IEEE%201394%20Devices%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


