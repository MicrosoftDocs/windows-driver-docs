---
title: OID_GEN_CO_RCV_PDUS_NO_BUFFER
author: windows-driver-content
description: This topic describes the OID_GEN_CO_RCV_PDUS_NO_BUFFER object identifier (OID).
ms.assetid: b20bd89a-d5a7-4fc3-a492-27dc61ee6f44
keywords:
- OID_GEN_CO_RCV_PDUS_NO_BUFFER
ms.author: windowsdriverdev
ms.date: 11/02/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# OID_GEN_CO_RCV_PDUS_NO_BUFFER

The OID_GEN_CO_RCV_PDUS_NO_BUFFER OID specifies the number of PDUs that the NIC could not receive because of a lack of NIC receive buffer space. Instead of providing the exact number, some NICs provide only the number of times that they have missed at least one PDU because of such a problem.

## Requirements

| | |
| --- | --- |
| Version | Windows Vista and later |
| Header | Ntddndis.h (include Ndis.h) |

