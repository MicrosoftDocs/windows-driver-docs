---
title: IPrinterBidiSchemaResponses AddString method
description: The AddString method adds a new response of type BIDI\_STRING to the collection.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: ACBE70E7-5A2B-4472-B1A3-40722D849119
keywords: ["AddString method Print Devices", "AddString method Print Devices , IPrinterBidiSchemaResponses interface", "IPrinterBidiSchemaResponses interface Print Devices , AddString method"]
topic_type:
- apiref
api_name:
- IPrinterBidiSchemaResponses.AddString
api_type:
- COM
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# IPrinterBidiSchemaResponses::AddString method

The AddString method adds a new response of type BIDI\_STRING to the collection.

Syntax
------

```cpp
HRESULT AddString(
  [in] BSTR bstrSchema,
  [in] BSTR bstrValue
);
```

Parameters
----------

*bstrSchema* \[in\]  
The schema.

*bstrValue* \[in\]  
The string response.

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
