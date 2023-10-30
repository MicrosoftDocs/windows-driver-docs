---
title: IPrinterBidiSchemaResponses AddText method
description: The AddText method adds a new response of type BIDI_TEXT to the collection.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
keywords: ["AddText method Print Devices", "AddText method Print Devices , IPrinterBidiSchemaResponses interface", "IPrinterBidiSchemaResponses interface Print Devices , AddText method"]
topic_type:
- apiref
ms.topic: reference
api_name:
- IPrinterBidiSchemaResponses.AddText
api_type:
- COM
ms.date: 06/26/2023
---

# IPrinterBidiSchemaResponses::AddText method

The AddText method adds a new response of type BIDI_TEXT to the collection.

## Syntax

```cpp
HRESULT AddText(
  [in] BSTR bstrSchema,
  [in] BSTR bstrValue
);
```

## Parameters

*bstrSchema* \[in\]  
The schema.

*bstrValue* \[in\]  
The text.

## Return value

This method returns an **HRESULT** value.

## Requirements

**Target platform:** Desktop

**Version:** Windows 8 and later

## See also

[**IPrinterBidiSchemaResponses**](iprinterbidischemaresponses.md)
