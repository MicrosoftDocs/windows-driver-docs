---
title: eHS_NETWORK_STATE enumeration
description: The eHS_NETWORK_STATE enumeration indicates whether a network is a hotspot network.
ms.assetid: a833d226-e2cf-41f9-a926-5b1f6daa03af
keywords: 
 - eHS_NETWORK_STATE enumeration Network Drivers Starting with Windows Vista
ms.date: 07/31/2017
ms.localizationpriority: medium
---

# eHS\_NETWORK\_STATE enumeration

[!include[Wi-Fi Hotspot Offloading deprecation](wi-fi-hotspot-offloading-deprecation.md)]


The **eHS\_NETWORK\_STATE** enumeration indicates whether a network is a hotspot network.

Syntax
------

```ManagedCPlusPlus
typedef enum _eHS_NETWORK_STATE { 
  HS_NETWORK_STATE_NOT_A_HOTSPOT,
  HS_NETWORK_STATE_HOTSPOT_MANUAL_CONNECT,
  HS_NETWORK_STATE_HOTSPOT_AUTO_CONNECT,
  HS_NETWORK_STATE_MAX
} eHS_NETWORK_STATE;
```

Constants
---------

<a href="" id="hs-network-state-not-a-hotspot"></a>**HS\_NETWORK\_STATE\_NOT\_A\_HOTSPOT**  
Indicates the network is not a hotspot network.

<a href="" id="hs-network-state-hotspot-manual-connect"></a>**HS\_NETWORK\_STATE\_HOTSPOT\_MANUAL\_CONNECT**  
Indicates the user can manually connect to the hotspot network.

<a href="" id="hs-network-state-hotspot-auto-connect"></a>**HS\_NETWORK\_STATE\_HOTSPOT\_AUTO\_CONNECT**  
Indicates the device can connect automatically to the hotspot network.

<a href="" id="hs-network-state-max"></a>**HS\_NETWORK\_STATE\_MAX**  
Indicates an out-of-range value.

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
<td><p>Windows 10 Mobile</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Hotspotoffloadplugin.h (include Hotspotoffloadplugin.h)</td>
</tr>
</tbody>
</table>

 

 




