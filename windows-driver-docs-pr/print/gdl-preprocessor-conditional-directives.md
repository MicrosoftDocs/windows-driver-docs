---
title: GDL Preprocessor Conditional Directives
author: windows-driver-content
description: GDL Preprocessor Conditional Directives
ms.assetid: 5eb4bcbf-3f5e-44cc-b4e5-716a15e43b15
keywords:
- directives WDK GDL , source file preprocessor directives
- source files WDK GDL , preprocessor directives
- preprocessor directives WDK GDL , conditional directives
- directives WDK GDL , conditional directives
- conditional directives WDK GDL
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20GDL%20Preprocessor%20Conditional%20Directives%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


