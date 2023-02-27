---
title: KSPROPERTY_EXTXPORT_MEDIUM_INFO
description: The KSPROPERTY_EXTXPORT_MEDIUM_INFO property retrieves information about an external device's medium.
keywords: ["KSPROPERTY_EXTXPORT_MEDIUM_INFO Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_EXTXPORT_MEDIUM_INFO
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 10/20/2021
---

# KSPROPERTY_EXTXPORT_MEDIUM_INFO

The **KSPROPERTY_EXTXPORT_MEDIUM_INFO** property retrieves information about an external device's medium.

## Usage Summary Table

| Get | Set | Target | Property descriptor type      | Property value type |
|-----|-----|--------|-------------------------------|---------------------|
| Yes | No  | Device | [**KSPROPERTY_EXTXPORT_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_extxport_s) | [**MEDIUM_INFO**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-medium_info) |

The property value (operation data) is a **MEDIUM_INFO** structure that describes the media loaded into the external device. For example cassette tape, tape grade and write protection.

## Remarks

The **MediumInfo** member of the **KSPROPERTY_EXTXPORT_S** structure specifies the information.

## Requirements

**Header:** ksmedia.h (include Ksmedia.h)

## See also

[**KSPROPERTY**](ksproperty-structure.md)

[**KSPROPERTY_EXTXPORT_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_extxport_s)

[**MEDIUM_INFO**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-medium_info)
