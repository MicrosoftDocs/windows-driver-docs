---
title: OID_DOT11_EXTSTA_CAPABILITY
author: windows-driver-content
description: When queried, the OID\_DOT11\_EXTSTA\_CAPABILITY object identifier (OID) requests that the miniport driver return the sizes of various tables and lists supported by the 802.11 station.
ms.assetid: 0ecbaca2-67ab-4185-ae84-d72f52fffe39
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_EXTSTA_CAPABILITY Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_EXTSTA\_CAPABILITY


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When queried, the OID\_DOT11\_EXTSTA\_CAPABILITY object identifier (OID) requests that the miniport driver return the sizes of various tables and lists supported by the 802.11 station.

The data type for this OID is the DOT11\_EXTSTA\_CAPABILITY structure.

```ManagedCPlusPlus
    typedef struct DOT11_EXTSTA_CAPABILITY {
         NDIS_OBJECT_HEADER Header;
         ULONG uScanSSIDListSize;
         ULONG uDesiredBSSIDListSize;
         ULONG uDesiredSSIDListSize;
         ULONG uExcludedMacAddressListSize;
         ULONG uPrivacyExemptionListSize;
         ULONG uKeyMappingTableSize;
         ULONG uDefaultKeyTableSize;
         ULONG uWEPKeyValueMaxLength;
         ULONG uPMKIDCacheSize;
         ULONG uMaxNumPerSTADefaultKeyTables;
    } DOT11_EXTSTA_CAPABILITY, *PDOT11_EXTSTA_CAPABILITY;
  
```

This structure includes the following members:

<a href="" id="header"></a>**Header**  
The type, revision, and size of the DOT11\_EXTSTA\_CAPABILITY structure. This member is formatted as an [**NDIS\_OBJECT\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff566588) structure.

The miniport driver must set the members of **Header** to the following values:

<a href="" id="type"></a>**Type**  
This member must be set to NDIS\_OBJECT\_TYPE\_DEFAULT.

<a href="" id="revision"></a>**Revision**  
This member must be set to DOT11\_EXTSTA\_CAPABILITY\_REVISION\_1.

<a href="" id="size"></a>**Size**  
This member must be set to sizeof(DOT11\_EXTSTA\_CAPABILITY).

For more information about these members, see [**NDIS\_OBJECT\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff566588).

<a href="" id="uscanssidlistsize"></a>**uScanSSIDListSize**  
The maximum number of service set identifiers (SSIDs) supported by the 802.11 station for scan operations. The 802.11 station must support an SSID list of at least four entries.

The SSID list that the 802.11 station uses for scanning is specified when [OID\_DOT11\_SCAN\_REQUEST](oid-dot11-scan-request.md) is set.

<a href="" id="udesiredbssidlistsize"></a>**uDesiredBSSIDListSize**  
The maximum number of entries in the desired list of basic service set identifiers (BSSIDs) supported by the 802.11 station. The 802.11 station must support a BSSID list with at least one entry.

For more information about the desired BSSID list, see [OID\_DOT11\_DESIRED\_BSSID\_LIST](oid-dot11-desired-bssid-list.md).

<a href="" id="udesiredssidlistsize"></a>**uDesiredSSIDListSize**  
The maximum number of entries in the desired SSID list supported by the 802.11 station. The 802.11 station must support a desired SSID list with at least one entry.

For more information about the desired SSID list, see [OID\_DOT11\_DESIRED\_SSID\_LIST](oid-dot11-desired-ssid-list.md).

<a href="" id="uexcludedmacaddresslistsize"></a>**uExcludedMacAddressListSize**  
The maximum number of entries in the excluded MAC address list supported by the 802.11 station. The 802.11 station must support an excluded MAC address list with at least four entries.

For more information about the desired excluded MAC address list, see [OID\_DOT11\_EXCLUDED\_MAC\_ADDRESS\_LIST](oid-dot11-excluded-mac-address-list.md).

<a href="" id="uprivacyexemptionlistsize"></a>**uPrivacyExemptionListSize**  
The maximum number of entries in the privacy exemption list supported by the 802.11 station. The 802.11 station must support a privacy exemption list with at least one entry.

For more information about the privacy exemption list, see [OID\_DOT11\_PRIVACY\_EXEMPTION\_LIST](oid-dot11-privacy-exemption-list.md).

<a href="" id="ukeymappingtablesize"></a>**uKeyMappingTableSize**  
The maximum number of cipher key-mapping keys supported by the 802.11 station. It is recommended that the 802.11 station support at least 32 key-mapping keys.

For more information about key mapping keys, see [OID\_DOT11\_CIPHER\_KEY\_MAPPING\_KEY](oid-dot11-cipher-key-mapping-key.md)

<a href="" id="udefaultkeytablesize"></a>**uDefaultKeyTableSize**  
The maximum number of cipher keys the 802.11 station supports for the default key and per-station default key tables. For more information about default keys and per-station default keys, see [802.11 Cipher Key Types](https://msdn.microsoft.com/library/windows/hardware/ff543625).

For standard 802.11 cipher algorithms, the 802.11 station must support a table size of at least four cipher keys. For cipher algorithms developed by the independent hardware vendor (IHV), the table size can be four or greater.

<a href="" id="uwepkeyvaluemaxlength"></a>**uWEPKeyValueMaxLength**  
The maximum length, in bytes, of a WEP cipher key supported by the 802.11 station.

The following table lists the minimum and maximum key lengths, in bytes, for the various WEP cipher enumerator values defined through [**DOT11\_CIPHER\_ALGORITHM**](https://msdn.microsoft.com/library/windows/hardware/ff547672).

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>WEP cipher</th>
<th>Minimum key length</th>
<th>Maximum key length</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>DOT11_CIPHER_ALGO_WEP40</strong></p></td>
<td><p>5</p></td>
<td><p>5</p></td>
</tr>
<tr class="even">
<td><p><strong>DOT11_CIPHER_ALGO_WEP104</strong></p></td>
<td><p>13</p></td>
<td><p>13</p></td>
</tr>
<tr class="odd">
<td><p><strong>DOT11_CIPHER_ALGO_WEP</strong></p></td>
<td><p>13</p></td>
<td><p>Any length supported by the 802.11 station</p></td>
</tr>
</tbody>
</table>

 

<a href="" id="upmkidcachesize"></a>**uPMKIDCacheSize**  
The maximum number of entries in the pairwise master key identifier (PMKID) cache supported by the 802.11 station.

If the 802.11 station does not support a PMKID cache, the miniport driver must set this member to zero. Otherwise, the 802.11 station must support a PMKID cache size of at least three entries.

For more information about the PMKID cache, see [OID\_DOT11\_PMKID\_LIST](oid-dot11-pmkid-list.md).

<a href="" id="umaxnumperstadefaultkeytables"></a>**uMaxNumPerSTADefaultKeyTables**  
The maximum number of per station default cipher key tables supported by the 802.11 station. It is recommended that the 802.11 station support at least 32 per-station default cipher key tables.

For more information about per-station default cipher key tables, see [Per-Station Default Keys](https://msdn.microsoft.com/library/windows/hardware/ff570016).

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
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_DOT11_EXTSTA_CAPABILITY%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


