---
title: Buffering Isochronous DMA Transfers for IEEE 1394 Devices
author: windows-driver-content
description: Buffering Isochronous DMA Transfers for IEEE 1394 Devices
MS-HAID:
- '1394-isoch\_c355e228-b716-45a4-a713-8b35550a8302.xml'
- 'IEEE.buffering\_isochronous\_dma\_transfers\_for\_ieee\_1394\_devices'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 5a08303b-8a4a-4c55-ba48-c4d5ea06157e
keywords: ["isochronous I/O WDK IEEE 1394 bus , buffering DMA transfers", "buffers WDK IEEE 1394 bus", "DMA transfers WDK IEEE 1394 bus"]
---

# Buffering Isochronous DMA Transfers for IEEE 1394 Devices


## <a href="" id="ddk-buffering-isochronous-dma-transfers-for-ieee-1394-devices-kg"></a>


Once begun, isochronous transfer is continuous until halted. The host controller must have a ready supply of buffers to handle the transaction's demands. The bus driver uses the buffers attached to the resource handle until they are used up, and then halts the DMA. Before this happens, the driver attaches additional buffers to continue the transaction. The ISOCH\_DESCRIPTOR for a buffer optionally provides a callback for when the bus driver has finished with a buffer—the driver can use this to attach additional buffers. For optimal performance, the driver should attach several buffers at a time, and provide a callback only with the last buffer to signal that the supply of buffers has run out.

The following diagram illustrates buffers used in isochronous transfer.

![diagram illustrating buffers used in isochronous transfer](images/1394lin.png)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5BIEEE\buses%5D:%20Buffering%20Isochronous%20DMA%20Transfers%20for%20IEEE%201394%20Devices%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


