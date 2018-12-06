---
title: GDL Preprocessor Conditional Directives
description: GDL Preprocessor Conditional Directives
ms.assetid: 5eb4bcbf-3f5e-44cc-b4e5-716a15e43b15
keywords:
- directives WDK GDL , source file preprocessor directives
- source files WDK GDL , preprocessor directives
- preprocessor directives WDK GDL , conditional directives
- directives WDK GDL , conditional directives
- conditional directives WDK GDL
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GDL Preprocessor Conditional Directives


GDL preprocessor conditional directives define conditional constructs. Each conditional construct begins with the **\#Ifdef** directive and is terminated by the **\#Endif** directive. In between, the **\#Elseifdef** directive might appear zero, one, or more times. The optional **\#Else** directive must appear between the last **\#Elseifdef** directive (if any used) and the final **\#Endif** directive.

Each of these directives partition the intervening data (non-preprocessor directives) into conditional sections; each section is preserved for the next stage of parsing or deleted during preprocessing as described below. Data that is not to be processed and that is not contained within any conditional constructs is always preserved.

Conditional section directives can be nested. The entire conditional construct from the **\#Ifdef** to the closing **\#Endif** must reside entirely within one section of the enclosing conditional construct.

GDL uses the following conditional directives:

[\#Ifdef](-ifdef-conditional-preprocessor-directive.md)

[\#Elseifdef](-elseifdef-conditional-preprocessor-directive.md)

[\#Else](-else-conditional-preprocessor-directive.md)

[\#Endif](-endif-conditional-preprocessor-directive.md)

 

 




