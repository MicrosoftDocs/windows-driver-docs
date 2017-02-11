---
title: NET_PACKET_FRAGMENT structure
---

# NET_PACKET_FRAGMENT structure


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

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

**NextFragment_Reserved**  

**Reserved**  

**NextFragment_Reserved**  

**PHYSICAL_ADDRESS**  

**VirtualAddress**  

**ValidLength**  

**Capacity**  

**Offset**  

**Completed**  

**Scratch**  

 

 





