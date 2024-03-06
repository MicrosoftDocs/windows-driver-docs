---
title: "!amli dl (WinDbg)"
description: "The !amli dl extension displays a portion of the AML interpreter's event log."
keywords: ["amli dl Windows Debugging"]
ms.date: 09/17/2018
topic_type:
- apiref
ms.topic: reference
api_name:
- amli dl
api_type:
- NA
---

# !amli dl

The **!amli dl** extension displays a portion of the AML interpreter's event log.

Syntax

```dbgcmd
    !amli dl
```

## DLL

Kdexts.dll

### Additional Information

For information about related commands and their uses, see [The AMLI Debugger](../debugger/the-amli-debugger.md).

## Remarks

The event log chronicles the most recent 150 events that occurred in the interpreter.

Here is an example of the log display:

```console
kd> !amli dl
RUN!: [c15a6618]QTh=00000000,QCt=00000000,QFg=00000000: Ctx=c18b4000,rc=0
KICK: [c15a6618]QTh=00000000,QCt=00000000,QFg=00000000: rc=0
SYNC: [c15a6618]QTh=00000000,QCt=00000000,QFg=00000002,LockPhase=0,Locked=0,IRQL=00: Obj=\_WAK
ASYN: [c15a6618]QTh=00000000,QCt=00000000,QFg=00000002,LockPhase=0,Locked=0,IRQL=00: Obj=\_WAK
REST: [c15a6618]QTh=00000000,QCt=00000000,QFg=00000002: Ctx=c18b4000,Obj=\_WAK
INSQ: [c15a6618]QTh=00000000,QCt=00000000,QFg=00000002: Ctx=c18b4000,Obj=\_WAK
EVAL: [c15a6618]QTh=00000000,QCt=00000000,QFg=00000002: Ctx=c18b4000,Obj=\_WAK
RUNC: [c15a6618]QTh=c15a6618,QCt=c18b4000,QFg=00000002: Ctx=c18b4000,Obj=\_WAK
```
