---
title: "!wdfkd.wdftraceprtdebug"
description: "The !wdfkd.wdftraceprtdebug extension enables and disables the Traceprt.dll diagnostic mode, which generates verbose debugging information."
keywords: ["!wdfkd.wdftraceprtdebug Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- wdfkd.wdftraceprtdebug
api_type:
- NA
---

# !wdfkd.wdftraceprtdebug

The **!wdfkd.wdftraceprtdebug** extension enables and disables the Traceprt.dll diagnostic mode, which generates verbose debugging information.

```dbgcmd
!wdfkd.wdftraceprtdebug {on | off}
```

## Parameters

<span id="_______on______"></span><span id="_______ON______"></span> **on**   
Enables the Traceprt.dll diagnostic mode.

<span id="_______off______"></span><span id="_______OFF______"></span> **off**   
Disables the Traceprt.dll diagnostic mode.

## DLL

Wdfkd.dll

### Frameworks

KMDF 1, UMDF 2

## Additional Information

For more information, see [Kernel-Mode Driver Framework Debugging](../debugger/kernel-mode-driver-framework-debugging.md).

## Remarks

You should use the !wdfkd.wdftraceprtdebug extension only at the direction of technical support.
