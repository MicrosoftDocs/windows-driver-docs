---
title: "!gpiokd.pininfo"
description: "The !gpiokd.pininfo extension displays information about a specified GPIO pin."
keywords: ["!gpiokd.pininfo Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- gpiokd.pininfo
api_type:
- NA
---

# !gpiokd.pininfo

The **!gpiokd.pininfo** extension displays information about a specified GPIO pin.

```dbgcmd
!gpiokd.pininfo PinAddress
```

## Parameters

<span id="_______PinAddress______"></span><span id="_______pinaddress______"></span><span id="_______PINADDRESS______"></span> *PinAddress*   
Address of the [\_GPIO\_PIN\_INFORMATION\_ENTRY](gpio-extensions.md#data-structures-used-by-the-gpio-commands) data structure that represents the pin.

## DLL

Gpiokd.dll

## See also

[GPIO Extensions](gpio-extensions.md)
