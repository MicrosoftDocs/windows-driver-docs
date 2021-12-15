---
title: KSMETHOD_BDA_CREATE_TOPOLOGY
description: Clients use KSMETHOD_BDA_CREATE_TOPOLOGY to create a topology structure in Ring 3 that reflects the known connections in a filter.
keywords: ["KSMETHOD_BDA_CREATE_TOPOLOGY Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSMETHOD_BDA_CREATE_TOPOLOGY
api_location:
- Bdamedia.h
api_type:
- HeaderDef
ms.date: 10/12/2021
---

# KSMETHOD_BDA_CREATE_TOPOLOGY

Clients use KSMETHOD_BDA_CREATE_TOPOLOGY to create a topology structure in Ring 3 that reflects the known connections in a filter.

## Specifying This Method

KSMETHOD with the **Flags** member set to KSMETHOD_TYPE_WRITE.

## Method Data

A KSMULTIPLE_ITEM structure, which is the header for a list of topology information.

## Requirements

**Header:** bdamedia.h (include Bdamedia.h)

## See also

[**BdaMethodCreateTopology**](/windows-hardware/drivers/ddi/bdasup/nf-bdasup-bdamethodcreatetopology)

[**KSMETHOD**](./ksmethod-structure.md)

[**KSMULTIPLE_ITEM**](/windows-hardware/drivers/ddi/ks/ns-ks-ksmultiple_item)
