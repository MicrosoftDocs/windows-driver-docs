---
title: HS_NETWORK_IDENTITY structure
description: The HS_NETWORK_IDENTITY structure contains information that uniquely identifies a Wi-Fi network.
ms.assetid: 40d9720b-c122-4d19-8907-cfa2a05014e7
keywords: 
- HS_NETWORK_IDENTITY structure Network Drivers Starting with Windows Vista
- PHS_NETWORK_IDENTITY structure pointer Network Drivers Starting with Windows Vista
ms.date: 07/31/2017
ms.localizationpriority: medium
---

# HS\_NETWORK\_IDENTITY structure

[!include[Wi-Fi Hotspot Offloading deprecation](wi-fi-hotspot-offloading-deprecation.md)]


The **HS\_NETWORK\_IDENTITY** structure contains information that uniquely identifies a Wi-Fi network.

Syntax
------

```ManagedCPlusPlus
typedef struct _HS_NETWORK_IDENTITY {
  HS_SSID             Ssid;
  HS_AUTH_ALGORITHM   hsAuthAlgo;
  HS_CIPHER_ALGORITHM hsCipherAlgo;
} HS_NETWORK_IDENTITY, *PHS_NETWORK_IDENTITY;
```

Members
-------

**Ssid**  
The network SSID.

**hsAuthAlgo**  
The authentication algorithm used by the wireless network.

**hsCipherAlgo**  
The cipher algorithm used by the wireless network.

Requirements
------------

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

 

 




