---
title: GDL Preprocessor Keywords
description: GDL Preprocessor Keywords
ms.assetid: 95ad9645-7c16-421a-937e-d4ada587d1e1
keywords:
- directives WDK GDL , source file preprocessor directives
- source files WDK GDL , preprocessor directives
- preprocessor directives WDK GDL , keywords
- keywords WDK GDL
- reserved keywords WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 




