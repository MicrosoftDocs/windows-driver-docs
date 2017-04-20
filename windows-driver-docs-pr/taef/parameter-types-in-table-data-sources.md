---
title: Parameter Types in Table Data Sources
description: Parameter Types in Table Data Sources
ms.assetid: 034F171E-716F-4795-9B07-46A109052227
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[taef\taef]:%20Parameter%20Types%20in%20Table%20Data%20Sources%20%20RELEASE:%20%289/12/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




