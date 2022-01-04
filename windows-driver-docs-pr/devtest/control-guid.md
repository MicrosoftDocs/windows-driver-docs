---
title: Control GUID
description: Control GUID
keywords:
- control GUIDs WDK
- GUIDs WDK software tracing
- identifiers WDK software tracing
ms.date: 04/20/2017
---

# Control GUID

## <span id="ddk_control_guid_tools"></span><span id="DDK_CONTROL_GUID_TOOLS"></span>

Each [trace provider](trace-provider.md) defines a *control GUID* that uniquely identifies the provider. This GUID is used to enable or disable the trace provider through [Event Tracing for Windows (ETW)](event-tracing-for-windows--etw-.md).

The control GUID appears in the [WPP\_CONTROL\_GUIDS](/previous-versions/windows/hardware/previsioning-framework/ff556186(v=vs.85)) macro in the source code file for an instrumented trace provider.

```C
#define WPP_CONTROL_GUIDS \
    WPP_DEFINE_CONTROL_GUID(GUIDFriendlyName, (ControlGUID),  \
        WPP_DEFINE_BIT(NameOfTraceFlag1)  \
        WPP_DEFINE_BIT(NameOfTraceFlag2)  \
        .............................   \
        .............................   \
        WPP_DEFINE_BIT(NameOfTraceFlag31) )
```

[Tracepdb](tracepdb.md) creates a [trace (MOF) file](trace-managed-object-format--mof--file.md) that contains the control GUID and the trace levels of each trace provider that is represented in the PDB file. The name of the MOF file is the module name of the trace provider. Tracepdb can also produce a TMC file if you use the **-c** option.

Because the control GUID identifies the trace provider to ETW, you can use the control GUID to define and redefine the scope of a [trace provider](trace-provider.md). For example, multiple drivers can be part of a single trace provider by specifying the same control GUID. Or, a single driver can include multiple trace providers by specifying different control GUIDs in each instance of the [WPP\_CONTROL\_GUIDS](/previous-versions/windows/hardware/previsioning-framework/ff556186(v=vs.85)) macro.
