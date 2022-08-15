---
title: KSPROPERTY_DISPLAY_ADAPTER_GUID
description: The KSPROPERTY_DISPLAY_ADAPTER_GUID property returns the adapter GUID from the capture minidriver.To use VRAM transport, a capture minidriver must support this property.
keywords: ["KSPROPERTY_DISPLAY_ADAPTER_GUID Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_DISPLAY_ADAPTER_GUID
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 10/19/2021
---

# KSPROPERTY_DISPLAY_ADAPTER_GUID

The **KSPROPERTY_DISPLAY_ADAPTER_GUID** property returns the adapter GUID from the capture minidriver.

To use VRAM transport, a capture minidriver must support this property.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | No | Pin | [**KSPROPERTY**](./ksproperty-structure.md) | GUID |

## Return value

A **KSPROPERTY_DISPLAY_ADAPTER_GUID** property returns **STATUS_SUCCESS** to indicate that it has completed successfully. If the Property Type Value is incorrect, it returns **STATUS_INVALID_PARAMETER**.

## Remarks

The minidriver should return the adapter identifier of the first head on the GPU.

The capture GUID uniquely identifies a VRAM subsystem with which the capture device is compatible. The system-supplied kernel-streaming (KS) proxy module (KsProxy) uses this GUID to allocate surfaces on a compatible VRAM subsystem.

AVStream matches this GUID with the GUID of the downstream render pin to verify that both capture and render pins are on the same graphics adapter.

## Requirements

**Header:** ksmedia.h (include Ksmedia.h)

## See also

[**KSPROPERTY**](ksproperty-structure.md)