---
title: ndiskd.pkt
description: Warning  This extension is for legacy NDIS 5.x drivers. The ndiskd.pkt extension displays information about an NDIS_PACKET structure.
keywords: ["ndiskd.pkt Windows Debugging"]
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

**Warning**  This extension is for legacy NDIS 5.x drivers. The [NDIS\_PACKET](/previous-versions/windows/hardware/network/ff557086(v=vs.85)) structure and its associated architecture have been deprecated.

The **!ndiskd.pkt** extension displays information about an [NDIS\_PACKET](/previous-versions/windows/hardware/network/ff557086(v=vs.85)) structure.

```console
!ndiskd.pkt [-packet] [-verbosity] 
```

## Parameters

<span id="_______Packet______"></span><span id="_______packet______"></span><span id="_______PACKET______"></span> *Packet*   
Specifies the address of the packet.

<span id="_______Verbosity______"></span><span id="_______verbosity______"></span><span id="_______VERBOSITY______"></span> *Verbosity*   
Specifies the amount of detail to be displayed.

### DLL

Ndiskd.dll

## See also

[NDIS\_PACKET](/previous-versions/windows/hardware/network/ff557086(v=vs.85))
