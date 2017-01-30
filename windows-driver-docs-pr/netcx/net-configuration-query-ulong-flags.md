---
title: NET_CONFIGURATION_QUERY_ULONG_FLAGS enumeration
description: The NET\_CONFIGURATION\_QUERY\_ULONG\_FLAGS enumeration is used as an input parameter to the NetConfigurationQueryUlong method.
ms.assetid: 6396d551-5e78-4bb1-adcc-ce9a0ac84849
keywords: ["NET_CONFIGURATION_QUERY_ULONG_FLAGS enumeration Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NET_CONFIGURATION_QUERY_ULONG_FLAGS
api_location:
- netconfiguration.h
api_type:
- HeaderDef
---

# NET\_CONFIGURATION\_QUERY\_ULONG\_FLAGS enumeration


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The **NET\_CONFIGURATION\_QUERY\_ULONG\_FLAGS** enumeration is used as an input parameter to the [**NetConfigurationQueryUlong**](netconfigurationqueryulong.md) method.

Syntax
------

```ManagedCPlusPlus
typedef enum _NET_CONFIGURATION_QUERY_ULONG_FLAGS { 
  NET_CONFIGURATION_QUERY_ULONG_NO_FLAGS                     = = 0x00000000,
  NET_CONFIGURATION_QUERY_ULONG_MAY_BE_STORED_AS_HEX_STRING  = = 0x00000001
} NET_CONFIGURATION_QUERY_ULONG_FLAGS;
```

Constants
---------

<a href="" id="net-configuration-query-ulong-no-flags"></a>**NET\_CONFIGURATION\_QUERY\_ULONG\_NO\_FLAGS**  
No flags are set.

<a href="" id="net-configuration-query-ulong-may-be-stored-as-hex-string"></a>**NET\_CONFIGURATION\_QUERY\_ULONG\_MAY\_BE\_STORED\_AS\_HEX\_STRING**  
Specifies that the ULONG may be stored in the configuration database as a string in hex format.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Minimum KMDF version</p></td>
<td align="left"><p>1.21</p></td>
</tr>
<tr class="even">
<td align="left"><p>Minimum NetAdapterCx version</p></td>
<td align="left"><p>1.0</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Netconfiguration.h</td>
</tr>
</tbody>
</table>

 

 





