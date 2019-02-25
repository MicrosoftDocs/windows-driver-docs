---
title: OID_CO_ADDRESS_CHANGE
description: This topic describes the OID_CO_ADDRESS_CHANGE object identifier (OID).
ms.assetid: 18b185dd-b282-4182-a761-008e5d0c88d7
keywords:
- OID_CO_ADDRESS_CHANGE
ms.date: 11/03/2017
ms.localizationpriority: medium
---

# OID_CO_ADDRESS_CHANGE

The OID_CO_ADDRESS_CHANGE OID is sent by the call manager to each client that opened an address family with the call manager. This action is taken in response to a change in the switch address that the call manager uses. For example, the call manager sends this request if someone disconnects the NIC from one switch and plugs it into another switch. Each notified client must send an OID_CO_GET_ADDRESSES query to the call manager to retrieve a list of currently valid addresses.

The call manager also sends OID_CO_ADDRESS_CHANGE to a client immediately after the client opens an address family with the call manager. This ensures that a client that opens an address family after the switch address has changed is notified of the change. The client must then must then send an OID_CO_GET_ADDRESSES query to the call manager.

## Requirements

| | |
| --- | --- |
| Version | Windows Vista and later |
| Header | Ntddndis.h (include Ndis.h) |

