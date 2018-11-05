---
title: popolicy
description: The popolicy extension displays the power policy of the target computer.
ms.assetid: 4917e6e8-982f-41d7-acd8-047e590e1253
keywords: ["popolicy Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- popolicy
api_type:
- NA
ms.localizationpriority: medium
---

# !popolicy


The **!popolicy** extension displays the power policy of the target computer.

```dbgcmd
!popolicy [Address]
```

## <span id="ddk__popolicy_dbg"></span><span id="DDK__POPOLICY_DBG"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the address of the power policy structure to display. If this is omitted, then nt!PopPolicy is displayed.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Windows 2000</p></td>
<td align="left"><p>Kdextx86.dll</p></td>
</tr>
<tr class="even">
<td align="left"><p>Windows XP and later</p></td>
<td align="left"><p>Kdexts.dll</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

To view the system's power capabilities, use the [**!pocaps**](-pocaps.md) extension command. For information about power capabilities and power policy, see the Windows Driver Kit (WDK) documentation and *Microsoft Windows Internals*, by Mark Russinovich and David Solomon. (These resources may not be available in some languages and countries.)

Remarks
-------

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

## <span id="see_also"></span>See also


[Plug and Play and Power Debugger Commands](plug-and-play-and-power-debugger-commands.md)

 

 






