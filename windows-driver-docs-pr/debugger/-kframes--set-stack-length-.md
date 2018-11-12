---
title: .kframes (Set Stack Length)
description: The .kframes command sets the default length of a stack trace display.
ms.assetid: 4f11a197-add1-4957-8345-dfbdb2037605
keywords: ["Set Stack Length (.kframes) command", ".kframes (Set Stack Length) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .kframes (Set Stack Length)
api_type:
- NA
ms.localizationpriority: medium
---

# .kframes (Set Stack Length)


The **.kframes** command sets the default length of a stack trace display.

```dbgcmd
.kframes FrameCountDefault 
```

## <span id="ddk_meta_set_stack_length_dbg"></span><span id="DDK_META_SET_STACK_LENGTH_DBG"></span>Parameters


<span id="_______FrameCountDefault______"></span><span id="_______framecountdefault______"></span><span id="_______FRAMECOUNTDEFAULT______"></span> *FrameCountDefault*   
Specifies the number of stack frames to display when a stack trace command is used.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>User mode, kernel mode</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>Live, crash dump</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>All</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

You can use the **.kframes** command to set the default length of a stack trace display. This length controls the number of frames that the [**k, kb, kp, kP, and kv**](k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-.md) commands display and the number of DWORD\_PTRs that the **kd** command displays.

You can override this default length by using the *FrameCount* or *WordCount* parameters for these commands.

If you never issue the **.kframes** command, the default count is 20 (0x14).

## <span id="see_also"></span>See also


[**k, kb, kc, kd, kp, kP, kv (Display Stack Backtrace)**](k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-.md)

 

 






