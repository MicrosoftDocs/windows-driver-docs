---
title: KSMETHOD_BDA_CHECK_CHANGES
description: Clients use KSMETHOD_BDA_CHECK_CHANGES to determine whether a list of requested changes will work.
keywords: ["KSMETHOD_BDA_CHECK_CHANGES Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSMETHOD_BDA_CHECK_CHANGES
api_location:
- Bdamedia.h
api_type:
- HeaderDef
ms.date: 10/12/2021
ms.localizationpriority: medium
---

# KSMETHOD_BDA_CHECK_CHANGES

Clients use KSMETHOD_BDA_CHECK_CHANGES to determine whether a list of requested changes will work.

## Specifying This Method

KSMETHOD with **Flags** member set to KSMETHOD_TYPE_NONE.

## Method Data

None

## Remarks

Before committing a list of changes, the network provider makes a KSMETHOD_BDA_CHECK_CHANGES request to determine whether the requested changes will work. The minidriver may reserve resources when this request is made, to guarantee that the resources are available.

## Requirements

**Header:** bdamedia.h (include Bdamedia.h)

## See also

[**BdaCheckChanges**](/windows-hardware/drivers/ddi/bdasup/nf-bdasup-bdacheckchanges)

[**KSMETHOD**](./ksmethod-structure.md)
