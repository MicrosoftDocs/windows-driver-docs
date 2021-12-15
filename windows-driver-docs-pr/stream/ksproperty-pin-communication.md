---
title: KSPROPERTY_PIN_COMMUNICATION
description: The KSPROPERTY_PIN_COMMUNICATION property specifies the direction of IRP flow on pins instantiated by the pin factory.
keywords: ["KSPROPERTY_PIN_COMMUNICATION Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_PIN_COMMUNICATION
api_location:
- ks.h
api_type:
- HeaderDef
ms.date: 11/03/2021
---

# KSPROPERTY_PIN_COMMUNICATION

The **KSPROPERTY_PIN_COMMUNICATION** property specifies the direction of IRP flow on pins instantiated by the pin factory.

## Usage Summary Table

| Get | Set | Target | Property Descriptor Type | Property Value Type |
|--|--|--|--|--|
| Yes | No | Pin | [**KSP_PIN**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_pin) | **KSPIN_COMMUNICATION** |

## Remarks

The KS filter returns one of the following values, which specifies the communication direction of a pin instantiated by this pin factory.

| Value | Description |
|--|--|
| KSPIN_COMMUNICATION_NONE | The pin factory instantiates IRP sink pins. Such pins can only be connected to IRP source pins. |
| KSPIN_COMMUNICATION_SOURCE | The pin factory instantiates IRP source pins. Such pins can only be connected to IRP sink pins. |
| KSPIN_COMMUNICATION_BOTH | The pin factory instantiates pins that are both IRP sinks and IRP sources. |
| KSPIN_COMMUNICATION_BRIDGE | This pin cannot connect to other pins, but instances can be created on it to receive non-KS I/O requests. |

The source pins send IRPs to sink pins. A source pin may read or write data, and a sink pin may have data read to it or written from it. For more information, see [**KSPROPERTY_PIN_DATAFLOW**](ksproperty-pin-dataflow.md).

Stream minidrivers do not need to handle this property directly; the stream class driver handles this property using Stream Request Blocks to query for more information where necessary.

## Requirements

**Header:** ks.h (include Ks.h)

## See also

[**KSPROPERTY_PIN_DATAFLOW**](ksproperty-pin-dataflow.md)

[**KSP_PIN**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_pin)
