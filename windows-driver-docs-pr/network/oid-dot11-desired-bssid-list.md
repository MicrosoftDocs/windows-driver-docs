---
title: OID\_DOT11\_DESIRED\_BSSID\_LIST
author: windows-driver-content
description: When set, the OID\_DOT11\_DESIRED\_BSSID\_LIST object identifier (OID) requests that the miniport driver set the value of the Extensible Station (ExtSTA) msDot11DesiredBSSIDList management information base (MIB) object to the specified data.
ms.assetid: 17989e77-0a75-48f3-8fda-e9f9cf124f1a
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_DESIRED_BSSID_LIST Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_DESIRED\_BSSID\_LIST


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When set, the OID\_DOT11\_DESIRED\_BSSID\_LIST object identifier (OID) requests that the miniport driver set the value of the Extensible Station (ExtSTA) **msDot11DesiredBSSIDList** management information base (MIB) object to the specified data.

When queried, OID\_DOT11\_DESIRED\_BSSID\_LIST requests that the miniport driver return the value of the **msDot11DesiredBSSIDList** MIB object.

The **msDot11DesiredBSSIDList** MIB object specifies the list of 802.11 basic service set identifiers (BSSIDs) that the 802.11 station uses when connecting to a basic service set (BSS) network. After [OID\_DOT11\_CONNECT\_REQUEST](oid-dot11-connect-request.md) is set, the 802.11 station will attempt to connect to a BSS with a BSSID that matches an entry from this list.

The data type for this OID is the DOT11\_BSSID\_LIST structure.

```ManagedCPlusPlus
    typedef struct DOT11_BSSID_LIST {
         NDIS_OBJECT_HEADER Header;
         ULONG uNumOfEntries;
         ULONG uTotalNumOfEntries;
         DOT11_MAC_ADDRESS BSSIDs[1];
    } DOT11_BSSID_LIST, *PDOT11_BSSID_LIST;
  
```

This structure includes the following members:

<a href="" id="header"></a>**Header**  
The type, revision, and size of the DOT11\_BSSID\_LIST structure. This member is formatted as an [**NDIS\_OBJECT\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff566588) structure.

The miniport driver must set the members of **Header** to the following values:

<a href="" id="type"></a>**Type**  
This member must be set to NDIS\_OBJECT\_TYPE\_DEFAULT.

<a href="" id="revision"></a>**Revision**  
This member must be set to DOT11\_BSSID\_LIST\_REVISION\_1.

<a href="" id="size"></a>**Size**  
This member must be set to sizeof(DOT11\_BSSID\_LIST).

For more information about these members, see [**NDIS\_OBJECT\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff566588).

<a href="" id="unumofentries"></a>**uNumOfEntries**  
Number of entries in the **BSSIDs** array. A zero value for this member indicates an empty desired BSSID list.

<a href="" id="utotalnumofentries"></a>**uTotalNumOfEntries**  
Maximum number of entries that the **BSSIDs** array can contain.

