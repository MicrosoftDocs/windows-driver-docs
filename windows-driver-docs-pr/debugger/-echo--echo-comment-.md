---
title: .echo (Echo Comment)
description: The .echo command displays a comment string.
keywords: [".echo (Echo Comment) Windows Debugging"]
ms.date: 11/19/2021
topic_type:
- apiref
ms.topic: reference
api_name:
- .echo (Echo Comment)
api_type:
- NA
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

### Environment

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |

 

## Remarks

The **.echo** command causes the debugger to display *String* immediately after you enter the command.

An **.echo** command is ended if the debugger encounters a semicolon (unless the semicolon occurs within a quoted string). This restriction enables you to use **.echo** in more complex constructions such as with the [j (Execute If - Else)](j--execute-if---else-.md) command, as the following example shows.

```dbgcmd
0:000> j (poi(MyVar)>5) '.echo MyVar Too Big'; '.echo MyVar Acceptable;
```

The **.echo** command also provides an easy way for users of debugging servers and debugging clients to communicate with one another. For more information about this situation, see [Controlling a Remote Debugging Session](controlling-a-remote-debugging-session.md).

The **.echo** command differs from the [**$$ (Comment Specifier)**](-----comment-specifier-.md) token and the [**\* (Comment Line Specifier)**](----comment-line-specifier-.md) token, because these tokens cause the debugger to ignore the input text without displaying it.

 

 





