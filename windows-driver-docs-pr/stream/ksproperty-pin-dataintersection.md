---
title: KSPROPERTY_PIN_DATAINTERSECTION
description: A client uses the KSPROPERTY_PIN_DATAINTERSECTION property to find a data format supported by pins instantiated by the pin factory. The client supplies a list of data formats; the KS filter returns the first data format on the list that is supported.
keywords: ["KSPROPERTY_PIN_DATAINTERSECTION Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_PIN_DATAINTERSECTION
api_location:
- ks.h
api_type:
- HeaderDef
ms.date: 11/03/2021
---

# KSPROPERTY_PIN_DATAINTERSECTION

A client uses the **KSPROPERTY_PIN_DATAINTERSECTION** property to find a data format supported by pins instantiated by the pin factory. The client supplies a list of data formats; the KS filter returns the first data format on the list that is supported.

## Usage Summary Table

| Get | Set | Target | Property Descriptor Type | Property Value Type |
|--|--|--|--|--|
| Yes | No | Pin | [**KSP_PIN**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_pin) | [**KSDATAFORMAT**](/windows-hardware/drivers/ddi/ks/ns-ks-ksdataformat) |

## Remarks

To specify this property, provide a [**KSP_PIN**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_pin) structure followed by a [**KSMULTIPLE_ITEM**](/windows-hardware/drivers/ddi/ks/ns-ks-ksmultiple_item) structure and a sequence of 64-bit aligned [**KSDATARANGE**](/previous-versions/ff561658(v=vs.85)) structures. The **PinId** member of **KSP_PIN** specifies the pin factory.

This property returns the first matching data format from the client-supplied list.

Stream minidrivers do not need to handle this property directly; the stream class driver handles this property using stream request blocks to query for more information.

For more information, see [KS Data Formats and Data Ranges](ks-data-formats-and-data-ranges.md).

## Requirements

**Header:** ks.h (include Ks.h)

## See also

[**KSP_PIN**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_pin)

[**KSMULTIPLE_ITEM**](/windows-hardware/drivers/ddi/ks/ns-ks-ksmultiple_item)

[**KSDATARANGE**](/previous-versions/ff561658(v=vs.85))

[**KSDATAFORMAT**](/windows-hardware/drivers/ddi/ks/ns-ks-ksdataformat)
