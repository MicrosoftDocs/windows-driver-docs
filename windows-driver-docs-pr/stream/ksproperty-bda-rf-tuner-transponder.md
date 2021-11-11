---
title: KSPROPERTY_BDA_RF_TUNER_TRANSPONDER
description: Clients use KSPROPERTY_BDA_RF_TUNER_TRANSPONDER to inform the tuner node of the appropriate transponder number.
keywords: ["KSPROPERTY_BDA_RF_TUNER_TRANSPONDER Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_BDA_RF_TUNER_TRANSPONDER
api_location:
- Bdamedia.h
api_type:
- HeaderDef
ms.date: 10/14/2021
ms.localizationpriority: medium
---

# KSPROPERTY_BDA_RF_TUNER_TRANSPONDER

Clients use **KSPROPERTY_BDA_RF_TUNER_TRANSPONDER** to inform the tuner node of the appropriate transponder number.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | Yes | Filter | [**KSP_NODE**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_node) | ULONG |

## Remarks

The **NodeId** member of KSP_NODE specifies the identifier of the tuner node.

The property value specifies the transponder number to set.

Some tuning spaces have all of the information about how to acquire a frequency imbedded in hardware. These tuning spaces specify a transponder number. This property informs the tuner node of this transponder number. The tuner hardware can then automatically determine the tuning characteristics needed to acquire the intermediate frequency. In this case, the other properties in the **KSPROPSETID_BdaFrequencyFilter** property set are set to −1.

## Requirements

**Header:** bdamedia.h (include Bdamedia.h)

## See also

[**KSP_NODE**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_node)
