---
title: NDIS_STATUS_DOT11_PMKID_CANDIDATE_LIST
author: windows-driver-content
description: A miniport driver uses the NDIS_STATUS_DOT11_PMKID_CANDIDATE_LIST indication to request pairwise master key identifiers (PMKIDs) for basic service set (BSS) identifiers (BSSIDs) that the 802.11 station can potentially roam to.
ms.assetid: 5c0376f3-71e3-4fa6-89e5-6580fc85cfa8
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -NDIS_STATUS_DOT11_PMKID_CANDIDATE_LIST Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_DOT11\_PMKID\_CANDIDATE\_LIST


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

A miniport driver uses the NDIS\_STATUS\_DOT11\_PMKID\_CANDIDATE\_LIST indication to request pairwise master key identifiers (PMKIDs) for basic service set (BSS) identifiers (BSSIDs) that the 802.11 station can potentially roam to. When roaming, the 802.11 station uses the PMKID value to pre-authenticate with an access point (AP).

The data type for this indication is the DOT11\_PMKID\_CANDIDATE\_LIST\_PARAMETERS structure:

```ManagedCPlusPlus
    typedef struct DOT11_PMKID_CANDIDATE_LIST_PARAMETERS {
         NDIS_OBJECT_HEADER Header;
         ULONG uCandidateListSize;
         ULONG uCandidateListOffset;
    } DOT11_PMKID_CANDIDATE_LIST_PARAMETERS,   *PDOT11_PMKID_CANDIDATE_LIST_PARAMETERS;
  
```

The DOT11\_PMKID\_CANDIDATE\_LIST\_PARAMETERS structure contains the following members:

<a href="" id="header"></a>**Header**  
The type, revision, and size of the DOT11\_PMKID\_CANDIDATE\_LIST\_PARAMETERS structure. This member is formatted as an [**NDIS\_OBJECT\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff566588) structure.

The miniport driver must set the members of **Header** to the following values:

<a href="" id="type"></a>**Type**  
This member must be set to NDIS\_OBJECT\_TYPE\_DEFAULT.

<a href="" id="revision"></a>**Revision**  
This member must be set to DOT11\_PMKID\_CANDIDATE\_LIST\_PARAMETERS\_REVISION\_1.

<a href="" id="size"></a>**Size**  
This member must be set to sizeof(DOT11\_PMKID\_CANDIDATE\_LIST\_PARAMETERS).

For more information about these members, see [**NDIS\_OBJECT\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff566588).

<a href="" id="ucandidatelistsize"></a>**uCandidateListSize**  
The size, in bytes, of the list of BSSID candidates for PMKIDs.

<a href="" id="ucandidatelistoffset"></a>**uCandidateListOffset**  
The offset of the BSSID candidate list.

This offset is relative to the start of the buffer that contains the DOT11\_PMKID\_CANDIDATE\_LIST\_PARAMETERS structure.

Each entry in the BSSID candidate list is formatted as a DOT11\_BSSID\_CANDIDATE structure:

``` syntax
typedef struct DOT11_BSSID_CANDIDATE {         
         DOT11_MAC_ADDRESS BSSID;
         ULONG uFlags;   
     } DOT11_BSSID_CANDIDATE, *PDOT11_BSSID_CANDIDATE;
```

The DOT11\_BSSID\_CANDIDATE structure contains the following members:

<a href="" id="bssid"></a>**BSSID**  
The BSSID of the AP for which the miniport driver is requesting a PMKID.

BSSID candidates that are specified by the **BSSID** member must:

-   Be in the service set identifier (SSID) that the 802.11 station is currently associated with.

-   Match an entry in the desired BSSID list that is defined by the Extensible Station (ExtSTA) **msDot11DesiredBSSIDList** MIB object. For more information about this MIB object, see [OID\_DOT11\_DESIRED\_BSSID\_LIST](oid-dot11-desired-bssid-list.md).

-   Be a member of the SSID with which the 802.11 station is currently associated and authenticated with.

**Note**  The miniport can only request a PMKID for the AP with which the 802.11 station is currently associated.

 

<a href="" id="uflags"></a>**uFlags**  
A bitmask that specifies pre-authentication attributes of the BSSID candidates. This bitmask is defined as follows:

