---
title: Example 3 Typical Start Command
description: Example 3 Typical Start Command
ms.assetid: a0e8580d-b841-4077-82f5-6aaef57b0ff7
keywords: ["trace sessions WDK , starting", "start command", "-start command", "starting trace sessions"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Example%203:%20Typical%20Start%20Command%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




