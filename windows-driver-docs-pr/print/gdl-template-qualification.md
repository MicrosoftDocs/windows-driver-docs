---
title: GDL Template Qualification
description: GDL Template Qualification
ms.assetid: 6a0fef55-4097-4d5b-b192-ce8a03b9c41f
keywords:
- templates WDK GDL , associating templates with keywords
- keywords WDK GDL , associating templates with keywords
- templates WDK GDL , association search criteria
- association search criteria WDK GDL
- GDL WDK , searching for entries
- GDL WDK , entries
- templates WDK GDL , qualifying to represent GDL entry
- templates WDK GDL , derived templates
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GDL Template Qualification


A template and all templates that are directly or indirectly derived from that template form an *inheritance tree* or *sub-tree*. However, derived templates that have redefined \*Name constructs are excluded from this tree.

When a template is named in a \*Members list, the GDL parser considers the named template and every template that derived from the named template as a candidate for association. If there is more than one template in this inheritance tree that qualifies, the parser will select the template that most closely fits the criteria to associate with the data entry. To qualify as the template that will represent a given data entry, the template must meet the following criteria:

-   A template that is declared as \*Virtual is automatically disqualified. However, any derived templates are considered.

-   The template's \*Name construct must match the data entry's keyword. Note that the \*Name can be inherited.

-   If the data entry is a construct, one element in the template's \*Instances list must match the data construct's instance name. Also, every base template from which the qualifying template inherits must also satisfy this requirement. Not all templates in an inheritance chain are required to have an \*Instances entry; those that do not have this entry are assumed to have satisfied this requirement by default.

-   If more than one template in an inheritance tree qualifies, the following additional criteria are considered:
    -   If a template qualifies by having every template in its inheritance chain satisfy the instance name requirement by default or by using the wildcard &lt;ANY&gt; and if another qualifying template has one or more templates in its inheritance chain satisfy the instance name requirement with an explicit match, the template that uses the explicit match will be used.
    -   Of the remaining qualifying templates, the most derived template will be used.
    -   Of the remaining qualifying templates, the most recently defined template will be used.

 

 




