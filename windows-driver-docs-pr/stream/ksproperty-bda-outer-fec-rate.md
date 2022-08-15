---
title: KSPROPERTY_BDA_OUTER_FEC_RATE
description: Clients use KSPROPERTY_BDA_OUTER_FEC_RATE to control the binary convolution scheme used for the outer forward error correction (FEC) type of a demodulator node.
keywords: ["KSPROPERTY_BDA_OUTER_FEC_RATE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_BDA_OUTER_FEC_RATE
api_location:
- Bdamedia.h
api_type:
- HeaderDef
ms.date: 10/13/2021
---

# KSPROPERTY_BDA_OUTER_FEC_RATE

Clients use **KSPROPERTY_BDA_OUTER_FEC_RATE** to control the binary convolution scheme used for the outer forward error correction (FEC) type of a demodulator node.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | Yes | Filter | [**KSP_NODE**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_node) | [**BinaryConvolutionCodeRate**](/previous-versions/windows/desktop/mstv/binaryconvolutioncoderate) |

## Remarks

The returned value from the BinaryConvolutionCodeRate enumerated type identifies a binary convolution scheme.

The **NodeId** member of **KSP_NODE** specifies the identifier of the demodulator node.

## Requirements

**Header:** bdamedia.h (include Bdamedia.h)

## See also

[**BinaryConvolutionCodeRate**](/previous-versions/windows/desktop/mstv/binaryconvolutioncoderate)

[**KSP_NODE**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_node)
