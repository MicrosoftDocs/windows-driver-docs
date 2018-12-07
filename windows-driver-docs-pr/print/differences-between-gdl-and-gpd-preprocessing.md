---
title: Differences Between GDL and GPD Preprocessing
description: Differences Between GDL and GPD Preprocessing
ms.assetid: 0ca79e85-1697-4f8d-b534-fe24748aaf5b
keywords:
- GPD file entries WDK Unidrv , preprocessor directives
- GPD file entries WDK Unidrv , vs. GDL file entries
- GDL WDK , vs GPD
- preprocessor directives WDK GDL , vs. GDL preprocessing
- directives WDK GDL , source file preprocessor directives
- source files WDK GDL , preprocessor directives
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Differences Between GDL and GPD Preprocessing


There are four new preprocessor directives in GDL that did not exist in the GPD implementation: **\#PreCompiled**, **\#UndefinePrefix**, **\#EnablePPDirective**, and **\#DisablePPDirective**.

In addition, the **\#Undefine** directive now also accepts no argument. The absence of the argument means that the most recently defined symbol is undefined, which restores the previously defined symbol.

We recommend that you do not use these new directives if the GDL file is also intended to be parsed by the GPD parser. If you want tp incorporate the new preprocessor directives into a GDL file that is also intended for use by GPD parsers, an alternate (backward compatibility) path must be provided that allows the older preprocessor to avoid executing these new directives. Each path should be enclosed within a **\#Ifdef:**, **\#Else**, **\#Endif** construct, as the following code example shows.

```cpp
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

 

 




