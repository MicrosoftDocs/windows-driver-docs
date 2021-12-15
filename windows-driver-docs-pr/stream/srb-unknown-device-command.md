---
title: SRB\_UNKNOWN\_DEVICE\_COMMAND
description: SRB\_UNKNOWN\_DEVICE\_COMMAND
ms.date: 11/28/2017
---

# SRB\_UNKNOWN\_DEVICE\_COMMAND


## <span id="ddk_srb_unknown_device_command_ks"></span><span id="DDK_SRB_UNKNOWN_DEVICE_COMMAND_KS"></span>


The class driver sends this request to pass IRPs that it does not know how to handle to the minidriver. *pSrb*-&gt;**Irp** points to the unhandled IRP. See [**HW\_STREAM\_REQUEST\_BLOCK**](/windows-hardware/drivers/ddi/strmini/ns-strmini-_hw_stream_request_block).

This request can be used as an IRP pass-through mechanism for IRPs that the stream class does not understand, but that the minidriver might. For example, there are several Plug and Play (PnP) IRPs that the stream class does not process, but that a 1394 camera driver does.

If the minidriver does not support SRB\_UNKNOWN\_DEVICE\_COMMAND or does not handle the IRP, it should set pSRB-&gt;Status to STATUS\_NOT\_IMPLEMENTED.

 

