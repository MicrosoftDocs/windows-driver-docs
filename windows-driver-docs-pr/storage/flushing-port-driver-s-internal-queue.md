---
title: Flushing Port Driver's Internal Queue
description: Flushing Port Driver's Internal Queue
ms.assetid: b0e6762e-0380-4ff5-aac7-36bdb5a60aa7
---

# Flushing Port Driver's Internal Queue


## <span id="ddk_flushing_port_driver_s_internal_queue_kg"></span><span id="DDK_FLUSHING_PORT_DRIVER_S_INTERNAL_QUEUE_KG"></span>


The SCSI Port driver supports a flush request that allows higher-level drivers to flush the caches of devices and adapters that cache data internally. To maintain data integrity, all internal caches should be flushed before the system is shut down. Upon receiving a flush request SCSI Port flushes its own internal queues as well, canceling all queued requests.

Higher-level drivers can flush a host adapter's cache and SCSI Port's internal queue by sending an SRB of type SRB\_FUNCTION\_FLUSH\_QUEUE to the SCSI Port driver. Upon receiving this SRB, SCSI Port flushes the host adapter cache and then completes all requests in its internal queue with their **SrbStatus** members set to SRB\_STATUS\_REQUEST\_FLUSHED. If SCSI Port's queue is frozen, SRB\_FUNCTION\_FLUSH\_QUEUE has the side effect of unfreezing the queue.

For a discussion of how storage miniport drivers handle flush requests, see [Handling SRB\_FUNCTION\_FLUSH and SRB\_FUNCTION\_SHUTDOWN](handling-srb-function-flush-and-srb-function-shutdown.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Flushing%20Port%20Driver's%20Internal%20Queue%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




