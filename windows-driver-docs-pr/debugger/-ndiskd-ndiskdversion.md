---
title: ndiskd.ndiskdversion
description: The ndiskd.ndiskdversion extension displays information about ndiskd itself.
keywords: ["ndiskd.ndiskdversion Windows Debugging"]
ms.date: 06/11/2020
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

## Parameters

This extension has no parameters.

## DLL

Ndiskd.dll

## Examples

The following example shows output for **!ndiskd.ndiskdversion**.

```console
0: kd> !ndiskd.ndiskdversion
    NDISKD Version     17.08.00 (NDISKD codename "We'll deploy IPv6 real soon now")
    Build              Release
    Debugger CPU       AMD64
    Hyperlinks (DML)   Enabled
    Unicode            Enabled
    Debug NDISKD       Disabled
```

## See also

[Network Driver Design Guide](../network/index.md)

[Windows Vista and Later Networking Reference](/windows-hardware/drivers/ddi/_netvista/)

[Debugging the Network Stack](https://channel9.msdn.com/Shows/Defrag-Tools/Defrag-Tools-175-Debugging-the-Network-Stack)

[**NDIS extensions (Ndiskd.dll)**](ndis-extensions--ndiskd-dll-.md)

[**!ndiskd.help**](-ndiskd-help.md)
