---
title: "!tls (WinDbg)"
description: "The !tls extension displays a thread local storage (TLS) slot."
keywords: ["TLS (thread local storage)", "thread local storage (TLS)", "!tls Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- tls
api_type:
- NA
---

# !tls

The **!tls** extension displays a thread local storage (TLS) slot.

```dbgcmd
!tls Slot [TEB]
```

## Parameters

<span id="_______Slot______"></span><span id="_______slot______"></span><span id="_______SLOT______"></span> *Slot*   
Specifies the TLS slot. This can be any value between 0 and 1088 (decimal). If *Slot* is -1, all slots are displayed.

<span id="_______TEB______"></span><span id="_______teb______"></span> *TEB*   
Specifies the thread environment block (TEB). If this is 0 or omitted, the current thread is used.

## DLL

Exts.dll

## Remarks

Here is an example:

```dbgcmd
0:000> !tls -1
TLS slots on thread: c08.f54
0x0000 : 00000000
0x0001 : 003967b8
0:000> !tls 0
c08.f54: 00000000
```
