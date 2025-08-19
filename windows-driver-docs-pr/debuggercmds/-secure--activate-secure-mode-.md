---
title: ".secure (Activate Secure Mode)"
description: "The .secure command activates or displays the status of Secure Mode."
keywords: [".secure (Activate Secure Mode) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .secure (Activate Secure Mode)
api_type:
- NA
---

# .secure (Activate Secure Mode)

The **.secure** command activates or displays the status of Secure Mode.

```dbgcmd
.secure 1 
.secure 
```

## Environment

Secure Mode can only be enabled while the debugger is dormant. Secure Mode applies only to kernel-mode sessions because, by definition, Secure Mode prevents user-mode debugging operations.

|  Item       | Description       |
|-----------|------------------|
| Modes     | kernel mode only |
| Targets   | live, crash dump |
| Platforms | all              |

## Additional Information

For details, see [Secure Mode](../debugger/secure-mode.md).

## Remarks

To activate Secure Mode, use the command **.secure 1** (or **.secure** followed by any nonzero value).

The command **.secure** will show whether Secure Mode is currently active.
