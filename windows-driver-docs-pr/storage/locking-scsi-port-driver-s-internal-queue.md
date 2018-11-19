---
title: Locking SCSI Port Driver's Internal Queue
description: Locking SCSI Port Driver's Internal Queue
ms.assetid: ea5be4e1-4908-431c-9c80-96539157b87e
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Locking SCSI Port Driver's Internal Queue


## <span id="ddk_locking_scsi_port_driver_s_internal_queue_kg"></span><span id="DDK_LOCKING_SCSI_PORT_DRIVER_S_INTERNAL_QUEUE_KG"></span>


The class driver and other higher-level drivers can force SCSI Port to halt processing of the requests in its queue. The class driver halts SCSI Port's queue by sending it an SRB of type SRB\_FUNCTION\_LOCK\_QUEUE. The class driver typically halts processing of requests in the SCSI Port's queue in order to change a device's power state. After changing the power state of the device, the class driver unlocks the queue. The sequence is as follows:

1.  Class driver locks SCSI Port's queue (using IRP\_MJ\_SCSI with an SRB function value of SRB\_FUNCTION\_LOCK\_QUEUE).

2.  Class driver requests change of power state (using IRP\_MJ\_SCSI with the SRB\_FLAGS\_BYPASS\_LOCKED\_QUEUE flag set to ensure that a power IRP is not queued).

3.  Class driver unlocks SCSI Port's queue (IRP\_MJ\_SCSI with an SRB function value of SRB\_FUNCTION\_UNLOCK\_QUEUE and the SRB\_FLAGS\_BYPASS\_LOCKED\_QUEUE flag set).

Once its queue is unlocked, SCSI Port resumes processing queued SRBs. A class driver should not attempt to bypass a queue that was locked by another driver.

For more information about unlocking queues from the perspective of the class driver, see [Storage Class Driver's ReleaseQueue Routine](storage-class-driver-s-releasequeue-routine.md).

 

 




