---
title: OID_CO_GET_ADDRESSES
author: windows-driver-content
description: This topic describes the OID_CO_GET_ADDRESSES object identifier (OID).
ms.assetid: 0c30e184-be01-49ab-b9ad-3ccc2fdf9fc5
keywords:
- OID_CO_GET_ADDRESSES
ms.author: windowsdriverdev
ms.date: 11/03/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_WWAN_DEVICE_CAPS_EX%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")