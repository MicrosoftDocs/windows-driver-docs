---
title: KSPROPERTY_DVDCOPY_CHLG_KEY
description: The KSPROPERTY_DVDCOPY_CHLG_KEY property transfers the bus challenge keys that the DVD decoder and DVD drive provide.
keywords: ["KSPROPERTY_DVDCOPY_CHLG_KEY Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_DVDCOPY_CHLG_KEY
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 10/19/2021
---

# KSPROPERTY_DVDCOPY_CHLG_KEY

The **KSPROPERTY_DVDCOPY_CHLG_KEY** property transfers the bus challenge keys that the DVD decoder and DVD drive provide.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | Yes | Pin | [**KSPROPERTY**](./ksproperty-structure.md) | [**KS_DVDCOPY_CHLGKEY**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_ks_dvdcopy_chlgkey) |

The property value (operation data) is a KS_DVDCOPY_CHLGKEY structure that describes the bus challenge key.

## Remarks

For **Get** requests, the DVD decoder provides its bus challenge key. For **Set** requests, the DVD decoder is provided the bus challenge key from the DVD drive.

For more information about the bus challenge key, see [DVD Copyright Protection](dvd-copyright-protection.md).

## Requirements

**Header:** ksmedia.h (include Ksmedia.h)

## See also

[**KS_DVDCOPY_CHLGKEY**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_ks_dvdcopy_chlgkey)