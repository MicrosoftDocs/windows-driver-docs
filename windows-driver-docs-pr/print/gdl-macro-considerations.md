---
title: GDL Macro Considerations
description: GDL Macro Considerations
ms.assetid: b1e3e32f-2f5f-47ae-b69b-7645ada59c2a
keywords:
- GDL WDK , macros
- macros WDK GDL , considerations
- passing GDL macro references WDK
- macros WDK GDL , passing macro references
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GDL Macro Considerations


GDL macros have scope and lifetime. Macros can be referenced only from the point of definition until the end of the nesting level that contains the macro definition construct.

A macro that is defined at the root level has unlimited scope and lifetime. Multiple macros with the same name can be defined in the same namespace. The more recent definitions hide any previous definitions. The previous definitions will be uncovered after the topmost definition expires.

If a block macro definition uses a **\#Includes** directive to include a precompiled file, the contents of the file will not appear in the macro definition because files that are declared as precompiled are not used in-line but become stand-alone entities.

For backward compatibility, parameter value support is enabled for all value macro definitions.

A macro definition cannot reference itself. However, a macro reference can pass a reference to itself as a parameter.

The following code example shows how to pass a reference.

```cpp
*InsertBlock:  Myself(Myself(AnotherMacro))
```

 

 




