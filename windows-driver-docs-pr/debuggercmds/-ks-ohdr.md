---
title: "!ks.ohdr (WinDbg)"
description: "The !ks.ohdr extension displays details of a kernel streaming object header."
keywords: ["!ks.ohdr Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- ks.ohdr
api_type:
- NA
---

# !ks.ohdr


The **!ks.ohdr** extension displays details of a kernel streaming object header.

```dbgcmd
!ks.ohdr Object [Level] [Flags]  
```

## Parameters


<span id="_______Object______"></span><span id="_______object______"></span><span id="_______OBJECT______"></span> *Object*   
This parameter specifies a pointer to a KS object header. If *Object* is not valid, the command returns an error.

<span id="_______Level______"></span><span id="_______level______"></span><span id="_______LEVEL______"></span> *Level*   
Optional. Values are the same as those for [**!ks.dump**](-ks-dump.md).

<span id="_______Flags______"></span><span id="_______flags______"></span><span id="_______FLAGS______"></span> *Flags*   
Optional. Values are the same as those for [**!ks.dump**](-ks-dump.md).

## DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>winxp\Ks.dll</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Ks.dll</p></td>
</tr>
</tbody>
</table>

 

## Additional Information

For more information, see [Kernel Streaming Debugging](../debugger/kernel-streaming-debugging.md).

## Remarks

The **!ks.ohdr** command works similarly to [**!ks.objhdr**](-ks-objhdr.md) in that it displays details of a KS object header. The difference is that the caller provides the direct address of the KS object header, instead of the address of the associated file object.

Levels and flags for **!ks.ohdr** are identical to those described in [**!ks.dump**](-ks-dump.md).

If the data you are querying is not paged out, consider using [**!ks.dump**](-ks-dump.md) instead of **!ks.ohdr**.

