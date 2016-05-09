---
title: Freezing SCSI Port Driver's Internal Queue
author: windows-driver-content
description: Freezing SCSI Port Driver's Internal Queue
ms.assetid: 8e93b7d4-8429-43ec-a439-75cfeaa95887
---

# Freezing SCSI Port Driver's Internal Queue


## <span id="ddk_freezing_scsi_port_drivers_internal_queue_kg"></span><span id="DDK_FREEZING_SCSI_PORT_DRIVERS_INTERNAL_QUEUE_KG"></span>


The SCSI Port driver freezes its internal queue whenever an error condition occurs that requires arbitration from the class driver. Freezing the queue allows SCSI Port to report the error condition to the class driver and to give the class driver an opportunity to analyze the error before resuming the processing of the requests that remain in the queue. For example, if the media is changed, a queued request might need to be canceled, but arbitration by the class driver is required. Only the class driver has enough contextual information to determine whether the removal of a certain type of media affects a particular request.

If a storage class driver ORs the **SrbFlags** for a given request with SRB\_FLAGS\_NO\_QUEUE\_FREEZE, SCSI Port will not freeze its queue as a result of problems with that particular request. Otherwise, SCSI Port freezes its queue under any of the following conditions:

-   The device fails the request and returns a status of SCSISTAT\_CHECK\_CONDITION or SCSISTAT\_COMMAND\_TERMINATED

-   The request times out

-   A bus reset occurs while the device is executing a request

-   A request is terminated by a bus message command such as SCSIMESS\_ABORT

SCSI Port indicates that its queue is frozen by returning the request that provoked the freeze with the SRB\_STATUS\_QUEUE\_FROZEN flag set in the **SrbStatus** member of the SRB. SCSI Port inserts any new requests from the class driver into the queue, but as long as the queue is frozen SCSI Port will not forward any requests to the device other than autosense and power requests.

If the SRB\_FLAGS\_BYPASS\_FROZEN\_QUEUE flag is set in the **SrbFlags** member of a request, SCSI Port bypasses the frozen queue and executes the request immediately. Any subsequent request in which **SrbFlags** is ORed with SRB\_FLAGS\_BYPASS\_FROZEN\_QUEUE will cause SCSI Port to flush the queue.

Higher-level drivers can force SCSI Port to unfreeze its queue using a SRB\_FUNCTION\_RELEASE\_QUEUE release queue request. SRB\_FUNCTION\_FLUSH\_QUEUE also unfreezes the queue after canceling all of the queued requests.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Freezing%20SCSI%20Port%20Driver's%20Internal%20Queue%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


