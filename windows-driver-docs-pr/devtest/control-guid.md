---
title: Control GUID
description: Control GUID
ms.assetid: a85a5e1a-c4c1-40d4-a0ef-d8e552590f03
keywords: ["control GUIDs WDK", "GUIDs WDK software tracing", "identifiers WDK software tracing"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Control%20GUID%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




