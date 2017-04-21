---
title: GDL Template Qualification
author: windows-driver-content
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
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20GDL%20Template%20Qualification%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


