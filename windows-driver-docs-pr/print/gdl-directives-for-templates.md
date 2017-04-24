---
title: GDL Directives for Templates
author: windows-driver-content
description: GDL Directives for Templates
ms.assetid: c68650ae-d6ee-4ae3-afa2-655f2bcad916
keywords:
- directives WDK GDL , template directives
- source files WDK GDL , template directives
- template directives WDK GDL
- parser WDK GDL , directives
- Template directive WDK GDL
- Name directive WDK GDL
- Inherits directive WDK GDL
- Members directive WDK GDL
- Type directive WDK GDL
- Production directive WDK GDL
- Member directive WDK GDL
- Occurs directive WDK GDL
- Additive directive WDK GDL
- ValueType directive WDK GDL
- DataType directive WDK GDL
- ElementType directive WDK GDL
- ArrayLabel directive WDK GDL
- ElementTags directive WDK GDL
- templates WDK GDL , directives
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# GDL Directives for Templates


GDL has template directives that define the GDL schema by using templates.

GDL contains the following template directive:

-   **\*Template** defines a template construct.

Several other directives are used within the template construct to complete the definition. The following lists describes some of the directives that are used within the template construct:

-   **\*Name** is the name of the data entry keyword to bind to.

-   **\*Inherits** inherits the properties of the specified template.

-   **\*Members** uses the specified template trees in the binding process.

-   **\*Type** is the type of object that this template defines.

-   **\*Production**, **\*Member**, and **\*Occurs** define the content that is allowed for a construct. Note that the content depends on the configuration.

-   **\*Additive** describes which definition of an entry shall be shown in the snapshot if the entry is multiply defined.

-   **\*ValueType** assigns a data type to the value of an attribute.

-   **\*DataType**, **\*ElementType**, **\*ArrayLabel**, and **\*ElementTags** define the data types.

For more information about template directives, see [GDL Template Directives](gdl-template-directives.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20GDL%20Directives%20for%20Templates%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


