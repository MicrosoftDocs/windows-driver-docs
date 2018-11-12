---
title: ndiskd.findpacket
description: Warning  This extension is for legacy NDIS 5.x drivers. The NDIS_PACKET structure and its associated architecture have been deprecated. The ndiskd.findpacket extension finds the specified packets.
ms.assetid: fc07b2d8-85ca-4be1-ae9d-40b7c7f81b08
keywords: ["ndiskd.findpacket Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- ndiskd.findpacket
api_type:
- NA
ms.localizationpriority: medium
---

# !ndiskd.findpacket


**Warning**  This extension is for legacy NDIS 5.x drivers. The [NDIS\_PACKET](https://msdn.microsoft.com/library/windows/hardware/ff557086) structure and its associated architecture have been deprecated.

 

The **!ndiskd.findpacket** extension finds the specified packets.

```console
!ndiskd.findpacket [-VirtualAddress] [-PoolAddress]  
```

## <span id="ddk__ndiskd_findpacket_dbg"></span><span id="DDK__NDISKD_FINDPACKET_DBG"></span>Parameters


<span id="_______VirtualAddress______"></span><span id="_______virtualaddress______"></span><span id="_______VIRTUALADDRESS______"></span> *VirtualAddress*   
Specifies a virtual address that is contained in the desired packet.

<span id="_______PoolAddress______"></span><span id="_______pooladdress______"></span><span id="_______POOLADDRESS______"></span> *PoolAddress*   
Specifies a pool address. All unreturned packets in this pool will be displayed.

### <span id="DLL"></span><span id="dll"></span>DLL

Ndiskd.dll

## <span id="see_also"></span>See also


[Windows 2000 and Windows XP Networking Design Guide](https://msdn.microsoft.com/library/windows/hardware/ff565849)

[Windows 2000 and Windows XP Networking Reference](https://msdn.microsoft.com/library/windows/hardware/ff565850)

[NDIS\_PACKET](https://msdn.microsoft.com/library/windows/hardware/ff557086)

 

 






