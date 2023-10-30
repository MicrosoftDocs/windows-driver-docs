---
title: IPrinterBidiSchemaResponses AddRequeryKey method
description: The AddRequeryKey method adds a new QueryKey to re-query upon return from the getSchemas call.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
keywords: ["AddRequeryKey method Print Devices", "AddRequeryKey method Print Devices , IPrinterBidiSchemaResponses interface", "IPrinterBidiSchemaResponses interface Print Devices , AddRequeryKey method"]
topic_type:
- apiref
ms.topic: reference
api_name:
- IPrinterBidiSchemaResponses.AddRequeryKey
api_type:
- COM
ms.date: 06/26/2023
---

# IPrinterBidiSchemaResponses::AddRequeryKey method

The AddRequeryKey method adds a new QueryKey to re-query upon return from the getSchemas call.

## Syntax

```cpp
HRESULT AddRequeryKey(
  [in] BSTR   bstrQueryKey
);
```

## Parameters

 *bstrQueryKey* \[in\]  
The new QueryKey.

## Return value

This method returns an **HRESULT** value.

## Requirements

**Target platform:** Desktop

**Version:** Windows 8 and later

## See also

[**IPrinterBidiSchemaResponses**](iprinterbidischemaresponses.md)
