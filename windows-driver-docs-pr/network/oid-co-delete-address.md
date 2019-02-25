---
title: OID_CO_DELETE_ADDRESS
description: This topic describes the OID_CO_DELETE_ADDRESS object identifier (OID).
ms.assetid: 987c839b-f673-4c7a-90b4-fc5f93454b2e
keywords:
- OID_CO_DELETE_ADDRESS
ms.date: 11/03/2017
ms.localizationpriority: medium
---

# OID_CO_DELETE_ADDRESS

The OID_CO_DELETE_ADDRESS OID is sent by a client to a call manager to delete an alias address for a host. The alias address is formatted as a CO_ADDRESS structure, defined as follows:

```c++
typedef struct _CO_ADDRESS {
    ULONG   AddressSize;
    UCHAR   Address[1];
} CO_ADDRESS, *PCO_ADDRESS; 
```

The members of this structure contain the following information:

**AddressSize**  
Specifies the size in bytes of the structure at Address .

**Address**  
Specifies a variable-length array that contains the alias address. The address format is specific to the signaling protocol used by the call manager.

## Requirements

| | |
| --- | --- |
| Version | Windows Vista and later |
| Header | Ntddndis.h (include Ndis.h) |

