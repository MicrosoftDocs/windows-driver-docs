---
title: General Attributes
description: General Attributes
ms.assetid: c48fabff-0580-478f-b423-d959815bbeb4
keywords:
- printer attributes WDK Unidrv , general
- general printer attributes WDK Unidrv
- general printer attributes WDK Unidrv , about general printer attributes
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# General Attributes





*General attributes* represent one of the [attribute types](attribute-types.md) defined by the GPD language. General attributes are not associated with a particular feature or option. The general attributes are divided into the following groups:

[Root-Level-Only Attributes](root-level-only-attributes.md)

[General Printing Attributes](general-printing-attributes.md)

[Text Printing Attributes](text-printing-attributes.md)

[Raster Printing Attributes](raster-printing-attributes.md)

[Vector Printing Attributes](vector-printing-attributes.md)

Usually, you place all general attributes in a GPD file at root level (that is, not inside braces). The root-level-only attributes must always be placed at root level.

Occasionally, the value of a general attribute (except for the root-level-only attributes) is dependent on configuration parameters. In such a case, the attribute entry might be placed within an \*Option statement, or a within a [\*Case](conditional-statements.md) statement (located either at root level or contained in an \*Option statement). If the attribute is not at root level (either because it is contained in an \*Option statement or because it is in a nonroot-level \*Case statement), the attribute name must be prefixed by the EXTERN\_GLOBAL symbol, as follows:

<table>
<colgroup>
<col width="100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>EXTERN_GLOBAL: *<em>AttributeName</em>: <em>AttributeValue</em></p></td>
</tr>
</tbody>
</table>

 

For more information about specifying configuration dependencies, see [Conditional Statements](conditional-statements.md).

 

 




