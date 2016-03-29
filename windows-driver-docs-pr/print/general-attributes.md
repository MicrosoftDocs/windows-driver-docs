---
title: General Attributes
description: General Attributes
ms.assetid: c48fabff-0580-478f-b423-d959815bbeb4
keywords: ["printer attributes WDK Unidrv , general", "general printer attributes WDK Unidrv", "general printer attributes WDK Unidrv , about general printer attributes"]
---

# General Attributes


## <a href="" id="ddk-general-attributes-gg"></a>


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
<td align="left"><p>EXTERN_GLOBAL: *<em>AttributeName</em>: <em>AttributeValue</em></p></td>
</tr>
</tbody>
</table>

 

For more information about specifying configuration dependencies, see [Conditional Statements](conditional-statements.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20General%20Attributes%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




