---
title: OID_DOT11_SUPPORTED_COUNTRY_OR_REGION_STRING
author: windows-driver-content
description: When queried, the OID_DOT11_SUPPORTED_COUNTRY_OR_REGION_STRING object identifier (OID) requests that the miniport driver return a list of the country strings identifying the regulatory domains supported by the 802.11 station.
ms.assetid: a8efc910-898a-4790-9da8-79d216c7ccff
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_SUPPORTED_COUNTRY_OR_REGION_STRING Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_SUPPORTED\_COUNTRY\_OR\_REGION\_STRING


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When queried, the OID\_DOT11\_SUPPORTED\_COUNTRY\_OR\_REGION\_STRING object identifier (OID) requests that the miniport driver return a list of the country strings identifying the regulatory domains supported by the 802.11 station. For more information about country strings, refer to the IEEE 802.11d-2001 standard.

The data type for this OID is the DOT11\_COUNTRY\_OR\_REGION\_STRING\_LIST structure.

```ManagedCPlusPlus
    typedef struct DOT11_COUNTRY_OR_REGION_STRING_LIST {
         NDIS_OBJECT_HEADER Header;
         ULONG uNumOfEntries;
         ULONG uTotalNumOfEntries;
         DOT11_COUNTRY_OR_REGION_STRING CountryOrRegionStrings[1];
    } DOT11_COUNTRY_OR_REGION_STRING_LIST, *PDOT11_COUNTRY_OR_REGION_STRING_LIST;
  
```

This structure includes the following members:

<a href="" id="header"></a>**Header**  
The type, revision, and size of the DOT11\_COUNTRY\_OR\_REGION\_STRING\_LIST structure. This member is formatted as an [**NDIS\_OBJECT\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff566588) structure.

The miniport driver must set the members of **Header** to the following values:

<a href="" id="type"></a>**Type**  
This member must be set to NDIS\_OBJECT\_TYPE\_DEFAULT.

<a href="" id="revision"></a>**Revision**  
This member must be set to DOT11\_COUNTRY\_OR\_REGION\_STRING\_LIST\_REVISION\_1.

<a href="" id="size"></a>**Size**  
This member must be set to sizeof(DOT11\_COUNTRY\_OR\_REGION\_STRING\_LIST).

For more information about these members, see [**NDIS\_OBJECT\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff566588).

<a href="" id="unumofentries"></a>**uNumOfEntries**  
Number of entries in the **CountryOrRegionStrings** array. A zero value for this member indicates an empty country string list.

<a href="" id="utotalnumofentries"></a>**uTotalNumOfEntries**  
Maximum number of entries that the **CountryOrRegionStrings** array can contain.

<a href="" id="countryorregionstrings"></a>**CountryOrRegionStrings**  
The list of supported 802.11d country strings. For more information about the data type of this member, see [**DOT11\_COUNTRY\_OR\_REGION\_STRING**](dot11-country-or-region-string.md).

When OID\_DOT11\_SUPPORTED\_COUNTRY\_OR\_REGION\_STRING is queried, the miniport driver must verify that the **InformationBuffer** member of the [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function's *OidRequest* parameter is large enough to return the entire DOT11\_COUNTRY\_OR\_REGION\_STRING\_LIST structure, including all entries in the **CountryOrRegionStrings** array. The value of the **InformationBufferLength** member of the *OidRequest* parameter determines what the miniport driver must do, as the following list shows:

-   If the value of the **InformationBufferLength** member is less than the length, in bytes, of the entire DOT11\_COUNTRY\_OR\_REGION\_STRING\_LIST structure, the miniport driver must do the following:

    -   Set the **uNumOfEntries** member to zero.

    -   Set the **uTotalNumOfEntries** member to the number of entries in the **CountryOrRegionStrings** array.

    -   For the *OidRequest* parameter, set the **BytesWritten** member to zero and the **BytesNeeded** member to the length, in bytes, of the entire DOT11\_COUNTRY\_OR\_REGION\_STRING\_LIST structure.

    -   Fail the query request by returning NDIS\_STATUS\_BUFFER\_OVERFLOW from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.

-   If the value of the **InformationBufferLength** member is greater than or equal to the length, in bytes, of the entire DOT11\_COUNTRY\_OR\_REGION\_STRING\_LIST structure, the miniport driver must do the following to complete a successful query request:

    -   For the DOT11\_COUNTRY\_OR\_REGION\_STRING\_LIST structure, set the **uNumOfEntries** and **uTotalNumOfEntries** members to the total number of entries in the **CountryOrRegionStrings** array.

    -   For the *OidRequest* parameter, set the **BytesNeeded** member to zero and the **BytesWritten** member to the length, in bytes, of the entire DOT11\_COUNTRY\_OR\_REGION\_STRING\_LIST structure. The miniport driver must also copy the entire DOT11\_COUNTRY\_OR\_REGION\_STRING\_LIST structure to the **InformationBuffer** member.

    -   Return NDIS\_STATUS\_SUCCESS from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.

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

 

 




