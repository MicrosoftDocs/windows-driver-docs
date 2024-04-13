---
title: "sq (Set Quiet Mode)"
description: "The sq command turns quiet mode on or off."
keywords: ["sq (Set Quiet Mode) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- sq (Set Quiet Mode)
api_type:
- NA
---

# sq (Set Quiet Mode)


The **sq** command turns quiet mode on or off.

```dbgcmd
sq 
sq{e|d} 
```

## <span id="ddk_cmd_set_quiet_mode_dbg"></span><span id="DDK_CMD_SET_QUIET_MODE_DBG"></span>


## Environment

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |

 

## Remarks

The **sqe** command turns quiet mode on, and the **sqd** command turns it off. The **sq** command turns on and off quiet mode. Each of these commands also displays the new quiet mode status.

You can set quiet mode in KD or kernel-mode WinDbg by using the KDQUIET [environment variable](../debugger/kernel-mode-environment-variables.md). (Note that quiet mode exists in both user-mode and kernel-mode debugging, but the KDQUIET environment variable is only recognized in kernel mode.)

*Quiet mode* has three distinct effects:

-   The debugger does not display messages every time that an extension DLL is loaded or unloaded.

-   The [**r (Registers)**](r--registers-.md) command no longer requires an equal sign (=) in its syntax.

-   When you break into a target computer while kernel debugging, the long warning message is suppressed.

Do not confuse quiet mode with the effects of the **-myob** [command-line option](../debugger/command-line-options.md) (in CDB and KD) or the **-Q** [**command-line option**](../debugger/windbg-command-line-options.md) (in WinDbg).

