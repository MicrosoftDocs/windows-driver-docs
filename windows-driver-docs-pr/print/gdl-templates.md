---
title: GDL Templates
author: windows-driver-content
description: GDL Templates
ms.assetid: 9cce885d-395e-4f8d-8076-951d75d82410
keywords: ["GDL WDK , templates", "templates WDK GDL", "validating GDL entries WDK GDL", "GDL WDK , validating entries", "attributes WDK GDL , in templates", "constructs WDK GDL , in templates", "inheritance WDK GDL", "schemas WDK GDL , inheritance-based schemas"]
---

# GDL Templates


*GDL templates* provide a way for the parser to validate GDL entries. Each entry can be associated with a particular template.

GDL provides a standard template that you can extend by adding new templates. The standard template defines all of the [attributes](gdl-attributes.md) and [constructs](gdl-constructs.md) that are known to the operating system.

The relationship between templates is defined by [inheritance](gdl-template-inheritance.md).

The GDL parser associates every data entry in a GDL file with a template. If a data entry is a construct, the template specifies in an indirect manner all of the members that can appear within that construct. This association is applied recursively so that every data entry can have a template associated with it. Templates use specific [criteria](criteria-for-associating-gdl-templates-with-keywords.md) to define how the template relates to the data, and specific [data types](gdl-template-data-types.md) are used for templates.

GDL uses specific [directives](gdl-template-directives.md) for templates.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20GDL%20Templates%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


