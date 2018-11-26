---
title: HS_PLUGIN_SUPPORTED_SIMS structure
description: The HS_PLUGIN_SUPPORTED_SIMS structure contains the list of supported SIM configurations. This list must be supplied if the hotspot plugin requires HTTP or EAP authentication for any of its networks.
ms.assetid: 7ec8fb95-b227-4feb-882e-457a9ad6ec3e
keywords: 
- HS_PLUGIN_SUPPORTED_SIMS structure Network Drivers Starting with Windows Vista
- PHS_PLUGIN_SUPPORTED_SIMS structure pointer Network Drivers Starting with Windows Vista
ms.date: 07/31/2017
ms.localizationpriority: medium
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

 

 




