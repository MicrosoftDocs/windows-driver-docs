---
title: PRINTERBIDISCHEMAELEMENTTYPE enumeration
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
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# PRINTERBIDISCHEMAELEMENTTYPE enumeration

Specifies the possible values of data transferred in a bidi operation

Syntax
------

```cpp
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

**PrinterBidiSchemaElementType\_Null**  
No data.

**PrinterBidiSchemaElementType\_Int**  
Data is an integer.

**PrinterBidiSchemaElementType\_Float**  
Data is a floating-point number.

**PrinterBidiSchemaElementType\_Bool**  
Data is a boolean value.

**PrinterBidiSchemaElementType\_String**  
Data is a Unicode character string.

**PrinterBidiSchemaElementType\_Text**  
Data is a non-localizable Unicode string.

**PrinterBidiSchemaElementType\_Enum**  
Data is a Unicode string.

**PrinterBidiSchemaElementType\_Blob**  
Data is binary data.

## See also

[**BidiType**](iprinterbidischemaelement-biditype.md)
