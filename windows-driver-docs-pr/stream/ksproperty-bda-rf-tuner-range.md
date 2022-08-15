---
title: KSPROPERTY_BDA_RF_TUNER_RANGE
description: Clients use KSPROPERTY_BDA_RF_TUNER_RANGE to control the tuner range, that is, the domain on which to find a particular carrier frequency.
keywords: ["KSPROPERTY_BDA_RF_TUNER_RANGE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_BDA_RF_TUNER_RANGE
api_location:
- Bdamedia.h
api_type:
- HeaderDef
ms.date: 10/14/2021
---

# KSPROPERTY_BDA_RF_TUNER_RANGE

Clients use **KSPROPERTY_BDA_RF_TUNER_RANGE** to control the tuner range, that is, the domain on which to find a particular carrier frequency.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | Yes | Filter | [**KSP_NODE**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_node) | ULONG |

## Remarks

The **NodeId** member of **KSP_NODE** specifies the identifier of the tuner node.

The property value specifies the tuner range to set.

Specifying the **KSPROPERTY_BDA_RF_TUNER_RANGE** property with:

- **BDA_RANGE_NOT_SET** (−1) indicates that the tuner range is not set.

- **BDA_RANGE_NOT_DEFINED** (0) indicates that the tuner range is not defined.

Some tuners control an external device, such as a multiswitch, that defines the domain on which to find a particular carrier frequency. This property sets the tuner range either to −1, meaning that tuner range is not used for the particular tuning space, or to a value that is specific to the tuning space.

## Requirements

**Header:** bdamedia.h (include Bdamedia.h)

## See also

[**KSP_NODE**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_node)
