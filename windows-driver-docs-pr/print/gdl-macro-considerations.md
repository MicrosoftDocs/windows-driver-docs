---
title: GDL Macro Considerations
author: windows-driver-content
description: GDL Macro Considerations
ms.assetid: b1e3e32f-2f5f-47ae-b69b-7645ada59c2a
keywords:
- GDL WDK , macros
- macros WDK GDL , considerations
- passing GDL macro references WDK
- macros WDK GDL , passing macro references
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# GDL Macro Considerations


GDL macros have scope and lifetime. Macros can be referenced only from the point of definition until the end of the nesting level that contains the macro definition construct.

A macro that is defined at the root level has unlimited scope and lifetime. Multiple macros with the same name can be defined in the same namespace. The more recent definitions hide any previous definitions. The previous definitions will be uncovered after the topmost definition expires.

If a block macro definition uses a **\#Includes** directive to include a precompiled file, the contents of the file will not appear in the macro definition because files that are declared as precompiled are not used in-line but become stand-alone entities.

For backward compatibility, parameter value support is enabled for all value macro definitions.

A macro definition cannot reference itself. However, a macro reference can pass a reference to itself as a parameter.

The following code example shows how to pass a reference.

```
*InsertBlock:  Myself(Myself(AnotherMacro))
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20GDL%20Macro%20Considerations%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


