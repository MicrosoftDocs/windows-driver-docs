---
title: KSMETHOD_BDA_DELETE_PIN_FACTORY
description: Clients use KSMETHOD_BDA_DELETE_PIN_FACTORY to delete a pin factory for a filter.
keywords: ["KSMETHOD_BDA_DELETE_PIN_FACTORY Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSMETHOD_BDA_DELETE_PIN_FACTORY
api_location:
- Bdamedia.h
api_type:
- HeaderDef
ms.date: 10/12/2021
---

# KSMETHOD_BDA_DELETE_PIN_FACTORY

Clients use KSMETHOD_BDA_DELETE_PIN_FACTORY to delete a pin factory for a filter.

## Specifying This Method

KSM_PIN with the **Flags** member of the **Method** member set to KSMETHOD_TYPE_NONE.

## Method Data

None

## Remarks

Specifies the pin factory to delete in the **PinId** member of the KSM_PIN structure.

## Requirements

**Header:** bdamedia.h (include Bdamedia.h)

## See also

[**BdaMethodDeletePin**](/windows-hardware/drivers/ddi/bdasup/nf-bdasup-bdamethoddeletepin)

[**KSM_PIN**](/windows-hardware/drivers/ddi/bdasup/ns-bdasup-_ksm_pin)
