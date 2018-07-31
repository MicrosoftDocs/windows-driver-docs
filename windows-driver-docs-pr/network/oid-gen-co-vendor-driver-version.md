---
title: OID_GEN_CO_VENDOR_DRIVER_VERSION
author: windows-driver-content
description: This topic describes the OID_GEN_CO_VENDOR_DRIVER_VERSION object identifier (OID).
ms.assetid: c5cf91b7-f0fe-4deb-ad07-bc7304f1e878
keywords:
- OID_GEN_CO_VENDOR_DRIVER_VERSION
ms.author: windowsdriverdev
ms.date: 11/02/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# OID_GEN_CO_VENDOR_DRIVER_VERSION

The vendor-assigned version number of the NIC driver.

This OID is two bytes in length; the low-order half of the return value specifies the minor version, while the high-order half specifies the major version.

## Requirements

| | |
| --- | --- |
| Version | Windows Vista and later |
| Header | Ntddndis.h (include Ndis.h) |

