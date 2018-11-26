---
title: Member Template Directive
description: Member Template Directive
ms.assetid: 3f4bdf3c-30cb-4edc-bd9e-422c4bfbb5b7
keywords:
- Member directive WDK GDL
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Member Template Directive


The \*`Member` directive is also a construct. The value of this construct is a template name. This template name must appear in the \*Members list of the host template (that is, the template that the production resides within) or in the \*Members list that the host template inherits from (directly or indirectly). The \*`Member` construct can contain an optional child attribute called \***Occurs**.

\***Occurs** specifies the number of instances that are bound to the template that the \*Members production specifies, which might appear within an instance of the host template. Instances that bind-to templates derive from the template that is named by the \*Members production will count as an occurrence of an instance of that template. If the number of such occurrences falls within the range that the \***Occurs** directive defines, the \*`Member` directive will evaluate to **TRUE**; otherwise, the directive will evaluate as **FALSE**. Attribute or construct templates (\*Type: CONSTRUCT or \*Type: ATTRIBUTE) can be referenced in a \*`Member` construct. The \*`Member` construct that appears within a \*Production directive is not the same as the \*Members directive that appears as a child of a \*Template directive. \*`Member` is a construct and is singular, and \*Members is an attribute and is plural (ends with the letter "s").

\***Occurs** specifies the number of instances that are bound to the template that the \*Members production specifies. A specific value can be specified or a range of values can be specified by using a pair of numbers that are separated with a hyphen (-). If a range is specified, the first number must be smaller than the second. Negative numbers are not allowed. The allowed range includes the specified endpoints. The value 0 is allowed. The GPD wildcard (\*) is allowed and matches any value that ranges from 0 to infinity. If the wildcard (\*) appears as the upper endpoint of a range, there is no upper limit. If the wildcard appears as the lower limit of a range, the upper limit is ignored. The number or pair of numbers can be enclosed within square brackets (\[\]) for visual emphasis.

If the \***Occurs** attribute is omitted from the \*`Member` construct, a range from 0 through infinity (that is, \[0-\*\]) is assumed and the \*`Member` production will always evaluate to **TRUE**.

When a \*`Member` production names a construct template, the \***Occurs** count does not distinguish between the different instances of the construct. So three different instances of a construct that are bound to the same template will have the same occurrence count as three identical instances of the same construct.

For example, if both **PaperSize** and **InputSlot** are bound to the same template and if \***Feature: PaperSize** is defined twice, the occurrence count will be two. If \***Feature: PaperSize** is defined once and \***Feature: InputSlot** is defined twice, the occurrence count will be three.

No other attributes or constructs are allowed within the \*`Member` directive.

When the \*Members directive is in conjunction with the template binding process, the \*Members directive attempts to associate a template with each child element that appears within a construct. But it does not specify how many times a child element can appear or specify any dependencies among or between child elements. The \*Production directive is responsible for specifying these requirements. Note that the \*Members directive is still required even when you use the \*Production directive.

 

 




