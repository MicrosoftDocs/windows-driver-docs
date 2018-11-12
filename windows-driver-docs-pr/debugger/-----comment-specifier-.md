---
title: $$ (Comment Specifier)
description: If two dollar signs ( $$ ) appear at the start of a command, then the rest of the line is treated as a comment, unless the comment is terminated by a semicolon.
ms.assetid: bafd5e97-d443-4bfc-b3ee-c2867ed139a2
keywords: ["comment token ($$)", "$$ (Comment Specifier) Windows Debugging"]
ms.author: domars
ms.date: 09/17/2018
topic_type:
- apiref
api_name:
- $$ (Comment Specifier)
api_type:
- NA
ms.localizationpriority: medium
---

# $$ (Comment Specifier)


If two dollar signs ( **$$** ) appear at the start of a command, then the rest of the line is treated as a comment, unless the comment is terminated by a semicolon.


   $$ [any text]


Remarks
-------

The **$$** token is parsed like any other debugger command. Therefore, if you want to create a comment after another command, you must precede the **$$** token with a semicolon.

The **$$** token will cause the text after it to be ignored until the end of the line or until a semicolon is encountered. A semicolon terminates the comment; text after the semicolon is parsed as a standard command. This differs from [**\* (Comment Line Specifier)**](----comment-line-specifier-.md), which makes the remainder of the line a comment even if a semicolon is present.

For example, the following command will display **eax** and **ebx**, but not **ecx**:

```console
0:000> r eax; $$ some text; r ebx; * more text; r ecx 
```

Text prefixed by the [**\\***](----comment-line-specifier-.md) or **$$** tokens is not processed in any way. If you are performing remote debugging, a comment entered in the debugging server will not be visible in the debugging client, nor vice-versa. If you wish to make comment text appear in the Debugger Command window in a way visible to all parties, you should use [**.echo (Echo Comment)**](-echo--echo-comment-.md).

 

 





