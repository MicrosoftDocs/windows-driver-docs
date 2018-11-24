---
title: '#Elseifdef Conditional Preprocessor Directive'
description: '#Elseifdef Conditional Preprocessor Directive'
ms.assetid: 0239696a-ea6a-4fd4-b4ca-870a87022c81
keywords:
- preprocessor directives WDK GDL , conditional directives
- directives WDK GDL , conditional directives
- conditional directives WDK GDL
- Elseifdef directive WDK GDL
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# \#Elseifdef Conditional Preprocessor Directive


```GDL
#Elseifdef: symbol
```

The \#Elseifdef directive defines the end of the previous section and the start of a new conditional section. The section is preserved if the symbol is found in the preprocessor symbol dictionary and no previous section in the construct has been preserved. If the symbol is not found, the construct is deleted. The *symbol* value is required.
