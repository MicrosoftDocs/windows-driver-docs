---
title: GDL Miscellaneous Macros
description: GDL Miscellaneous Macros
ms.assetid: d3c66bc1-815d-484b-b69b-6616d2b43069
keywords:
- GDL WDK , macros
- macros WDK GDL , miscellaneous macros
- IgnoreBlock directive WDK GDL
- macros WDK GDL , examples
- constructs WDK GDL , disabling processing of constructs
- disabling processing of GDL constructs WDK GDL
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GDL Miscellaneous Macros


GDL uses a **\*IgnoreBlock** directive to disable processing of the contents of the construct. This directive is useful when implementing divide and conquer debugging strategies or to comment out obsolete code. The contents of **\*IgnoreBlock** must still conform to the basic syntax rules. Invalid GDL or large comment blocks can be enclosed within &lt;Begin/EndValue:&gt; delimiters and made the value of the **\*IgnoreBlock**.

The following code example shows how to use **\*IgnoreBlock**.

```cpp
*IgnoreBlock: <BeginValue:garbage> The code in between does not even need to be valid GDL. }{ " % !!! 
This directive is great for large blocks of comments 
or when you do not want to mark each line with *%  <EndValue:garbage> {}
```

 

 




