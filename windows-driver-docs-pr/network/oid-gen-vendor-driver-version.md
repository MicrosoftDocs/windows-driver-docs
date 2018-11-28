---
title: OID_GEN_VENDOR_DRIVER_VERSION
description: As a query, the OID_GEN_VENDOR_DRIVER_VERSION OID specifies the vendor-assigned version number of the miniport driver.
ms.assetid: 37CB6A21-9AF2-49BF-AFBA-868C0C6C5383
keywords:
- OID_GEN_VENDOR_DRIVER_VERSION
ms.date: 11/01/2017
ms.localizationpriority: medium
---

# OID_GEN_VENDOR_DRIVER_VERSION

As a query, the OID_GEN_VENDOR_DRIVER_VERSION OID specifies the vendor-assigned version number of the miniport driver.

Set requests are not supported.

## Remarks

The low-order half of the return value specifies the minor version; the high-order half specifies the major version.

This OID is mandatory for NDIS 6.0 and later miniport drivers.

## Requirements

| | |
| --- | --- |
| Version | Windows Vista and later |
| Header | Ntddndis.h (include Ndis.h) |

