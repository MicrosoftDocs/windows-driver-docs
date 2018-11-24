---
title: GDL Templates
description: GDL Templates
ms.assetid: 9cce885d-395e-4f8d-8076-951d75d82410
keywords:
- GDL WDK , templates
- templates WDK GDL
- validating GDL entries WDK GDL
- GDL WDK , validating entries
- attributes WDK GDL , in templates
- constructs WDK GDL , in templates
- inheritance WDK GDL
- schemas WDK GDL , inheritance-based schemas
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GDL Templates


*GDL templates* provide a way for the parser to validate GDL entries. Each entry can be associated with a particular template.

GDL provides a standard template that you can extend by adding new templates. The standard template defines all of the [attributes](gdl-attributes.md) and [constructs](gdl-constructs.md) that are known to the operating system.

The relationship between templates is defined by [inheritance](gdl-template-inheritance.md).

The GDL parser associates every data entry in a GDL file with a template. If a data entry is a construct, the template specifies in an indirect manner all of the members that can appear within that construct. This association is applied recursively so that every data entry can have a template associated with it. Templates use specific [criteria](criteria-for-associating-gdl-templates-with-keywords.md) to define how the template relates to the data, and specific [data types](gdl-template-data-types.md) are used for templates.

GDL uses specific [directives](gdl-template-directives.md) for templates.

 

 




