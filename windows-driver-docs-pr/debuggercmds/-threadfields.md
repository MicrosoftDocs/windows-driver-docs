---
title: "!threadfields"
description: "The !threadfields extension command is not available. Instead, use dt (Display Type)."
keywords: ["!threadfields Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- threadfields
api_type:
- NA
---

# !threadfields

The **!threadfields** extension command is not available. Instead, use dt (Display Type)..

```dbgcmd
!threadfields
```

## DLL

Unavailable (see the Remarks section)

## Additional Information

For information about the ETHREAD block, see *Microsoft Windows Internals*, by Mark Russinovich and David Solomon.

## Remarks

This extension command is not available. Instead, use the [**dt (Display Type)**](dt--display-type-.md) command to show the ETHREAD structure directly:

```dbgcmd
kd> dt nt!_ETHREAD 
```
