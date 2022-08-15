---
title: KSPROPERTY_BDA_GUARD_INTERVAL
description: Clients use KSPROPERTY_BDA_GUARD_INTERVAL to control the setting for guard interval of a demodulator node.
keywords: ["KSPROPERTY_BDA_GUARD_INTERVAL Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_BDA_GUARD_INTERVAL
api_location:
- Bdamedia.h
api_type:
- HeaderDef
ms.date: 10/13/2021
---

# KSPROPERTY_BDA_GUARD_INTERVAL

Clients use **KSPROPERTY_BDA_GUARD_INTERVAL** to control the setting for guard interval of a demodulator node.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | Yes | Filter | KSP_NODE | GuardInterval |

## Remarks

The returned value from the GuardInterval enumerated type identifies a setting for guard interval.

The **NodeId** member of KSP_NODE specifies the identifier of the demodulator node.

## Requirements

**Header:** bdamedia.h (include Bdamedia.h)

## See also

[**GuardInterval**](/previous-versions/windows/desktop/mstv/guardinterval)

[**KSP_NODE**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_node)
