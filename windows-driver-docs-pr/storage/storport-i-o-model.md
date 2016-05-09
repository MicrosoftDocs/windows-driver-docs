---
title: Storport I/O Model
author: windows-driver-content
description: Storport I/O Model
ms.assetid: 9220b01e-725f-4a03-87f1-402c0686cccd
keywords: ["Storport drivers WDK , I/O", "I/O WDK Storport"]
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Storport%20I/O%20Model%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


