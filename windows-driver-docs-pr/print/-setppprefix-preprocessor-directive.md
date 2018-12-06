---
title: '#SetPPPrefix Preprocessor Directive'
description: '#SetPPPrefix Preprocessor Directive'
ms.assetid: 3520aa66-1090-40db-9c9f-cfba0e6e2bee
keywords:
- preprocessor directives WDK GDL , keywords
- keywords WDK GDL
- reserved keywords WDK
- SetPPPrefix directive WDK GDL
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# \#SetPPPrefix Preprocessor Directive


```GDL
#SetPPPrefix: prefix
```

The \#SetPPPrefix directive makes the *prefix* value the current preprocessor prefix. *prefix* can be any token value and is required.

You can define the same prefix more than once. The prefix is user-selectable because it allows directives to be unambiguously distinguished from any existing not-to-be-processed data. The following code example shows how to change a prefix if a normal GDL entry contains a value that might be confused with an actual directive.

```GDL
*%  assume current prefix is #
#SetPPPrefix: #Temp#
#Temp#Ifdef:  WINNT_60
*InfoMessage: "Use the Preprocessor Directive
#PreCompiled to make your GDL file sharable."
#Temp#Endif:  WINNT_60
#Temp#UndefinePrefix
*%  now back to normal # prefix.
```
