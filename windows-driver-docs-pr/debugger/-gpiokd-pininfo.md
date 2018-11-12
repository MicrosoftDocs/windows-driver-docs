---
title: gpiokd.pininfo
description: The gpiokd.pininfo command displays information about a specified GPIO pin.
ms.assetid: 67A8F87A-E1E4-42AC-B626-66C2CB177A61
keywords: ["gpiokd.pininfo Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- gpiokd.pininfo
api_type:
- NA
ms.localizationpriority: medium
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

 

 






