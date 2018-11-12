---
title: wdfkd.wdfsettraceprefix
description: The wdfkd.wdfsettraceprefix extension sets the trace prefix format string.
ms.assetid: dec47b55-4b6a-4ff5-8622-4a377a1903b8
keywords: ["wdfkd.wdfsettraceprefix Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- wdfkd.wdfsettraceprefix
api_type:
- NA
ms.localizationpriority: medium
---

# !wdfkd.wdfsettraceprefix


The **!wdfkd.wdfsettraceprefix** extension sets the trace prefix format string.

```dbgcmd
!wdfkd.wdfsettraceprefix String
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______String______"></span><span id="_______string______"></span><span id="_______STRING______"></span> *String*   
A trace prefix string.

### <span id="DLL"></span><span id="dll"></span>DLL

Wdfkd.dll

### <span id="Frameworks"></span><span id="frameworks"></span><span id="FRAMEWORKS"></span>Frameworks

KMDF 1, UMDF 2

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information, see [Kernel-Mode Driver Framework Debugging](kernel-mode-driver-framework-debugging.md).

Remarks
-------

The trace prefix string is prepended to each trace message in the Kernel-Mode Driver Framework (KMDF) error log. The TRACE\_FORMAT\_PREFIX environment variable also controls the trace prefix string.

The format of the trace prefix string is defined by the Microsoft Windows tracing tools. For more information about the format of this string and how to customize it, see the "Trace Message Prefix" topic in the Driver Development Tools section of the Windows Driver Kit (WDK).

 

 





