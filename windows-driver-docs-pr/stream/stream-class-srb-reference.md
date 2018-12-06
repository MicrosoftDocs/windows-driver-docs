---
title: Stream Class SRB Reference
description: Stream Class SRB Reference
ms.assetid: fdd2de58-8825-429a-937a-0bd27a180f2a
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Stream Class SRB Reference


## <span id="ddk_stream_class_srb_reference_ks"></span><span id="DDK_STREAM_CLASS_SRB_REFERENCE_KS"></span>


The class driver uses the [**HW\_STREAM\_REQUEST\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff559702) structure to pass SRB requests to the minidriver. In this reference section, pSRB refers to a pointer to a HW\_STREAM\_REQUEST\_BLOCK object. The stream class driver passes this pointer when it calls minidriver-provided callbacks.

SRB requests are either device/instance-specific or stream-specific. Depending on the SRB command, additional parameters may be passed in the HW\_STREAM\_REQUEST\_BLOCK.

See [Device-Specific Command Codes](device-specific-command-codes.md) and [Stream-Specific Command Codes](stream-specific-command-codes.md).

 

 





