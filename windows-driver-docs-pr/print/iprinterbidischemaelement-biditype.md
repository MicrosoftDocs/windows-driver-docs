---
title: IPrinterBidiSchemaElement BidiType method
description: The BidiType method returns the Bidi schema element type.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
keywords: ["BidiType method Print Devices", "BidiType method Print Devices , IPrinterBidiSchemaElement interface", "IPrinterBidiSchemaElement interface Print Devices , BidiType method"]
topic_type:
- apiref
ms.topic: reference
api_name:
- IPrinterBidiSchemaElement.BidiType
api_type:
- COM
ms.date: 06/26/2023
---

# IPrinterBidiSchemaElement::BidiType method

The BidiType method returns the Bidi schema element type.

## Syntax

```cpp
HRESULT BidiType(
  [out, retval] PrinterBidiSchemaElementType *pType
);
```

## Parameters

*pType* \[out, retval\]  
The returned element type.

## Return value

This method returns an **HRESULT** value.

## Requirements

**Target platform:** Desktop

**Version:** Windows 8 and later

## See also

[**IPrinterBidiSchemaElement**](iprinterbidischemaelement-interface.md)

[**PrinterBidiSchemaElementType**](printerbidischemaelementtype.md)
