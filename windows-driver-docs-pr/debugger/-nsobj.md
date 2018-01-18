---
title: nsobj
description: The nsobj extension displays an ACPI namespace object.
ms.assetid: 348aeb42-41c6-42de-bb43-b075f55076c4
keywords: ["nsobj Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- nsobj
api_type:
- NA
---

# !nsobj


The **!nsobj** extension displays an ACPI namespace object.

Syntax

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!nsobj%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




