---
title: "!dflink (WinDbg)"
description: "The !dflink extension displays a linked list in the forward direction."
keywords: ["!dflink Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- dflink
api_type:
- NA
---

# !dflink

The **!dflink** extension displays a linked list in the forward direction.

```dbgcmd
!dflink Address [Count] [Bias]  
```

## <span id="ddk__dflink_dbg"></span><span id="DDK__DFLINK_DBG"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the address of a LIST\_ENTRY structure. The display will begin with this node.

<span id="_______Count______"></span><span id="_______count______"></span><span id="_______COUNT______"></span> *Count*   
Specifies the maximum number of list entries to display. If this is omitted, the default is 32.

<span id="_______Bias______"></span><span id="_______bias______"></span><span id="_______BIAS______"></span> *Bias*   
Specifies a mask of bits to ignore in each pointer. Each **Flink** address is ANDed with (NOT *Bias*) before following it to the next location. The default is zero (in other words, do not ignore any bits).

### DLL

Kdexts.dll

 

## Remarks

The **!dflink** extension traverses the **Flink** fields of the LIST\_ENTRY structure and displays up to four ULONGs at each address. To go in the other direction, use [**!dblink**](-dblink.md).

The [**dl (Display Linked List)**](dl--display-linked-list-.md) command is more versatile than [**!dblink**](-dblink.md) and **!dflink**.

