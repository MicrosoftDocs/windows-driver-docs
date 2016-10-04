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


