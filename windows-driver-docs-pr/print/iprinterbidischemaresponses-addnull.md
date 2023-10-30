---
title: IPrinterBidiSchemaResponses AddNull method
description: The AddNull method adds a new response of type BIDI_NULL to the collection.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
keywords: ["AddNull method Print Devices", "AddNull method Print Devices , IPrinterBidiSchemaResponses interface", "IPrinterBidiSchemaResponses interface Print Devices , AddNull method"]
topic_type:
- apiref
ms.topic: reference
api_name:
- IPrinterBidiSchemaResponses.AddNull
api_type:
- COM
ms.date: 06/26/2023
---

# IPrinterBidiSchemaResponses::AddNull method

The AddNull method adds a new response of type BIDI_NULL to the collection.

## Syntax

```cpp
HRESULT AddNull(
  [in] BSTR bstrSchema
);
```

## Parameters

*bstrSchema* \[in\]  
The schema name.

## Return value

This method returns an **HRESULT** value.

## Requirements

**Target platform:** Desktop

**Version:** Windows 8 and later

## See also

[**IPrinterBidiSchemaResponses**](iprinterbidischemaresponses.md)
