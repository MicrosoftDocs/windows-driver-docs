---
title: IPrinterBidiSchemaResponses AddInt32 method
description: The AddInt32 method adds a new response of type BIDI_INT to the collection.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
keywords: ["AddInt32 method Print Devices", "AddInt32 method Print Devices , IPrinterBidiSchemaResponses interface", "IPrinterBidiSchemaResponses interface Print Devices , AddInt32 method"]
topic_type:
- apiref
ms.topic: reference
api_name:
- IPrinterBidiSchemaResponses.AddInt32
api_type:
- COM
ms.date: 06/26/2023
---

# IPrinterBidiSchemaResponses::AddInt32 method

The AddInt32 method adds a new response of type BIDI_INT to the collection.

## Syntax

```cpp
HRESULT  AddInt32(
  [in] BSTR bstrSchema,
  [in] LONG lValue
);
```

## Parameters

*bstrSchema* \[in\]  
The schema.

*lValue* \[in\]  
The new value.

## Return value

This method returns an **HRESULT** value.

## Requirements

**Target platform:** Desktop

**Version:** Windows 8 and later

## See also

[**IPrinterBidiSchemaResponses**](iprinterbidischemaresponses.md)
