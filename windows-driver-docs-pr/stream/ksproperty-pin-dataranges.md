---
title: KSPROPERTY_PIN_DATARANGES
description: Clients use the KSPROPERTY_PIN_DATARANGES property to determine the data ranges supported by pins instantiated by the pin factory.
keywords: ["KSPROPERTY_PIN_DATARANGES Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_PIN_DATARANGES
api_location:
- ks.h
api_type:
- HeaderDef
ms.date: 11/03/2021
---

# KSPROPERTY_PIN_DATARANGES

Clients use the **KSPROPERTY_PIN_DATARANGES** property to determine the data ranges supported by pins instantiated by the pin factory.

## Usage Summary Table

| Get | Set | Target | Property Descriptor Type | Property Value Type |
|--|--|--|--|--|
| Yes | No | Pin | [**KSP_PIN**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_pin) | A [**KSMULTIPLE_ITEM**](/windows-hardware/drivers/ddi/ks/ns-ks-ksmultiple_item) structure, followed by a sequence of 64-bit aligned [**KSDATARANGE**](/previous-versions/ff561658(v=vs.85)) structures. |

## Remarks

Specify this property using **KSP_PIN**, where the **PinId** member specifies the pin factory for which to return acceptable data ranges.

KS filters return all data ranges supported by pins instantiated by the pin factory. A KS filter may not support a reported data range in its current internal state. To determine the data ranges supported by the current internal state, use [**KSPROPERTY_PIN_CONSTRAINEDDATARANGES**](ksproperty-pin-constraineddataranges.md).

Stream minidrivers do not need to handle this property directly; the stream class driver handles this property using stream request blocks to query for more information.

For more information, see [KS Data Formats and Data Ranges](ks-data-formats-and-data-ranges.md).

## Requirements

**Header:** ks.h (include Ks.h)

## See also

[**KSP_PIN**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_pin)

[**KSMULTIPLE_ITEM**](/windows-hardware/drivers/ddi/ks/ns-ks-ksmultiple_item)

[**KSDATARANGE**](/previous-versions/ff561658(v=vs.85))

[**KSPROPERTY_PIN_CONSTRAINEDDATARANGES**](ksproperty-pin-constraineddataranges.md)

[KS Data Formats and Data Ranges](ks-data-formats-and-data-ranges.md)
