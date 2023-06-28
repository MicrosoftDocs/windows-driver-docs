---
title: IPrinterBidiSchemaResponses AddEnum method
description: The AddEnum method adds a new response of type BIDI_ENUM to the collection.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
keywords: ["AddEnum method Print Devices", "AddEnum method Print Devices , IPrinterBidiSchemaResponses interface", "IPrinterBidiSchemaResponses interface Print Devices , AddEnum method"]
topic_type:
- apiref
ms.topic: reference
api_name:
- IPrinterBidiSchemaResponses.AddEnum
api_type:
- COM
ms.date: 06/26/2023
---

# IPrinterBidiSchemaResponses::AddEnum method

The AddEnum method adds a new response of type BIDI_ENUM to the collection.

## Syntax

```cpp
HRESULT AddEnum(
  [in] BSTR bstrSchema,
  [in] BSTR bstrValue
);
```

## Parameters

*bstrSchema* \[in\]  
The schema.

*bstrValue* \[in\]  
The enum value.

## Return value

This method returns an **HRESULT** value.

## Requirements

**Target platform:** Desktop

**Version:** Windows 8 and later

## See also

[**IPrinterBidiSchemaResponses**](iprinterbidischemaresponses.md)
