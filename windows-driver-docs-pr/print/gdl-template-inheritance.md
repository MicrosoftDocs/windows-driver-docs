---
title: GDL Template Inheritance
description: GDL Template Inheritance
ms.assetid: 0e3271ee-6b58-4f57-a0be-18715705604f
keywords:
- GDL WDK , templates
- templates WDK GDL , inheritance
- inheritance WDK GDL
- schemas WDK GDL , inheritance-based schemas
- templates WDK GDL , derived templates
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GDL Template Inheritance


The relationship between one GDL template and another is defined by *inheritance*. A template can inherit the properties from only one other template. Many templates can inherit from one base template. Multiple inheritance (that is, inheriting from more than one template) is not supported.

Template inheritance creates compact definitions, addresses the need to express variants of a basic type in a simple and clear way, and clearly shows the structure and organization of the data. Template inheritance also enables you to extend and build on the base framework without needing to alter or redefine the base framework.

Because the content of the data depends on the context in which the construct occurs, template relationships are not defined by an XML-type schema. For example, the \*Options construct that appears within PaperSize \*Feature has different members than the \*Options construct that appears within Resolution \*Feature. By using the object-oriented concept of inheritance, the relationship between data constructs can be precise without ambiguity.

Inheritance of templates also requires you to understand the structure of the data. For example, all \*Feature constructs share some properties in common. These properties are most appropriately defined by a base feature template. You can then derive specific feature definitions from the base template by adding feature-specific properties or restrictions. Deriving each template from the base feature template assures that all derived templates inherit all of the essential properties that are common to all feature definitions. If you always consider what properties a particular template should define and which properties should be left to the derived templates, you can focus on the organization, structure of, and relationships between the data.

 

 




