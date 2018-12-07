---
title: Storage Class Driver's ReleaseQueue Routine
description: Storage Class Driver's ReleaseQueue Routine
ms.assetid: 4d0f74f2-6c98-4de1-bc28-dfff3c01e319
keywords:
- ReleaseQueue
- queues WDK storage
- freezing queues WDK storage
- frozen queues WDK storage
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Storage Class Driver's ReleaseQueue Routine


## <span id="ddk_storage_class_drivers_releasequeue_routine_kg"></span><span id="DDK_STORAGE_CLASS_DRIVERS_RELEASEQUEUE_ROUTINE_KG"></span>


Unless a storage class driver ORs the **SrbFlags** for a given request with SRB\_FLAGS\_NO\_QUEUE\_FREEZE, the system port driver freezes a queue for a given logical unit after any of the following:

-   A bus reset occurred while the logical unit was executing a request.

-   The logical unit returned SCSISTAT\_CHECK\_CONDITION or SCSISTAT\_COMMAND\_TERMINATED, which the class driver can find in the SRB's **ScsiStatus** member.

-   A request was timed out.

-   A request was terminated by a bus message command such as SCSIMESS\_ABORT.

The port driver indicates that an LU-specific queue has been frozen by returning a request with SRB\_STATUS\_QUEUE\_FROZEN in the **SrbStatus** member. New requests from the class driver can be inserted into the queue, but only autosense requests are sent to the logical unit as long as its queue is frozen.

Freezing the queue under these conditions gives each storage class driver an opportunity to analyze an error before other queued jobs are executed. For example, queued jobs might need to be canceled if the media has changed. To flush the queue, the driver can send a request with the **SrbFlags** ORed with SRB\_FLAGS\_BYPASS\_FROZEN\_QUEUE.

A *ReleaseQueue* routine allocates and sets up an IRP and an SRB to either release or flush a frozen queue. The **Function** member of the SRB must be set to SRB\_FUNCTION\_RELEASE\_QUEUE or SRB\_FUNCTION\_FLUSH\_QUEUE, which both releases a frozen queue and cancels all currently queued requests for the target logical unit. The port driver completes all requests in a flushed queue with their **SrbStatus** members set to SRB\_STATUS\_REQUEST\_FLUSHED.

Failing to release a frozen queue makes the device inaccessible, so a driver's *ReleaseQueue* routine should be designed to succeed even in low memory conditions. A *ReleaseQueue* routine should first attempt to allocate memory for an SRB by calling [**ExAllocatePool**](https://msdn.microsoft.com/library/windows/hardware/ff544501) with the **NonPagedPool** memory type and, if that allocation fails, use an SRB that was preallocated during driver initialization. If the driver allocates an SRB to hold in reserve when it initializes its device extension, as described in [Setting Up a Storage Class Driver's Device Extension](setting-up-a-storage-class-driver-s-device-extension.md), its *ReleaseQueue* can use that SRB if the memory pool is low, with an appropriate synchronization mechanism in case multiple concurrent release operations might be needed.

Note that a class driver's *ReleaseQueue* routine is called asynchronously, generally from its *IoCompletion* routine. A class driver's *IoCompletion* routine cannot call *ReleaseQueue* to flush a queue that is not frozen. However, it can call *ReleaseQueue* to release an unfrozen queue, and the port driver simply ignores such a request.

 

 




