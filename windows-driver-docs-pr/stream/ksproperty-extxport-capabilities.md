---
title: KSPROPERTY_EXTXPORT_CAPABILITIES
description: The KSPROPERTY_EXTXPORT_CAPABILITIES property retrieves an external device's transport-specific capabilities.
keywords: ["KSPROPERTY_EXTXPORT_CAPABILITIES Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_EXTXPORT_CAPABILITIES
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 10/20/2021
ms.localizationpriority: medium
---

# KSPROPERTY_EXTXPORT_CAPABILITIES

The **KSPROPERTY_EXTXPORT_CAPABILITIES** property retrieves an external device's transport-specific capabilities.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | No | Device | [**KSPROPERTY_EXTXPORT_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_extxport_s) | ULONG |

The property value (operation data) is a ULONG that specifies the capabilities of the external transport.

## Remarks

The **Capabilities** member of the **KSPROPERTY_EXTXPORT_S** structure describes transport-specific capabilities.

## Requirements

**Header:** ksmedia.h (include Ksmedia.h)

## See also

[**KSPROPERTY**](ksproperty-structure.md)

[**KSPROPERTY_EXTXPORT_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_extxport_s)
