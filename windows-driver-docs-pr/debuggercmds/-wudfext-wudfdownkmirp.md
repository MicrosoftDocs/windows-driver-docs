---
title: "!wudfext.wudfdownkmirp"
description: "The !wudfext.downkmmirp extension displays the kernel-mode I/O request packet (IRP) that corresponds to the specified user-mode I/O request packet (UM IRP)."
keywords: ["!wudfext.wudfdownkmirp Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- wudfext.wudfdownkmirp
api_type:
- NA
---

# !wudfext.wudfdownkmirp

The **!wudfext.downkmmirp** extension displays the kernel-mode I/O request packet (IRP) that corresponds to the specified user-mode I/O request packet (UM IRP).

```dbgcmd
!wudfext.wudfdownkmirp Address
```

## Parameters

<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the address of the UM IRP whose corresponding kernel-mode IRP is to be displayed.

## DLL

Wudfext.dll

## Additional Information

For more information, see [User-Mode Driver Framework Debugging](../debugger/user-mode-driver-framework-debugging.md).

## Remarks

You can use the [**!wudfext.umirps**](-wudfext-umirps.md) extension command to display a list of all outstanding UM IRPs in the host process.
