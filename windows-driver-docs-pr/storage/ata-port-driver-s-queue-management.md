---
title: ATA Port Driver's Queue Management
description: ATA Port Driver's Queue Management
ms.assetid: feba86a6-2b89-41c9-9b14-b76c2522a332
keywords: ["ATA Port drivers WDK , queues", "queues WDK ATA Port driver", "device queues WDK ATA Port driver", "LUN queues WDK ATA Port driver"]
---

# ATA Port Driver's Queue Management


## <span id="ddk_ata_port_drivers_queue_management_kg"></span><span id="DDK_ATA_PORT_DRIVERS_QUEUE_MANAGEMENT_KG"></span>


The ATA port driver maintains a device queue for each logical unit number (LUN) that is exposed by the miniport driver and a separate queue for each channel that is enabled on the IDE controller. These queues work together to control the flow of requests to the miniport driver.

The following figure shows how requests flow from the port driver's LUN queues into the channel queues.

![ata device and channel queues](images/ataqueues.png)

Because the ATA port driver uses a push model of I/O, the ATA port driver does not wait for the miniport driver to request input before it forwards the next packet to the miniport driver. For information about the I/O model that the ATA port driver uses, see [ATA Port I/O Model](ata-port-i-o-model.md).

Nevertheless, the ATA port driver *does* limit the number of requests that it pushes down to the miniport driver. The number of requests is the value that the miniport driver assigns to the **NumberOfOverlappedRequests** member of the [**IDE\_CHANNEL\_CONFIGURATION**](https://msdn.microsoft.com/library/windows/hardware/ff559029) structure. The ATA port driver maintains a count of the number of uncompleted "overlapped" requests that it has forwarded to its miniport driver for a given channel. If this number exceeds the value in **NumberOfOverlappedRequests**, the ATA port driver stops passing new requests to the miniport driver. The ATA port driver keeps all new requests in its queues and waits for the miniport driver to complete some requests. After the number of outstanding requests falls below the value in **NumberOfOverlappedRequests**, the port driver resumes sending requests to the miniport driver.

The ATA miniport driver can also control the flow of requests that it receives from the port driver by calling the [**AtaPortDeviceBusy**](https://msdn.microsoft.com/library/windows/hardware/ff550155) and [**AtaPortDeviceReady**](https://msdn.microsoft.com/library/windows/hardware/ff550157) routines.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20ATA%20Port%20Driver's%20Queue%20Management%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




