---
title: GDL Template Data Types
author: windows-driver-content
description: GDL Template Data Types
ms.assetid: 9dd7ff66-9e50-490d-b7a4-76d645e2b9a5
keywords:
- templates WDK GDL , data types
- GDL WDK , templates
- data types WDK GDL
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20GDL%20Template%20Data%20Types%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


