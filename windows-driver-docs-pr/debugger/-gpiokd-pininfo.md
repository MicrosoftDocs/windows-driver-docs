---
title: gpiokd.pininfo
description: The gpiokd.pininfo command displays information about a specified GPIO pin.
keywords: ["gpiokd.pininfo Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- gpiokd.pininfo
api_type:
- NA
---

# !gpiokd.pininfo


The **!gpiokd.pininfo** command displays information about a specified GPIO pin.

```dbgcmd
!gpiokd.pininfo PinAddress
```

## <span id="ddk__devobj_dbg"></span><span id="DDK__DEVOBJ_DBG"></span>Parameters


<span id="_______PinAddress______"></span><span id="_______pinaddress______"></span><span id="_______PINADDRESS______"></span> *PinAddress*   
Address of the [\_GPIO\_PIN\_INFORMATION\_ENTRY](gpio-extensions.md#data-structures-used-by-the-gpio-commands) data structure that represents the pin.

## <span id="DLL"></span><span id="dll"></span>DLL


Gpiokd.dll

## <span id="see_also"></span>See also


[GPIO Extensions](gpio-extensions.md)

 

 






