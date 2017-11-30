---
title: OID_DOT11_PMKID_LIST
author: windows-driver-content
description: When set, the OID_DOT11_PMKID_LIST object identifier (OID) requests that the miniport driver flush its cache of pairwise master key identifiers (PMKIDs) and add the PMKID entries from the specified list to its cache.
ms.assetid: 815a29e6-29f6-4a7d-82cb-40d4d6cedc25
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_PMKID_LIST Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_PMKID\_LIST


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When set, the OID\_DOT11\_PMKID\_LIST object identifier (OID) requests that the miniport driver flush its cache of pairwise master key identifiers (PMKIDs) and add the PMKID entries from the specified list to its cache.

When queried, this OID requests that the miniport driver return a list of the entries from its PMKID cache.

The 802.11 station uses the PMKID cache for preauthentication to access points that have enabled the Robust Security Network Association (RSNA) authentication algorithm. If the 802.11 station is associating or reassociating to a BSSID that matches an entry in its PMKID cache, the 802.11 station must use the PMKID data in the RSN information element (RSN IE) of its Association or Reassociation frame. For more information about the RSN IE, refer to Clause 7.3.2.25 of the 802.11i-2004 standard.

**Note**  Support for OID\_DOT11\_PMKID\_LIST is mandatory if the 802.11 station supports PMKID caching for the **DOT11\_AUTH\_ALGO\_RSNA** authentication algorithms. The miniport driver specifies its support for this authentication algorithm when [OID\_DOT11\_SUPPORTED\_UNICAST\_ALGORITHM\_PAIR](oid-dot11-supported-unicast-algorithm-pair.md) or [OID\_DOT11\_SUPPORTED\_MULTICAST\_ALGORITHM\_PAIR](oid-dot11-supported-multicast-algorithm-pair.md) are queried.

 

The data type for OID\_DOT11\_PMKID\_LIST is the DOT11\_PMKID\_LIST structure.

```ManagedCPlusPlus
    typedef struct DOT11_PMKID_LIST {
         NDIS_OBJECT_HEADER Header; 
         ULONG uNumOfEntries;
         ULONG uTotalNumOfEntries;
         DOT11_PMKID_ENTRY PMKIDs[1];
    } DOT11_PMKID_LIST, *PDOT11_PMKID_LIST;
  
```

This structure includes the following members:

<a href="" id="header"></a>**Header**  
The type, revision, and size of the DOT11\_PMKID\_LIST structure. This member is formatted as an [**NDIS\_OBJECT\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff566588) structure.

The miniport driver must set the members of **Header** to the following values:

<a href="" id="type"></a>**Type**  
This member must be set to NDIS\_OBJECT\_TYPE\_DEFAULT.

<a href="" id="revision"></a>**Revision**  
This member must be set to DOT11\_PMKID\_LIST\_REVISION\_1.

<a href="" id="size"></a>**Size**  
This member must be set to sizeof(DOT11\_PMKID\_LIST).

For more information about these members, see [**NDIS\_OBJECT\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff566588).

<a href="" id="unumofentries"></a>**uNumOfEntries**  
Number of entries in the **PMKIDs** array. A zero value for this member indicates an empty list of PMKID entries.

<a href="" id="utotalnumofentries"></a>**uTotalNumOfEntries**  
Maximum number of entries that the **PMKIDs** array can contain.

<a href="" id="pmkids"></a>**PMKIDs**  
The list of PMKID entries.

The data type for the elements of the **PMKIDs** array is the DOT11\_PMKID\_ENTRY structure.

``` syntax
typedef struct DOT11_PMKID_ENTRY {         
         DOT11_MAC_ADDRESS BSSID;
         DOT11_PMKID_VALUE PMKID; 
         ULONG uFlags;   
     } DOT11_PMKID_ENTRY, *PDOT11_PMKID_ENTRY;
```

This structure includes the following members:

