---
title: HS\_PLUGIN\_SUPPORTED\_SIMS structure
author: windows-driver-content
description: The HS\_PLUGIN\_SUPPORTED\_SIMS structure contains the list of supported SIM configurations. This list must be supplied if the hotspot plugin requires HTTP or EAP authentication for any of its networks.
ms.assetid: 7ec8fb95-b227-4feb-882e-457a9ad6ec3e
keywords: 
- HS_PLUGIN_SUPPORTED_SIMS structure Network Drivers Starting with Windows Vista
- PHS_PLUGIN_SUPPORTED_SIMS structure pointer Network Drivers Starting with Windows Vista
ms.author: windowsdriverdev
ms.date: 07/31/2017 
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# HS\_PLUGIN\_SUPPORTED\_SIMS structure

[!include[Wi-Fi Hotspot Offloading deprecation](wi-fi-hotspot-offloading-deprecation.md)]


The **HS\_PLUGIN\_SUPPORTED\_SIMS** structure contains the list of supported SIM configurations. This list must be supplied if the hotspot plugin requires HTTP or EAP authentication for any of its networks.

Syntax
------

```ManagedCPlusPlus
typedef struct _HS_PLUGIN_SUPPORTED_SIMS {
  DWORD           dwCount;
  HS_SIM_IDENTITY pSupportedSIMs[*];
  HS_SIM_IDENTITY pSupportedSIMs[1];
} HS_PLUGIN_SUPPORTED_SIMS, *PHS_PLUGIN_SUPPORTED_SIMS;
```

Members
-------

**dwCount**  
The list size.

**pSupportedSIMs**  
Used if MIDL is utilized. Unique, size is (dwCount).

An array of HS\_SIM\_IDENTITY structures that make up the list of supported SIM configurations.

**pSupportedSIMs**  
Used if MIDL is not utilized.

An array of HS\_SIM\_IDENTITY structures that make up the list of supported SIM configurations.

Remarks
-------

In the **dwEapMethods** field of the [**HS\_SIM\_IDENTITY**](hs-sim-identity.md) structure for each SIM configuration, you must specify the EAP methods that it supports.

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

## See also


[**HS\_SIM\_IDENTITY**](hs-sim-identity.md)

[Microsoft Interface Definition Language](https://msdn.microsoft.com//library/windows/desktop/aa367091)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20HS_PLUGIN_SUPPORTED_SIMS%20structure%20%20RELEASE:%20%287/31/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


