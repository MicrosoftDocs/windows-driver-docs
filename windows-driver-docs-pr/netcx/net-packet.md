---
title: NET\_PACKET structure
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NET_PACKET%20structure%20%20RELEASE:%20%281/19/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




