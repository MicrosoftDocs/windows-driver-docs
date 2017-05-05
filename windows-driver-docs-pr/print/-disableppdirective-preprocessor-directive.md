---
title: '\ DisablePPDirective Preprocessor Directive'
author: windows-driver-content
description: '\ DisablePPDirective Preprocessor Directive'
ms.assetid: 5f85a6b1-a72f-45e2-901a-7bce94b4793c
keywords:
- preprocessor directives WDK GDL , keywords
- keywords WDK GDL
- reserved keywords WDK
- DisablePPDirective directive WDK GDL
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# \#DisablePPDirective Preprocessor Directive


```
#DisablePPDirective:    Directive
```

The \#DisablePPDirective directive disables an enabled directive. If a new GDL file includes an older GDL file that has a namespace collision with one or more of the new directive names, the new directives can be disabled before including the file and then reenabled afterwards. The base name is a required value.

This preprocessor directive is new for GDL.

The following code examples shows how you can use this directive.

```
#DisablePPDirective: duplicateDirective
#Include: "OlderFile.gdl"  *%  This file uses the name 
    *%  duplicateDirective because it does not expect that name to be interpreted by 
    *%  the preprocessor.
#EnablePPDirective: duplicateDirective
    *%  Reactivate  duplicateDirective  so it can be used by 
    *%  the newer host file.
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20#DisablePPDirective%20Preprocessor%20Directive%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


