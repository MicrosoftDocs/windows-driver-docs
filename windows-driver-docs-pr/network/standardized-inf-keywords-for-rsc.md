---
title: Standardized INF Keywords for RSC
description: Standardized INF Keywords for RSC
keywords:
- receive-side coalescing WDK networking , standardized INF keywords
- RSC WDK networking , standardized INF keywords
- standardized INF keywords WDK RSC
- INF entries WDK RSC
ms.date: 04/20/2017
---

# Standardized INF Keywords for RSC





In Windows 8, Windows Server 2012, and later, the receive segment coalescing (RSC) interface supports [standardized INF keywords](standardized-inf-keywords-for-network-devices.md) that appear in the registry and are specified in INF files.

The following list shows the enumeration [standardized INF keywords](standardized-inf-keywords-for-network-devices.md) for RSC:

**\*RscIPv4**  
Enable or disable support for RSC for the IPv4 datagram version.

**\*RscIPv6**  
Enable or disable support for RSC for the IPv6 datagram version.

Enumeration standardized INF keywords have the following attributes:

**SubkeyName**  
The name of the keyword that you must specify in the INF file and that appears in the registry.

**ParamDesc**  
The display text that is associated with **SubkeyName**.

**Value**  
The enumeration integer value that is associated with each option in the list. This value is stored in NDI\\params\\ *SubkeyName*\\*Value*.

**EnumDesc**  
The display text that is associated with each value that appears in the menu.

**Default**  
The default value for the menu.

The following table describes the possible INF entries for the RSC enumeration keywords.


|SubkeyName|ParamDesc|Value|EnumDesc|
|--- |--- |--- |--- |
|**\*RscIPv4**|Recv Segment Coalescing (IPv4)|0|Disabled|
|||1 (Default)|Enabled|
|**\*RscIPv6**|Recv Segment Coalescing (IPv6)|0|Disabled|
|||1 (Default)|Enabled|

 

For more information about standardized INF keywords, see [Standardized INF Keywords for Network Devices](standardized-inf-keywords-for-network-devices.md).

For more information about using enumeration keywords, see [Enumeration Keywords](enumeration-keywords.md).

 

 





