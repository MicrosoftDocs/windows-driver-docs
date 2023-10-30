---
title: KSPROPERTY_AUDDECOUT_CUR_MODE
description: The KSPROPERTY_AUDDECOUT_CUR_MODE property indicates the current audio output mode.
keywords: ["KSPROPERTY_AUDDECOUT_CUR_MODE Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_AUDDECOUT_CUR_MODE
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 10/13/2021
---

# KSPROPERTY_AUDDECOUT_CUR_MODE

The KSPROPERTY_AUDDECOUT_CUR_MODE property indicates the current audio output mode.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | Yes | Pin | [**KSPROPERTY**](./ksproperty-structure.md) | DWORD |

The property value (operation data) is a DWORD that represents the current output mode of the audio decoder.

## Remarks

The property value can be one of the following mode constants defined in the header file *ksmedia.h*:

**KSAUDDECOUTMODE_STEREO_ANALOG**  
Indicates that the output is in analog stereo.

**KSAUDDECOUTMODE_PCM_51**  
Indicates that the output is in PCM 5.1 channel digital.

**KSAUDDECOUTMODE_SPDIFF**  
Indicates that the output is SPDIFF format AC3 digital.

The audio miniport driver get-property handler returns the current mode of the decoder, whereas the audio miniport driver set-property handler requests that the decoder switch the output audio format to the requested mode.

We recommend that you specify a default value for the KSPROPERTY_AUDDECOUT_CUR_MODE property in the minidriver's serialized property set in the registry.

For more information, see [Audio Miniport Drivers](../audio/audio-miniport-drivers.md).

## Requirements

**Header:** ksmedia.h (include Ksmedia.h)

## See also

[**KSPROPERTY_AUDDECOUT_MODES**](ksproperty-auddecout-modes.md)