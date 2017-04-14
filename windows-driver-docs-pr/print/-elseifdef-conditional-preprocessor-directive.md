---
title: \ Elseifdef Conditional Preprocessor Directive
author: windows-driver-content
description: \ Elseifdef Conditional Preprocessor Directive
ms.assetid: 0239696a-ea6a-4fd4-b4ca-870a87022c81
keywords: ["preprocessor directives WDK GDL , conditional directives", "directives WDK GDL , conditional directives", "conditional directives WDK GDL", "Elseifdef directive WDK GDL"]
---

# \#Elseifdef Conditional Preprocessor Directive


```
#Elseifdef: symbol
```

The \#Elseifdef directive defines the end of the previous section and the start of a new conditional section. The section is preserved if the symbol is found in the preprocessor symbol dictionary and no previous section in the construct has been preserved. If the symbol is not found, the construct is deleted. The *symbol* value is required.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20#Elseifdef%20Conditional%20Preprocessor%20Directive%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


