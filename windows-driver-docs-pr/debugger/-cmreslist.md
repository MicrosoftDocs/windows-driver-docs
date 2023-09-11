---
title: cmreslist (WinDbg)
description: The cmreslist extension displays the CM_RESOURCE_LIST structure for the specified device object.
keywords: ["CM_RESOURCE_LIST", "cmreslist Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- cmreslist
api_type:
- NA
---

# !cmreslist


The **!cmreslist** extension displays the CM\_RESOURCE\_LIST structure for the specified device object.

```dbgsyntax
!cmreslist Address
```

## <span id="ddk__cmreslist_dbg"></span><span id="DDK__CMRESLIST_DBG"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the hexadecimal address of the CM\_RESOURCE\_LIST structure.

### DLL

Kdexts.dll

 

### Additional Information

See [Plug and Play Debugging](plug-and-play-debugging.md) for applications of this extension command. For information about the CM\_RESOURCE\_LIST structure, see the Windows Driver Kit (WDK) documentation.

 

 





