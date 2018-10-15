---
title: PRINTERBIDISCHEMAELEMENTTYPE enumeration
author: windows-driver-content
description: Specifies the possible values of data transferred in a bidi operation.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 18F2325D-DA22-4D73-8560-62FDEF1E04A8
keywords: ["PRINTERBIDISCHEMAELEMENTTYPE enumeration Print Devices"]
topic_type:
- apiref
api_name:
- PRINTERBIDISCHEMAELEMENTTYPE
api_type:
- NA
ms.localizationpriority: medium
---

# PRINTERBIDISCHEMAELEMENTTYPE enumeration


Specifies the possible values of data transferred in a bidi operation

Syntax
------

```ManagedCPlusPlus
typedef enum _PRINTERBIDISCHEMAELEMENTTYPE { 
  PrinterBidiSchemaElementType_Null    = 0,
  PrinterBidiSchemaElementType_Int     = 1,
  PrinterBidiSchemaElementType_Float   = 2,
  PrinterBidiSchemaElementType_Bool    = 3,
  PrinterBidiSchemaElementType_String  = 4,
  PrinterBidiSchemaElementType_Text    = 5,
  PrinterBidiSchemaElementType_Enum    = 6,
  PrinterBidiSchemaElementType_Blob    = 7
} PRINTERBIDISCHEMAELEMENTTYPE;
```

Constants
---------

<span id="PrinterBidiSchemaElementType_Null"></span><span id="printerbidischemaelementtype_null"></span><span id="PRINTERBIDISCHEMAELEMENTTYPE_NULL"></span>**PrinterBidiSchemaElementType\_Null**  
No data.

<span id="PrinterBidiSchemaElementType_Int"></span><span id="printerbidischemaelementtype_int"></span><span id="PRINTERBIDISCHEMAELEMENTTYPE_INT"></span>**PrinterBidiSchemaElementType\_Int**  
Data is an integer.

<span id="PrinterBidiSchemaElementType_Float"></span><span id="printerbidischemaelementtype_float"></span><span id="PRINTERBIDISCHEMAELEMENTTYPE_FLOAT"></span>**PrinterBidiSchemaElementType\_Float**  
Data is a floating-point number.

<span id="PrinterBidiSchemaElementType_Bool"></span><span id="printerbidischemaelementtype_bool"></span><span id="PRINTERBIDISCHEMAELEMENTTYPE_BOOL"></span>**PrinterBidiSchemaElementType\_Bool**  
Data is a boolean value.

<span id="PrinterBidiSchemaElementType_String"></span><span id="printerbidischemaelementtype_string"></span><span id="PRINTERBIDISCHEMAELEMENTTYPE_STRING"></span>**PrinterBidiSchemaElementType\_String**  
Data is a Unicode character string.

<span id="PrinterBidiSchemaElementType_Text"></span><span id="printerbidischemaelementtype_text"></span><span id="PRINTERBIDISCHEMAELEMENTTYPE_TEXT"></span>**PrinterBidiSchemaElementType\_Text**  
Data is a non-localizable Unicode string.

<span id="PrinterBidiSchemaElementType_Enum"></span><span id="printerbidischemaelementtype_enum"></span><span id="PRINTERBIDISCHEMAELEMENTTYPE_ENUM"></span>**PrinterBidiSchemaElementType\_Enum**  
Data is a Unicode string.

<span id="PrinterBidiSchemaElementType_Blob"></span><span id="printerbidischemaelementtype_blob"></span><span id="PRINTERBIDISCHEMAELEMENTTYPE_BLOB"></span>**PrinterBidiSchemaElementType\_Blob**  
Data is binary data.

## See also


[**BidiType**](iprinterbidischemaelement-biditype.md)

 

 




