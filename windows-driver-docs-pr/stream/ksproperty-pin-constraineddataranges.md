---
title: KSPROPERTY_PIN_CONSTRAINEDDATARANGES
description: The KSPROPERTY_PIN_CONSTRAINEDDATARANGES property specifies the list of data ranges currently supported by pins instantiated on the pin factory.
keywords: ["KSPROPERTY_PIN_CONSTRAINEDDATARANGES Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_PIN_CONSTRAINEDDATARANGES
api_location:
- ks.h
api_type:
- HeaderDef
ms.date: 11/03/2021
---

# KSPROPERTY_PIN_CONSTRAINEDDATARANGES

The **KSPROPERTY_PIN_CONSTRAINEDDATARANGES** property specifies the list of data ranges currently supported by pins instantiated on the pin factory.

## Usage Summary Table

| Get | Set | Target | Property Descriptor Type | Property Value Type |
|--|--|--|--|--|
| Yes | No | Pin | [**KSP_PIN**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_pin) | [**KSMULTIPLE_ITEM**](/windows-hardware/drivers/ddi/ks/ns-ks-ksmultiple_item) and [**KSDATARANGE**](/previous-versions/ff561658(v=vs.85)) |

## Remarks

The **PinId** member of the [**KSP_PIN**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_pin) structure specifies the pin factory for which to query.

This property returns a [**KSMULTIPLE_ITEM**](/windows-hardware/drivers/ddi/ks/ns-ks-ksmultiple_item) structure, followed by a sequence of 64-bit aligned [**KSDATARANGE**](/previous-versions/ff561658(v=vs.85)) structures.

A KS filter uses this property to report the data ranges currently supported by pins instantiated on this pin factory, based on any constraints imposed by the current internal state of the KS filter. Use the [**KSPROPERTY_PIN_DATARANGES**](ksproperty-pin-dataranges.md) property to report the complete list of all data ranges supported by the KS filter, regardless of dynamic constraints.

Stream minidrivers do not need to handle this property directly; the stream class driver handles this property using stream request blocks to query for more information.

For more information, see [KS Data Formats and Data Ranges](./ks-data-formats-and-data-ranges.md).

## Requirements

**Header:** ks.h (include Ks.h)

## See also

[**KSMULTIPLE_ITEM**](/windows-hardware/drivers/ddi/ks/ns-ks-ksmultiple_item)

[**KSDATARANGE**](/previous-versions/ff561658(v=vs.85))

[**KSPROPERTY_PIN_DATARANGES**](ksproperty-pin-dataranges.md)

[**KSP_PIN**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_pin)
