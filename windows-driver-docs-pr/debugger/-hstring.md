---
title: hstring
description: The hstring extension displays the fields of an HSTRING. The last item in the display is the string itself.
ms.assetid: 6FB85609-0FB1-457E-A58E-804F69016406
keywords: ["hstring Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- hstring
api_type:
- NA
ms.localizationpriority: medium
---

# !hstring


The **!hstring** extension displays the fields of an **HSTRING**. The last item in the display is the string itself.

```dbgcmd
!hstring Address
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="Address"></span><span id="address"></span><span id="ADDRESS"></span>*Address*  
The address of an **HSTRING**.

Remarks
-------

The **HSTRING** data type supports strings that have embedded NULL characters. However, the **!hstring** extension displays the string only up to the first NULL character. To see the entire string including the embedded NULL characters, use the [**!hstring2**](-hstring2.md) extension.

## <span id="see_also"></span>See also


[Windows Runtime Debugger Commands](windows-runtime-debugger-commands.md)

[**!hstring2**](-hstring2.md)

[**!winrterr**](-winrterr.md)

 

 






