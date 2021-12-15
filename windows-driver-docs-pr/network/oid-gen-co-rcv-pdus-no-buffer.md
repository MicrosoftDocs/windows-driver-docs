---
title: OID_GEN_CO_RCV_PDUS_NO_BUFFER
description: This topic describes the OID_GEN_CO_RCV_PDUS_NO_BUFFER object identifier (OID).
keywords:
- OID_GEN_CO_RCV_PDUS_NO_BUFFER
ms.date: 11/02/2017
---

# OID_GEN_CO_RCV_PDUS_NO_BUFFER

The OID_GEN_CO_RCV_PDUS_NO_BUFFER OID specifies the number of PDUs that the NIC could not receive because of a lack of NIC receive buffer space. Instead of providing the exact number, some NICs provide only the number of times that they have missed at least one PDU because of such a problem.

## Requirements

**Version**: Windows Vista and later
**Header**: Ntddndis.h (include Ndis.h)

