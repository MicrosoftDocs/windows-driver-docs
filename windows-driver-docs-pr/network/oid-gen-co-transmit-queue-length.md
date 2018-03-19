---
title: OID_GEN_CO_TRANSMIT_QUEUE_LENGTH
author: windows-driver-content
description: This topic describes the OID_GEN_CO_TRANSMIT_QUEUE_LENGTH object identifier (OID).
ms.assetid: bd99e26d-abd4-4b71-8106-e474f61630ff
keywords:
- OID_GEN_CO_TRANSMIT_QUEUE_LENGTH
ms.author: windowsdriverdev
ms.date: 11/02/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# OID_GEN_CO_TRANSMIT_QUEUE_LENGTH

The OID_GEN_CO_TRANSMIT_QUEUE_LENGTH OID specifies the number of PDUs currently queued for transmission, whether on the NIC or in a driver-internal queue. The number returned is always the total number of PDUs currently queued, which can include unsubmitted send requests queued in the NDIS library.

## Requirements

| | |
| --- | --- |
| Version | Windows Vista and later |
| Header | Ntddndis.h (include Ndis.h) |

