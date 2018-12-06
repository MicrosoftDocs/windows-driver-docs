---
title: Storport's Interface with Storport Miniport Drivers
description: Storport's Interface with Storport Miniport Drivers
ms.assetid: 8e09d6a6-7e4f-44fc-a2b0-5f21b4ac0593
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Storport's Interface with Storport Miniport Drivers


Communication between the Storport driver and the Storport miniport drivers takes place by means of SCSI request blocks (SRBs) and miniport driver callback routines. For a detailed discussion of the Storport miniport driver callback routines, see [Storport Driver Miniport Routines](https://msdn.microsoft.com/library/windows/hardware/ff567543).

For an overview and definition of the individual SRB functions, SRB flags, and SRB status values, see [**SCSI\_REQUEST\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff565393).

For discussions about how miniport drivers must respond to each individual SRB function, see [**HwStorStartIo**](https://msdn.microsoft.com/library/windows/hardware/ff557423).

Storport forwards SRBs to Storport miniport drivers for asynchronous processing. Typically, the miniport driver will take some time to actually complete the request. Host bus adapters that support tagged queuing can queue requests internally and process them in the order that is indicated by the tags that Storport assigns to each request. The [**SCSI\_REQUEST\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff565393) (SRB) structure contains two members that the Storport driver uses to specify how SRBs should be ordered in the host adapter's internal queue: **QueuedTag** and **QueueAction**. Storport assigns a count, or *"tag"* value, to the **QueuedTag** member of each SRB that indicates the order in which the adapter should process the packets. The tag values also allow Storport to track which SRBs have completed successfully and which SRBs have timed out.

The **QueueAction** member is assigned one of the following values:

SRB\_SIMPLE\_TAG\_REQUEST

SRB\_HEAD\_OF\_QUEUE\_TAG\_REQUEST

SRB\_ORDERED\_QUEUE\_TAG\_REQUEST

For an explanation of these values, see the SCSI-3 specification.

 

 




