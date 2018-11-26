---
title: IPrinterBidiSchemaResponses AddBlob method
description: The AddBlob method adds a new response of type BIDI\_BLOB to the collection.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 9CB33F44-5DB8-4504-AD88-AEBE99C1E527
keywords: ["AddBlob method Print Devices", "AddBlob method Print Devices , IPrinterBidiSchemaResponses interface", "IPrinterBidiSchemaResponses interface Print Devices , AddBlob method"]
topic_type:
- apiref
api_name:
- IPrinterBidiSchemaResponses.AddBlob
api_type:
- COM
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# IPrinterBidiSchemaResponses::AddBlob method

The AddBlob method adds a new response of type BIDI\_BLOB to the collection.

Syntax
------

```cpp
HRESULT AddBlob(
  [in] BSTR      bstrSchema,
  [in] IDispatch *pArray
);
```

Parameters
----------

*bstrSchema* \[in\]  
The schema.

*pArray* \[in\]  
The array.

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
