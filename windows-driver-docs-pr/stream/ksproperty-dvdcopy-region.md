---
title: KSPROPERTY_DVDCOPY_REGION
description: The KSPROPERTY_DVDCOPY_REGION property specifies the DVD copy-protection region according to language restrictions.
keywords: ["KSPROPERTY_DVDCOPY_REGION Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_DVDCOPY_REGION
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 10/19/2021
---

# KSPROPERTY_DVDCOPY_REGION

The **KSPROPERTY_DVDCOPY_REGION** property specifies the DVD copy-protection region according to language restrictions.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | No | Pin | [**KSPROPERTY**](./ksproperty-structure.md) | [**KS_DVDCOPY_REGION**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_ks_dvdcopy_region) |

The property value (operation data) is a KS_DVDCOPY_REGION structure that describes the region code for the nationality or language.

## Remarks

For more information about language restrictions, see [DVD Regionalization](dvd-regionalization.md) and [DVD Copyright Protection](dvd-copyright-protection.md).

## Requirements

**Header:** ksmedia.h (include Ksmedia.h)

## See also

[**KS_DVDCOPY_REGION**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_ks_dvdcopy_region)