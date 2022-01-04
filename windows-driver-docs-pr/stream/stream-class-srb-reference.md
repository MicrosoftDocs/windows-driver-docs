---
title: Stream Class SRB Reference
description: Stream Class SRB Reference
ms.date: 11/28/2017
---

# Stream Class SRB Reference


## <span id="ddk_stream_class_srb_reference_ks"></span><span id="DDK_STREAM_CLASS_SRB_REFERENCE_KS"></span>


The class driver uses the [**HW\_STREAM\_REQUEST\_BLOCK**](/windows-hardware/drivers/ddi/strmini/ns-strmini-_hw_stream_request_block) structure to pass SRB requests to the minidriver. In this reference section, pSRB refers to a pointer to a HW\_STREAM\_REQUEST\_BLOCK object. The stream class driver passes this pointer when it calls minidriver-provided callbacks.

SRB requests are either device/instance-specific or stream-specific. Depending on the SRB command, additional parameters may be passed in the HW\_STREAM\_REQUEST\_BLOCK.

See [Device-Specific Command Codes](device-specific-command-codes.md) and [Stream-Specific Command Codes](stream-specific-command-codes.md).

 

