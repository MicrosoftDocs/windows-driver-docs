---
title: KSINTERFACE\_STANDARD\_STREAMING
description: KSINTERFACE\_STANDARD\_STREAMING
keywords: ["KSINTERFACE_STANDARD_STREAMING Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSINTERFACE_STANDARD_STREAMING
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSINTERFACE\_STANDARD\_STREAMING


## <span id="ddk_ksinterface_standard_streaming_ks"></span><span id="DDK_KSINTERFACE_STANDARD_STREAMING_KS"></span>


The KSINTERFACE\_STANDARD\_STREAMING interface is used between most KS audio filters and is supported by all audio miniports. If a pin supports this interface, the relevant filter processes the data embedded in each [**KSSTREAM\_HEADER**](/windows-hardware/drivers/ddi/ks/ns-ks-ksstream_header) structure once.

### See Also

[KSINTERFACESETID\_Standard](ksinterfacesetid-standard.md), [**KSPIN\_INTERFACE**](./kspin-interface-structure.md), [**KSPIN\_DESCRIPTOR**](/windows-hardware/drivers/ddi/ks/ns-ks-kspin_descriptor), [**KSSTREAM\_HEADER**](/windows-hardware/drivers/ddi/ks/ns-ks-ksstream_header)

