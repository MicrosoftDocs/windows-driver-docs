---
title: IPrinterBidiSchemaResponses AddRequeryKey method
description: The AddRequeryKey method adds a new QueryKey to re-query upon return from the getSchemas call.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: D2C418C4-3C1B-4CEA-9F39-036C4DB2A483
keywords: ["AddRequeryKey method Print Devices", "AddRequeryKey method Print Devices , IPrinterBidiSchemaResponses interface", "IPrinterBidiSchemaResponses interface Print Devices , AddRequeryKey method"]
topic_type:
- apiref
api_name:
- IPrinterBidiSchemaResponses.AddRequeryKey
api_type:
- COM
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# IPrinterBidiSchemaResponses::AddRequeryKey method

The AddRequeryKey method adds a new QueryKey to re-query upon return from the getSchemas call.

Syntax
------

```cpp
HRESULT AddRequeryKey(
  [in] BSTR   bstrQueryKey
);
```

Parameters
----------

 *bstrQueryKey* \[in\]  
The new QueryKey.

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
