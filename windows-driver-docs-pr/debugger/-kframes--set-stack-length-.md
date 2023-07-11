---
title: .kframes (Set Stack Length)
description: The .kframes command sets the default length of a stack trace display.
keywords: ["Set Stack Length (.kframes) command", ".kframes (Set Stack Length) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .kframes (Set Stack Length)
api_type:
- NA
---

# .kframes (Set Stack Length)

The **.kframes** command sets the default length of a stack trace display.

```dbgcmd
.kframes FrameCountDefault 
```

## Parameters

*FrameCountDefault*

Specifies the number of stack frames to display when a stack trace command is used.

### Environment

| Environment | &nbsp;                 |
|-------------|------------------------|
| Modes       | User mode, kernel mode |
| Targets     | Live, crash dump       |
| Platforms   | All                    |

## Remarks

You can use the **.kframes** command to set the default length of a stack trace display. This length controls the number of frames that the [**k, kb, kp, kP, and kv**](k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-.md) commands display and the number of DWORD\_PTRs that the **kd** command displays.

You can override this default length by using the *FrameCount* or *WordCount* parameters for these commands.

Use the **.kframes** command, without any parameters to see current value.

```dbgcmd
.kframes
Default stack trace depth is 0n256 frames
```

Use the following command to set the stack trace depth to 0x2.

```dbgcmd
.kframes 0x2
Default stack trace depth is 0n2 frames
```

Using the k command to display two stack and two raw stack values.

```dbgcmd
k
 # Child-SP          RetAddr               Call Site
00 00000054`b71ffb78 00007ffe`1ee672ae     ntdll!DbgBreakPoint
01 00000054`b71ffb80 00007ffe`1e2a3e2d     ntdll!DbgUiRemoteBreakin+0x4e

kd
00000054`b71ffb70  00000000
00000054`b71ffb74  00000000
```

Specify the *FrameCount* and *WordCount*  to display additional values.

```dbgcmd
k 3
 # Child-SP          RetAddr               Call Site
00 00000054`b71ffb78 00007ffe`1ee672ae     ntdll!DbgBreakPoint
01 00000054`b71ffb80 00007ffe`1e2a3e2d     ntdll!DbgUiRemoteBreakin+0x4e
02 00000054`b71ffbb0 00007ffe`1eddef48     KERNEL32!BaseThreadInitThunk+0x1d

kd 5
00000054`b71ffb70  00000000
00000054`b71ffb74  00000000
00000054`b71ffb78  1ee672ae
00000054`b71ffb7c  00007ffe
00000054`b71ffb80  00000000
```

## See also

[**k, kb, kc, kd, kp, kP, kv (Display Stack Backtrace)**](k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-.md)
