---
title: Locking SCSI Port Driver's Internal Queue
author: windows-driver-content
description: Locking SCSI Port Driver's Internal Queue
ms.assetid: ea5be4e1-4908-431c-9c80-96539157b87e
---

# Locking SCSI Port Driver's Internal Queue


## <span id="ddk_locking_scsi_port_driver_s_internal_queue_kg"></span><span id="DDK_LOCKING_SCSI_PORT_DRIVER_S_INTERNAL_QUEUE_KG"></span>


The class driver and other higher-level drivers can force SCSI Port to halt processing of the requests in its queue. The class driver halts SCSI Port's queue by sending it an SRB of type SRB\_FUNCTION\_LOCK\_QUEUE. The class driver typically halts processing of requests in the SCSI Port's queue in order to change a device's power state. After changing the power state of the device, the class driver unlocks the queue. The sequence is as follows:

1.  Class driver locks SCSI Port's queue (using IRP\_MJ\_SCSI with an SRB function value of SRB\_FUNCTION\_LOCK\_QUEUE).

2.  Class driver requests change of power state (using IRP\_MJ\_SCSI with the SRB\_FLAGS\_BYPASS\_LOCKED\_QUEUE flag set to ensure that a power IRP is not queued).

3.  Class driver unlocks SCSI Port's queue (IRP\_MJ\_SCSI with an SRB function value of SRB\_FUNCTION\_UNLOCK\_QUEUE and the SRB\_FLAGS\_BYPASS\_LOCKED\_QUEUE flag set).

Once its queue is unlocked, SCSI Port resumes processing queued SRBs. A class driver should not attempt to bypass a queue that was locked by another driver.

For more information about unlocking queues from the perspective of the class driver, see [Storage Class Driver's ReleaseQueue Routine](storage-class-driver-s-releasequeue-routine.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Locking%20SCSI%20Port%20Driver's%20Internal%20Queue%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


