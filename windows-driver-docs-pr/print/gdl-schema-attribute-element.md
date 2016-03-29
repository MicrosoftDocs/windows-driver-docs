---
title: GDL Schema Attribute Element
description: GDL Schema Attribute Element
ms.assetid: b46c0c6c-28af-4121-9182-65dc23b0ce7d
keywords: ["GDL WDK , elements", "GDL WDK , schemas", "attribute element WDK GDL", "GDL_ATTRIBUTE WDK GDL", "GDL_UntypedAtt WDK GDL", "untyped attribute WDK GDL", "snapshots WDK GDL , structure"]
---

# GDL Schema Attribute Element


The data type of all &lt;GDL\_ATTRIBUTE&gt; elements is specified on a per-instance basis by using **xsi:type**. Attributes without a specific data type definition are designated instances of the generic attribute element (&lt;GDL\_UntypedAtt&gt;), which is defined in the GDL-produced schema as follows:

```
    <complexType name="GDL_UntypedAtt"  mixed="true">
        <sequence>
            <any processContents="lax" minOccurs="0" maxOccurs="unbounded"/>
        </sequence>
        <attribute name="Name" type="string" use="required"/>
        <attribute name="Personality" type="string" use="optional"/>
    </complexType>
```

This generic data type is used when the content of the attribute is not described by a more specific data type. The generic data type does not restrict the element content that can appear. The actual element content is determined by the GDL data type templates.

&lt;GDL\_UntypedAtt&gt; has two attributes: **Name** and **Personality**. **Name** is required and holds the GDL attribute's keyword name. **Personality** is optional and specifies the personality tag if the attribute is defined as a \*DataType: MULTIPLE\_PERSONALITY.

If the GDL data type of the value is specifically defined in the XSD schema, the definition's data type is referenced by the **xsi:type** attribute. The XML\_TYPE, ENUMERATOR, and XSD\_DEFINED data types create new data types in the XSD schema.

GDL compound data types are represented by the generic data type. Instances of compound data types contain child elements that might contain other child elements or character content that represents a simple XML data type. The names of the child elements are defined by the **\*ElementTags** directive of the DATATYPE template.

Values of GDL attributes that have no defined data type or are not associated with a template or do not conform to the syntax that is expected for the specified data type are represented by a &lt;CDATA&gt; section in the &lt;GDL\_ATTRIBUTE&gt; element. This section enables clients or other Parser-Filters to process the value as they desire. Such unknown data types will not contain the **xsi:type** attribute. More than one &lt;CDATA&gt; section might be required to represent the value if the value contains the string "\]\]&gt;".

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20GDL%20Schema%20Attribute%20Element%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




