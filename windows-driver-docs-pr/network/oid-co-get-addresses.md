---
title: OID_CO_GET_ADDRESSES
description: This topic describes the OID_CO_GET_ADDRESSES object identifier (OID).
ms.assetid: 0c30e184-be01-49ab-b9ad-3ccc2fdf9fc5
keywords:
- OID_CO_GET_ADDRESSES
ms.date: 11/03/2017
ms.localizationpriority: medium
---

# OID_CO_GET_ADDRESSES

The OID_CO_GET_ADDRESSES OID is used by the client to make a query to the call manager. This query is made in response to the call manager sending an OID_CO_ADDRESS_CHANGE to the client. In response to this query, the call manager sends the client an address list that is formatted as a CO_ADDRESS_LIST structure, defined as follows:

```c++
typedef struct _CO_ADDRESS_LIST {
    ULONG       NumberOfAddressesAvailable;
    ULONG       NumberOfAddresses;
    CO_ADDRESS  AddressList;
} CO_ADDRESS_LIST, *PCO_ADDRESS_LIST;
```

The members of this structure contain the following information:

**NumberOfAddressesAvailable**  
Specifies the maximum number of addresses in the call manager's list of addresses. Regardless of the actual number of addresses that the call manager returns to the client at **AddressList**, the size of the buffer at **AddressList** is always **NumberOfAddressesAvailable** multiplied by the address size, which is a fixed size specific to the call manager.

**NumberOfAddresses**  
Specifies the number of addresses that the call manager has written to **AddressList**.

**AddressList**  
The alias address is formatted as a CO_ADDRESS structure, defined as follows:

```c++
typedef struct _CO_ADDRESS {
    ULONG   AddressSize;
    UCHAR   Address[1];
} CO_ADDRESS, *PCO_ADDRESS;
```

The members of this structure contain the following information:

**AddressSize**  
Specifies the size in bytes of the structure at **Address** .

**Address**  
Specifies a variable-length array that contains the list of addresses. The address format is specific to the signaling protocol used by the call manager.

The **AddressList** contains network addresses at which the local host can be reached. The **AddressList** returned to a particular client contains addresses that are common to all clients, as well as any addresses that the client itself has added to call manager's list of addresses with OID_CO_ADD_ADDRESS.

## Requirements

| | |
| --- | --- |
| Version | Windows Vista and later |
| Header | Ntddndis.h (include Ndis.h) |

