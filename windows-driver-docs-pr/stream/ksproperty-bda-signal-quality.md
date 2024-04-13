---
title: KSPROPERTY_BDA_SIGNAL_QUALITY
description: Clients use KSPROPERTY_BDA_SIGNAL_QUALITY to determine the amount of data successfully extracted from the signal as a percent.
keywords: ["KSPROPERTY_BDA_SIGNAL_QUALITY Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_BDA_SIGNAL_QUALITY
api_location:
- Bdamedia.h
api_type:
- HeaderDef
ms.date: 10/14/2021
---

# KSPROPERTY_BDA_SIGNAL_QUALITY

Clients use **KSPROPERTY_BDA_SIGNAL_QUALITY** to determine the amount of data successfully extracted from the signal as a percent.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | Yes | Pin or Filter | [**KSP_NODE**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_node) | LONG |

## Remarks

The **NodeId** member of **KSP_NODE** specifies the identifier of the control node or is set to −1 to specify a pin.

The returned value specifies the data that is extracted from the signal as a percent.

The demodulation node typically reports signal quality, which is a representation of how much of the original data could be extracted from the signal.

In the case of analog signals, this percentage can be computed by examining the timing of horizontal sync (HSync) and vertical sync (VSync) as well as by looking at information contained in horizontal-blanking (HBlanking) and vertical-blanking (VBlanking) intervals.

In the case of digital signals, this percentage can be computed by examining packet cyclic redundancy checks (CRC) and forward error correction (FEC) confidence values as follows:

- 100 percent is ideal.

- 95 percent shows very little (almost unnoticeable) artifacts when rendered.

- 90 percent contains few enough artifacts as to be easily viewable.

- 80 percent is the minimum level to be viewable.

- 60 percent is the minimum level to expect data services, including receiving an electronic program guide (EPG), to work.

- 20 percent indicates that the demodulator is aware that a properly modulated signal exists but cannot produce enough data to be useful.

## Requirements

**Header:** bdamedia.h (include Bdamedia.h)

## See also

[**KSP_NODE**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_node)
