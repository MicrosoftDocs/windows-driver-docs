---
title: Trace Log
description: Trace Log
ms.assetid: c15fcfec-b584-4cb8-bc48-9ff122f5a8fc
keywords: ["event trace logs WDK", "log files WDK tracing", ".etl files", "etl files", "trace logs WDK", "storing trace messages"]
---

# Trace Log


## <span id="ddk_trace_log_tools"></span><span id="DDK_TRACE_LOG_TOOLS"></span>


An event trace log (.etl) file, also known as a *trace log*, stores the trace messages generated during one or more [trace sessions](trace-session.md).

The system first stores the trace messages that [trace providers](trace-provider.md) generate in trace session buffers, and then delivers them directly to a [trace consumer](trace-consumer.md) or writes them to a trace log.

Because the messages can occupy a large amount of disk space, trace logs store them in a compressed binary format. To read the messages, trace consumers use information supplied by the trace provider (the *FormatString* parameter in the [**DoTraceMessage**](https://msdn.microsoft.com/library/windows/hardware/ff544918) macro) to parse and format the messages so that they are readable. The trace consumer can find this information in the [PDB symbol file](pdb-symbol-files.md) or the [trace message format file](trace-message-format-file.md) for the provider.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Trace%20Log%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




