---
title: Enumerator Template Data Type
author: windows-driver-content
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
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Enumerator Template Data Type


The ENUMERATOR data type has allowed values that are limited to a set of tokens.

\*DataType: ENUMERATOR directs a template to define an enumeration data type. This data type will be output as an XML schema simpleType declaration that is derived from the **string** type with restrictions to specify each allowed enumerator. The following directives are used to completely define the ENUMERATOR data type:

-   \*XMLDataType (Required). The NCName to assign to the XML data type that will be used to define this enumeration in the generated XML schema. Each enumeration type must have a unique NCName. This name must be unique to all XSD\_DEFINED and ENUMERATOR types. To avoid conflicts with data types that the GDL parser defines, you should avoid NCNames that begin with "GDL\_" and "GDLW\_".

-   \*EnumeratorList (Required). The list of enumerator tokens. Each token must be a valid GDL symbol and must conform to any additional requirements that the XSD schema imposes for the value of the schema component: &lt;enumeration&gt;.

-   \*ArrayLabel (Optional). If this directive is specified, the parser filter expects the value to be enclosed by parentheses, preceded by the specified array label.

The value to be parsed as an ENUMERATOR data type must match one of the tokens that the \*ElementTags directive defines.

Consider the following template.

```
*Template:  COLORS
{
    *Type:  DATATYPE
    *DataType:   ENUMERATOR
    *XMLDataType: "colors"
    *EnumeratorList: (YELLOW, MAGENTA, CYAN, BLACK, RED, GREEN, BLUE)
}
```

The preceding template will cause the parser filter to create the following XML schema entry.

```
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

```
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

```
*Color: GREEN
```

And consider the ACOLOR template, which declares the **\*Color** GDL attribute to have a **\*ValueType** that is defined by the template COLORS, as the following code example shows.

```
*Template:  ACOLOR
{
    *Name:  "*Color"
    *Type:  ATTRIBUTE
    *ValueType:  COLORS
    *Additive: LEAST_TO_MOST_RECENT
}
```

If the earlier GDL entry is interpreted by using the ACOLOR template, the resulting XML output would occur.

```
    <GDL_ATTRIBUTE Name="*Color"  xsi:type="GDLW_colors" >GREEN</GDL_ATTRIBUTE>
```

The XML attribute **xsi:type** defines this instance of the GDL\_ATTRIBUTE element to hold a template-defined value type that represents an enumeration that is defined in the XML default namespace.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Enumerator%20Template%20Data%20Type%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


