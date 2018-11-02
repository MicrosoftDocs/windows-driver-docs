---
title: Parameter Types in Table Data Sources
description: Parameter Types in Table Data Sources
ms.assetid: 034F171E-716F-4795-9B07-46A109052227
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Parameter Types in Table Data Sources


The following table gives a summary of various parameter types available in table based DataSource and which type string can be used to make your DataSource file compatible in native, managed and script tests.

Native
Managed
Script
ParameterType
LanguageType
ParameterType
LanguageType
ParameterType
LanguageType
"String"
WEX::Common::String
"String"
string
"String" or "BSTR"
VT\_BSTR
"int"
int
"Int32" or "int"
int
"int"
VT\_INT
"unsigned int"
unsigned int
"uint" or "uint32"
uint
"unsigned int" or "uint"
VT\_UINT
"bool"
bool
"bool" or "boolean"
bool
"bool"
VT\_BOOL
"double"
double
"double" or "decimal"
decimal
"double"
VT\_R8
"\_\_int64"
\_\_int64
"\_\_int64" or "int64"
int64
"\_\_int64"
VT\_I8
"unsigned \_\_int64"
unsigned \_\_int64
"unsigned \_\_int64" or "uint64"
uint64
"unsigned \_\_int64"
VT\_UI8
"DWORD"
DWORD
"DWORD"
uint
"size\_t"
size\_t
"NoThrowString"
WEX::Common::NoThrowString
"XML"
WEX::Common::String
"XML"
string
"XML"
VT\_BSTR
 

NOTE: The "String", "int", "bool", "double", "\_\_int64", "unsigned \_\_int64", and "XML" types can be used in all, managed, native or script tests.

By default, if the type is not specified, the type is assumed to be "String". See first row above.

To specify array type in conjuction with any types specified above, just append "\[\]" to the end of the type.

 

 





