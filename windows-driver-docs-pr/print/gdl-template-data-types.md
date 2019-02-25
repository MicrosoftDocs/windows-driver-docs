---
title: GDL Template Data Types
description: GDL Template Data Types
ms.assetid: 9dd7ff66-9e50-490d-b7a4-76d645e2b9a5
keywords:
- templates WDK GDL , data types
- GDL WDK , templates
- data types WDK GDL
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GDL Template Data Types


*GDL template data types* can be classified as [primitive](gdl-primitive-data-types.md) data types and [compound](gdl-compound-data-types.md) data types.

After a data type has been assigned to an attribute template, the parser filter will attempt to parse the value that appears in any GDL entry that is an instance of this template by using the syntax rules that are defined for that data type. You can define some of the syntax by [template directives](gdl-template-directives.md). If the parsing is successful, that data type will map to one or more XML primitive types, which are then emitted in the snapshot as child elements of the attribute.

Templates have special rules for [inheritance](data-type-template-inheritance.md).

For more information about template data types, see the following sections:

[GDL Primitive Data Types](gdl-primitive-data-types.md)

[GDL Compound Data Types](gdl-compound-data-types.md)

[Using Templates to Define Data Types](defining-data-types-by-using-templates.md)

[Data Type Template Inheritance](data-type-template-inheritance.md)

 

 




