---
title: "!wdfkd.wdfsetdriver"
description: "The !wdfkd.wdfsetdriver extension sets the name of the default Kernel-Mode Driver Framework (KMDF) driver to which debugger extension commands apply."
keywords: ["!wdfkd.wdfsetdriver Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- wdfkd.wdfsetdriver
api_type:
- NA
---

# !wdfkd.wdfsetdriver

The **!wdfkd.wdfsetdriver** extension sets the name of the default Kernel-Mode Driver Framework (KMDF) driver to which debugger extension commands apply.

```dbgcmd
!wdfkd.wdfsetdriver DriverName
```

## Parameters

<span id="_______DriverName______"></span><span id="_______drivername______"></span><span id="_______DRIVERNAME______"></span> *DriverName*   
The name of a driver. *DriverName* must not include the .sys file name extension.

## DLL

Wdfkd.dll

### Frameworks

KMDF 1, UMDF 2

## Additional Information

For more information, see [Kernel-Mode Driver Framework Debugging](../debugger/kernel-mode-driver-framework-debugging.md).

## Remarks

The **!wdfkd.wdfsetdriver** extension sets the default driver name. You can use this name with other **wdfkd** extensions that would otherwise require you to specify a driver name.

To obtain the name of the current default KMDF driver, use the [**!wdfkd.wdfgetdriver**](-wdfkd-wdfgetdriver.md) extension.
