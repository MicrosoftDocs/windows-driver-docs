---
title: Production Template Directive
description: Production Template Directive
ms.assetid: 5deae299-389a-4de4-8f2f-7c247f045ada
keywords:
- Production directive WDK GDL
- constructs WDK GDL , valid combinations
- templates WDK GDL , host template
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Production Template Directive


The \*Production template directive specifies valid combinations of members that can appear within a particular construct. This directive can appear only within templates with \*Type: CONSTRUCT.

If this directive is present, the production is evaluated against each instance of a construct that is bound to the production's host template. The host template is the template that contains the Production directive. If the Production directive evaluates to **FALSE**, a warning message is issued, but processing is otherwise unaffected. If the host template contains no Production directives, no validation is performed.

The \*Production directive appears at the root level of the host template construct. If more than one \*Production directive appears at the root level, only the most recently defined directive will be evaluated. The result of evaluating a Production directive is a Boolean value.

The \*Production directive is itself a construct. The child elements of the \*Production directive are either other \*Production constructs or \*Member constructs or a combination of both (also called child productions). You cannot use namespace directives within the \*Production directive.

Each child production that is contained within the \*Production directive also evaluates to **TRUE** or **FALSE**. The Production directive is evaluated by first evaluating each of its child productions. The result for the enclosing parent Production directive is obtained by performing a simple logical operation on the results of each of the child productions. The type of logical operation to apply is specified by vValue of the \*Production directive.

The value of the \*Production directive can be one of the following symbols: EXACTLY\_ONE, SATISFY\_ALL, or AT\_LEAST\_ONE.

The following example shows a production directive.

```cpp
*Production: EXACTLY_ONE
{   ... child Productions ... }
```

The following algorithm defines the production directive values:

1.  If the production specifies EXACTLY\_ONE, this production evaluates to **TRUE** if exactly one child production evaluates to **TRUE**, with the remainder being **FALSE**. Otherwise, the production evaluates to **FALSE**.

2.  If the production specifies SATISFY\_ALL, this production evaluates to **TRUE** only if all of the child productions evaluate to **TRUE**. Otherwise, the production evaluates to **FALSE**.

3.  If the production specifies AT\_LEAST\_ONE, this production evaluates to **TRUE** if at least one or more child productions evaluate to **TRUE**. Otherwise, the production evaluates to **FALSE**.

\*Production directives can be nested to arbitrary depth.

 

 




