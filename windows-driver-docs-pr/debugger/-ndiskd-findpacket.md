---
title: ndiskd.findpacket
description: Warning  This extension is for legacy NDIS 5.x drivers. The NDIS_PACKET structure and its associated architecture have been deprecated. The ndiskd.findpacket extension finds the specified packets.
keywords: ["ndiskd.findpacket Windows Debugging"]
ms.date: 06/15/2020
topic_type:
- apiref
api_name:
- ndiskd.findpacket
api_type:
- NA
ms.localizationpriority: medium
---

# !ndiskd.findpacket

**Warning**  This extension is for legacy NDIS 5.x drivers. The [NDIS\_PACKET](/previous-versions/windows/hardware/network/ff557086(v=vs.85)) structure and its associated architecture have been deprecated.

The **!ndiskd.findpacket** extension finds the specified packets.

```console
!ndiskd.findpacket [-VirtualAddress] [-PoolAddress]  
```

## Parameters

<span id="_______VirtualAddress______"></span><span id="_______virtualaddress______"></span><span id="_______VIRTUALADDRESS______"></span> *VirtualAddress*   
Specifies a virtual address that is contained in the desired packet.

<span id="_______PoolAddress______"></span><span id="_______pooladdress______"></span><span id="_______POOLADDRESS______"></span> *PoolAddress*   
Specifies a pool address. All unreturned packets in this pool will be displayed.

### DLL

Ndiskd.dll

## See also

[NDIS\_PACKET](/previous-versions/windows/hardware/network/ff557086(v=vs.85))
