---
title: '#DisablePPDirective Preprocessor Directive'
description: '#DisablePPDirective Preprocessor Directive'
ms.assetid: 5f85a6b1-a72f-45e2-901a-7bce94b4793c
keywords:
- preprocessor directives WDK GDL , keywords
- keywords WDK GDL
- reserved keywords WDK
- DisablePPDirective directive WDK GDL
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# \#DisablePPDirective Preprocessor Directive


```GDL
#DisablePPDirective:    Directive
```

The \#DisablePPDirective directive disables an enabled directive. If a new GDL file includes an older GDL file that has a namespace collision with one or more of the new directive names, the new directives can be disabled before including the file and then reenabled afterwards. The base name is a required value.

This preprocessor directive is new for GDL.

The following code examples shows how you can use this directive.

```GDL
#DisablePPDirective: duplicateDirective
#Include: "OlderFile.gdl"  *%  This file uses the name 
    *%  duplicateDirective because it does not expect that name to be interpreted by 
    *%  the preprocessor.
#EnablePPDirective: duplicateDirective
    *%  Reactivate  duplicateDirective  so it can be used by 
    *%  the newer host file.
```

 

 




