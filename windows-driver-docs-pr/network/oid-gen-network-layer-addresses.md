---
title: OID_GEN_NETWORK_LAYER_ADDRESSES
description: As a set, the OID_GEN_NETWORK_LAYER_ADDRESSES OID notifies underlying miniport driver and other layered drivers about the list of network-layer addresses that are associated with bound instances.
ms.assetid: 4a75c2ca-1a58-462e-876a-a65cfe63441e
ms.date: 08/08/2017
keywords: 
 -OID_GEN_NETWORK_LAYER_ADDRESSES Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_GEN\_NETWORK\_LAYER\_ADDRESSES


As a set, the OID\_GEN\_NETWORK\_LAYER\_ADDRESSES OID notifies underlying miniport driver and other layered drivers about the list of network-layer addresses that are associated with bound instances.

**Version Information**

<a href="" id="windows-vista-and-later-versions-of-windows"></a>Windows Vista and later versions of Windows  
Supported.

<a href="" id="ndis-6-0-and-later-miniport-drivers"></a>NDIS 6.0 and later miniport drivers  
Optional.

<a href="" id="ndis-5-1-miniport-drivers"></a>NDIS 5.1 miniport drivers  
Optional.

<a href="" id="windows-xp"></a>Windows XP  
Supported.

<a href="" id="ndis-5-1-miniport-drivers"></a>NDIS 5.1 miniport drivers  
Optional.

Remarks
-------

A bound instance is the binding between the calling transport and a driver set up by a call to [**NdisOpenAdapterEx**](https://msdn.microsoft.com/library/windows/hardware/ff563715). Transports use TRANSPORT\_ADDRESS and TA\_ADDRESS structures to notify underlying miniport drivers and other layered drivers about the list of network-layer addresses. Miniport drivers and other layered drivers use compatible NETWORK\_ADDRESS\_LIST and NETWORK\_ADDRESS structures, defined as follows, to set the list of network-layer addresses on a bound interface.

```C++
typedef struct _NETWORK_ADDRESS_LIST {
  LONG  AddressCount; 
  USHORT  AddressType; 
  NETWORK_ADDRESS  Address[1]; 
} NETWORK_ADDRESS_LIST, *PNETWORK_ADDRESS_LIST;
```

The members of this structure contain the following information:

<a href="" id="addresscount"></a>**AddressCount**  
Specifies the number of network-layer addresses listed in the array in the **Address** member.

<a href="" id="addresstype"></a>**AddressType**  
Specifies the protocol type that sends this OID. This member is only valid if the **AddressCount** member is set to zero. The **AddressCount** member is set to zero to notify a miniport driver or other layered driver to clear the list of network-layer addresses on a bound interface. The protocol can be one of the following values:

<a href="" id="ndis-protocol-id-default"></a>NDIS\_PROTOCOL\_ID\_DEFAULT  
Default protocol

<a href="" id="ndis-protocol-id-tcp-ip"></a>NDIS\_PROTOCOL\_ID\_TCP\_IP  
TCP/IP protocol

<a href="" id="ndis-protocol-id-ipx"></a>NDIS\_PROTOCOL\_ID\_IPX  
NetWare IPX protocol

<a href="" id="ndis-protocol-id-nbf"></a>NDIS\_PROTOCOL\_ID\_NBF  
NetBIOS protocol

<a href="" id="address"></a>**Address**  
Array of network-layer addresses of type NETWORK\_ADDRESS. The **AddressCount** member specifies the number of elements in this array.

```C++
typedef struct _NETWORK_ADDRESS {
  USHORT  AddressLength; 
  USHORT  AddressType; 
  UCHAR   Address[1]; 
} NETWORK_ADDRESS, *PNETWORK_ADDRESS;
```

The members of this structure contain the following information:

<a href="" id="addresslength"></a>**AddressLength**  
Specifies the size, in bytes, of this network-layer address. The **Address** member contains the array of bytes that specify this address.

<a href="" id="addresstype"></a>**AddressType**  
Specifies the protocol type that sends this OID and this network-layer address. This member is only valid if the **AddressCount** member in the NETWORK\_ADDRESS\_LIST structure is set to a nonzero value. The **AddressCount** member in NETWORK\_ADDRESS\_LIST is set to a nonzero value to notify a miniport driver or other layered driver to change the list of network-layer addresses on a bound interface. Protocol types are defined in the preceding list.

<a href="" id="address"></a>**Address**  
Array of bytes that specify this network-layer address. The **AddressLength** member specifies the number of bytes in this array.

The transport can call the [**NdisOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff563710) function and can pass an [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure that is filled with the OID\_GEN\_NETWORK\_LAYER\_ADDRESSES code. This call notifies a bound instance of a change in the addresses that are associated with that instance. In this call, the transport also passes the bound instance in the *NdisBindingHandle* parameter. The bound instance is the binding set up between the transport and the underlying miniport driver or other layered driver. For this call, the transport should fill the **InformationBuffer** member of NDIS\_OID\_REQUEST with a pointer to a TRANSPORT\_ADDRESS structure. TRANSPORT\_ADDRESS corresponds to a NETWORK\_ADDRESS\_LIST structure and should contain the list of network-layer addresses.

Suppose a transport passes addresses through an intermediate driver down to an underlying miniport driver. If the intermediate driver also requires the addresses, it should take note of them before passing them on to the underlying miniport driver. An underlying miniport driver, especially an old driver, can return a status value of NDIS\_STATUS\_NOT\_SUPPORTED or NDIS\_STATUS\_SUCCESS. The underlying miniport driver propagates the status of the operation back up towards the transport. If the intermediate driver must continue receiving address notifications, and if it is necessary, the intermediate driver should change the status to NDIS\_STATUS\_SUCCESS.Otherwise, the transport might interpret NDIS\_STATUS\_NOT\_SUPPORTED as an indication that the underlying miniport driver does not require that the transport issue additional address updates. If NDIS\_STATUS\_SUCCESS is returned, transports are obligated to continue notifying underlying drivers of any change in associated addresses, including addition and deletion of addresses.

A protocol can set the **AddressCount** member of TRANSPORT\_ADDRESS to zero to notify a miniport driver or other layered driver to clear the list of network-layer addresses on a bound interface. If **AddressCount** is set to zero, the **AddressType** member in NETWORK\_ADDRESS\_LIST is valid and the **AddressType** members in NETWORK\_ADDRESS structures are not valid. On the other hand, a protocol can set **AddressCount** to a nonzero value to notify a miniport driver or other layered driver to change the list of network-layer addresses on a bound interface. In this case, the **AddressType** member in NETWORK\_ADDRESS\_LIST is not valid and the **AddressType** members in NETWORK\_ADDRESS structures are valid.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710)

[**NdisOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff563710)

[**NdisOpenAdapterEx**](https://msdn.microsoft.com/library/windows/hardware/ff563715)

 

 




