---
title: KSPROPERTY_PIN_DATAFLOW
description: The KSPROPERTY_PIN_DATAFLOW property specifies the direction of data flow on pins instantiated by the pin factory. Sink pins are entry points into a filter; source pins output from a filter.
keywords: ["KSPROPERTY_PIN_DATAFLOW Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_PIN_DATAFLOW
api_location:
- ks.h
api_type:
- HeaderDef
ms.date: 11/03/2021
---

# KSPROPERTY_PIN_DATAFLOW

The **KSPROPERTY_PIN_DATAFLOW** property specifies the direction of data flow on pins instantiated by the pin factory. Sink pins are entry points into a filter; source pins output from a filter.

## Usage Summary Table

| Get | Set | Target | Property Descriptor Type | Property Value Type |
|--|--|--|--|--|
| Yes | No | Pin | [**KSP_PIN**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_pin) | [**KSPIN_DATAFLOW**](/windows-hardware/drivers/ddi/ks/ne-ks-kspin_dataflow) |

## Remarks

Specify the pin factory in the **PinId** member of the [**KSP_PIN**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_pin) structure.

**KSPROPERTY_PIN_DATAFLOW** returns an enumeration of type [**KSPIN_DATAFLOW**](/windows-hardware/drivers/ddi/ks/ne-ks-kspin_dataflow), set to either **KSPIN_DATAFLOW_IN** or **KSPIN_DATAFLOW_OUT**.

Stream minidrivers do not need to handle this property directly; the stream class driver handles this property using stream request blocks to query for more information.

## Requirements

**Header:** ks.h (include Ks.h)

## See also

[**KSP_PIN**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_pin)

[**KSPIN_DATAFLOW**](/windows-hardware/drivers/ddi/ks/ne-ks-kspin_dataflow)
