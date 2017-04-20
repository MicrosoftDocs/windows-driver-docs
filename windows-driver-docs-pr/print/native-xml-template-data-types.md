---
title: Native XML Template Data Types
author: windows-driver-content
description: Native XML Template Data Types
ms.assetid: a34dec46-de5d-4f12-8863-2fe6b6e5eed4
keywords:
- templates WDK GDL , data types
- data types WDK GDL , primitive
- native data type WDK GDL
- XML_TYPE WDK GDL
- ArrayLabel directive WDK GDL
- XMLDataType directive WDK GDL
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

```
*Template:  XML_STRING
{
    *Type:  DATATYPE
    *DataType:   XML_TYPE
    *XMLDataType: "string"
}
```

If you use the preceding template, the following XML schema entry will be created. This entry defines a new data type that is derived from the type that is originally specified by the \***XMLDataType** directive, but this new data type has additional XML attributes that can appear in the snapshot. If you used the original data type, you would receive schema validation errors because the original predefined types do not allow XML attributes to appear.

```
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

```
*Text: Hello World
```

Consider the PHRASE template, which declares the GDL attribute \***Text** to have a \***ValueType** that is defined by the XML\_STRING template, as the following code example shows.

```
*Template:  PHRASE
{
    *Name:  "*Text"
    *Type:  ATTRIBUTE
    *ValueType:  XML_STRING
}
```

If the earlier GDL entry is interpreted by using the PHRASE template, the following XML output will occur.

```
<GDL_ATTRIBUTE Name="*Text"  xsi:type="GDLW_string" >Hello World</GDL_ATTRIBUTE>
```

The XML attribute **xsi:type** is used to specify the data type that is held by this attribute element because the schema contains no declaration for this element.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Native%20XML%20Template%20Data%20Types%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


