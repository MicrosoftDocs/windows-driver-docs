---
title: ndiskd.pktpools
description: Warning  This extension is for legacy NDIS 5.x drivers. The ndiskd.pktpools extension displays a list of all allocated packet pools.
ms.assetid: 0aceb22c-17ab-4199-a313-ecbc4c8f0b6e
keywords: ["ndiskd.pktpools Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- ndiskd.pktpools
api_type:
- NA
ms.localizationpriority: medium
---

# !ndiskd.pktpools


**Warning**  This extension is for legacy NDIS 5.x drivers. The [NDIS\_PACKET](https://msdn.microsoft.com/library/windows/hardware/ff557086) structure and its associated architecture have been deprecated.

 

The **!ndiskd.pktpools** extension displays a list of all allocated packet pools.

```console
!ndiskd.pktpools 
```

## <span id="ddk__ndiskd_pktpools_dbg"></span><span id="DDK__NDISKD_PKTPOOLS_DBG"></span>


### <span id="DLL"></span><span id="dll"></span>DLL

Ndiskd.dll

Examples
--------

Run the **!ndiskd.pktpools** extension to see a list of all allocated packet pools on the system. Note that the handles for the packet pools are not clickable, which means you can't explore further information about the packet pool. This is because NDIS does not use packet pools starting with NDIS 6.0, so these pools are allocated only for legacy drivers which may still be on older systems. The debugee machine in this example does not have any legacy NDIS 5.x drivers installed so the packet pools are not used. This example is for illustrative purposes only.

```console
3: kd> !ndiskd.pktpools
Pool      Allocator  BlocksAllocated  BlockSize  PktsPerBlock  PacketLength
ffffdf80131d58c0  fffff80f1fbe3e8f   0x1          0x1000     0xa           0x190   ndis!DriverEntry+6af
ffffdf80131d5940  fffff80f1fbe3e71   0x1          0x1000     0xa           0x180   ndis!DriverEntry+691
```

## <span id="see_also"></span>See also


[Windows 2000 and Windows XP Networking Design Guide](https://msdn.microsoft.com/library/windows/hardware/ff565849)

[Windows 2000 and Windows XP Networking Reference](https://msdn.microsoft.com/library/windows/hardware/ff565850)

[NDIS\_PACKET](https://msdn.microsoft.com/library/windows/hardware/ff557086)

 

 






