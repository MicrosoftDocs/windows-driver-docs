---
title: NET_PACKET structure
description: TBD.
ms.assetid: 40C19288-8DA8-4610-958A-B215D6E4704B
keywords: ["NET_PACKET structure Network Drivers Starting with Windows Vista", "PNET_PACKET structure pointer Network Drivers Starting with Windows Vista"]
---

# NET\_PACKET structure


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

TBD

Syntax
------

```ManagedCPlusPlus
typedef struct _NET_PACKET {
  NET_PACKET_FRAGMENT Data;
  NET_PACKET_LAYOUT   Layout;
  NET_PACKET_CHECKSUM Checksum;
  UINT16              IgnoreThisPacket  :1;
  UINT16              AdvancedOffloadRequested  :1;
  UINT16              Reserved1  :14;
  UINT32              Hash;
  UINT32              Reserved2;
  PVOID               Reserved3;
} NET_PACKET, *PNET_PACKET;
```

Members
-------

**Data**  
TBD

**Layout**  

**Checksum**  

**IgnoreThisPacket**  

**AdvancedOffloadRequested**  

**Reserved1**  

**Hash**  

**Reserved2**  

**Reserved3**  

 

 





