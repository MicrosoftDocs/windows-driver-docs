---
title: Filter Template Data Type
description: Filter Template Data Type
ms.assetid: cfbe8f39-9a8d-4e6b-91d8-f25926057e7b
keywords:
- templates WDK GDL , data types
- data types WDK GDL , primitive
- FILTER_TYPE data type WDK GDL
- ArrayLabel directive WDK GDL
- ElementType directive WDK GDL
- FilterTypeName directive WDK GDL
- ElementTags directive WDK GDL
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Filter Template Data Type


The FILTER\_TYPE type is recognized by the parser filter. Examples of this data type include the GPD integer type, GPD string type, and GPD symbol type.

\*DataType: FILTER\_TYPE associates a template with a specific parser filter built-in data type. The syntax of the value is determined by the parser filter. The parser filter will convert this value into one or more native XML data types. The specific XML data type that is produced is hard-coded and you cannot change it. The value will be output as if it were \*DataType: XML\_TYPE.

The following directives are used to completely define the FILTER\_TYPE data type:

-   **\*ElementType** (Required). A list of \*DataType: XML\_TYPE templates that define the XML types that this data type will be converted to and output in the generated XML. The XML type that is required varies with the specific filter type. The XML data types that this directive references must match the XML data types that the parser filter expects.

-   **\*ElementTags** (Optional). If filter type is converted into more than one XML element, this directive specifies the name of each XML element. If this directive is used, the number of tags that are specified must equal the number of XML elements that each conversion produces. Tags are not used if only one XML element is produced.
    **Note**   The **\*ElementTags** directive might be required for some future filter types.

     

-   **\*FilterTypeName** (Required) The particular filter-implemented data type. The default parser filter currently supports the following types:
    -   "HEX\_OR\_INT": GPD 4-byte integer that accepts hex format and wildcard (\*). The result is converted into a decimal number and output as XSD **int** data type. The optional **\*MinValue** and **\*MaxValue** template directives are recognized for this data type. If this type is present, the parser will verify that the supplied value falls within the defined range. One limit can be defined without the other.
    -   "SYMBOLNAME": GPD/GDL symbol token. The token is output as XSD **string** data type. The optional **\*MinLength** and **\*MaxLength** template directives are recognized for this data type. If this type is present, the parser will verify that the supplied token's length falls within the defined range. One limit can be defined without the other.
    -   "COMMAND\_STRING": GPD command-string value. No string interpretation is performed. The raw value is converted to and output as XSD base64Binary data. The value is not output as XSD **string** data type because command strings might contain characters that are not legal for XML strings.
    -   "NORMAL\_STRING": GPD/GDL quoted string value. The result is converted into a pure 8-bit binary string, and the array of words output as XSD **string** data type. The optional **\*MinLength** and **\*MaxLength** template directives are recognized for this data type. If this type is present, the parser will verify that the supplied string's length falls within the defined range. One limit can be defined without the other.
    -   "CODEPAGE\_STRING": GPD/GDL quoted string value. The result is converted into a 16-bit Unicode string by using the codepage that the appropriate **\*CodePage** entry specifies and output as XSD **string** data type. The optional **\*MinLength** and **\*MaxLength** template directives are recognized for this data type. If this type is present, the parser will verify that the supplied string's length falls within the defined range. One limit can be defined without the other. Note that the length of the string is the number of WideChars that are actually produced after codepage translation.
    -   "DEFAULT\_CODEPAGE\_STRING": GPD/GDL quoted string value. The result is converted into a 16-bit Unicode string by using the CP\_ACP codepage and output as XSD **string** data type. The optional **\*MinLength** and **\*MaxLength** template directives are recognized for this data type. If this type is present, the parser will verify that the supplied string's length falls within the defined range. One limit can be defined without the other. Note that the length of the string is the number of Unicode characters that are actually produced after codepage translation.
    -   "UNICODE\_STRING": GPD/GDL quoted string value. The string is assumed to be the binary representation of a set of Unicode characters and is output directly as XSD **string** data type.

        Each Unicode character is represented by a pair of bytes. The bytes are typically represented as a hex substring to make editing easier. For backward compatibility, the GDL parser follows the convention that the GPD parser established, so that the least significant byte in the pair appears to the left of the most significant byte. Unlike the GPD parser, this convention is independent of the processor's byte ordering. The optional **\*MinLength** and **\*MaxLength** template directives are recognized for this data type. If this type is present, the parser will verify that the supplied string's length falls within the defined range. One limit can be defined without the other. Note that the length of the string is the number of Unicode characters that are actually produced.

    -   "BINARY\_STRING": GPD/GDL quoted string value. The string is assumed to represent binary 8-bit data. The result in converted to and output as XSD base64Binary data. Since 'control characters' are not permitted within XML files, they cannot be represented using the XSD 'string' data type. Thus the BINARY\_STRING filter must be used to convert such characters to a form that can be processed by XML. The optional template directives \*MinLength and \*MaxLength are recognized for this data type. If this type is present, the parser will verify that the supplied string's length falls within the defined range. One limit can be defined without the other. Note that the length of the string is the number of bytes that are actually represented by the base64 encoded data.

-   **\*ArrayLabel** (Optional). If this directive is specified, the parser filter expects the value to be enclosed by parentheses, preceded by the specified array label.

The value to be parsed must conform to the syntax that is defined for the specific filter type that the \*FilterTypeName directive specifies. The parser filter will convert and output this value into one or more XML data types, as specified earlier. If the conversion results in more than one XML element, each element will be tagged by using the names that are specified in the \*ElementTags directive.

When emitting the XML snapshot, the parser will automatically represent special characters with the appropriate XML entity if they are present in the values of string filter types. For example, the ampersand character (&) is represented by t& in the snapshot. You do not need to follow XML syntax rules when using parser filter defined data types.

Consider the following template.

```cpp
*Template:  INTEGER
{
    *Type:  DATATYPE
    *DataType:   FILTER_TYPE
    *ElementType:  XSD_INT
    *FilterTypeName: "HEX_OR_INT"
}
```

This template specifies a filter type of "HEX\_OR\_INT". According to the information that is provided for \*FilterTypeName, the filter will convert this data type to the built-in XSD type int. To ensure that the generated XML maintains the intent of the filter, you must name the template that represents the XSD data type int in the **\*ElementType** directive.

In the following example, the XSD\_INT template is named. This template is defined as follows.

```cpp
*Template:  XSD_INT
{
    *Type:  DATATYPE
    *DataType:   XML_TYPE
    *XMLDataType: "int"  
}
```

The XSD\_INT template defines a native XSD type int, which ensures that the intent of the parser filter will be implemented correctly.

\*DataType: FILTER\_TYPE templates do not generate a corresponding schema.

Consider the following GDL entry.

```cpp
*MaxCopies:   0x1ff
```

And consider the following template, MAXCOPIES.

```cpp
*Template:  MAXCOPIES
{
    *Name:  "*MaxCopies"
    *Type:  ATTRIBUTE
    *ValueType:  INTEGER
}
```

If the earlier GDL entry is interpreted by the preceding template, the resulting XML output will be.

```cpp
    <GDL_ATTRIBUTE Name="*MaxCopies"  xsi:type="GDLW_int" >511</GDL_ATTRIBUTE> 
```

Note that the parser filter has converted the GPD-defined hex format into the decimal format that is appropriate for the XSD data type **xsd:int**. Note also that the type that is actually referenced is the wrapped type GDLW\_int.

 

 




