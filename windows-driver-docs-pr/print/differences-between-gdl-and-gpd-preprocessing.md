---
title: Differences Between GDL and GPD Preprocessing
author: windows-driver-content
description: Differences Between GDL and GPD Preprocessing
ms.assetid: 0ca79e85-1697-4f8d-b534-fe24748aaf5b
keywords: ["GPD file entries WDK Unidrv , preprocessor directives", "GPD file entries WDK Unidrv , vs. GDL file entries", "GDL WDK , vs GPD", "preprocessor directives WDK GDL , vs. GDL preprocessing", "directives WDK GDL , source file preprocessor directives", "source files WDK GDL , preprocessor directives"]
---

# Differences Between GDL and GPD Preprocessing


There are four new preprocessor directives in GDL that did not exist in the GPD implementation: **\#PreCompiled**, **\#UndefinePrefix**, **\#EnablePPDirective**, and **\#DisablePPDirective**.

In addition, the **\#Undefine** directive now also accepts no argument. The absence of the argument means that the most recently defined symbol is undefined, which restores the previously defined symbol.

We recommend that you do not use these new directives if the GDL file is also intended to be parsed by the GPD parser. If you want tp incorporate the new preprocessor directives into a GDL file that is also intended for use by GPD parsers, an alternate (backward compatibility) path must be provided that allows the older preprocessor to avoid executing these new directives. Each path should be enclosed within a **\#Ifdef:**, **\#Else**, **\#Endif** construct, as the following code example shows.

```
#Ifdef: NewParserVersion
*%   Use new preprocessor directives if the parser supports them.
*%   Lock out this entire code path by changing the prefix.
      #SetPPPrefix: #New_
      #New_PreCompiled: ...
      *%  Actually might use a mixture of old and new directives!
      #New_UndefinePrefix:
#Else:
*%  Otherwise only use the original set of directives.
      #OldDirectives: ...
#Endif:
```

In addition, the preprocessor prefix should be set to something different while running the new directives fork. The parser will warn if it encounters directives with the wrong prefix.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Differences%20Between%20GDL%20and%20GPD%20Preprocessing%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


