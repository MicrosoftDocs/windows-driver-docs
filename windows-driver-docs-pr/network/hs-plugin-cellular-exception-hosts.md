---
title: HS_PLUGIN_CELLULAR_EXCEPTION_HOSTS structure
description: The HS_PLUGIN_CELLULAR_EXCEPTION_HOSTS structure contains the list of hosts that the plugin requires to be connected over a cellular bearer only during the authentication process.
keywords: 
- HS_PLUGIN_CELLULAR_EXCEPTION_HOSTS structure Network Drivers Starting with Windows Vista
- PHS_PLUGIN_CELLULAR_EXCEPTION_HOSTS structure pointer Network Drivers Starting with Windows Vista
ms.date: 07/31/2017
ms.topic: reference
---

# HS\_PLUGIN\_CELLULAR\_EXCEPTION\_HOSTS structure

[!include[Wi-Fi Hotspot Offloading deprecation](../includes/wi-fi-hotspot-offloading-deprecation.md)]


The **HS\_PLUGIN\_CELLULAR\_EXCEPTION\_HOSTS** structure contains the list of hosts that the plugin requires to be connected over a cellular bearer only during the authentication process. This is an optional capability that can be requested by the plugin. For more information, see [**HS\_PLUGIN\_QUERY\_CELLULAR\_EXCEPTION\_HOSTS**](hs-plugin-query-cellular-exception-hosts.md).

## Syntax

```ManagedCPlusPlus
typedef struct _HS_PLUGIN_CELLULAR_EXCEPTION_HOSTS {
  DWORD               dwCount;
  HS_PLUGIN_HOST_NAME pExceptions[*];
  HS_PLUGIN_HOST_NAME pExceptions[1];
} HS_PLUGIN_CELLULAR_EXCEPTION_HOSTS, *PHS_PLUGIN_CELLULAR_EXCEPTION_HOSTS;
```

## Members

**dwCount**  
The number of host names in the list pointed to by **pExceptions**.

**pExceptions**  
Used if MIDL is utilized. Unique, size is (dwCount).

Pointer to the list of host names.

**pExceptions**  
Used if MIDL is not utilized.

Pointer to the list of host names.

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Header</p></td>
<td>Hotspotoffloadplugin.h (include Hotspotoffloadplugin.h)</td>
</tr>
</tbody>
</table>

## See also


[**HS\_PLUGIN\_QUERY\_CELLULAR\_EXCEPTION\_HOSTS**](hs-plugin-query-cellular-exception-hosts.md)

[Microsoft Interface Definition Language](/windows/desktop/Midl/midl-start-page)

 

