---
title: IPrinterBidiSchemaResponses AddInt32 method
description: The AddInt32 method adds a new response of type BIDI\_INT to the collection.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: F937B098-9C13-4337-82A6-C26DAA8B7068
keywords: ["AddInt32 method Print Devices", "AddInt32 method Print Devices , IPrinterBidiSchemaResponses interface", "IPrinterBidiSchemaResponses interface Print Devices , AddInt32 method"]
topic_type:
- apiref
api_name:
- IPrinterBidiSchemaResponses.AddInt32
api_type:
- COM
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# IPrinterBidiSchemaResponses::AddInt32 method

The AddInt32 method adds a new response of type BIDI\_INT to the collection.

Syntax
------

```cpp
HRESULT  AddInt32(
  [in] BSTR bstrSchema,
  [in] LONG lValue
);
```

Parameters
----------

*bstrSchema* \[in\]  
The schema.

*lValue* \[in\]  
The new value.

Return value
------------

This method returns an **HRESULT** value.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Target platform</p></td>
<td>Desktop</td>
</tr>
<tr class="even">
<td><p>Version</p></td>
<td><p>Windows 8 and later</p></td>
</tr>
</tbody>
</table>

## See also

[**IPrinterBidiSchemaResponses**](iprinterbidischemaresponses.md)
