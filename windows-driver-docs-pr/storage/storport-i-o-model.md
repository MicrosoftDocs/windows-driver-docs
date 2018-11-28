---
title: Storport I/O Model
description: Storport I/O Model
ms.assetid: 9220b01e-725f-4a03-87f1-402c0686cccd
keywords:
- Storport drivers WDK , I/O
- I/O WDK Storport
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Storport I/O Model


## <span id="ddk_storport_i_o_model_kg"></span><span id="DDK_STORPORT_I_O_MODEL_KG"></span>


This section describes the Storport driver's I/O model and contrasts this model with that of the SCSI Port driver. The Storport I/O model consists of several features designed to make maximum use of the performance potential of high-speed buses and storage devices.

The Storport driver uses a push model of I/O. This means that the driver forwards I/O requests asynchronously to its miniport driver, up to a maximum number of overlapping packets, without waiting for the miniport driver to request input. In the push model, the port driver controls the flow of the I/O requests and pushes requests down to the miniport driver.

On the other hand, the SCSI port driver uses a pull model of I/O. In a pull model of I/O, the SCSI port driver forwards I/O requests to its miniport driver synchronously and waits for the miniport driver to request new input before it sends the next I/O request. Additionally, the miniport driver controls the flow of I/O requests and pulls the requests down from the port driver.

For more information about the I/O model of the SCSI port driver, see [SCSI Port I/O Model](scsi-port-i-o-model.md).

The topics covered in this section are as follows:

[Full-Duplex Mode](full-duplex-mode.md)

[Half-Duplex Mode: Not Appropriate for Shipped Products](half-duplex-mode--not-appropriate-for-shipped-products.md)

[Unsynchronized HwStorBuildIo Routine](unsynchronized-hwstorbuildio-routine.md)

[Synchronized Access within Unsynchronized Miniport Driver Routines](synchronized-access-within-unsynchronized-miniport-driver-routines.md)

[Access to Scatter/Gather Lists in the Storport I/O Model](access-to-scatter-gather-lists-in-the-storport-i-o-model.md)

[Use of Mapping Buffers in the Storport I/O Model](use-of-mapping-buffers-in-the-storport-i-o-model.md)

[Performance Tip: Completing Requests During HwStartIo](performance-tip--completing-requests-during-hwstartio.md)

[Pre- and Post-Processing of CDBs and Sense Codes](pre--and-post-processing-of-cdbs-and-sense-codes.md)

 

 




