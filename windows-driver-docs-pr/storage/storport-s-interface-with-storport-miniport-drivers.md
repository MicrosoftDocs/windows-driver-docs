---
title: Storport's Interface with Storport Miniport Drivers
description: Storport's Interface with Storport Miniport Drivers
ms.date: 06/18/2019
---

# Storport's Interface with Storport Miniport Drivers

Communication between the Storport driver and the Storport miniport drivers takes place by means of SCSI request blocks (SRBs) and miniport driver callback routines. For a detailed discussion of the Storport miniport driver callback routines, see [Storport Miniport Driver Routines](./storport-miniport-driver-routines.md).

For an overview and definition of the individual SRB functions, SRB flags, and SRB status values, see [**SCSI_REQUEST_BLOCK**](/windows-hardware/drivers/ddi/srb/ns-srb-_scsi_request_block).

For discussions about how miniport drivers must respond to each individual SRB function, see [**HwStorStartIo**](/windows-hardware/drivers/ddi/storport/nc-storport-hw_startio).

Storport forwards SRBs to Storport miniport drivers for asynchronous processing. Typically, the miniport driver will take some time to actually complete the request. Host bus adapters (HBAs) that support tagged queuing can queue requests internally and process them in the order that is indicated by the tags that Storport assigns to each request. The [**SCSI_REQUEST_BLOCK**](/windows-hardware/drivers/ddi/storport/nc-storport-hw_startio) (SRB) structure contains two members that the Storport and miniport drivers use to specify how SRBs should be ordered in the host adapter's internal queue:

* **QueueTag**: Storport assigns a count, or *"tag"* value, to the **QueuedTag** member of each SRB. This tag indicates the order in which the adapter should process the packets. The tag values also allow Storport to track which SRBs are still outstanding, which have completed successfully, and which have timed out.

* **QueueAction**: indicates the tagged-queueing message to be used when the SRB_FLAGS_QUEUE_ACTION_ENABLE flag is set in **SRB.SrbFlags**. The miniport's use of **QueueAction** is miniport-specific. SCSI-based miniports can follow the SCSI specification if the HBA supports it. **QueueAction** can be one of the following values:

| Value | Meaning |
| ----- | ------- |
| SRB_SIMPLE_TAG_REQUEST | Queue the request and execute it in any order once all older SRB_HEAD_OF_QUEUE_TAG_REQUEST and SRB_ORDERED_QUEUE_TAG_REQUEST requests have ended. |
| SRB_ORDERED_QUEUE_TAG_REQUEST | Execute the request only after all older SRB_HEAD_OF_QUEUE_TAG_REQUEST and all older requests have been completed. |
| SRB_HEAD_OF_QUEUE_TAG_REQUEST | Place the request at the front of the queue, and execute it ahead of all other requests in the queue, including all other SRB_HEAD_OF_QUEUE_TAG_REQUEST-tagged requests. |

See the SCSI specification for details.
