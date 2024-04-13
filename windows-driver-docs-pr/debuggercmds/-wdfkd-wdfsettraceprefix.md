---
title: "!wdfkd.wdfsettraceprefix"
description: "The !wdfkd.wdfsettraceprefix extension sets the trace prefix format string."
keywords: ["!wdfkd.wdfsettraceprefix Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- wdfkd.wdfsettraceprefix
api_type:
- NA
---

# !wdfkd.wdfsettraceprefix

The **!wdfkd.wdfsettraceprefix** extension sets the trace prefix format string.

```dbgcmd
!wdfkd.wdfsettraceprefix String
```

## Parameters

<span id="_______String______"></span><span id="_______string______"></span><span id="_______STRING______"></span> *String*   
A trace prefix string.

## DLL

Wdfkd.dll

### Frameworks

KMDF 1, UMDF 2

## Additional Information

For more information, see [Kernel-Mode Driver Framework Debugging](../debugger/kernel-mode-driver-framework-debugging.md).

## Remarks

The trace prefix string is prepended to each trace message in the Kernel-Mode Driver Framework (KMDF) error log. The TRACE\_FORMAT\_PREFIX environment variable also controls the trace prefix string.

The format of the trace prefix string is defined by the Microsoft Windows tracing tools. For more information about the format of this string and how to customize it, see the "Trace Message Prefix" topic in the Driver Development Tools section of the Windows Driver Kit (WDK).

