---
title: HS_CONNECTION_CONTEXT structure
description: The HS_CONNECTION_CONTEXT structure contains the information required by the plugin for post connect authentication.
ms.assetid: 22b219fc-691b-4813-a523-a76de037e64d
keywords: 
- HS_CONNECTION_CONTEXT structure Network Drivers Starting with Windows Vista
- PHS_CONNECTION_CONTEXT structure pointer Network Drivers Starting with Windows Vista
ms.date: 07/31/2017
ms.localizationpriority: medium
---

# HS\_CONNECTION\_CONTEXT structure

[!include[Wi-Fi Hotspot Offloading deprecation](wi-fi-hotspot-offloading-deprecation.md)]


The **HS\_CONNECTION\_CONTEXT** structure contains the information required by the plugin for post connect authentication.

Syntax
------

```ManagedCPlusPlus
typedef struct _HS_CONNECTION_CONTEXT {
  HS_MAC_ADDRESS  MacAddress;
  HS_SIM_IDENTITY SIMIdentity;
  WCHAR           pszPhoneNumber[HS_MAX_PHONE_NUMBER_LENGTH+1];
} HS_CONNECTION_CONTEXT, *PHS_CONNECTION_CONTEXT;
```

Members
-------

**MacAddress**  
The [**HS\_MAC\_ADDRESS**](hs-mac-address.md) structure that contains the MAC address.

**SIMIdentity**  
The [**HS\_SIM\_IDENTITY**](hs-sim-identity.md) structure that contains information required for EAP-SIM/AKA authentication.

**pszPhoneNumber**  
Pointer to the phone number.

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


[**HS\_MAC\_ADDRESS**](hs-mac-address.md)

[**HS\_SIM\_IDENTITY**](hs-sim-identity.md)

 

 




