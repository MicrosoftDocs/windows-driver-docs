---
title: ndiskd.pkt
description: Warning  This extension is for legacy NDIS 5.x drivers. The ndiskd.pkt extension displays information about an NDIS_PACKET structure.
ms.assetid: 8e704173-3b09-4377-b73a-ba67a3c3c930
keywords: ["ndiskd.pkt Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- ndiskd.pkt
api_type:
- NA
ms.localizationpriority: medium
---

# !ndiskd.pkt


**Warning**  This extension is for legacy NDIS 5.x drivers. The [NDIS\_PACKET](https://msdn.microsoft.com/library/windows/hardware/ff557086) structure and its associated architecture have been deprecated.

 

The **!ndiskd.pkt** extension displays information about an [NDIS\_PACKET](https://msdn.microsoft.com/library/windows/hardware/ff557086) structure.

```console
!ndiskd.pkt [-packet] [-verbosity] 
```

## <span id="ddk__ndiskd_pkt_dbg"></span><span id="DDK__NDISKD_PKT_DBG"></span>Parameters


<span id="_______Packet______"></span><span id="_______packet______"></span><span id="_______PACKET______"></span> *Packet*   
Specifies the address of the packet.

<span id="_______Verbosity______"></span><span id="_______verbosity______"></span><span id="_______VERBOSITY______"></span> *Verbosity*   
Specifies the amount of detail to be displayed.

### <span id="DLL"></span><span id="dll"></span>DLL

Ndiskd.dll

## <span id="see_also"></span>See also


[Windows 2000 and Windows XP Networking Design Guide](https://msdn.microsoft.com/library/windows/hardware/ff565849)

[Windows 2000 and Windows XP Networking Reference](https://msdn.microsoft.com/library/windows/hardware/ff565850)

[NDIS\_PACKET](https://msdn.microsoft.com/library/windows/hardware/ff557086)

 

 






