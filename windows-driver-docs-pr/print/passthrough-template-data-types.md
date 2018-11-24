---
title: Passthrough Template Data Types
description: Passthrough Template Data Types
ms.assetid: 9e5e6a12-5847-45fe-bee5-68944cd546d7
keywords:
- templates WDK GDL , data types
- data types WDK GDL , primitive
- PASSTHROUGH data type WDK GDL
- schemas WDK GDL , validating PASSTHROUGH data types
- ArrayLabel directive WDK GDL
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Passthrough Template Data Types


\***DataType**: **PASSTHROUGH** defines a template to represent an unprocessed data type. The characters that comprise the GDL value are inserted as Element Content of the XML element that represents the GDL attribute.

The following directives are recognized within a template that defines the PASSTHROUGH data type:

-   \*ArrayLabel. If this directive is specified, the parser filter expects the value to be enclosed by parentheses and preceded by the specified array label. This directive is optional.

The syntax of the value must adhere to the syntax that is defined for XML element content that can include character data, child elements, and so on. Also note that the GDL parser will not escape special XML characters like an opening or closing bracket (&lt; or &gt;) or an ampersand (&). The creator of the value is responsible for conforming the value to the XML syntax for element content.

If the XML syntax conflicts with the basic GDL syntax rules, the entire value (or just the conflicting portion) must be enclosed within &lt;Begin/EndValue:&gt; constructs. XML values with such incompatible syntaxes, or whose syntax is incompatible with the syntax that is used by compound data types, cannot appear as a member of a compound data type but must appear directly as the value of a GDL attribute.

For example, consider the following example template.

```cpp
*Template:  ELEMENT_CONTENT
{
    *Type:  DATATYPE
    *DataType:   PASSTHROUGH
}
```

With the preceding template, the parser filter does not create an XSD schema data type declaration for PASSTHROUGH data.

Consider the following GDL entry.

```cpp
*InLineXML:  <BeginValue:XML>
 <Cell CellOrdinal="0">
         <Value xsi:type="xsd:double">16890</Value>
         <FmtValue>16,890.00</FmtValue>
         <FormatString>Standard</FormatString>
      </Cell>
<EndValue:XML>
```

If the preceding entry is interpreted by using the earlier example template, the following XML output would occur.

```cpp
<GDL_ATTRIBUTE Name="*InLineXML"  >
  <Cell CellOrdinal="0">
    <Value xsi:type="xsd:double">16890</Value>
    <FmtValue>16,890.00</FmtValue>
    <FormatString>Standard</FormatString>
  </Cell>
</GDL_ATTRIBUTE>
```

If you want to validate the PASSTHROUGH instances by using an XML schema, you should use the [XSD\_DEFINED data type](xsd-template-data-types.md) instead of PASSTHROUGH, because the XSD\_DEFINED data type allows the XSD schema to be explicitly defined in the template and is integrated into the schema output by the parser.

 

 




