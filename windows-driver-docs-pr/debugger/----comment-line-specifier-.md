---
title: \ (Comment Line Specifier)
description: If the asterisk ( \ ) character is at the start of a command, then the rest of the line is treated as a comment, even if a semicolon appears after it.
ms.assetid: 46f68e92-0758-49f2-82bb-bc4d25ddb641
keywords: ["comment line token ( )", "(Comment Line Specifier) Windows Debugging"]
topic_type:
- apiref
api_name:
- (Comment Line Specifier)
api_type:
- NA
---

# \* (Comment Line Specifier)


If the asterisk ( **\*** ) character is at the start of a command, then the rest of the line is treated as a comment, even if a semicolon appears after it.

``` syntax
* [any text]
```

Remarks
-------

The **\*** token is parsed like any other debugger command. Therefore, if you want to create a comment after another command, you must precede the **\*** token with a semicolon.

The **\*** token will cause the remainder of the line to be ignored, even if a semicolon appears after it. This differs from [**$$ (Comment Specifier)**](-----comment-specifier-.md), which creates a comment that can be terminated by a semicolon.

For example, the following command will display **eax** and **ebx**, but not **ecx**:

``` syntax
0:000> r eax; $$ some text; r ebx; * more text; r ecx 
```

Text prefixed by the **\*** or [**$$**](-----comment-specifier-.md) tokens is not processed in any way. If you are performing remote debugging, a comment entered in the debugging server will not be visible in the debugging client, nor vice-versa. If you wish to make comment text appear in the Debugger Command window in a way visible to all parties, you should use [**.echo (Echo Comment)**](-echo--echo-comment-.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20*%20%20%28Comment%20Line%20Specifier%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




