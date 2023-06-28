---
title: IPrinterBidiSchemaResponses AddString method
description: The AddString method adds a new response of type BIDI_STRING to the collection.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
keywords: ["AddString method Print Devices", "AddString method Print Devices , IPrinterBidiSchemaResponses interface", "IPrinterBidiSchemaResponses interface Print Devices , AddString method"]
topic_type:
- apiref
ms.topic: reference
api_name:
- IPrinterBidiSchemaResponses.AddString
api_type:
- COM
ms.date: 06/26/2023
---

# IPrinterBidiSchemaResponses::AddString method

The AddString method adds a new response of type BIDI_STRING to the collection.

## Syntax

```cpp
HRESULT AddString(
  [in] BSTR bstrSchema,
  [in] BSTR bstrValue
);
```

## Parameters

*bstrSchema* \[in\]  
The schema.

*bstrValue* \[in\]  
The string response.

## Return value

This method returns an **HRESULT** value.

## Requirements

**Target platform:** Desktop

**Version:** Windows 8 and later

## See also

[**IPrinterBidiSchemaResponses**](iprinterbidischemaresponses.md)
