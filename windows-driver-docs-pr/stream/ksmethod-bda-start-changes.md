---
title: KSMETHOD_BDA_START_CHANGES
description: Clients use KSMETHOD_BDA_START_CHANGES to reset a change list.
keywords: ["KSMETHOD_BDA_START_CHANGES Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSMETHOD_BDA_START_CHANGES
api_location:
- Bdamedia.h
api_type:
- HeaderDef
ms.date: 10/12/2021
---

# KSMETHOD_BDA_START_CHANGES

Clients use KSMETHOD_BDA_START_CHANGES to reset a change list.

## Specifying This Method

KSMETHOD with **Flags** member set to KSMETHOD_TYPE_NONE.

## Method Data

None

## Remarks

Before the network provider begins to make changes, it makes a KSMETHOD_BDA_START_CHANGES request, which causes any existing change list that has not been committed to be discarded and informs the filter's pins and nodes to start keeping track of a new set of changes. The network provider then calls the necessary interface methods on the filter or its pins, but the methods are not actually called yet. If at any point the network provider determines that the changes will not work, it can call this method to clear out the list.

## Requirements

**Header:** bdamedia.h (include Bdamedia.h)

## See also

[**BdaStartChanges**](/windows-hardware/drivers/ddi/bdasup/nf-bdasup-bdastartchanges)

[**KSMETHOD**](./ksmethod-structure.md)
