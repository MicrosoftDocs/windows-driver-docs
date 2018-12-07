---
title: Queuing Storage Requests
description: Queuing Storage Requests
ms.assetid: 077f7e4f-feb5-4a2e-b22b-b1d8d6871987
keywords:
- peripherals WDK storage , queued requests
- storage peripherals WDK , queued requests
- queued requests WDK storage
- queues WDK storage
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Queuing Storage Requests


## <span id="ddk_queueing_storage_requests_kg"></span><span id="DDK_QUEUEING_STORAGE_REQUESTS_KG"></span>


Although it is possible for a storage class driver to set up internal queues for IRPs, it is seldom necessary to do so and likely to degrade the driver's performance as well, because the storage port driver already maintains driver-created, LU-specific device queues for IRPs. Whether or not a particular HBA supports multiple outstanding commands (for example, SCSI tagged queuing), storage class drivers can send every request to their devices as each IRP comes in and rely on the system-supplied port driver or the HBA to handle queued requests expeditiously.

When certain SCSI errors occur, the system port driver freezes the appropriate LU-specific queue and notifies the class driver. For more information about handling errors and releasing frozen request queues, see the following:

[Storage Class Driver's ReleaseQueue Routine](storage-class-driver-s-releasequeue-routine.md)

[Storage Class Driver's InterpretRequestSense Routine](storage-class-driver-s-interpretrequestsense-routine.md)

[Storage Class Driver's RetryRequest Routine](storage-class-driver-s-retryrequest-routine.md)

If an HBA supports command queuing, as indicated in the returned STORAGE\_ADAPTER\_DESCRIPTOR data, the class driver sets SRB\_FLAGS\_QUEUE\_ENABLE and uses the **QueueAction** member of the SRBs it creates to control how its requests are queued.

 

 




