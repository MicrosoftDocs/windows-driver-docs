---
title: eHS_NETWORK_STATE enumeration
author: windows-driver-content
description: The eHS\_NETWORK\_STATE enumeration indicates whether a network is a hotspot network.
ms.assetid: a833d226-e2cf-41f9-a926-5b1f6daa03af
keywords: 
 - eHS_NETWORK_STATE enumeration Network Drivers Starting with Windows Vista
ms.author: windowsdriverdev
ms.date: 07/31/2017 
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20eHS_NETWORK_STATE%20enumeration%20%20RELEASE:%20%287/31/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


