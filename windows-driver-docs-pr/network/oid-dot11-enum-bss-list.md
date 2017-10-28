---
title: OID_DOT11_ENUM_BSS_LIST
author: windows-driver-content
description: OID_DOT11_ENUM_BSS_LIST
ms.assetid: eaf6f81f-f420-4027-a45d-3c935c1b8b07
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_ENUM_BSS_LIST Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_ENUM\_BSS\_LIST


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When a method request of the OID\_DOT11\_ENUM\_BSS\_LIST OID is made, the miniport driver must return a list of the basic service set (BSS) networks within range of the 802.11 station. For more information about the method request type, see [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710).

The miniport driver derives this list from the cache of BSS networks that the 802.11 station detected during the most recent scan operation. For more information about scan operations, see [OID\_DOT11\_SCAN\_REQUEST](oid-dot11-scan-request.md).

When the method request of OID\_DOT11\_ENUM\_BSS\_LIST is made through a call to the miniport driver's [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function, the **InformationBuffer** member of the *OidRequest* parameter contains a three-character country string as defined in the IEEE 802.11d-2001 standard. For more information about country strings, see [OID\_DOT11\_COUNTRY\_STRING](oid-dot11-country-string.md).

The miniport driver completes the method request by overwriting the **InformationBuffer** member with a [**DOT11\_BYTE\_ARRAY**](https://msdn.microsoft.com/library/windows/hardware/ff547670) structure. The miniport driver sets the members of this structure as follows:

<a href="" id="header"></a>**Header**  
The type and size of the DOT11\_BYTE\_ARRAY structure and the revision of the [**DOT11\_BSS\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/ff547665) structures that follow it. This member is formatted as an [**NDIS\_OBJECT\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff566588) structure.

The miniport driver must set the members of **Header** to the following values:

<a href="" id="type"></a>**Type**  
This member must be set to NDIS\_OBJECT\_TYPE\_DEFAULT.

<a href="" id="revision"></a>**Revision**  
This member must be set to DOT11\_BSS\_ENTRY\_BYTE\_ARRAY\_REVISION\_1.

<a href="" id="size"></a>**Size**  
This member must be set to `sizeof(DOT11_BYTE_ARRAY)`.

For more information about these members, see [**NDIS\_OBJECT\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff566588).

<a href="" id="unumofbytes"></a>**uNumOfBytes**  
Number of bytes within the **ucBuffer** array. A zero value for this member indicates an empty BSS list.

<a href="" id="utotalnumofbytes"></a>**uTotalNumOfBytes**  
Maximum number of bytes that the **ucBuffer** array requires.

<a href="" id="ucbuffer"></a>**ucBuffer**  
The BSS list.

Each entry in the BSS list is formatted as a [**DOT11\_BSS\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/ff547665) structure.

When this OID is queried, the miniport driver must do the following:

-   Verify that the **InformationBuffer** member of its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function's *OidRequest* parameter is large enough to return the BSS list. For more information about this procedure, see [**DOT11\_BYTE\_ARRAY**](https://msdn.microsoft.com/library/windows/hardware/ff547670).

-   The [**DOT11\_BSS\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/ff547665) structure has a variable length. However, the miniport driver must not add padding for alignment between DOT11\_BSS\_ENTRY structures returned in the **InformationBuffer** member of the *OidRequest* parameter.

-   Use the following formula for calculating the values of the **uNumOfBytes** and **uTotalNumOfBytes** members of the [**DOT11\_BYTE\_ARRAY**](https://msdn.microsoft.com/library/windows/hardware/ff547670) structure:

    ```
     FIELD_OFFSET(DOT11_BSS_ENTRY, ucBuffer) + uBufferLength 
    ```

-   If the 802.11 station is connected to an infrastructure BSS network, include an entry in the BSS list for the AP with which the 802.11 station is currently associated. The DOT11\_BSS\_ENTRY entry must reflect the last 802.11 Beacon or Probe Response frame received from the AP, regardless of whether these frames were received when the Native 802.11 miniport driver was performing the scan operation.

If an 802.11n PHY is used to detect the BSS network, the miniport driver should perform the following operations.

-   Set the **uPhyId** member of DOT11\_BSS\_ENTRY to the **dot11\_phy\_type\_ht** value.

-   Set the DOT11\_BSS\_ENTRY-&gt; **PhySpecificInfo** -&gt; **uChCenterFrequency** member to the appropriate channel center frequency, in MHz.

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
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_DOT11_ENUM_BSS_LIST%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


