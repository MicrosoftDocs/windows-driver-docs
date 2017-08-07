---
title: OID\_DOT11\_EXCLUDED\_MAC\_ADDRESS\_LIST
author: windows-driver-content
description: When set, the OID\_DOT11\_EXCLUDED\_MAC\_ADDRESS\_LIST object identifier (OID) requests that the miniport driver set the value of the Extensible Station (ExtSTA) msDot11ExcludedMacAddressList management information base (MIB) object to the specified data.
ms.assetid: ef2e3313-576b-4072-aba4-a940e50b0a5c
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords:
 - OID_DOT11_EXCLUDED_MAC_ADDRESS_LIST Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_EXCLUDED\_MAC\_ADDRESS\_LIST


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When set, the OID\_DOT11\_EXCLUDED\_MAC\_ADDRESS\_LIST object identifier (OID) requests that the miniport driver set the value of the Extensible Station (ExtSTA) **msDot11ExcludedMacAddressList** management information base (MIB) object to the specified data.

When queried, OID\_DOT11\_EXCLUDED\_MAC\_ADDRESS\_LIST requests that the miniport driver return the value of the **msDot11ExcludedMacAddressList** MIB object.

The **msDot11ExcludedMacAddressList** MIB object specifies the list of media access control (MAC) addresses of remote stations that the 802.11 station must not connect to. When [OID\_DOT11\_CONNECT\_REQUEST](oid-dot11-connect-request.md) is set, the 802.11 station must attempt to connect with any remote station, such as an access point (AP) in an infrastructure basic service set (BSS) network or peer station in an independent BSS (IBSS) network, that does not have a MAC address within the excluded MAC address list.

The data type for OID\_DOT11\_EXCLUDED\_MAC\_ADDRESS\_LIST is the DOT11\_MAC\_ADDRESS\_LIST structure.

```ManagedCPlusPlus
    typedef struct DOT11_MAC_ADDRESS_LIST {
         NDIS_OBJECT_HEADER Header;
         ULONG uNumOfEntries;
         ULONG uTotalNumOfEntries;
         DOT11_MAC_ADDRESS MacAddrs[1];
    } DOT11_MAC_ADDRESS_LIST,   *PDOT11_MAC_ADDRESS_LIST;
  
```

This structure includes the following members:

<a href="" id="header"></a>**Header**  
The type, revision, and size of the DOT11\_MAC\_ADDRESS\_LIST structure. This member is formatted as an [**NDIS\_OBJECT\_HEADER**](ndis-object-header.md) structure.

The miniport driver must set the members of **Header** to the following values:

<a href="" id="type"></a>**Type**  
This member must be set to NDIS\_OBJECT\_TYPE\_DEFAULT.

<a href="" id="revision"></a>**Revision**  
This member must be set to DOT11\_MAC\_ADDRESS\_LIST\_REVISION\_1.

<a href="" id="size"></a>**Size**  
This member must be set to sizeof(DOT11\_MAC\_ADDRESS\_LIST).

For more information about these members, see [**NDIS\_OBJECT\_HEADER**](ndis-object-header.md).

<a href="" id="unumofentries"></a>**uNumOfEntries**  
Number of entries in the **MacAddrs** array. A zero value for this member indicates an empty excluded MAC address list.

<a href="" id="utotalnumofentries"></a>**uTotalNumOfEntries**  
Maximum number of entries that the **MacAddrs** array can contain.

<a href="" id="macaddrs"></a>**MacAddrs**  
The excluded MAC address list. For more information about the data type of this member, see [**DOT11\_MAC\_ADDRESS**](dot11-mac-address.md).

A wildcard MAC address has the value of 0xFFFFFFFFFFFF. The wildcard MAC address matches the MAC address of any AP or peer station. If the excluded MAC address list contains the wildcard MAC address, the 802.11 station must not connect to any AP or peer station.

**Note**  A list of excluded MAC address that contains the wildcard MAC address must be the only entry in the list.

 

When OID\_DOT11\_EXCLUDED\_MAC\_ADDRESS\_LIST is set, the miniport driver should ensure that the value of the **InformationBufferLength** member of the [*MiniportOidRequest*](miniportoidrequest.md) function's OidRequest parameter is at least the value returned by the following formula:

