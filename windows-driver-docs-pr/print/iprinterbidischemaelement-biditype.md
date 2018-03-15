---
title: IPrinterBidiSchemaElement BidiType method
author: windows-driver-content
description: The BidiType method returns the Bidi schema element type.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 7E074633-E3AA-45F3-A0B6-621E97E983A8
keywords: ["BidiType method Print Devices", "BidiType method Print Devices , IPrinterBidiSchemaElement interface", "IPrinterBidiSchemaElement interface Print Devices , BidiType method"]
topic_type:
- apiref
api_name:
- IPrinterBidiSchemaElement.BidiType
api_type:
- COM
---

# IPrinterBidiSchemaElement::BidiType method


The BidiType method returns the Bidi schema element type.

Syntax
------

```ManagedCPlusPlus
HRESULT BidiType(
  [out, retval] PrinterBidiSchemaElementType *pType
);
```

Parameters
----------

*pType* \[out, retval\]  
The returned element type.

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


[**IPrinterBidiSchemaElement**](iprinterbidischemaelement-interface.md)

[**PrinterBidiSchemaElementType**](printerbidischemaelementtype.md)

 

 




