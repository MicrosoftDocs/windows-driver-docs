---
title: GDL Schema Attribute Element
description: GDL Schema Attribute Element
ms.assetid: b46c0c6c-28af-4121-9182-65dc23b0ce7d
keywords:
- GDL WDK , elements
- GDL WDK , schemas
- attribute element WDK GDL
- GDL_ATTRIBUTE WDK GDL
- GDL_UntypedAtt WDK GDL
- untyped attribute WDK GDL
- snapshots WDK GDL , structure
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GDL Schema Attribute Element


The data type of all &lt;GDL\_ATTRIBUTE&gt; elements is specified on a per-instance basis by using **xsi:type**. Attributes without a specific data type definition are designated instances of the generic attribute element (&lt;GDL\_UntypedAtt&gt;), which is defined in the GDL-produced schema as follows:

```cpp
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

 

 




