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

## <span id="see_also"></span>See also


[**BidiType**](iprinterbidischemaelement-biditype.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20PRINTERBIDISCHEMAELEMENTTYPE%20enumeration%20%20RELEASE:%20%281/8/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





