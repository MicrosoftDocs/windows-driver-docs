---
title: KSMETHOD_BDA_CREATE_PIN_FACTORY
description: Clients use KSMETHOD_BDA_CREATE_PIN_FACTORY to create a pin factory for a filter.
keywords: ["KSMETHOD_BDA_CREATE_PIN_FACTORY Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSMETHOD_BDA_CREATE_PIN_FACTORY
api_location:
- Bdamedia.h
api_type:
- HeaderDef
ms.date: 10/12/2021
ms.localizationpriority: medium
---

# KSMETHOD_BDA_CREATE_PIN_FACTORY

Clients use KSMETHOD_BDA_CREATE_PIN_FACTORY to create a pin factory for a filter.

## Specifying This Method

KSM_PIN with the **Flags** member of the **Method** member set to KSMETHOD_TYPE_READ.

## Method Data

ULONG, representing the identifier of the pin factory.

## Requirements

**Header:** bdamedia.h (include Bdamedia.h)

## See also

[**BdaMethodCreatePin**](/windows-hardware/drivers/ddi/bdasup/nf-bdasup-bdamethodcreatepin)

[**KSM_PIN**](/windows-hardware/drivers/ddi/bdasup/ns-bdasup-_ksm_pin)
