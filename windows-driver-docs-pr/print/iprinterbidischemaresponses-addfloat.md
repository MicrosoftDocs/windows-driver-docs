---
title: IPrinterBidiSchemaResponses AddFloat method
description: The AddFloat method adds a new response of type BIDI_FLOAT to the collection.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
keywords: ["AddFloat method Print Devices", "AddFloat method Print Devices , IPrinterBidiSchemaResponses interface", "IPrinterBidiSchemaResponses interface Print Devices , AddFloat method"]
topic_type:
- apiref
ms.topic: reference
api_name:
- IPrinterBidiSchemaResponses.AddFloat
api_type:
- COM
ms.date: 06/26/2023
---

# IPrinterBidiSchemaResponses::AddFloat method

The AddFloat method adds a new response of type BIDI_FLOAT to the collection.

## Syntax

```cpp
HRESULT AddFloat(
  [in] BSTR    bstrSchema,
  [in] FLOAT  fValue 
);
```

## Parameters

 *bstrSchema* \[in\]  
The schema.

 *fValue* \[in\]  
The new floating point value.

## Return value

This method returns an **HRESULT** value.

## Requirements

**Target platform:** Desktop

**Version:** Windows 8 and later

## See also

[**IPrinterBidiSchemaResponses**](iprinterbidischemaresponses.md)
