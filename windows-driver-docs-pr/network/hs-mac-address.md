---
title: HS_MAC_ADDRESS structure
description: The HS_MAC_ADDRESS structure contains the host Media Access Control (MAC) address.
ms.assetid: 2d632ed4-4522-48ae-b23d-927517185d73
keywords: 
- HS_MAC_ADDRESS structure Network Drivers Starting with Windows Vista
- PHS_MAC_ADDRESS structure pointer Network Drivers Starting with Windows Vista
ms.date: 07/31/2017
ms.localizationpriority: medium
---

# HS\_MAC\_ADDRESS structure

[!include[Wi-Fi Hotspot Offloading deprecation](wi-fi-hotspot-offloading-deprecation.md)]


The **HS\_MAC\_ADDRESS** structure contains the host Media Access Control (MAC) address.

Syntax
------

```ManagedCPlusPlus
typedef struct _HS_MAC_ADDRESS {
  UCHAR ucHSMacAddress[6];
} HS_MAC_ADDRESS, *PHS_MAC_ADDRESS;
```

Members
-------

**ucHSMacAddress**  
The MAC address.

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

 

 




