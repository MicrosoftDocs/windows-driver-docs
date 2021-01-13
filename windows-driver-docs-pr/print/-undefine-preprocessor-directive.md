---
title: '#Undefine Preprocessor Directive'
description: '#Undefine Preprocessor Directive'
keywords:
- preprocessor directives WDK GDL , keywords
- keywords WDK GDL
- reserved keywords WDK
- Undefine directive WDK GDL
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# \#Undefine Preprocessor Directive


```GDL
#Undefine: symbol
```

The \#Undefine directive removes the *symbol* value from the preprocessor symbol dictionary. If the symbol has been defined multiple times, only the most recent definition of *symbol* is removed.

The *symbol* value is optional. If you omit this value, the most recently defined symbol is removed. However, the delimiting colon (:) is still required.
