---
title: NET_CONFIGURATION_QUERY_ULONG_FLAGS enumeration
topic_type:
- apiref
api_name:
- NET_CONFIGURATION_QUERY_ULONG_FLAGS
api_location:
- netconfiguration.h
api_type:
- HeaderDef
---

# NET_CONFIGURATION_QUERY_ULONG_FLAGS enumeration

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The **NET_CONFIGURATION_QUERY_ULONG_FLAGS** enumeration is used as an input parameter to the [**NetConfigurationQueryUlong**](netconfigurationqueryulong.md) method.

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

**NET_CONFIGURATION_QUERY_ULONG_NO_FLAGS**  
No flags are set.

**NET_CONFIGURATION_QUERY_ULONG_MAY_BE_STORED_AS_HEX_STRING**  
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

See Also
-----
[**NetConfigurationQueryUlong**](netconfigurationqueryulong.md)


