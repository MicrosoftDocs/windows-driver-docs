---
title: '#Ifdef Conditional Preprocessor Directive'
description: '#Ifdef Conditional Preprocessor Directive'
ms.assetid: 57c59bf8-19bd-47bc-858d-ea500d44fb4d
keywords:
- preprocessor directives WDK GDL , conditional directives
- directives WDK GDL , conditional directives
- conditional directives WDK GDL
- Ifdef directive WDK GDL
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# \#Ifdef Conditional Preprocessor Directive


```GDL
#Ifdef: symbol
```

The \#Ifdef directive defines the start of a conditional construct and section. The section is preserved if the symbol is found in the preprocessor symbol dictionary. If the symbol is not found, it is deleted. The *symbol* value is required.
