---
title: TraceView Command-Line Interface
description: TraceView Command-Line Interface
ms.assetid: da38268f-ebdf-468c-95fe-500ba747047a
keywords: ["TraceView WDK , command-line interface", "commands WDK TraceView"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20TraceView%20Command-Line%20Interface%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




