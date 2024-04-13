---
title: '#UndefinePrefix Preprocessor Directive'
description: '#UndefinePrefix Preprocessor Directive'
keywords:
- preprocessor directives WDK GDL , keywords
- keywords WDK GDL
- reserved keywords WDK
- UndefinePrefix directive WDK GDL
ms.date: 04/20/2017
---

# \#UndefinePrefix Preprocessor Directive


```GDL
#UndefinePrefix:
```

The \#UndefinePrefix directive deletes the current prefix. The previously defined prefix becomes the current prefix. Only prefixes that you define by using the [\#SetPPPrefix](-setppprefix-preprocessor-directive.md) directive can be undefined. The system default prefix cannot be undefined. This directive does not use a symbol.

This preprocessor prefix is new for GDL.
