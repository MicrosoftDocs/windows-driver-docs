---
title: Trace Message Format File
description: Trace Message Format File
ms.assetid: ac45475e-bf2d-4fa6-82fc-37ef8f4c0f6c
keywords:
- trace message format files WDK
- TMF files WDK
- TMF files WDK , about TMF files
- files WDK software tracing
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Trace Message Format File


## <span id="ddk_trace_message_format_file_tools"></span><span id="DDK_TRACE_MESSAGE_FORMAT_FILE_TOOLS"></span>


The *trace message format* (TMF) file is a structured text file that contains instructions for parsing and formatting the binary trace messages that a [trace provider](trace-provider.md) generates. The formatting instructions are included in the trace provider's source code and are added to the trace provider's PDB symbol file by the [WPP preprocessor](wpp-preprocessor.md).

Some tools that log and display formatted trace messages require a TMF file. [Tracefmt](tracefmt.md) and [TraceView](traceview.md), WDK tools that format and display trace messages, can use a TMF file or they can extract the formatting information directly from a PDB symbol file.

You can create a TMF file by using [Tracefmt](https://docs.microsoft.com/windows-hardware/drivers/devtest/tracefmt) and including the **-i** parameter, which directs Tracefmt to create a TMF file for Tracedrv. For more info, see [Example 9: Creating a TMF file](https://docs.microsoft.com/windows-hardware/drivers/devtest/example-9--creating-a-tmf-file).

If you do not have a TMF file for a [trace provider](trace-provider.md), use [Tracepdb](tracepdb.md). Tracepdb extracts the formatting instructions from the PDB symbol file and creates a TMF file to store them. Many application and driver developers prefer shipping a TMF file, rather than a PDB symbol file.

The name of the TMF file is the [message GUID](message-guid.md) of the messages associated with that TMF file. ETW uses the message GUID to associate particular trace messages with the TMF file that holds their formatting instructions.

A TMF file contains the following data:

-   The name of the PDB file from which the TMF file data was extracted.

-   The [message GUID](message-guid.md) of the trace messages in the source file and the source file name.

-   For each trace message, an entry that specifies the message type, the source code file name, a line number, a message number, a message definition string, a trace flag name, and the name of the C function that contains the macro call.

-   A list of variables whose values appear in the trace messages and their associated internal type names. The variables are represented by the %*n* notation in a message definition string.

**Note**  The TMF file is reserved for internal use, and its format is subject to change between different versions of Windows.

 

 

 





