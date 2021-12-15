---
title: KSPROPERTY_CROSSBAR_PININFO
description: The KSPROPERTY_CROSSBAR_PININFO property retrieves the type of physical connection represented by the pin including settings such as data flow direction, medium GUID(s) and pin-type.
keywords: ["KSPROPERTY_CROSSBAR_PININFO Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CROSSBAR_PININFO
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 10/18/2021
---

# KSPROPERTY_CROSSBAR_PININFO

The **KSPROPERTY_CROSSBAR_PININFO** property retrieves the type of physical connection represented by the pin including settings such as data flow direction, medium GUID(s) and pin-type. For video pins this property also indicates if there is an audio pin associated with a particular video pin. This property must be implemented.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | No | Filter | [**KSPROPERTY_CROSSBAR_PININFO_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_crossbar_pininfo_s) | [**KSPROPERTY_CROSSBAR_PININFO_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_crossbar_pininfo_s) |

The property value (operation data) is a **KSPROPERTY_CROSSBAR_PININFO_S** structure.

## Requirements

**Header:** ksmedia.h (include Ksmedia.h)

## See also

[**KSPROPERTY**](ksproperty-structure.md)

[**KSPROPERTY_CROSSBAR_PININFO_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_crossbar_pininfo_s)
