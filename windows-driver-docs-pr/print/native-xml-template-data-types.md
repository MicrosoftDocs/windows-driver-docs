---
title: Native XML Template Data Types
description: Native XML Template Data Types
ms.assetid: a34dec46-de5d-4f12-8863-2fe6b6e5eed4
keywords:
- templates WDK GDL , data types
- data types WDK GDL , primitive
- native data type WDK GDL
- XML_TYPE WDK GDL
- ArrayLabel directive WDK GDL
- XMLDataType directive WDK GDL
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Native XML Template Data Types


The native XML data type is defined as XML\_TYPE.

The syntax is defined by XML. Any data type that is recognized by the XML schema can be defined. The parser filter does not depend on the XML data types so the current parser can support future XML data types without any changes.

\***DataType**: **XML\_TYPE** associates a template with a built-in simple data type for a specific XML schema definition language . The instance data value will be output as the content of an XML element whose **xsi:type** is derived from the \***XMLDataType** construct that is specified by this template.

The following directives are used to define the XML\_TYPE data type:

-   \*XMLDataType (Required). Any XSD schema built-in simple type. The [World Wide Web Consortium (W3C)](http://go.microsoft.com/fwlink/p/?linkid=73527) recommendation for the XML schema recognizes the following built-in simple data types: string, normalizedString, token, byte, unsignedByte, base64Binary, hexBinary, integer, positiveInteger, negativeInteger, nonNegativeInteger, nonPositiveInteger, int, unsignedInt, long, unsignedLong, short, unsignedShort, decimal, float, double, boolean, time, dateTime, duration, date, gMonth, gYear, gYearMonth, gDay, gMonthDay, Name, QName, NCName, anyURI, language, ID, IDREF, IDREFS, ENTITY, ENTITIES, NOTATION, NMTOKEN, and NMTOKENS. Note that the GDL parser is not limited to these data types and is designed to handle future XML data types without any changes.

-   \*ArrayLabel (Optional). If you specify this directive, the parser filter expects the value to be enclosed by parentheses, preceded by the specified array label.

The syntax of the value must adhere to the syntax that the W3C XML standard defines for that particular data type. If the XML syntax conflicts with the basic GDL syntax rules, the value (or just the conflicting portion) must be enclosed within &lt;Begin/EndValue:&gt; constructs. XML values with such incompatible syntaxes, or whose syntax is incompatible with the syntax that is used by compound data types, cannot appear as a member of a compound data type. Also note that the GDL parser will not escape special XML characters like opening or closing brackets (&lt; or &gt;) or an ampersand (&). The creator of the value is responsible for conforming to XML syntax for character data.

For example, consider the following template.

```cpp
*Template:  XML_STRING
{
    *Type:  DATATYPE
    *DataType:   XML_TYPE
    *XMLDataType: "string"
}
```

If you use the preceding template, the following XML schema entry will be created. This entry defines a new data type that is derived from the type that is originally specified by the \***XMLDataType** directive, but this new data type has additional XML attributes that can appear in the snapshot. If you used the original data type, you would receive schema validation errors because the original predefined types do not allow XML attributes to appear.

```cpp
    <complexType name = "GDLW_string">
        <simpleContent>
            <extension base="string">
                <attribute name="Name" type="string" use="optional"/>
                <attribute name="Personality" type="string" use="optional"/>
            </extension>
        </simpleContent>
    </complexType>
```

Consider the following GDL entry.

```cpp
*Text: Hello World
```

Consider the PHRASE template, which declares the GDL attribute \***Text** to have a \***ValueType** that is defined by the XML\_STRING template, as the following code example shows.

```cpp
*Template:  PHRASE
{
    *Name:  "*Text"
    *Type:  ATTRIBUTE
    *ValueType:  XML_STRING
}
```

If the earlier GDL entry is interpreted by using the PHRASE template, the following XML output will occur.

```cpp
<GDL_ATTRIBUTE Name="*Text"  xsi:type="GDLW_string" >Hello World</GDL_ATTRIBUTE>
```

The XML attribute **xsi:type** is used to specify the data type that is held by this attribute element because the schema contains no declaration for this element.

 

 




