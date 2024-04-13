---
title: KSINTERFACE_STANDARD_LOOPED_STREAMING
description: The KSINTERFACE_STANDARD_LOOPED_STREAMING interface is used by clients of DSound.
keywords: ["KSINTERFACE_STANDARD_LOOPED_STREAMING Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSINTERFACE_STANDARD_LOOPED_STREAMING
api_type:
- NA
ms.date: 10/12/2021
---

# KSINTERFACE_STANDARD_LOOPED_STREAMING

The **KSINTERFACE_STANDARD_LOOPED_STREAMING** interface is used by clients of DSound. At release time of Windows XP, Kmixer and Portcls are the only KS Audio filters that support this interface.

If a pin supports KSINTERFACE_STANDARD_LOOPED_STREAMING, the relevant filter does not complete buffers until the pin is placed into the *Stop* state. The filter processes data by continuously looping around the data in the single buffer submitted to the filter.

## See also

[KSINTERFACESETID_Standard](ksinterfacesetid-standard.md)

[**KSPIN_INTERFACE**](./kspin-interface-structure.md)

[**KSPIN_DESCRIPTOR**](/windows-hardware/drivers/ddi/ks/ns-ks-kspin_descriptor)
