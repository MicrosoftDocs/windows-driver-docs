---
title: GDL Directives for Templates
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
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 




