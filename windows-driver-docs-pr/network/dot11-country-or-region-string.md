---
title: DOT11\_COUNTRY\_OR\_REGION\_STRING
author: windows-driver-content
description: Important  The Native 802.11 Wireless LAN interface is deprecated in Windows 10 and later.
ms.assetid: f8302c7d-de43-45e4-a03b-d1bf2b0a9fc1
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords:
 - DOT11_COUNTRY_OR_REGION_STRING
---

# DOT11\_COUNTRY\_OR\_REGION\_STRING


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

The **DOT11\_COUNTRY\_OR\_REGION\_STRING** array defines an 802.11 regulatory domain. For more information about country strings and regulatory domains, refer to the IEEE 802.11d-2001 standard.

```ManagedCPlusPlus
typedef UCHAR DOT11_COUNTRY_OR_REGION_STRING[3];
```

**DOT11\_COUNTRY\_OR\_REGION\_STRING**  
A 3-byte string that identifies the country in which the 802.11 station is operating.

****  

Remarks
-------

The first two bytes of the **DOT11\_COUNTRY\_OR\_REGION\_STRING** array are the country code as described in the ISO/IEC 3166-1 standard. The third byte must be one of the following:

-   An ASCII space character (0x20) if the regulations under which the 802.11 station is operating encompass all environments in the country.

-   An ASCII 'O' character (0x4F) if the regulations under which the 802.11 station is operating are for an outdoor environment only.

-   An ASCII 'I' character (0x49) if the regulations under which the 802.11 station is operating are for an indoor environment only.

A **DOT11\_COUNTRY\_OR\_REGION\_STRING** array with a value of all zeros is used to specify a null country string.

The PDOT11\_COUNTRY\_OR\_REGION\_STRING type is defined as a pointer to the DOT11\_COUNTRY\_OR\_REGION\_STRING type as follows:

```
typedef DOT11_COUNTRY_OR_REGION_STRING  *PDOT11_COUNTRY_OR_REGION_STRING;
```

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


[OID\_DOT11\_DESIRED\_COUNTRY\_OR\_REGION\_STRING](oid-dot11-desired-country-or-region-string.md)

[OID\_DOT11\_SUPPORTED\_COUNTRY\_OR\_REGION\_STRING](oid-dot11-supported-country-or-region-string.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20DOT11_COUNTRY_OR_REGION_STRING%20%20RELEASE:%20%288/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


