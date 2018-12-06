---
title: OID_CO_ADD_ADDRESS
description: This topic describes the OID_CO_ADD_ADDRESS object identifier (OID).
ms.assetid: ca6bb3eb-87db-4e71-9585-34cd1e978b6a
keywords:
- OID_CO_ADD_ADDRESS
ms.date: 11/03/2017
ms.localizationpriority: medium
---

# OID_CO_ADD_ADDRESS

The OID_CO_ADD_ADDRESS OID is sent by a client to a call manager to specify an alias address for a host. The alias address is formatted as a CO_ADDRESS structure, defined as follows:

```c++
typedef struct _CO_ADDRESS{
    ULONG   AddressSize;
    UCHAR   Address[1];
} CO_ADDRESS, *PCO_ADDRESS;
```

The members of this structure contain the following information:

**AddressSize**  
Specifies the size in bytes of the structure at **Address**.

**Address**  
Specifies a variable-length array that contains the alias address. The address format is specific to the signaling protocol used by the call manager.

This OID is typically used to specify a well-known address at which a host offers a particular service. For example, a client could specify a well-known address for a LAN emulation server. The call manager's response to this OID is specific to the signaling protocol used by the call manager. An ATM call manager, for example, sends a message to the switch that notifies the switch of the alias address.


## Requirements

| | |
| --- | --- |
| Version | Windows Vista and later |
| Header | Ntddndis.h (include Ndis.h) |

