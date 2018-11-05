---
title: Trace Log
description: Trace Log
ms.assetid: c15fcfec-b584-4cb8-bc48-9ff122f5a8fc
keywords:
- event trace logs WDK
- log files WDK tracing
- .etl files
- etl files
- trace logs WDK
- storing trace messages
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Trace Log


## <span id="ddk_trace_log_tools"></span><span id="DDK_TRACE_LOG_TOOLS"></span>


An event trace log (.etl) file, also known as a *trace log*, stores the trace messages generated during one or more [trace sessions](trace-session.md).

The system first stores the trace messages that [trace providers](trace-provider.md) generate in trace session buffers, and then delivers them directly to a [trace consumer](trace-consumer.md) or writes them to a trace log.

Because the messages can occupy a large amount of disk space, trace logs store them in a compressed binary format. To read the messages, trace consumers use information supplied by the trace provider (the *FormatString* parameter in the [**DoTraceMessage**](https://msdn.microsoft.com/library/windows/hardware/ff544918) macro) to parse and format the messages so that they are readable. The trace consumer can find this information in the [PDB symbol file](pdb-symbol-files.md) or the [trace message format file](trace-message-format-file.md) for the provider.

 

 





