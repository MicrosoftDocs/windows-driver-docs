---
title: ndiskd.ndiskdversion
description: The ndiskd.ndiskdversion extension displays information about ndiskd itself.
ms.assetid: 12EB9E0F-7D2F-447B-B678-1E23EFF522FE
keywords: ["ndiskd.ndiskdversion Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- ndiskd.ndiskdversion
api_type:
- NA
ms.localizationpriority: medium
---

# !ndiskd.ndiskdversion


The **!ndiskd.ndiskdversion** extension displays information about !ndiskd itself.

```console
!ndiskd.ndiskdversion 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


This extension has no parameters.

### <span id="DLL"></span><span id="dll"></span>DLL

Ndiskd.dll

Examples
--------

The following example shows output for **!ndiskd.ndiskdversion**.

```console
1: kd> !ndiskd.ndiskdversion
    NDISKD Version     17.01.00 (NDISKD codename "All your WDF are belong to us")
    Build              Release
    Debugger CPU       AMD64
    NDIS symbols       Private             More info
    Hyperlinks (DML)   Enabled
    Unicode            Enabled
    Debug NDISKD       Enabled
```

## <span id="see_also"></span>See also


[Network Driver Design Guide](https://msdn.microsoft.com/windows/hardware/drivers/network/index)

[Windows Vista and Later Networking Reference](https://msdn.microsoft.com/library/windows/hardware/ff571081)

[Debugging the Network Stack](https://go.microsoft.com/fwlink/p/?linkid=845311)

[**NDIS extensions (Ndiskd.dll)**](ndis-extensions--ndiskd-dll-.md)

[**!ndiskd.help**](-ndiskd-help.md)

 

 






