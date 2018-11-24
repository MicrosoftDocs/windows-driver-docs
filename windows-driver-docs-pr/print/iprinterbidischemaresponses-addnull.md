---
title: IPrinterBidiSchemaResponses AddNull method
description: The AddNull method adds a new response of type BIDI\_NULL to the collection.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 36796227-7EE4-43C8-9AD7-51A3929D1CE2
keywords: ["AddNull method Print Devices", "AddNull method Print Devices , IPrinterBidiSchemaResponses interface", "IPrinterBidiSchemaResponses interface Print Devices , AddNull method"]
topic_type:
- apiref
api_name:
- IPrinterBidiSchemaResponses.AddNull
api_type:
- COM
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# IPrinterBidiSchemaResponses::AddNull method

The AddNull method adds a new response of type BIDI\_NULL to the collection.

Syntax
------

```cpp
HRESULT AddNull(
  [in] BSTR bstrSchema
);
```

Parameters
----------

*bstrSchema* \[in\]  
The schema name.

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
