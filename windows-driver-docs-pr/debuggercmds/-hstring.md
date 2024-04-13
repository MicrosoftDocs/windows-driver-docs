---
title: "!hstring (WinDbg)"
description: "The !hstring extension displays the fields of an HSTRING. The last item in the display is the string itself."
keywords: ["!hstring Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- hstring
api_type:
- NA
---

# !hstring

The **!hstring** extension displays the fields of an **HSTRING**. The last item in the display is the string itself.

```dbgcmd
!hstring Address
```

## Parameters

<span id="Address"></span><span id="address"></span><span id="ADDRESS"></span>*Address*  
The address of an **HSTRING**.

## Remarks

The **HSTRING** data type supports strings that have embedded NULL characters. However, the **!hstring** extension displays the string only up to the first NULL character. To see the entire string including the embedded NULL characters, use the [**!hstring2**](-hstring2.md) extension.

## See also

[Windows Runtime Debugger Commands](../debugger/windows-runtime-debugger-commands.md)

[**!hstring2**](-hstring2.md)

[**!winrterr**](-winrterr.md)
