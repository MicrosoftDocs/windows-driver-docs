---
title: Example 3 Typical Start Command
description: Example 3 Typical Start Command
ms.assetid: a0e8580d-b841-4077-82f5-6aaef57b0ff7
keywords:
- trace sessions WDK , starting
- start command
- -start command
- starting trace sessions
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Example 3: Typical Start Command


## <span id="ddk_typical_start_command_tools"></span><span id="DDK_TYPICAL_START_COMMAND_TOOLS"></span>


The following command format is typically used to start a trace session:

```
tracelog -start MyTrace -guid MyProvider.guid -f d:\traces\testtrace.etl -flag 2 -level 0xFFFF
```

The command starts a trace session named "MyTrace".

It uses the **-guid** parameter to indicate the MyProvider.guid file, a simple text file that contains nothing but the provider's control GUID. You can also use a [control GUID file](control-guid-file.md), such as Tracedrv.ctl, with the **-guid** parameter. Tracedrv.ctl is included in the [TraceDrv](http://go.microsoft.com/fwlink/p/?linkid=256197) sample.

The command includes the **-f** parameter to specify the name and location of the event trace log file. It includes the **-flag** parameter to specify the flags set and the **-level** parameter to specify the level setting. You can omit these parameters, but some trace providers do not generate any trace messages unless you set the flag or the level.

 

 





