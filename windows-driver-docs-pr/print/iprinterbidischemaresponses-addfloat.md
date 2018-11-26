---
title: IPrinterBidiSchemaResponses AddFloat method
description: The AddFloat method adds a new response of type BIDI\_FLOAT to the collection.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 99A66884-3528-43C3-AC56-CE0AA64AB328
keywords: ["AddFloat method Print Devices", "AddFloat method Print Devices , IPrinterBidiSchemaResponses interface", "IPrinterBidiSchemaResponses interface Print Devices , AddFloat method"]
topic_type:
- apiref
api_name:
- IPrinterBidiSchemaResponses.AddFloat
api_type:
- COM
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# IPrinterBidiSchemaResponses::AddFloat method

The AddFloat method adds a new response of type BIDI\_FLOAT to the collection.

Syntax
------

```cpp
HRESULT AddFloat(
  [in] BSTR    bstrSchema,
  [in] FLOAT  fValue 
);
```

Parameters
----------

 *bstrSchema* \[in\]  
The schema.

 *fValue* \[in\]  
The new floating point value.

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
