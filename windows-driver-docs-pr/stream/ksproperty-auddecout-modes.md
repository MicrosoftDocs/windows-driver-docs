---
title: KSPROPERTY_AUDDECOUT_MODES
description: The KSPROPERTY_AUDDECOUT_MODES property returns the available output modes of the audio decoder.This property is read-only.
keywords: ["KSPROPERTY_AUDDECOUT_MODES Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_AUDDECOUT_MODES
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 10/13/2021
ms.localizationpriority: medium
---

# KSPROPERTY_AUDDECOUT_MODES

The KSPROPERTY_AUDDECOUT_MODES property returns the available output modes of the audio decoder.

This property is read-only.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | No | Pin | [**KSPROPERTY**](/windows-hardware/drivers/stream/ksproperty-structure) | DWORD |

The property value (operation data) is a DWORD that represents a bitmask of the audio output modes that the audio decoder supports.

## Remarks

The property value can contain a bitwise OR of the following constants that are defined in the *Ksmedia.h* header file:

**KSAUDDECOUTMODE_STEREO_ANALOG**  
Indicates that the output is in analog stereo.

**KSAUDDECOUTMODE_PCM_51**  
Indicates that the output is in PCM 5.1 channel digital.

**KSAUDDECOUTMODE_SPDIFF**  
Indicates that the output is SPDIFF format AC3 digital.

## Requirements

**Header:** ksmedia.h (include Ksmedia.h)

## See also

[**KSPROPERTY_AUDDECOUT_CUR_MODE**](ksproperty-auddecout-cur-mode.md)
