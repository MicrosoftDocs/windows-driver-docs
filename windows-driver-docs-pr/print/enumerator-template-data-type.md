---
title: Enumerator Template Data Type
description: Enumerator Template Data Type
ms.assetid: deb95ca1-05a5-47f4-8e2a-1d1aa1ae2261
keywords:
- templates WDK GDL , data types
- data types WDK GDL , primitive
- ENUMERATOR data type WDK GDL
- ArrayLabel directive WDK GDL
- XMLDataType directive WDK GDL
- EnumeratorList directive WDK GDL
- ElementTags directive WDK GDL
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Enumerator Template Data Type


The ENUMERATOR data type has allowed values that are limited to a set of tokens.

\*DataType: ENUMERATOR directs a template to define an enumeration data type. This data type will be output as an XML schema simpleType declaration that is derived from the **string** type with restrictions to specify each allowed enumerator. The following directives are used to completely define the ENUMERATOR data type:

-   \*XMLDataType (Required). The NCName to assign to the XML data type that will be used to define this enumeration in the generated XML schema. Each enumeration type must have a unique NCName. This name must be unique to all XSD\_DEFINED and ENUMERATOR types. To avoid conflicts with data types that the GDL parser defines, you should avoid NCNames that begin with "GDL\_" and "GDLW\_".

-   \*EnumeratorList (Required). The list of enumerator tokens. Each token must be a valid GDL symbol and must conform to any additional requirements that the XSD schema imposes for the value of the schema component: &lt;enumeration&gt;.

-   \*ArrayLabel (Optional). If this directive is specified, the parser filter expects the value to be enclosed by parentheses, preceded by the specified array label.

The value to be parsed as an ENUMERATOR data type must match one of the tokens that the \*ElementTags directive defines.

Consider the following template.

```cpp
*Template:  COLORS
{
    *Type:  DATATYPE
    *DataType:   ENUMERATOR
    *XMLDataType: "colors"
    *EnumeratorList: (YELLOW, MAGENTA, CYAN, BLACK, RED, GREEN, BLUE)
}
```

The preceding template will cause the parser filter to create the following XML schema entry.

```cpp
    <simpleType name = "colors">
        <restriction base="string">
            <enumeration value="YELLOW"/>
            <enumeration value="MAGENTA"/>
            <enumeration value="CYAN"/>
            <enumeration value="BLACK"/>
            <enumeration value="RED"/>
            <enumeration value="GREEN"/>
            <enumeration value="BLUE"/>
        </restriction>
    </simpleType>
```

The parser filter will also create the corresponding wrapped data type.

```cpp
    <complexType name = "GDLW_colors">
        <simpleContent>
            <extension base="gdl:colors">
                <attribute name="Name" type="string" use="optional"/>
                <attribute name="Personality" type="string" use="optional"/>
            </extension>
        </simpleContent>
    </complexType>
```

Consider the following GDL entry.

```cpp
*Color: GREEN
```

And consider the ACOLOR template, which declares the **\*Color** GDL attribute to have a **\*ValueType** that is defined by the template COLORS, as the following code example shows.

```cpp
*Template:  ACOLOR
{
    *Name:  "*Color"
    *Type:  ATTRIBUTE
    *ValueType:  COLORS
    *Additive: LEAST_TO_MOST_RECENT
}
```

If the earlier GDL entry is interpreted by using the ACOLOR template, the resulting XML output would occur.

```cpp
    <GDL_ATTRIBUTE Name="*Color"  xsi:type="GDLW_colors" >GREEN</GDL_ATTRIBUTE>
```

The XML attribute **xsi:type** defines this instance of the GDL\_ATTRIBUTE element to hold a template-defined value type that represents an enumeration that is defined in the XML default namespace.

 

 




