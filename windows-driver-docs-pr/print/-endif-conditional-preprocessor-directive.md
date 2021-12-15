---
title: '#Endif Conditional Preprocessor Directive'
description: '#Endif Conditional Preprocessor Directive'
keywords:
- preprocessor directives WDK GDL , conditional directives
- directives WDK GDL , conditional directives
- conditional directives WDK GDL
- Endif directive WDK GDL
ms.date: 04/20/2017
---

# \#Endif Conditional Preprocessor Directive


```GDL
#Endif:
```

The \#Endif directive defines the end of the previous section and the conditional construct. No symbol is used. You can use a fake symbol name as the value of the \#Endif directive to help the reader. Consider the following code example.

```GDL
    #Ifdef: symbolA

        #Ifdef: symbolB

        #Elseifdef: symbolD

        #Endif: symbolB

    #Endif: symbolA
```

Indentation of each nested construct might also be helpful to the reader.
