---
title: NET_PACKET_FRAGMENT structure
description: TBD.
ms.assetid: E716E0DA-81CD-420E-B216-313B2E20FCCA
keywords: ["NET_PACKET_FRAGMENT structure Network Drivers Starting with Windows Vista", "PNET_PACKET_FRAGMENT structure pointer Network Drivers Starting with Windows Vista"]
---

# NET\_PACKET\_FRAGMENT structure


\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

TBD

Syntax
------

```ManagedCPlusPlus
typedef struct _NET_PACKET_FRAGMENT {
  ULONG_PTR         LastFragmentOfFrame  :1;
  ULONG_PTR         LastPacketOfChain  :1;
#if _WIN64
  ULONG_PTR         Reserved  :3;
  ULONG_PTR         NextFragment_Reserved  :59;
#else 
  ULONG_PTR         Reserved  :1;
  ULONG_PTR         NextFragment_Reserved  :29;
#endif 
  DmaLogicalAddress PHYSICAL_ADDRESS;
  PVOID             VirtualAddress;
  UINT64            ValidLength  :26;
  UINT64            Capacity  :26;
  UINT64            Offset  :10;
  UINT64            Completed  :1;
  UINT64            Scratch  :1;
} NET_PACKET_FRAGMENT, *PNET_PACKET_FRAGMENT;
```

Members
-------

**LastFragmentOfFrame**  
TBD

**LastPacketOfChain**  

**Reserved**  

**NextFragment\_Reserved**  

**Reserved**  

**NextFragment\_Reserved**  

**PHYSICAL\_ADDRESS**  

**VirtualAddress**  

**ValidLength**  

**Capacity**  

**Offset**  

**Completed**  

**Scratch**  

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NET_PACKET_FRAGMENT%20structure%20%20RELEASE:%20%281/19/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




