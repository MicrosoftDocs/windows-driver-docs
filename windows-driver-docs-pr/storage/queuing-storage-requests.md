---
title: Queuing Storage Requests
author: windows-driver-content
description: Queuing Storage Requests
ms.assetid: 077f7e4f-feb5-4a2e-b22b-b1d8d6871987
keywords: ["peripherals WDK storage , queued requests", "storage peripherals WDK , queued requests", "queued requests WDK storage", "queues WDK storage"]
---

# Queuing Storage Requests


## <span id="ddk_queueing_storage_requests_kg"></span><span id="DDK_QUEUEING_STORAGE_REQUESTS_KG"></span>


Although it is possible for a storage class driver to set up internal queues for IRPs, it is seldom necessary to do so and likely to degrade the driver's performance as well, because the storage port driver already maintains driver-created, LU-specific device queues for IRPs. Whether or not a particular HBA supports multiple outstanding commands (for example, SCSI tagged queuing), storage class drivers can send every request to their devices as each IRP comes in and rely on the system-supplied port driver or the HBA to handle queued requests expeditiously.

When certain SCSI errors occur, the system port driver freezes the appropriate LU-specific queue and notifies the class driver. For more information about handling errors and releasing frozen request queues, see the following:

[Storage Class Driver's ReleaseQueue Routine](storage-class-driver-s-releasequeue-routine.md)

[Storage Class Driver's InterpretRequestSense Routine](storage-class-driver-s-interpretrequestsense-routine.md)

[Storage Class Driver's RetryRequest Routine](storage-class-driver-s-retryrequest-routine.md)

If an HBA supports command queuing, as indicated in the returned STORAGE\_ADAPTER\_DESCRIPTOR data, the class driver sets SRB\_FLAGS\_QUEUE\_ENABLE and uses the **QueueAction** member of the SRBs it creates to control how its requests are queued.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Queuing%20Storage%20Requests%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


