---
title: KSPROPERTY_DVDCOPY_DVD_KEY1
description: The KSPROPERTY_DVDCOPY_DVD_KEY1 property retrieves the first bus key that is provided later to the decoder as part of the DVD copyright protection authentication process.
keywords: ["KSPROPERTY_DVDCOPY_DVD_KEY1 Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_DVDCOPY_DVD_KEY1
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 10/19/2021
---

# KSPROPERTY_DVDCOPY_DVD_KEY1

The **KSPROPERTY_DVDCOPY_DVD_KEY1** property retrieves the first bus key that is provided later to the decoder as part of the DVD copyright protection authentication process.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| No | Yes | Pin | [**KSPROPERTY**](/windows-hardware/drivers/stream/ksproperty-structure) | [**KS_DVDCOPY_BUSKEY**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_ks_dvdcopy_buskey) |

The property value (operation data) is a KS_DVDCOPY_BUSKEY structure that describes the DVD decoders first bus key.

## Remarks

For more information about the first bus key, see [DVD Copyright Protection](dvd-copyright-protection.md).

## Requirements

**Header:** ksmedia.h (include Ksmedia.h)

## See also

[**KS_DVDCOPY_BUSKEY**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_ks_dvdcopy_buskey)
