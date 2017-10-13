---
title: HS_NETWORK_PROFILE structure
author: windows-driver-content
description: The HS\_NETWORK\_PROFILE structure is provided by the plugin and contains information required for connection to the target network. Each instance of the Network Profile is uniquely associated with a corresponding HS\_NETWORK\_IDENTITY structure.
ms.assetid: 55e8786c-d7b8-48f3-9e54-312183cf8fb3
keywords: 
- HS_NETWORK_PROFILE structure Network Drivers Starting with Windows Vista
- PHS_NETWORK_PROFILE structure pointer Network Drivers Starting with Windows Vista
ms.author: windowsdriverdev
ms.date: 07/31/2017 
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# HS\_NETWORK\_PROFILE structure


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
A subset of the possible **HS\_FLAG\_CAPABILITY\_NETWORK\_\*** values. For more information about hotspot host capabilities, see [**Wi-Fi Hotspot Offloading Constants**](wi-fi-hotspot-offloading-constants.md).

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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20HS_NETWORK_PROFILE%20structure%20%20RELEASE:%20%287/31/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


