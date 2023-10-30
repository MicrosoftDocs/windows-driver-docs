---
title: IPrinterBidiSchemaResponses AddBool method
description: The AddBool method adds a new response of type BIDI_BOOL to the collection.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
keywords: ["AddBool method Print Devices", "AddBool method Print Devices , IPrinterBidiSchemaResponses interface", "IPrinterBidiSchemaResponses interface Print Devices , AddBool method"]
topic_type:
- apiref
ms.topic: reference
api_name:
- IPrinterBidiSchemaResponses.AddBool
api_type:
- COM
ms.date: 06/26/2023
---

# IPrinterBidiSchemaResponses::AddBool method

The AddBool method adds a new response of type BIDI_BOOL to the collection.

## Syntax

```cpp
HRESULT  AddBool(
  [in] BSTR bstrSchema,
  [in] BOOL bValue
);
```

## Parameters

*bstrSchema* \[in\]  
The schema.

*bValue* \[in\]  
The new value.

## Return value

This method returns an **HRESULT** value.

## Requirements

**Target platform:** Desktop

**Version:** Windows 8 and later

## See also

[**IPrinterBidiSchemaResponses**](iprinterbidischemaresponses.md)
