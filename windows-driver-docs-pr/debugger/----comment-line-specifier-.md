---
title: Asterisk character Comment Line Specifier
description: If the asterisk character is at the start of a command, then the rest of the line is treated as a comment, even if a semicolon appears after it.
ms.assetid: 46f68e92-0758-49f2-82bb-bc4d25ddb641
keywords: ["comment line token", "Comment Line Specifier Windows Debugging"]
ms.author: domars
ms.date: 09/17/2018
topic_type:
- apiref
api_name:
- (Comment Line Specifier)
api_type:
- NA
ms.localizationpriority: medium
---

# \* (Comment Line Specifier)


If the asterisk ( **\\*** ) character is at the start of a command, then the rest of the line is treated as a comment, even if a semicolon appears after it.

```dbgcmd
    * [any text]
```

Remarks
-------

The **\\*** token is parsed like any other debugger command. Therefore, if you want to create a comment after another command, you must precede the **\\*** token with a semicolon.

The **\\*** token will cause the remainder of the line to be ignored, even if a semicolon appears after it. This differs from [**$$ (Comment Specifier)**](-----comment-specifier-.md), which creates a comment that can be terminated by a semicolon.

For example, the following command will display **eax** and **ebx**, but not **ecx**:

```console
0:000> r eax; $$ some text; r ebx; * more text; r ecx 
```

Text prefixed by the **\\*** or [**$$**](-----comment-specifier-.md) tokens is not processed in any way. If you are performing remote debugging, a comment entered in the debugging server will not be visible in the debugging client, nor vice-versa. If you wish to make comment text appear in the Debugger Command window in a way visible to all parties, you should use [**.echo (Echo Comment)**](-echo--echo-comment-.md).

 

 





