---
title: KSPROPERTY_BDA_SAMPLE_TIME
description: Clients use KSPROPERTY_BDA_SAMPLE_TIME to determine the sample time over which signal level and quality are averaged.
keywords: ["KSPROPERTY_BDA_SAMPLE_TIME Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_BDA_SAMPLE_TIME
api_location:
- Bdamedia.h
api_type:
- HeaderDef
ms.date: 10/14/2021
---

# KSPROPERTY_BDA_SAMPLE_TIME

Clients use **KSPROPERTY_BDA_SAMPLE_TIME** to determine the sample time over which signal level and quality are averaged.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | Yes | Pin or Filter | [**KSP_NODE**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_node) | LONG |

## Remarks

The **NodeId** member of **KSP_NODE** specifies the identifier of the control node or is set to −1 to specify a pin.

The returned value specifies the sample time in milliseconds.

Each time a client requests a signal statistics property, the node should report the average value for the last n milliseconds where n is the value indicated by **KSPROPERTY_BDA_SAMPLE_TIME**. If no time value is set or if the driver does not support **KSPROPERTY_BDA_SAMPLE_TIME**, the driver should default to a sample time of 100 milliseconds.

The driver can report time values for the most recently completed sample period.

## Requirements

**Header:** bdamedia.h (include Bdamedia.h)

## See also

[**KSP_NODE**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_node)

[**KSPROPERTY_BDA_SIGNAL_QUALITY**](ksproperty-bda-signal-quality.md)

[**KSPROPERTY_BDA_SIGNAL_STRENGTH**](ksproperty-bda-signal-strength.md)
