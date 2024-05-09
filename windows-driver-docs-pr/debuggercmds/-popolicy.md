---
title: "!popolicy (WinDbg)"
description: "The !popolicy extension displays the power policy of the target computer."
keywords: ["!popolicy Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- popolicy
api_type:
- NA
---

# !popolicy

The **!popolicy** extension displays the power policy of the target computer.

```dbgcmd
!popolicy [Address]
```

## Parameters

<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the address of the power policy structure to display. If this is omitted, then nt!PopPolicy is displayed.

## DLL

Kdexts.dll

## Additional Information

To view the system's power capabilities, use the [**!pocaps**](-pocaps.md) extension command. For information about power capabilities and power policy, see the Windows Driver Kit (WDK) documentation and *Microsoft Windows Internals*, by Mark Russinovich and David Solomon.

## Remarks

Here is an example of this command's output:

```dbgcmd
kd> !popolicy
SYSTEM_POWER_POLICY (R.1) @ 0x80164d58
  PowerButton:      Shutdown  Flags: 00000003   Event: 00000000   Query UI
  SleepButton:          None  Flags: 00000003   Event: 00000000   Query UI
  LidClose:             None  Flags: 00000001   Event: 00000000   Query
  Idle:                 None  Flags: 00000001   Event: 00000000   Query
  OverThrottled:        None  Flags: c0000004   Event: 00000000   Override NoWakes Critical
  IdleTimeout:             0  IdleSensitivity:        50%
  MinSleep:               S0  MaxSleep:               S0
  LidOpenWake:            S0  FastSleep:              S0
  WinLogonFlags:           1  S4Timeout:               0
  VideoTimeout:            0  VideoDim:               209
  SpinTimeout:             0  OptForPower:             1
  FanTolerance:            0% ForcedThrottle:          0%
  MinThrottle:             0%
```

## See also

[Plug and Play and Power Debugger Commands](../debugger/plug-and-play-and-power-debugger-commands.md)
