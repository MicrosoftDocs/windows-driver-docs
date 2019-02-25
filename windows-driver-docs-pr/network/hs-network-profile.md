---
title: HS_NETWORK_PROFILE structure
description: The HS_NETWORK_PROFILE structure is provided by the plugin and contains information required for connection to the target network. Each instance of the Network Profile is uniquely associated with a corresponding HS_NETWORK_IDENTITY structure.
ms.assetid: 55e8786c-d7b8-48f3-9e54-312183cf8fb3
keywords: 
- HS_NETWORK_PROFILE structure Network Drivers Starting with Windows Vista
- PHS_NETWORK_PROFILE structure pointer Network Drivers Starting with Windows Vista
ms.date: 07/31/2017
ms.localizationpriority: medium
---

# HS\_NETWORK\_PROFILE structure

[!include[Wi-Fi Hotspot Offloading deprecation](wi-fi-hotspot-offloading-deprecation.md)]


The **HS\_NETWORK\_PROFILE** structure is provided by the plugin and contains information required for connection to the target network. Each instance of the Network Profile is uniquely associated with a corresponding [**HS\_NETWORK\_IDENTITY**](hs-network-identity.md) structure.

Syntax
------

```ManagedCPlusPlus
typedef struct _HS_NETWORK_PROFILE {
  DWORD  dwNetworkCapabilities;
  USHORT usPriority;
  DWORD  dwSupportedSIMCount;
  DWORD  dmNumCellularExceptions;
  DWORD  dwNetworkStringID;
  DWORD  dwKeepAliveTimeMins;
  WCHAR  szRealm[HS_CONST_MAX_REALM_LENGTH+1];
} HS_NETWORK_PROFILE, *PHS_NETWORK_PROFILE;
```

Members
-------

**dwNetworkCapabilities**  
A subset of the possible **HS\_FLAG\_CAPABILITY\_NETWORK\_\\*** values. For more information about hotspot host capabilities, see [**Wi-Fi Hotspot Offloading Constants**](wi-fi-hotspot-offloading-constants.md).

**usPriority**  
A unique priority value assigned to the associated network. It must be a value between 1 and 65000 (a hidden network must have a value of 1). A lower numeric value corresponds to a higher priority.

**dwSupportedSIMCount**  
Supported SIM count. This member is set for HTTP-based and EAP-SIM/AKA/AKA' authentication.

**dmNumCellularExceptions**  
Optional. Number of host connections over cellular only.

**dwNetworkStringID**  
Network name string ID. Maximum string size = MAX\_NETWORK\_DISPLAY\_NAME\_LENGTH.

**dwKeepAliveTimeMins**  
Optional. The time interval between network connection keep-alive messages.

**szRealm**  
Network-specific realm value.

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


[**HS\_NETWORK\_IDENTITY**](hs-network-identity.md)

[**Wi-Fi Hotspot Offloading Constants**](wi-fi-hotspot-offloading-constants.md)

 

 




