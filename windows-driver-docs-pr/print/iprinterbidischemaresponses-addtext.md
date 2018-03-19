---
title: IPrinterBidiSchemaResponses AddText method
author: windows-driver-content
description: The AddText method adds a new response of type BIDI\_TEXT to the collection.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 2421D77A-E0B2-4114-A27E-59E0D9A88E7C
keywords: ["AddText method Print Devices", "AddText method Print Devices , IPrinterBidiSchemaResponses interface", "IPrinterBidiSchemaResponses interface Print Devices , AddText method"]
topic_type:
- apiref
api_name:
- IPrinterBidiSchemaResponses.AddText
api_type:
- COM
---

# IPrinterBidiSchemaResponses::AddText method


The AddText method adds a new response of type BIDI\_TEXT to the collection.

Syntax
------

```ManagedCPlusPlus
HRESULT AddText(
  [in] BSTR bstrSchema,
  [in] BSTR bstrValue
);
```

Parameters
----------

*bstrSchema* \[in\]  
The schema.

*bstrValue* \[in\]  
The text.

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
<td><p>Windows 8</p></td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**IPrinterBidiSchemaResponses**](iprinterbidischemaresponses.md)

 

 




