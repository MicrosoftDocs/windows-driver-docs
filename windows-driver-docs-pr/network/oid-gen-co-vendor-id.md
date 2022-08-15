---
title: OID_GEN_CO_VENDOR_ID
description: This topic describes the OID_GEN_CO_VENDOR_ID object identifier (OID).
keywords:
- OID_GEN_CO_VENDOR_ID
ms.date: 11/02/2017
---

# OID_GEN_CO_VENDOR_ID

A 3-byte IEEE-registered vendor code, followed by a single byte that the vendor assigns to identify a particular NIC.

The IEEE code uniquely identifies the vendor and is the same as the three bytes appearing at the beginning of the NIC hardware address.

Vendors without an IEEE-registered code should use the value 0xFFFFFF.

## Requirements

**Version**: Windows Vista and later
**Header**: Ntddndis.h (include Ndis.h)

