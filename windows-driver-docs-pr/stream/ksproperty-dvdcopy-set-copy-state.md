---
title: KSPROPERTY_DVDCOPY_SET_COPY_STATE
description: The KSPROPERTY_DVDCOPY_SET_COPY_STATE property sets the copy state of the DVD decoder stream. This property is optional to implement.
keywords: ["KSPROPERTY_DVDCOPY_SET_COPY_STATE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_DVDCOPY_SET_COPY_STATE
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 10/19/2021
---

# KSPROPERTY_DVDCOPY_SET_COPY_STATE

The **KSPROPERTY_DVDCOPY_SET_COPY_STATE** property sets the copy state of the DVD decoder stream. This property is optional to implement.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | Yes | Pin | [**KSPROPERTY**](./ksproperty-structure.md) | [**KS_DVDCOPY_SET_COPY_STATE**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_ks_dvdcopy_set_copy_state) |

The property value (operation data) is a KS_DVDCOPY_SET_COPY_STATE structure that describes the copyright protection state of the DVD decoder stream.

## Remarks

This property indicates whether this pin requires CSS authentication. If the property is not implemented, the default is assumed to be the **KS_DVDCOPYSTATE_AUTHENTICATION_REQUIRED** value from the [**KS_DVDCOPYSTATE**](/windows-hardware/drivers/ddi/ksmedia/ne-ksmedia-ks_dvdcopystate) enumeration.

The main use for this property is for a decoder that supports multiple pins with the same decrypter. For example, if one filter provides both subpicture and video decoding, the keys only need to be exchanged for one of the two pins. If a filter is going to return **KS_DVDCOPYSTATE_AUTHENTICATION_NOT_REQUIRED** on one of the pins, then it must always return **KS_DVDCOPYSTATE_AUTHENTICATION_REQUIRED** on the first pin that the property is issued on.

When this property is issued as a **Get** call, the filter can respond with either **KS_DVDCOPYSTATE_AUTHENTICATION_REQUIRED** or KS_DVDCOPYSTATE_AUTHENTICATION_NOT_REQUIRED.

When this property is issued as a **Set** call, this is an informational call used by hardware decoders to indicate what phase of the copyright protection negotiation is being entered. The decoder can hold off the SET_STATE with one of the following until the correct bits, indicating that a new CSS key is required, have been received:

**KS_DVDCOPYSTATE_INITIALIZE**  
Indicates the start of a disc key negotiation sequence.

**KS_DVDCOPYSTATE_INITIALIZE_TITLE**  
Indicates the start of a title key negotiation sequence.

**KS_DVDCOPYSTATE_DONE**  
Indicates the completion of a key negotiation sequence.

## Requirements

**Header:** ksmedia.h (include Ksmedia.h)

## See also

[**KS_DVDCOPY_SET_COPY_STATE**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_ks_dvdcopy_set_copy_state)

[**KS_DVDCOPYSTATE**](/windows-hardware/drivers/ddi/ksmedia/ne-ksmedia-ks_dvdcopystate)

[DVD Copyright Protection](./dvd-copyright-protection.md)

[Multiple Data Streams on the same Hardware](./multiple-data-streams-on-the-same-hardware.md)

[Synchronizing Key Exchange with Data Flow](./synchronizing-key-exchange-with-data-flow.md)