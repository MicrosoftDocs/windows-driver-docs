---
title: Control GUID
description: Control GUID
ms.assetid: a85a5e1a-c4c1-40d4-a0ef-d8e552590f03
keywords:
- control GUIDs WDK
- GUIDs WDK software tracing
- identifiers WDK software tracing
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Control GUID


## <span id="ddk_control_guid_tools"></span><span id="DDK_CONTROL_GUID_TOOLS"></span>


Each [trace provider](trace-provider.md) defines a *control GUID* that uniquely identifies the provider. Windows, along with other applications and drivers, use the GUID to associate WMI control messages (such as start, enable, and stop) with the provider.

The control GUID appears in the [WPP\_CONTROL\_GUIDS](https://msdn.microsoft.com/library/windows/hardware/ff556186) macro in the source code file for an instrumented trace provider.

```
#define WPP_CONTROL_GUIDS \
    WPP_DEFINE_CONTROL_GUID(GUIDFriendlyName, (ControlGUID),  \
        WPP_DEFINE_BIT(NameOfTraceFlag1)  \
        WPP_DEFINE_BIT(NameOfTraceFlag2)  \
        .............................   \
        .............................   \
        WPP_DEFINE_BIT(NameOfTraceFlag31) )
```

[Tracepdb](tracepdb.md) creates a [trace (MOF) file](trace-managed-object-format--mof--file.md) that contains the control GUID and the trace levels of each trace provider that is represented in the PDB file. The name of the MOF file is the module name of the trace provider. Tracepdb can also produce a TMC file if you use the **-c** option.

Because the control GUID identifies the trace provider to Event Tracing for Windows (ETW), you can use the control GUID to define and redefine the scope of a [trace provider](trace-provider.md). For example, multiple drivers can be part of a single trace provider by specifying the same control GUID. Or, a single driver can include multiple trace providers by specifying different control GUIDs in each instance of the [WPP\_CONTROL\_GUIDS](https://msdn.microsoft.com/library/windows/hardware/ff556186) macro.

 

 





