---
title: KSMETHOD_BDA_GET_CHANGE_STATE
description: Clients use KSMETHOD_BDA_GET_CHANGE_STATE to determine the current change state for a filter.
keywords: ["KSMETHOD_BDA_GET_CHANGE_STATE Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSMETHOD_BDA_GET_CHANGE_STATE
api_location:
- Bdamedia.h
api_type:
- HeaderDef
ms.date: 10/12/2021
---

# KSMETHOD_BDA_GET_CHANGE_STATE

Clients use KSMETHOD_BDA_GET_CHANGE_STATE to determine the current change state for a filter.

## Specifying This Method

KSMETHOD with **Flags** member set to KSMETHOD_TYPE_READ.

## Method Data

Value from the BDA_CHANGE_STATE enumerated type that identifies the current change state for the filter.

## Requirements

**Header:** bdamedia.h (include Bdamedia.h)

## See also

[**BDA_CHANGE_STATE**](/previous-versions/windows/hardware/drivers/ff556518(v=vs.85))

[**BdaGetChangeState**](/windows-hardware/drivers/ddi/bdasup/nf-bdasup-bdagetchangestate)

[**KSMETHOD**](./ksmethod-structure.md)
