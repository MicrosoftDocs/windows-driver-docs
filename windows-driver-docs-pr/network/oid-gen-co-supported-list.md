---
title: OID_GEN_CO_SUPPORTED_LIST
description: This topic describes the OID_GEN_CO_SUPPORTED_LIST object identifier (OID).
keywords:
- OID_GEN_CO_SUPPORTED_LIST
ms.date: 11/02/2017
ms.localizationpriority: medium
---

# OID_GEN_CO_SUPPORTED_LIST

The OID_GEN_CO_SUPPORTED_LIST OID specifies an array of OIDs for objects that the underlying driver or its NIC supports. Objects include general, media-specific, and implementation-specific objects.

The underlying driver should order the OID list it returns in increasing numeric order. NDIS forwards a subset of the returned list to protocols that make this query. That is, NDIS filters any supported statistics OIDs out of the list since protocols never make statistics queries subsequently.

## Requirements

**Version**: Windows Vista and later
**Header**: Ntddndis.h (include Ndis.h)

