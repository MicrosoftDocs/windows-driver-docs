---
title: Parameter Types in Table Data Sources
description: Parameter Types in Table Data Sources
ms.date: 04/20/2017
---

# Parameter Types in Table Data Sources

The following tables are summaries of various parameter types available in table based DataSource and which type string can be used to make your DataSource file compatible in native, managed and script tests.

>[!NOTE]
>The "String", "int", "bool", "double", "\_\_int64", "unsigned \_\_int64", and "XML" types can be used in all, managed, native or script tests.

By default, if the type is not specified, the type is assumed to be "String". See the first row in each table.

To specify array type in conjunction with any types specified above, just append "\[\]" to the end of the type.

## For native tests

|ParameterType|LanguageType|
|----|----|
|"String"|WEX::Common::String|
|"int"|int|
|"unsigned int"|unsigned int|
|"bool"|bool|
|"double"|double|
|"\_\_int64"|\_\_int64|
|"unsigned \_\_int64"|unsigned \_\_int64|
|"DWORD"|DWORD|
|"size\_t"|size\_t|
|"NoThrowString"|WEX::Common::NoThrowString|
|"XML"|WEX::Common::String|

## For managed tests

|ParameterType|LanguageType|
|----|----|
|"String"|string|
|"Int32" or "int"|int|
|"uint" or "uint32"|uint|
|"bool" or "boolean"|bool|
|"double" or "decimal"|decimal|
|"\_\_int64" or "int64"|int64|
|"unsigned \_\_int64" or "uint64"|uint64|
|"DWORD"|uint|
|"XML"|string|

## For script tests

|ParameterType|LanguageType|
|----|----|
|"String" or "BSTR"|VT\_BSTR|
|"int"|VT\_INT|
|"unsigned int" or "uint"|VT\_UINT|
|"bool"|VT\_BOOL|
|"double"|VT\_R8|
|"\_\_int64"|VT\_I8|
|"unsigned \_\_int64"|VT\_UI8|
|"XML"|VT\_BSTR|
