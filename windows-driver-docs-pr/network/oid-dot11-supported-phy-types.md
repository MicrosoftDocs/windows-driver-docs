---
title: OID_DOT11_SUPPORTED_PHY_TYPES
author: windows-driver-content
description: When queried, the OID_DOT11_SUPPORTED_PHY_TYPES object identifier (OID) requests that the miniport driver return the value of the Native 802.11 Operational msDot11SupportedPhyTypes management information base (MIB) object.
ms.assetid: 4b267371-5e17-47d8-b521-bd4b130daa32
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_SUPPORTED_PHY_TYPES Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_SUPPORTED\_PHY\_TYPES


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When queried, the OID\_DOT11\_SUPPORTED\_PHY\_TYPES object identifier (OID) requests that the miniport driver return the value of the Native 802.11 Operational **msDot11SupportedPhyTypes** management information base (MIB) object. This MIB object defines the list of PHY types supported by the 802.11 station.

The data type for this OID is the DOT11\_SUPPORTED\_PHY\_TYPES structure.

```ManagedCPlusPlus
    typedef struct _DOT11_SUPPORTED_PHY_TYPES {
         ULONG uNumOfEntries;
         ULONG uTotalNumOfEntries;
         DOT11_PHY_TYPE dot11PHYType[1];
    } DOT11_SUPPORTED_PHY_TYPES, *PDOT11_SUPPORTED_PHY_TYPES;
  
```

This structure includes the following members:

<a href="" id="unumofentries"></a>**uNumOfEntries**  
Number of entries in the **dot11PhyType** array. A zero value for this member indicates an empty list of supported PHY types.

<a href="" id="utotalnumofentries"></a>**uTotalNumOfEntries**  
Maximum number of entries that the **dot11PhyType** array requires.

**Note**  The operating system supports a maximum of 64 entries for the **dot11PhyType** array.

 

<a href="" id="dot11phytype"></a>**dot11PhyType**  
The list of supported PHY types. Each entry in this list is specified through a [**DOT11\_PHY\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/ff548741) enumeration.

The following points apply to a miniport driver operating in Extensible Station (ExtSTA) mode:

-   When OID\_DOT11\_SUPPORTED\_PHY\_TYPES is queried, the miniport driver must add an entry in the **dot11PhyType** array for every PHY supported on the 802.11 station. If the 802.11 station supports proprietary or non-standard PHY types, the miniport driver must add an entry containing a PHY type value defined by the independent hardware vendor (IHV). For more information about IHV-defined PHY types, see [**DOT11\_PHY\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/ff548741).

    If the 802.11 station supports multiple PHYs of the same type, the miniport driver must add separate entries for each PHY.

-   The number of entries within the **dot11PhyType** array and the order of the entries within the array must remain unchanged during the lifetime of the installation of the miniport driver.

    For any PHY type supported by the 802.11 station, its index within the **dot11PhyType** array must persist and not change while the miniport driver is installed on the host computer system.

After OID\_DOT11\_SUPPORTED\_PHY\_TYPES is queried, the operating system will identify a PHY on the 802.11 station through one of the following methods:

-   If the miniport driver is operating in ExtSTA mode, the operating system will identify the PHY through a PHY identifier (ID). The PHY ID is the index into the list of PHYs returned in the **dot11PhyType** array. If the operating system specifies a PHY ID of DOT11\_PHY\_ID\_ANY, the miniport driver can use any supported PHY on the 802.11 station.

    The miniport driver will also use the PHY ID for Native 802.11 media-specific status indications. The miniport driver cannot use DOT11\_PHY\_ID\_ANY as a PHY ID for status indications. For more information about Native 802.11 media-specific status indications, see [Native 802.11 Wireless LAN Status Indications](https://msdn.microsoft.com/library/windows/hardware/ff560692).

-   If the miniport driver is not operating in ExtSTA mode, the operating system will identify the PHY through a PHY type as defined by a [**DOT11\_PHY\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/ff548741) enumeration value.

When OID\_DOT11\_SUPPORTED\_PHY\_TYPES is queried, the miniport driver must verify that the **InformationBuffer** member of the [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function's *OidRequest* parameter is large enough to return the entire DOT11\_SUPPORTED\_PHY\_TYPES structure, including all entries in the **dot11PhyType** array. The value of the **InformationBufferLength** member of the *OidRequest* parameter determines what the miniport driver must do, for example:

-   If the value of the **InformationBufferLength** member is less than the length, in bytes, of the entire DOT11\_SUPPORTED\_PHY\_TYPES structure, the miniport driver must do the following:

    -   For the *OidRequest* parameter, set the **BytesWritten** member to zero and the **BytesNeeded** member to the length, in bytes, of the entire DOT11\_SUPPORTED\_PHY\_TYPES structure.

    -   Fail the query request by returning NDIS\_STATUS\_BUFFER\_OVERFLOW from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.

-   If the value of the **InformationBufferLength** member is greater than or equal to the length, in bytes, of the entire DOT11\_SUPPORTED\_PHY\_TYPES structure, the miniport driver must do the following to complete a successful query request:

    -   For the DOT11\_SUPPORTED\_PHY\_TYPES structure, set the **uNumOfEntries** and **uTotalNumOfEntries** members to the total number of entries in the **dot11PhyType** array.

    -   For the *OidRequest* parameter, set the **BytesNeeded** member to zero and the **BytesWritten** member to the length, in bytes, of the entire DOT11\_SUPPORTED\_PHY\_TYPES structure. The miniport driver must also copy the entire DOT11\_SUPPORTED\_PHY\_TYPES structure to the **InformationBuffer** member.

    -   Return NDIS\_STATUS\_SUCCESS from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.

**Note**  If the miniport driver supports an 802.11n PHY, it must indicate this to the operating system as follows.
1.  During initialization of the miniport driver and 802.11 station, set the **dot11\_phy\_type\_ht** value in the NDIS\_MINIPORT\_ADAPTER\_NATIVE\_802\_11\_ATTRIBUTES-&gt;**SupportedPhyAttributes**-&gt;**PhyType** member.

2.  In response to an OID\_DOT11\_SUPPORTED\_PHY\_TYPES query, set the **dot11\_phy\_type\_ht** value in the DOT11\_SUPPORTED\_PHY\_TYPES-&gt;**dot11PhyType** member.

 

**Note**  If the miniport driver supports an 802.11ac PHY, it must indicate this to the operating system as follows.
1.  During initialization of the miniport driver and 802.11 station, set the **dot11\_phy\_type\_vht** value in the NDIS\_MINIPORT\_ADAPTER\_NATIVE\_802\_11\_ATTRIBUTES-&gt;**SupportedPhyAttributes**-&gt;**PhyType** member.

2.  In response to an OID\_DOT11\_SUPPORTED\_PHY\_TYPES query, set the **dot11\_phy\_type\_vht** value in the DOT11\_SUPPORTED\_PHY\_TYPES-&gt;**dot11PhyType** member.

 

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

 

 




