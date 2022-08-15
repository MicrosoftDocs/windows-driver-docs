---
title: KSPROPERTY_BDA_SPECTRAL_INVERSION
description: Clients use KSPROPERTY_BDA_SPECTRAL_INVERSION to control the setting for spectral inversion of a demodulator node.
keywords: ["KSPROPERTY_BDA_SPECTRAL_INVERSION Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_BDA_SPECTRAL_INVERSION
api_location:
- Bdamedia.h
api_type:
- HeaderDef
ms.date: 10/14/2021
---

# KSPROPERTY_BDA_SPECTRAL_INVERSION

Clients use **KSPROPERTY_BDA_SPECTRAL_INVERSION** to control the setting for spectral inversion of a demodulator node.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | Yes | Filter | [**KSP_NODE**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_node) | SpectralInversion |

## Remarks

The returned value from the SpectralInversion enumerated type identifies a setting for spectral inversion.

The **NodeId** member of **KSP_NODE** specifies the identifier of the demodulator node.

## Requirements

**Header:** bdamedia.h (include Bdamedia.h)

## See also

[**KSP_NODE**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_node)

[**SpectralInversion**](/previous-versions/windows/hardware/drivers/ff568154(v=vs.85))
