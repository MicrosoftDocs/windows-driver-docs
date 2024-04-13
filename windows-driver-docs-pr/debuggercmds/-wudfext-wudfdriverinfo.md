---
title: "!wudfext.wudfdriverinfo"
description: "The !wudfext.wudfdriverinfo extension displays information about a UMDF driver within the current host process."
keywords: ["!wudfext.wudfdriverinfo Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- wudfext.wudfdriverinfo
api_type:
- NA
---

# !wudfext.wudfdriverinfo

The **!wudfext.wudfdriverinfo** extension displays information about a UMDF driver within the current host process.

```dbgcmd
!wudfext.wudfdriverinfo Name
```

## Parameters

<span id="_______Name______"></span><span id="_______name______"></span><span id="_______NAME______"></span> *Name*   
Specifies the name of the UMDF driver to display information about.

## DLL

Wudfext.dll

## Additional Information

For more information, see [User-Mode Driver Framework Debugging](../debugger/user-mode-driver-framework-debugging.md).

## Remarks

The **!wudfext.wudfdriverinfo** extension iterates through each level in each device stack and displays the driver and device information for each entry that matches the driver whose name is specified in the *Name* parameter.

You can use **!wudfext.wudfdriverinfo** to quickly find the device object for your driver.

The following is an example of the **!wudfext.wudfdriverinfo** display:

```dbgcmd
kd> !wudfdriverinfo wudfechodriver 
IWDFDriver: 0xf2db8
  !WDFDEVICE 0xf2f80
    !devstack 0x34e4e0 @ level 0
```
