---
title: nsobj
description: The nsobj extension displays an ACPI namespace object.
ms.assetid: 348aeb42-41c6-42de-bb43-b075f55076c4
keywords: ["nsobj Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- nsobj
api_type:
- NA
ms.localizationpriority: medium
---

# !nsobj


The **!nsobj** extension displays an ACPI namespace object.

Syntax

```dbgcmd
!nsobj [Address]
```

## <span id="ddk__nsobj_dbg"></span><span id="DDK__NSOBJ_DBG"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the address of the namespace object. If this is omitted, the root of the namespace tree is used.

### <span id="DLL"></span><span id="dll"></span>DLL

Kdexts.dll

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information, see [ACPI Debugging](acpi-debugging.md).

Remarks
-------

This extension is equivalent to [**!amli dns**](-amli-dns.md).

 

 





