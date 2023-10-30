---
title: General attributes
description: General attributes
keywords:
- printer attributes WDK Unidrv , general
- general printer attributes WDK Unidrv
- general printer attributes WDK Unidrv , about general printer attributes
ms.date: 06/22/2023
---

# General attributes

[!include[Print Support Apps](../includes/print-support-apps.md)]

*General attributes* represent one of the [attribute types](attribute-types.md) defined by the GPD language. General attributes aren't associated with a particular feature or option. The general attributes are divided into the following groups:

[Root-Level-Only Attributes](root-level-only-attributes.md)

[General Printing Attributes](general-printing-attributes.md)

[Text Printing Attributes](text-printing-attributes.md)

[Raster Printing Attributes](raster-printing-attributes.md)

[Vector Printing Attributes](vector-printing-attributes.md)

Usually, you place all general attributes in a GPD file at root level (that is, not inside braces). The root-level-only attributes must always be placed at root level.

Occasionally, the value of a general attribute (except for the root-level-only attributes) is dependent on configuration parameters. In such a case, the attribute entry might be placed within an \*Option statement, or within a [\*Case](conditional-statements.md) statement (located either at root level or contained in an \*Option statement). If the attribute isn't at root level (either because it's contained in an \*Option statement or because it is in a nonroot-level \*Case statement), the attribute name must be prefixed by the EXTERN\_GLOBAL symbol, as follows:

EXTERN_GLOBAL: \**AttributeName*: *AttributeValue*

For more information about specifying configuration dependencies, see [Conditional Statements](conditional-statements.md).
