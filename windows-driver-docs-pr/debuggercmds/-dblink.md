---
title: "!dblink (WinDbg)"
description: "The !dblink extension displays a linked list in the backward direction."
keywords: ["!dblink Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- dblink
api_type:
- NA
---

# !dblink


The **!dblink** extension displays a linked list in the backward direction.

```dbgcmd
!dblink Address [Count] [Bias]  
```

## <span id="ddk__dblink_dbg"></span><span id="DDK__DBLINK_DBG"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the address of a LIST\_ENTRY structure. The display will begin with this node.

<span id="_______Count______"></span><span id="_______count______"></span><span id="_______COUNT______"></span> *Count*   
Specifies the maximum number of list entries to display. If this is omitted, the default is 32.

<span id="_______Bias______"></span><span id="_______bias______"></span><span id="_______BIAS______"></span> *Bias*   
Specifies a mask of bits to ignore in each pointer. Each **Blink** address is ANDed with (NOT *Bias*) before following it to the next location. The default is zero (in other words, do not ignore any bits).

### DLL

Kdexts.dll

 

## Remarks

The **!dblink** extension traverses the **Blink** fields of the LIST\_ENTRY structure and displays up to four ULONGs at each address. To go in the other direction, use [**!dflink**](-dflink.md).

The [**dl (Display Linked List)**](dl--display-linked-list-.md) command is more versatile than **!dblink** and [**!dflink**](-dflink.md).

