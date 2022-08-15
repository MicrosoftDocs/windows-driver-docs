---
title: KSPROPERTY_DVDCOPY_DISC_KEY
description: The KSPROPERTY_DVDCOPY_DISC_KEY property retrieves the disc key information for the DVD copyright protection authentication process.
keywords: ["KSPROPERTY_DVDCOPY_DISC_KEY Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_DVDCOPY_DISC_KEY
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 10/19/2021
---

# KSPROPERTY_DVDCOPY_DISC_KEY

The **KSPROPERTY_DVDCOPY_DISC_KEY** property retrieves the disc key information for the DVD copyright protection authentication process.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| No | Yes | Pin | [**KSPROPERTY**](./ksproperty-structure.md) | [**KS_DVDCOPY_DISCKEY**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_ks_dvdcopy_disckey) |

The property value (operation data) is a **KS_DVDCOPY_DISCKEY** structure that describes the DVD's disc key.

## Remarks

For more information about the disc key, see [DVD Copyright Protection](dvd-copyright-protection.md).

## Requirements

**Header:** ksmedia.h (include Ksmedia.h)

## See also

[**KS_DVDCOPY_DISCKEY**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_ks_dvdcopy_disckey)