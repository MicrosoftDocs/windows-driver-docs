---
title: "TTD Module Objects"
description: "This section describes the module model objects associated with time travel debugging."
keywords: ["TTD Module Objects", "TTD", "Time Travel", "WinDbg", "Windows Debugging"]
ms.date: 11/15/2024
---

# TTD Module Objects

## Description

*TTD Module* objects are used to give information about modules that were loaded and unloaded during a trace session.

## Properties

| Property | Description |
| -------- | ----------- |
| Name | The name and path of the module. |
| Address | The address where the module was loaded. |
| Size | The size of the module in bytes. |
| Checksum | The checksum of the module. |
| Timestamp | The timestamp of the module. |


## Example Usage

```dbgcmd
0:005> dx -r1 @$cursession.Processes[24848].Modules[10]
@$cursession.Processes[24848].Modules[10]                 : C:\Program Files\WindowsApps\Microsoft.VCLibs.140.00_14.0.30704.0_x64__8wekyb3d8bbwe\VCRUNTIME140_APP.dll [Force Symbol Reload]
    BaseAddress      : 0x7ff9adae0000
    Name             : C:\Program Files\WindowsApps\Microsoft.VCLibs.140.00_14.0.30704.0_x64__8wekyb3d8bbwe\VCRUNTIME140_APP.dll
    Size             : 0x1b000
    SymbolType       : Deferred
    Attributes      
    Contents        
    Symbols          : [SymbolModule]VCRUNTIME140_APP
```

## See Also

[Time Travel Debugging - Introduction to Time Travel Debugging objects](time-travel-debugging-object-model.md)

[Time Travel Debugging - Overview](time-travel-debugging-overview.md)

[dx (Display Debugger Object Model Expression)](dx--display-visualizer-variables-.md)