<a href="" id="dot11-pmkid-candidate-preauth-enabled"></a>DOT11\_PMKID\_CANDIDATE\_PREAUTH\_ENABLED  
The BSSID candidate supports pre-authentication. The BSSID candidate advertises its support for pre-authentication by setting the Pre-authentication Subfield of the RSN Capabilities field to one in the 802.11 Beacon and Probe Response frames that the BSSID candidate transmits.

If the DOT11\_PMKID\_CANDIDATE\_PREAUTH\_ENABLED bit is set, the 802.1X supplicant will initiate the 802.1X pre-authentication with the specified BSSID candidate.

If the DOT11\_PMKID\_CANDIDATE\_PREAUTH\_ENABLED bit is not set, pre-authentication cannot be performed with the BSSID candidate. However, the 802.1X supplicant can update the driver's PMKID cache by using the PMK from a prior association with the BSSID candidate.

Pre-authentication applies to infrastructure networks that support Robust Security Network Association (RSNA) authentication. For more information about RSNA authentication, refer to Clause 8.4.6 of the IEEE 802.11i-2004 standard.

The miniport driver calls [**NdisMIndicateStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff563600) to make an NDIS\_STATUS\_DOT11\_PMKID\_CANDIDATE\_LIST indication, and must pass a pointer to an [**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373) structure through the *StatusIndication* parameter. When making this indication, the driver must set the following members of the NDIS\_STATUS\_INDICATION structure:

-   **StatusCode** must be set to NDIS\_STATUS\_DOT11\_PMKID\_CANDIDATE\_LIST.

-   **StatusBuffer** must be set to the address of a DOT11\_LINK\_QUALITY\_PARAMETERS structure.

-   **StatusBufferSize** must be set to sizeof(DOT11\_PMKID\_CANDIDATE\_LIST\_PARAMETERS) plus the values of the **uCandidateListSize** and **uCandidateListoffset** members.

The miniport driver can make the NDIS\_STATUS\_DOT11\_PMKID\_CANDIDATE\_LIST indication only if:

-   The IEEE 802.11 **dot11DesiredBSSType** MIB object is set to **dot11\_BSS\_type\_infrastructure**. For more information about this MIB object, see [OID\_DOT11\_DESIRED\_BSS\_TYPE](oid-dot11-desired-bss-type.md).

-   The 802.11 station has associated with a BSS that supports RSNA authentication.

When it makes the NDIS\_STATUS\_DOT11\_PMKID\_CANDIDATE\_LIST indication, the miniport driver must do the following:

-   Order the PMKID candidate list from most preferred to least preferred.

    The miniport driver can use any criteria to define the preference order. For example, the miniport driver can order the PMKID candidate list based on RSSI strength.

-   Set the number of entries in the PMKID candidate list to a value less than or equal to the value of **uPMKIDCacheSize**, which the driver returned when [OID\_DOT11\_EXTSTA\_CAPABILITY](oid-dot11-extsta-capability.md) was previously queried.

-   Be associated with an RSNA-capable AP and have transferred cipher keys to the 802.11 station through set requests of [OID\_DOT11\_CIPHER\_DEFAULT\_KEY](oid-dot11-cipher-default-key.md) or [OID\_DOT11\_CIPHER\_KEY\_MAPPING\_KEY](oid-dot11-cipher-key-mapping-key.md).

**Note**  The miniport must make an NDIS\_STATUS\_DOT11\_PMKID\_CANDIDATE\_LIST indication within one minute after it has completed the association with the AP and the cipher keys have been transferred to the 802.11 station.

 

While the 802.11 station is associated with the AP, the miniport driver may generate additional NDIS\_STATUS\_DOT11\_PMKID\_CANDIDATE\_LIST indications if the BSSID candidate list changes. The driver should keep the frequency of these indications to a minimum. For example, the driver should not make an NDIS\_STATUS\_DOT11\_PMKID\_CANDIDATE\_LIST indication if only one new entry was added to its BSSID candidate list. Instead, it must make the indication after the number of new entries inserted into its BSSID candidate list reaches a driver-specific threshold.

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
<td><p>Available in Windows Vista and later versions of the Windows operating systemss.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Windot11.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NDIS_STATUS_DOT11_PMKID_CANDIDATE_LIST%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


