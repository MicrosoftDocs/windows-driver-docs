---
title: KSINTERFACE_STANDARD_STREAMING
description: The KSINTERFACE_STANDARD_STREAMING interface is used between most KS audio filters and is supported by all audio miniports.
keywords: ["KSINTERFACE_STANDARD_STREAMING Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSINTERFACE_STANDARD_STREAMING
api_type:
- NA
ms.date: 10/12/2021
---

# KSINTERFACE_STANDARD_STREAMING

The KSINTERFACE_STANDARD_STREAMING interface is used between most KS audio filters and is supported by all audio miniports.

If a pin supports this interface, the relevant filter processes the data embedded in each [**KSSTREAM_HEADER**](/windows-hardware/drivers/ddi/ks/ns-ks-ksstream_header) structure once.

## See also

[KSINTERFACESETID_Standard](ksinterfacesetid-standard.md)

[**KSPIN_INTERFACE**](./kspin-interface-structure.md)

[**KSPIN_DESCRIPTOR**](/windows-hardware/drivers/ddi/ks/ns-ks-kspin_descriptor)

[**KSSTREAM_HEADER**](/windows-hardware/drivers/ddi/ks/ns-ks-ksstream_header)
