---
title: IPrinterBidiSchemaElement Name method
description: The Name method returns the Bidi schema element name.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
keywords: ["Name method Print Devices", "Name method Print Devices , IPrinterBidiSchemaElement interface", "IPrinterBidiSchemaElement interface Print Devices , Name method"]
topic_type:
- apiref
ms.topic: reference
api_name:
- IPrinterBidiSchemaElement.Name
api_type:
- COM
ms.date: 06/26/2023
---

# IPrinterBidiSchemaElement::Name method

The Name method returns the Bidi schema element name.

## Syntax

```cpp
HRESULT Name(
  [out, retval] BSTR *pbstrSchema
);
```

## Parameters

*pbstrSchema* \[out, retval\]  
The returned element name.

## Return value

This method returns an **HRESULT** value.

## Requirements

**Target platform:** Desktop

**Version:** Windows 8 and later

## See also

[**IPrinterBidiSchemaElement**](iprinterbidischemaelement-interface.md)
