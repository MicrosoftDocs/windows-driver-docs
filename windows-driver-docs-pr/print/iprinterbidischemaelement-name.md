---
title: IPrinterBidiSchemaElement Name method
description: The Name method returns the Bidi schema element name.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 682B3DFE-EE21-4C96-B585-1D63287C33A0
keywords: ["Name method Print Devices", "Name method Print Devices , IPrinterBidiSchemaElement interface", "IPrinterBidiSchemaElement interface Print Devices , Name method"]
topic_type:
- apiref
api_name:
- IPrinterBidiSchemaElement.Name
api_type:
- COM
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# IPrinterBidiSchemaElement::Name method

The Name method returns the Bidi schema element name.

Syntax
------

```cpp
HRESULT Name(
  [out, retval] BSTR *pbstrSchema
);
```

Parameters
----------

*pbstrSchema* \[out, retval\]  
The returned element name.

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

[**IPrinterBidiSchemaElement**](iprinterbidischemaelement-interface.md)
