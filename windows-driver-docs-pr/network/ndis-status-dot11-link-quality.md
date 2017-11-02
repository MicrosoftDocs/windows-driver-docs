---
title: NDIS_STATUS_DOT11_LINK_QUALITY
author: windows-driver-content
description: A miniport driver makes the NDIS_STATUS_DOT11_LINK_QUALITY indication whenever the link quality of the association with an access point (AP) or peer station changes.
ms.assetid: 911397fd-e898-4970-9a1b-7baf57e16687
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -NDIS_STATUS_DOT11_LINK_QUALITY Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_DOT11\_LINK\_QUALITY


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

A miniport driver makes the NDIS\_STATUS\_DOT11\_LINK\_QUALITY indication whenever the link quality of the association with an access point (AP) or peer station changes.

The data type for this indication is the DOT11\_LINK\_QUALITY\_PARAMETERS structure:

```ManagedCPlusPlus
    typedef struct DOT11_LINK_QUALITY_PARAMETERS {
         NDIS_OBJECT_HEADER Header;
         ULONG uLinkQualityListSize;
         ULONG uLinkQualityListOffset;
    } DOT11_LINK_QUALITY_PARAMETERS,   *PDOT11_LINK_QUALITY_PARAMETERS;
  
```

The DOT11\_LINK\_QUALITY\_PARAMETERS structure contains the following members:

<a href="" id="header"></a>**Header**  
The type, revision, and size of the DOT11\_LINK\_QUALITY\_PARAMETERS structure. This member is formatted as an [**NDIS\_OBJECT\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff566588) structure.

The miniport driver must set the members of **Header** to the following values:

<a href="" id="type"></a>**Type**  
This member must be set to NDIS\_OBJECT\_TYPE\_DEFAULT.

<a href="" id="revision"></a>**Revision**  
This member must be set to DOT11\_LINK\_QUALITY\_PARAMETERS\_REVISION\_1.

<a href="" id="size"></a>**Size**  
This member must be set to sizeof(DOT11\_LINK\_QUALITY\_PARAMETERS).

For more information about these members, see [**NDIS\_OBJECT\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff566588).

<a href="" id="ulinkqualitylistsize"></a>**uLinkQualityListSize**  
The number of entries in the link quality list.

<a href="" id="ulinkqualitylistoffset"></a>**uLinkQualityListOffset**  
The offset of the link quality list. Each entry in the list specifies an association to an AP or peer station whose link quality has changed.

This offset is relative to the start of the buffer that contains the DOT11\_LINK\_QUALITY\_PARAMETERS structure.

Each entry in the link quality list is formatted as a DOT11\_LINK\_QUALITY\_ENTRY structure:

``` syntax
typedef struct DOT11_LINK_QUALITY_ENTRY {         DOT11_MAC_ADDRESS PeerMacAddr;
 UCHAR
 ucLinkQuality; } DOT11_LINK_QUALITY_ENTRY, *PDOT11_LINK_QUALITY_ENTRY;
```

The DOT11\_LINK\_QUALITY\_ENTRY structure contains the following members:

<a href="" id="peermacaddr"></a>**PeerMacAddr**  
The media access control (MAC) address of the AP or peer station with which the link quality has changed. This member is formatted as a [**DOT11\_MAC\_ADDRESS**](https://msdn.microsoft.com/library/windows/hardware/ff548681) structure.

<a href="" id="uclinkquality"></a>**ucLinkQuality**  
The link quality of the association, specified by a value within the range from 0 through 100.

The miniport driver must follow these guidelines when making the NDIS\_STATUS\_DOT11\_LINK\_QUALITY indication:

-   After the 802.11 station successfully associates with an AP or peer station, the miniport driver must make an NDIS\_STATUS\_DOT11\_LINK\_QUALITY indication shortly after it makes the [NDIS\_STATUS\_DOT11\_ASSOCIATION\_COMPLETION](ndis-status-dot11-association-completion.md) indication. The miniport driver makes this NDIS\_STATUS\_DOT11\_LINK\_QUALITY indication after it has determined the initial link quality of the association.

-   The miniport driver makes the Native 802.11 NDIS\_STATUS\_DOT11\_LINK\_QUALITY indication whenever the 802.11 station determines that the link quality to an associated AP or peer station has changed significantly since the last NDIS\_STATUS\_DOT11\_LINK\_QUALITY indication.

    The determination for making this indication is specific to the implementation by the independent hardware vendor (IHV). However, the miniport driver should implement some threshold mechanism to avoid making frequent indications.

-   Following each NDIS\_STATUS\_DOT11\_LINK\_QUALITY indication, the miniport driver must save the current link quality for each associated AP or peer station specified within the link quality list.

-   If the 802.11 station is connected to an independent basic service set (IBSS) network, the miniport driver can include entries in the link quality list for every associated peer station whose link quality has changed significantly since the last NDIS\_STATUS\_DOT11\_LINK\_QUALITY indication.

    **Note**  IBSS (Ad hoc) and SoftAP are deprecated. Starting with Windows 8.1 and Windows Server 2012 R2, use [Wi-Fi Direct](https://msdn.microsoft.com/library/windows/hardware/hh440289).

     

    If the 802.11 station is connected to an infrastructure BSS network, the link quality list must only contain an entry for the AP with which the 802.11 station is associated.

The miniport driver calls [**NdisMIndicateStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff563600) to make an NDIS\_STATUS\_DOT11\_LINK\_QUALITY indication, and must pass a pointer to an [**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373) structure through the *StatusIndication* parameter. When making this indication, the miniport driver must set the following members of the NDIS\_STATUS\_INDICATION structure:

-   **StatusCode** must be set to NDIS\_STATUS\_DOT11\_LINK\_QUALITY.

-   **StatusBuffer** must be set to the address of a DOT11\_LINK\_QUALITY\_PARAMETERS structure.

-   **StatusBufferSize** must be set to sizeof(DOT11\_LINK\_QUALITY\_PARAMETERS) plus the values of the **uLinkQualityListSize** and **uLinkQualityListOffset** members.

For more information about link quality and link quality indications, see [Link Quality Operations](https://msdn.microsoft.com/library/windows/hardware/ff557056).

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
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NDIS_STATUS_DOT11_LINK_QUALITY%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