<a href="" id="bssid"></a>**BSSID**  
The BSSID of the target access point (AP) with which the 802.11 station associates. For more information about the data type of this member, see [**DOT11\_MAC\_ADDRESS**](https://msdn.microsoft.com/library/windows/hardware/ff548681).

<a href="" id="pmkid"></a>**PMKID**  
The PMKID value. For more information about the data type of this member, see [**DOT11\_PMKID\_VALUE**](dot11-pmkid-value.md).

The 802.11 station uses this value in the RSN information element (IE) of the 802.11 Association or Reassociation Request frames when connecting to the target BSSID.

**Note**  When OID\_DOT11\_PMKID\_LIST is set, the entries in the **PMKIDs** array might be different than the entries in the list of PMKID candidates that the miniport driver specified when it made a previous [NDIS\_STATUS\_DOT11\_PMKID\_CANDIDATE\_LIST](ndis-status-dot11-pmkid-candidate-list.md) indication.

 

<a href="" id="uflags"></a>**uFlags**  
This member is reserved and must be set to zero.

When OID\_DOT11\_PMKID\_LIST is set, the miniport driver must do the following:

-   If the **uNumOfEntries** member has a value greater than the value of **uPMKIDCacheSize** that the driver previously returned through a query of [OID\_DOT11\_EXTSTA\_CAPABILITY](oid-dot11-extsta-capability.md), fail the set request by returning NDIS\_STATUS\_INVALID\_LENGTH from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.

-   If the 802.11 station does not support the **DOT11\_AUTH\_ALGO\_RSNA** authentication algorithm, fail the request by returning NDIS\_STATUS\_NOT\_SUPPORTED from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.

-   If the 802.11 station has not enabled the **DOT11\_AUTH\_ALGO\_RSNA** authentication algorithm, fail the request by returning NDIS\_STATUS\_INVALID\_DATA from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.

-   Ignore any list entry that has a **BSSID** member that is not in the miniport driver's desired BSSID list. For more information about the desired BSSID list, see [OID\_DOT11\_DESIRED\_BSSID\_LIST](oid-dot11-desired-bssid-list.md).

    If none of the entries in the list has a **BSSID** member that matches an entry in the miniport driver's desired BSSID list, the miniport driver must fail the request by returning NDIS\_STATUS\_INVALID\_DATA from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.

-   Ensure that the value of the **InformationBufferLength** member of the [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function's OidRequest parameter is at least the value returned by the following formula:

    ```
    FIELD_OFFSET(DOT11_PMKID_LIST, PMKIDs) + uNumOfEntries * sizeof(DOT11_PMKID_ENTRY))
    ```

When OID\_DOT11\_PMKID\_LIST is queried, the miniport driver must verify that the **InformationBuffer** member of the [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function's *OidRequest* parameter is large enough to return the entire DOT11\_PMKID\_LIST structure, including all entries in the **PMKIDs** array. The value of the **InformationBufferLength** member of the *OidRequest* parameter determines what the miniport driver must do, as the following list shows:

-   If the value of the **InformationBufferLength** member is less than the length, in bytes, of the entire DOT11\_PMKID\_LIST structure, the miniport driver must do the following:

    -   Set the **uNumOfEntries** member to zero.

    -   Set the **uTotalNumOfEntries** member to the number of entries in the **PMKIDs** array.

        For the *OidRequest* parameter, set the **BytesWritten** member to zero and the **BytesNeeded** member to the length, in bytes, of the entire DOT11\_PMKID\_LIST structure.

    -   Fail the query request by returning NDIS\_STATUS\_BUFFER\_OVERFLOW from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.

-   If the value of the **InformationBufferLength** member is greater than or equal to than the length, in bytes, of the entire DOT11\_PMKID\_LIST structure, the miniport driver must do the following to complete a successful query request:

    -   For the DOT11\_PMKID\_LIST structure, set the **uNumOfEntries** and **uTotalNumOfEntries** members to the total number of entries in the **PMKIDs** array.

    -   For the *OidRequest* parameter, set the **BytesNeeded** member to zero and the **BytesWritten** member to the length, in bytes, of the entire DOT11\_PMKID\_LIST structure. The miniport driver must also copy the entire DOT11\_PMKID\_LIST structure to the **InformationBuffer** member.

    -   Return NDIS\_STATUS\_SUCCESS from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.

The default PMKID cache is an empty list with **uNumEntries** set to zero. The miniport driver must set this cache to its default if any of the following occurs:

-   The miniport driver's [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function is called.

-   A method request of [OID\_DOT11\_RESET\_REQUEST](oid-dot11-reset-request.md) is made. The miniport driver must unconditionally set the PMKID cache to its default value whenever OID\_DOT11\_RESET\_REQUEST is set.

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
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_DOT11_PMKID_LIST%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