<a href="" id="bssids"></a>**BSSIDs**  
The list of desired BSSIDs. For more information about the data type of this member, see [**DOT11\_MAC\_ADDRESS**](https://msdn.microsoft.com/library/windows/hardware/ff548681).

A wildcard BSSID has the value of 0xFFFFFFFFFFFF. The wildcard BSSID matches any BSSID.

A desired BSSID list containing the wildcard BSSID cannot contain other BSSIDs. When this OID is set, the miniport driver must fail the request by returning NDIS\_STATUS\_INVALID\_DATA from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function if the **BSSIDs** array contains a wildcard BSSID and **uNumOfEntries** is greater than one.

If the miniport driver's desired BSS type is set to **dot11\_BSS\_type\_infrastructure**, the 802.11 station can associate with a BSS only if the following are true:

-   The service set identifier (SSID) of the BSS is in the miniport driver's desired SSID list. If the desired SSID list contains the wildcard SSID, the 802.11 station can associate with any infrastructure BSS network.

    For more information about the wildcard SSID, see [**DOT11\_SSID**](https://msdn.microsoft.com/library/windows/hardware/ff548773).

-   The BSSID of an access point (AP) in the BSS is in the miniport driver's desired BSSID list. If the desired BSSID list contains the wildcard BSSID, the 802.11 station can associate with any AP in the BSS network.

If the miniport driver's desired BSS type is set to **dot11\_BSS\_type\_independent**, the 802.11 station can join or start an IBSS only if the following are true:

-   The SSID of the BSS is in the miniport driver's desired SSID list. If the desired SSID list contains the wildcard SSID, the 802.11 station can connect to any IBSS network.

-   If an IBSS is within range, the 802.11 station can connect if the BSSID of the IBSS is in the miniport driver's desired BSSID list. If the desired BSSID list contains the wildcard BSSID, the 802.11 station can associate with any IBSS within range.

-   If an IBSS is not within range, the 802.11 station must start the IBSS network. The 802.11 station uses the first entry from the desired BSSID list as the BSSID for the IBSS network. If the desired BSSID list contains the wildcard BSSID, the 802.11 station can use any locally administered unicast media access control (MAC) address as the BSSID for the IBSS network.

**Note**  The 802.11 station cannot connect to a BSS network or start an IBSS if its desired BSSID list is empty.

 

For more information about the desired BSS type, see [OID\_DOT11\_DESIRED\_BSS\_TYPE](oid-dot11-desired-bss-type.md).

For more information about the desired SSID list, see [OID\_DOT11\_DESIRED\_SSID\_LIST](oid-dot11-desired-ssid-list.md).

When OID\_DOT11\_DESIRED\_BSSID\_LIST is set, the miniport driver should ensure that the value of the **InformationBufferLength** member of the [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function's OidRequest parameter is at least the value returned by the following formula:

```
 FIELD_OFFSET(DOT11_BSSID_LIST, BSSIDs) + uNumOfEntries * sizeof(DOT11_MAC_ADDRESS))
```

When OID\_DOT11\_DESIRED\_BSSID\_LIST is set, the miniport driver must fail the set request if the **uNumOfEntries** member has a value greater than the value of **uDesiredBSSIDListSize** that the driver previously returned through a query of [OID\_DOT11\_EXTSTA\_CAPABILITY](oid-dot11-extsta-capability.md). In this situation, the miniport driver must return NDIS\_STATUS\_INVALID\_LENGTH from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.

When OID\_DOT11\_DESIRED\_BSSID\_LIST is queried, the miniport driver must verify that the **InformationBuffer** member of the [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function's *OidRequest* parameter is large enough to return the entire DOT11\_BSSID\_LIST structure, including all entries in the **BSSIDs** array. The value of the **InformationBufferLength** member of the *OidRequest* parameter determines what the miniport driver must do, as the following list shows:

-   If the value of the **InformationBufferLength** member is less than the length, in bytes, of the entire DOT11\_BSSID\_LIST structure, the miniport driver must do the following:

    -   Set the **uNumOfEntries** member to zero.

    -   Set the **uTotalNumOfEntries** member to the number of entries in the **BSSIDs** array.

    -   For the *OidRequest* parameter, set the **BytesWritten** member to zero and the **BytesNeeded** member to the length, in bytes, of the entire DOT11\_BSSID\_LIST structure.

    -   Fail the query request by returning NDIS\_STATUS\_BUFFER\_OVERFLOW from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.

-   If the value of the **InformationBufferLength** member is greater than or equal to than the length, in bytes, of the entire DOT11\_BSSID\_LIST structure, the miniport driver must do the following to complete a successful query request:

    -   For the DOT11\_BSSID\_LIST structure, set the **uNumOfEntries** and **uTotalNumOfEntries** members to the total number of entries in the **BSSIDs** array.

    -   For the *OidRequest* parameter, set the **BytesNeeded** member to zero and the **BytesWritten** member to the length, in bytes, of the entire DOT11\_BSSID\_LIST structure. The miniport driver must also copy the entire DOT11\_BSSID\_LIST structure to the **InformationBuffer** member.

    -   Return NDIS\_STATUS\_SUCCESS from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.

The default for the **msDot11DesiredBSSIDList** MIB object contains a single entry with **BSSIDs\[0\]** set to the wildcard BSSID and **uNumEntries** set to one. The miniport driver must set this MIB object to its default if any of the following occur:

-   The miniport driver's [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function is called.

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
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_DOT11_DESIRED_BSSID_LIST%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


