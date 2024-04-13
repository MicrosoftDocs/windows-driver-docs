---
title: "!gpiokd.pinisrvec"
description: "The !gpiokd.pinisrvec extension displays Interrupt Service Routine (ISR) vector information for a specified pin."
keywords: ["!gpiokd.pinisrvec Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- gpiokd.pinisrvec
api_type:
- NA
---

# !gpiokd.pinisrvec

The **!gpiokd.pinisrvec** extension displays Interrupt Service Routine (ISR) vector information for a specified pin.

```dbgcmd
!gpiokd.bankinfo PinAddress
```

## Parameters


<span id="_______PinAddress______"></span><span id="_______pinaddress______"></span><span id="_______PINADDRESS______"></span> *PinAddress*   
Address of the [\_GPIO\_PIN\_INFORMATION\_ENTRY](gpio-extensions.md#data-structures-used-by-the-gpio-commands) data structure that represents the pin.

## DLL

Gpiokd.dll

## See also

[GPIO Extensions](gpio-extensions.md)
