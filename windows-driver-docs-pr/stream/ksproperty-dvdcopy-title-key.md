---
title: KSPROPERTY_DVDCOPY_TITLE_KEY
description: The KSPROPERTY_DVDCOPY_TITLE_KEY property retrieves the title key information from the current content for the DVD copyright protection authentication process.
keywords: ["KSPROPERTY_DVDCOPY_TITLE_KEY Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_DVDCOPY_TITLE_KEY
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 10/19/2021
---

# KSPROPERTY_DVDCOPY_TITLE_KEY

The **KSPROPERTY_DVDCOPY_TITLE_KEY** property retrieves the title key information from the current content for the DVD copyright protection authentication process.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| No | Yes | Pin | [**KSPROPERTY**](/windows-hardware/drivers/stream/ksproperty-structure) | [**KS_DVDCOPY_TITLEKEY**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_ks_dvdcopy_titlekey) |

The property value (operation data) is a **KS_DVDCOPY_TITLEKEY** structure that describes the current title key.

## Remarks

For more information about the title key, see [DVD Copyright Protection](dvd-copyright-protection.md).

## Requirements

**Header:** ksmedia.h (include Ksmedia.h)

## See also

[**KS_DVDCOPY_TITLEKEY**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_ks_dvdcopy_titlekey)
