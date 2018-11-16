---
title: IPrinterBidiSchemaResponses AddBool method
description: The AddBool method adds a new response of type BIDI\_BOOL to the collection.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 8D1C9198-DE72-4348-84EE-C3B875D14E6A
keywords: ["AddBool method Print Devices", "AddBool method Print Devices , IPrinterBidiSchemaResponses interface", "IPrinterBidiSchemaResponses interface Print Devices , AddBool method"]
topic_type:
- apiref
api_name:
- IPrinterBidiSchemaResponses.AddBool
api_type:
- COM
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# IPrinterBidiSchemaResponses::AddBool method

The AddBool method adds a new response of type BIDI\_BOOL to the collection.

Syntax
------

```cpp
HRESULT  AddBool(
  [in] BSTR bstrSchema,
  [in] BOOL bValue
);
```

Parameters
----------

*bstrSchema* \[in\]  
The schema.

*bValue* \[in\]  
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
