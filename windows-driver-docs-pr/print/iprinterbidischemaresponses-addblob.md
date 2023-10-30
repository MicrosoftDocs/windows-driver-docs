---
title: IPrinterBidiSchemaResponses AddBlob method
description: The AddBlob method adds a new response of type BIDI_BLOB to the collection.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
keywords: ["AddBlob method Print Devices", "AddBlob method Print Devices , IPrinterBidiSchemaResponses interface", "IPrinterBidiSchemaResponses interface Print Devices , AddBlob method"]
topic_type:
- apiref
ms.topic: reference
api_name:
- IPrinterBidiSchemaResponses.AddBlob
api_type:
- COM
ms.date: 06/26/2023
---

# IPrinterBidiSchemaResponses::AddBlob method

The AddBlob method adds a new response of type BIDI_BLOB to the collection.

## Syntax

```cpp
HRESULT AddBlob(
  [in] BSTR      bstrSchema,
  [in] IDispatch *pArray
);
```

## Parameters

*bstrSchema* \[in\]  
The schema.

*pArray* \[in\]  
The array.

## Return value

This method returns an **HRESULT** value.

## Requirements

**Target platform:** Desktop

**Version:** Windows 8 and later

## See also

[**IPrinterBidiSchemaResponses**](iprinterbidischemaresponses.md)
