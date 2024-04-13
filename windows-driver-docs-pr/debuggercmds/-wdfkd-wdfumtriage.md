---
title: "!wdfkd.wdfumtriage"
description: "The !wdfkd.wdfumtriage extension displays information UMDF devices on the system, including device objects, loaded drivers and class extensions, PnP device stack, dispatched IRPs."
keywords: ["!wdfkd.wdfumtriage Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- wdfkd.wdfumtriage
api_type:
- NA
---

# !wdfkd.wdfumtriage

The **!wdfkd.wdfumtriage** extension displays information about all UMDF devices on the system, including device objects, corresponding host process, loaded drivers and class extensions, PnP device stack, PnP device nodes, dispatched IRPs, and problem state if relevant.

```dbgcmd
!wdfkd.wdfumtriage
```

## DLL

Wdfkd.dll

## Frameworks

UMDF 2

## Additional Information

For more information, see [Kernel-Mode Driver Framework Debugging](../debugger/kernel-mode-driver-framework-debugging.md).

## Remarks

You can use this command in a kernel-mode debugging session.

Here is an example of the output of **!wdfkd.wdfumtriage**.

:::image type="content" source="images/wdfumtriage2.png" alt-text="Screenshot of driver object list output from !wdfkd.wdfumtriage command.":::
