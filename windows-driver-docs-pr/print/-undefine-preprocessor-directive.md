---
title: '\ Undefine Preprocessor Directive'
author: windows-driver-content
description: '\ Undefine Preprocessor Directive'
ms.assetid: 78f6a895-2c30-4a6f-8916-4c18e22e4e70
keywords:
- preprocessor directives WDK GDL , keywords
- keywords WDK GDL
- reserved keywords WDK
- Undefine directive WDK GDL
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# \#Undefine Preprocessor Directive


```
#Undefine: symbol
```

The \#Undefine directive removes the *symbol* value from the preprocessor symbol dictionary. If the symbol has been defined multiple times, only the most recent definition of *symbol* is removed.

The *symbol* value is optional. If you omit this value, the most recently defined symbol is removed. However, the delimiting colon (:) is still required.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20#Undefine%20Preprocessor%20Directive%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


