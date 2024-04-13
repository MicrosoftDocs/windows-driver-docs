---
title: KSMETHOD_BDA_COMMIT_CHANGES
description: Clients use KSMETHOD_BDA_COMMIT_CHANGES to commit a list of requested changes.
keywords: ["KSMETHOD_BDA_COMMIT_CHANGES Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSMETHOD_BDA_COMMIT_CHANGES
api_location:
- Bdamedia.h
api_type:
- HeaderDef
ms.date: 10/12/2021
---

# KSMETHOD_BDA_COMMIT_CHANGES

Clients use KSMETHOD_BDA_COMMIT_CHANGES to commit a list of requested changes.

## Specifying This Method

KSMETHOD with **Flags** member set to KSMETHOD_TYPE_NONE.

## Method Data

None

## Remarks

When the network provider makes a KSMETHOD_BDA_COMMIT_CHANGES request, the list of changes are committed on the underlying filter, at which point the filter resets its state and a new cycle can begin.

## Requirements

**Header:** bdamedia.h (include Bdamedia.h)

## See also

[**BdaCommitChanges**](/windows-hardware/drivers/ddi/bdasup/nf-bdasup-bdacommitchanges)

[**KSMETHOD**](./ksmethod-structure.md)
