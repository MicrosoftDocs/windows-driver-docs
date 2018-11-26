---
title: Flushing Port Driver's Internal Queue
description: Flushing Port Driver's Internal Queue
ms.assetid: b0e6762e-0380-4ff5-aac7-36bdb5a60aa7
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Flushing Port Driver's Internal Queue


## <span id="ddk_flushing_port_driver_s_internal_queue_kg"></span><span id="DDK_FLUSHING_PORT_DRIVER_S_INTERNAL_QUEUE_KG"></span>


The SCSI Port driver supports a flush request that allows higher-level drivers to flush the caches of devices and adapters that cache data internally. To maintain data integrity, all internal caches should be flushed before the system is shut down. Upon receiving a flush request SCSI Port flushes its own internal queues as well, canceling all queued requests.

Higher-level drivers can flush a host adapter's cache and SCSI Port's internal queue by sending an SRB of type SRB\_FUNCTION\_FLUSH\_QUEUE to the SCSI Port driver. Upon receiving this SRB, SCSI Port flushes the host adapter cache and then completes all requests in its internal queue with their **SrbStatus** members set to SRB\_STATUS\_REQUEST\_FLUSHED. If SCSI Port's queue is frozen, SRB\_FUNCTION\_FLUSH\_QUEUE has the side effect of unfreezing the queue.

For a discussion of how storage miniport drivers handle flush requests, see [Handling SRB\_FUNCTION\_FLUSH and SRB\_FUNCTION\_SHUTDOWN](handling-srb-function-flush-and-srb-function-shutdown.md).

 

 




