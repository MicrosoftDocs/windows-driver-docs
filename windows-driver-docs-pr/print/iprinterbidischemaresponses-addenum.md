---
title: IPrinterBidiSchemaResponses AddEnum method
author: windows-driver-content
description: The AddEnum method adds a new response of type BIDI\_ENUM to the collection.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: B172DF90-63F8-4064-8781-EB0E8D799C1A
keywords: ["AddEnum method Print Devices", "AddEnum method Print Devices , IPrinterBidiSchemaResponses interface", "IPrinterBidiSchemaResponses interface Print Devices , AddEnum method"]
topic_type:
- apiref
api_name:
- IPrinterBidiSchemaResponses.AddEnum
api_type:
- COM
ms.localizationpriority: medium
---

# IPrinterBidiSchemaResponses::AddEnum method


The AddEnum method adds a new response of type BIDI\_ENUM to the collection.

Syntax
------

```ManagedCPlusPlus
HRESULT AddEnum(
  [in] BSTR bstrSchema,
  [in] BSTR bstrValue
);
```

Parameters
----------

*bstrSchema* \[in\]  
The schema.

*bstrValue* \[in\]  
The enum value.

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

 

 




