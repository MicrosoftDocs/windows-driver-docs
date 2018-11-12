---
title: .echo (Echo Comment)
description: The .echo command displays a comment string.
ms.assetid: 4a291952-695c-4292-8aa5-82d497f0141c
keywords: [".echo (Echo Comment) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .echo (Echo Comment)
api_type:
- NA
ms.localizationpriority: medium
---

# .echo (Echo Comment)


The **.echo** command displays a comment string.

```dbgcmd
.echo String 
.echo "String" 
```

## <span id="ddk_meta_echo_comment_dbg"></span><span id="DDK_META_ECHO_COMMENT_DBG"></span>Parameters


<span id="_______String______"></span><span id="_______string______"></span><span id="_______STRING______"></span> *String*   
Specifies the text to display. You can also enclose *String* in quotation marks ("). Regardless of whether you use quotation marks, *String* can contain any number of spaces, commas, and single quotation marks ('). If you enclose *String* in quotation marks, it can include semicolons, but not additional quotation marks. If you do not enclose *String* in quotation marks, it can include quotation marks in any location except the first character, but it cannot include semicolons.

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

The **.echo** command causes the debugger to display *String* immediately after you enter the command.

An **.echo** command is ended if the debugger encounters a semicolon (unless the semicolon occurs within a quoted string). This restriction enables you to use **.echo** in complex constructions such as [conditional breakpoints](setting-a-conditional-breakpoint.md), as the following example shows.

```dbgcmd
0:000> bp `:143` "j (poi(MyVar)>5) '.echo MyVar Too Big'; '.echo MyVar Acceptable; gc' " 
```

The **.echo** command also provides an easy way for users of debugging servers and debugging clients to communicate with one another. For more information about this situation, see [Controlling a Remote Debugging Session](controlling-a-remote-debugging-session.md).

The **.echo** command differs from the [**$$ (Comment Specifier)**](-----comment-specifier-.md) token and the [**\* (Comment Line Specifier)**](----comment-line-specifier-.md) token, because these tokens cause the debugger to ignore the input text without displaying it.

 

 





