---
title: GDL Preprocessor Keywords
author: windows-driver-content
description: GDL Preprocessor Keywords
ms.assetid: 95ad9645-7c16-421a-937e-d4ada587d1e1
keywords:
- directives WDK GDL , source file preprocessor directives
- source files WDK GDL , preprocessor directives
- preprocessor directives WDK GDL , keywords
- keywords WDK GDL
- reserved keywords WDK
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# GDL Preprocessor Keywords


To avoid confusing the preprocessor, you should consider the GDL preprocessor keywords to be reserved. Because you can set the preprocessor prefix to any arbitrary string, you should avoid defining any keyword that might be mistaken for any of these directives.

The GDL preprocessor uses the following keyword commands, which should be considered reserved:

[\#Define](-define-preprocessor-directive.md)

[\#Undefine](-undefine-preprocessor-directive.md)

[\#Include](-include-preprocessor-directive.md)

[\#SetPPPrefix](-setppprefix-preprocessor-directive.md)

[\#UndefinePrefix](-undefineprefix-preprocessor-directive.md)

[\#PreCompiled](-precompiled-preprocessor-directive.md)

[\#EnablePPDirective](-enableppdirective-preprocessor-directive.md)

[\#DisablePPDirective](-disableppdirective-preprocessor-directive.md)

The preprocessor also uses [GDL preprocessor conditional directives](gdl-preprocessor-conditional-directives.md) to perform conditional tests on syntax blocks of code.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20GDL%20Preprocessor%20Keywords%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


