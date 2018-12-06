---
title: TraceView Command-Line Interface
description: TraceView Command-Line Interface
ms.assetid: da38268f-ebdf-468c-95fe-500ba747047a
keywords:
- TraceView WDK , command-line interface
- commands WDK TraceView
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# TraceView Command-Line Interface


The TraceView command-line interface enables you to control the TraceView features from a Command Prompt window.

The command-line interface has three parts:

<span id="TraceView_Control_Commands"></span><span id="traceview_control_commands"></span><span id="TRACEVIEW_CONTROL_COMMANDS"></span>[**TraceView Control Commands**](traceview-control-commands.md)  
Manage the [trace controller](trace-controller.md) features of TraceView. They are similar to [Tracelog](tracelog.md).

<span id="TraceView_-process"></span><span id="traceview_-process"></span><span id="TRACEVIEW_-PROCESS"></span>[**TraceView -process**](traceview--process.md)  
Manages the [trace consumer](trace-consumer.md) features of TraceView. It is similar to [Tracefmt](tracefmt.md).

<span id="TraceView_-parsepdb"></span><span id="traceview_-parsepdb"></span><span id="TRACEVIEW_-PARSEPDB"></span>[**TraceView -parsepdb**](traceview--parsepdb.md)  
Creates a [trace message format (.tmf) file](trace-message-format-file.md) by extracting trace message formatting instructions from a [PDB symbol file](pdb-symbol-files.md). It is similar to [Tracepdb](tracepdb.md).

### <span id="comments"></span><span id="COMMENTS"></span>Comments

The TraceView window and the TraceView command-line interface operate independently and cannot be used interchangeably. You can use the TraceView command-line interface to control trace session that you started by using the TraceView window, but you cannot use the TraceView window to control trace sessions that you started by using the TraceView command-line interface.

When you submit a TraceView command in a Command Prompt window, TraceView opens a new Command Prompt windows for its output. You cannot suppress the additional windows.

 

 





