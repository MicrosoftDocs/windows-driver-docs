---
title: Defining Data Types by Using Templates
description: Defining Data Types by Using Templates
ms.assetid: 9768f0da-b6cb-4f92-9ab4-2c95fedcb44c
keywords:
- templates WDK GDL , data types
- data types WDK GDL , defining data types by using templates
- defining data types WDK GDL
- data type template WDK GDL
ms.date: 04/20/2017
ms.localizationpriority: medium
---

#  Defining Data Types by Using Templates


All data types, both primitive and compound types, must be defined by using a template. After a data type is defined, any attribute template can declare its value to be of a specific data type by using the **\*ValueType** directive. The value of this directive is the name of a data type template.

When the parser filter encounters a GDL data entry that is an instance of an attribute, it will attempt to parse the value portion of that entry in accordance with the syntax rules that are defined for that data type. If successful, the parser filter will decompose the data type into its primitive XML equivalent data types and output those values in the appropriate XML. The generated XML that represents a compound data type retains the logical structure of the original data type definition. The child elements of a compound data type are given names that are defined by tags that are defined in the data type template. This naming enables a human reader or software client of the XML snapshot to easily locate and identify each value in a compound data type.

A template is designated as a *data type template* (one that defines a data type) by setting the **\*Type: DATATYPE** directive. The directives that are recognized within a data type template are:

**\*ValueType:** *\[Datatype Template Name\]*. This directive declares the value of an attribute to be of a particular data type. The **\*ValueType** directive can appear only within attribute templates. (Attribute templates are templates with the **\*Type: ATTRIBUTE** directive).

**\*DataType:** *symbol*. This directive has one of the following values: PASSTHROUGH, XML\_TYPE, XSD\_DEFINED, ENUMERATOR, FILTER\_TYPE, ARRAY, COMPOSITE, or MULTIPLE\_PERSONALITY.

**\*ElementType:** *list*. This directive defines a list of TEMPLATE data type names.

**\*RequiredDelimiter:** *delimiter*. This directive defines a delimiter with a quoted string.

**\*OptionalDelimiter:** *delimiter*. This directive defines an optional delimiter with a quoted string.

**\*ArrayLabel:** *symbol*. This directive defines an array label with a quoted string.

**\*ElementTags:** *list*. This directive defines a list of symbols to be used for element tags.

**\*EnumeratorList:** *list*. This directive defines a list of symbols to be used for an enumerator list.

**\*XSDTypeDefinition:** *symbol*. This directive defines an arbitrary value, enclosed by &lt;Begin/EndValue&gt; elements, to be used for an XSD type definition.

**\*ComplexType?:** *boolean*. This directive defines whether a type is complex or not. If the value is **TRUE**, the type is complex; otherwise, the type is simple.

**\*ArraySize:** *integer*. This directive defines the range of an array. You can use up to two integers to specify an array range.

**\*XMLDataType:** *string*. This directive defines an XML data type with a quoted string.

**FilterTypeName:** *string*. This directive defines a filter type name by using a quoted string.

**\*MaxValue:** *integer*. This directive defines the maximum size of a value by using a GDL integer.

**\*MinLength:** *integer*. This directive defines the minimum length of a value by using a non-negative GDL integer.

**\*MaxLength:** integer. This directive defines the maximum length of a value by using a non-negative GDL integer.

**Note**   Not all directives are recognized within all data type templates.

 

In general, if no template can be bound to the GDL attribute entry, the value of that attribute will be emitted in the snapshot without any change within a CDATA section. The CDATA shall reside as element content (that is, the child element) of the ATTRIBUTE element.

For example, assume that the parser cannot find a template that describes the following GDL attribute entry.

```cpp
*ModelName: "OEMName LaserJet "
```

Then, the entry will appear in the snapshot as follows.

```cpp
    <GDL_ATTRIBUTE Name="*ModelName" 
        <![CDATA["OEMName LaserJet "]]></GDL_ATTRIBUTE>
```

 

 




