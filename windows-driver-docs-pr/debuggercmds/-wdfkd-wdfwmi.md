---
title: "!wdfkd.wdfwmi"
description: "The !wdfkd.wdfwmi extension displays the Microsoft Windows Management Instrumentation (WMI) information for a specified framework device object. "
keywords: ["!wdfkd.wdfwmi Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- wdfkd.wdfwmi
api_type:
- NA
---

# !wdfkd.wdfwmi

The **!wdfkd.wdfwmi** extension displays the Microsoft Windows Management Instrumentation (WMI) information for a specified framework device object. This information includes all WMI provider objects and their associated WMI instance objects.

```dbgcmd
!wdfkd.wdfwmi Handle
```

## Parameters

<span id="_______Handle______"></span><span id="_______handle______"></span><span id="_______HANDLE______"></span> *Handle*   
A handle to a framework device object.

## DLL

Wdfkd.dll

### Frameworks

KMDF 1

## Additional Information

For more information, see [Kernel-Mode Driver Framework Debugging](../debugger/kernel-mode-driver-framework-debugging.md).

## Remarks

The output of the **!wdfkd.wdfwmi** extension includes information about the WMI registration, provider, and instances.
