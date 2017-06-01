---
title: wdfkd.wdfsettraceprefix
description: The wdfkd.wdfsettraceprefix extension sets the trace prefix format string.
ms.assetid: dec47b55-4b6a-4ff5-8622-4a377a1903b8
keywords: ["wdfkd.wdfsettraceprefix Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- wdfkd.wdfsettraceprefix
api_type:
- NA
---

# !wdfkd.wdfsettraceprefix


The **!wdfkd.wdfsettraceprefix** extension sets the trace prefix format string.

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!wdfkd.wdfsettraceprefix%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