```
 FIELD_OFFSET(DOT11_MAC_ADDRESS_LIST, MacAddrs) + uNumOfEntries * sizeof(DOT11_MAC_ADDRESS))
```

When OID\_DOT11\_EXCLUDED\_MAC\_ADDRESS\_LIST is set, the miniport driver must:

-   Fail the set request if the excluded MAC address list contains the wildcard MAC address but the **uNumOfEntries** member is not set to one. In this situation, the miniport driver must return NDIS\_STATUS\_INVALID\_DATA from its [*MiniportOidRequest*](miniportoidrequest.md) function.

-   Fail the set request if the **uNumOfEntries** member has a value greater than the value of **uExcludedMacAddressListSize** that the driver previously returned through a query of [OID\_DOT11\_EXTSTA\_CAPABILITY](oid-dot11-extsta-capability.md). In this situation, the miniport driver must return NDIS\_STATUS\_INVALID\_LENGTH from its [*MiniportOidRequest*](miniportoidrequest.md) function.

-   Overwrite the 802.11 station's excluded MAC address list with the entries from the **MacAddrs** array. If an entry has the MAC address of the AP or peer station that the 802.11 station is connected to, the 802.11 station must disassociate and roam to another station. For more information about the procedures for disassociating and roaming, see [Disassociation Operations](https://msdn.microsoft.com/library/windows/hardware/ff546439) and [Roaming Operations](https://msdn.microsoft.com/library/windows/hardware/ff570717).

When OID\_DOT11\_EXCLUDED\_MAC\_ADDRESS\_LIST is queried, the miniport driver must verify that the **InformationBuffer** member of the [*MiniportOidRequest*](miniportoidrequest.md) function's *OidRequest* parameter is large enough to return the entire DOT11\_MAC\_ADDRESS\_LIST structure, including all entries in the **MacAddrs** array. The value of the **InformationBufferLength** member of the *OidRequest* parameter determines what the miniport driver must do, as the following list shows:

-   If the value of the **InformationBufferLength** member is less than the length, in bytes, of the entire DOT11\_MAC\_ADDRESS\_LIST structure, the miniport driver must do the following:

    -   Set the **uNumOfEntries** member to zero.

    -   Set the **uTotalNumOfEntries** member to the number of entries in the **MacAddrs** array.

    -   For the *OidRequest* parameter, set the **BytesWritten** member to zero and the **BytesNeeded** member to the length, in bytes, of the entire DOT11\_MAC\_ADDRESS\_LIST structure.

    -   Fail the query request by returning NDIS\_STATUS\_BUFFER\_OVERFLOW from its [*MiniportOidRequest*](miniportoidrequest.md) function.

-   If the value of the **InformationBufferLength** member is greater than or equal to than the length, in bytes, of the entire DOT11\_MAC\_ADDRESS\_LIST structure, the miniport driver must do the following to complete a successful query request:

    -   For the DOT11\_MAC\_ADDRESS\_LIST structure, set the **uNumOfEntries** and **uTotalNumOfEntries** members to the total number of entries in the **MacAddrs** array.

    -   For the *OidRequest* parameter, set the **BytesNeeded** member to zero and the **BytesWritten** member to the length, in bytes, of the entire DOT11\_MAC\_ADDRESS\_LIST structure. The miniport driver must also copy the entire DOT11\_MAC\_ADDRESS\_LIST structure to the **InformationBuffer** member.

    -   Return NDIS\_STATUS\_SUCCESS from its [*MiniportOidRequest*](miniportoidrequest.md) function.

The default for the **msDot11ExcludedMacAddressList** MIB object is an empty list with **uNumEntries** set to zero. The miniport driver must set this MIB object to its default if any of the following occur:

-   The miniport driver's [*MiniportInitializeEx*](miniportinitializeex.md) function is called.

-   A method request of [OID\_DOT11\_RESET\_REQUEST](oid-dot11-reset-request.md) is made to reset the MAC layer of the 802.11 station and the **bSetDefaultMIB** member of the DOT11\_RESET\_REQUEST structure is **TRUE**.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Available in Windows Vista and later versions of the Windows operating systems.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Windot11.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[Native 802.11 Wireless LAN OIDs](https://msdn.microsoft.com/library/windows/hardware/ff560691)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_DOT11_EXCLUDED_MAC_ADDRESS_LIST%20%20RELEASE:%20%288/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


