---
title: Production Template Directive
author: windows-driver-content
description: Production Template Directive
ms.assetid: 5deae299-389a-4de4-8f2f-7c247f045ada
keywords:
- Production directive WDK GDL
- constructs WDK GDL , valid combinations
- templates WDK GDL , host template
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Production Template Directive


The \*Production template directive specifies valid combinations of members that can appear within a particular construct. This directive can appear only within templates with \*Type: CONSTRUCT.

If this directive is present, the production is evaluated against each instance of a construct that is bound to the production's host template. The host template is the template that contains the Production directive. If the Production directive evaluates to **FALSE**, a warning message is issued, but processing is otherwise unaffected. If the host template contains no Production directives, no validation is performed.

The \*Production directive appears at the root level of the host template construct. If more than one \*Production directive appears at the root level, only the most recently defined directive will be evaluated. The result of evaluating a Production directive is a Boolean value.

The \*Production directive is itself a construct. The child elements of the \*Production directive are either other \*Production constructs or \*Member constructs or a combination of both (also called child productions). You cannot use namespace directives within the \*Production directive.

Each child production that is contained within the \*Production directive also evaluates to **TRUE** or **FALSE**. The Production directive is evaluated by first evaluating each of its child productions. The result for the enclosing parent Production directive is obtained by performing a simple logical operation on the results of each of the child productions. The type of logical operation to apply is specified by vValue of the \*Production directive.

The value of the \*Production directive can be one of the following symbols: EXACTLY\_ONE, SATISFY\_ALL, or AT\_LEAST\_ONE.

The following example shows a production directive.

```
*Production: EXACTLY_ONE
{   ... child Productions ... }
```

The following algorithm defines the production directive values:

1.  If the production specifies EXACTLY\_ONE, this production evaluates to **TRUE** if exactly one child production evaluates to **TRUE**, with the remainder being **FALSE**. Otherwise, the production evaluates to **FALSE**.

2.  If the production specifies SATISFY\_ALL, this production evaluates to **TRUE** only if all of the child productions evaluate to **TRUE**. Otherwise, the production evaluates to **FALSE**.

3.  If the production specifies AT\_LEAST\_ONE, this production evaluates to **TRUE** if at least one or more child productions evaluate to **TRUE**. Otherwise, the production evaluates to **FALSE**.

\*Production directives can be nested to arbitrary depth.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Production%20Template%20Directive%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


