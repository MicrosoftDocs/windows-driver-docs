---
title: Trace Message Format File
description: Trace Message Format File
ms.assetid: ac45475e-bf2d-4fa6-82fc-37ef8f4c0f6c
keywords: ["trace message format files WDK", "TMF files WDK", "TMF files WDK , about TMF files", "files WDK software tracing"]
---

# Trace Message Format File


## <span id="ddk_trace_message_format_file_tools"></span><span id="DDK_TRACE_MESSAGE_FORMAT_FILE_TOOLS"></span>


The *trace message format* (TMF) file is a structured text file that contains instructions for parsing and formatting the binary trace messages that a [trace provider](trace-provider.md) generates. The formatting instructions are included in the trace provider's source code and are added to the trace provider's PDB symbol file by the [WPP preprocessor](wpp-preprocessor.md).

Some tools that log and display formatted trace messages require a TMF file. [Tracefmt](tracefmt.md) and [TraceView](traceview.md), WDK tools that format and display trace messages, can use a TMF file or they can extract the formatting information directly from a PDB symbol file.

TMF files are created automatically during the build process when the trace provider is specified in a [**place file**](place-file-syntax.md). By default, the TMF files are located in the TraceFormat subdirectory of your Symbol File path. However, you can specify the destination path in the %TRACE\_FORMAT\_SEARCH\_PATH% environment variable.

If you do not have a TMF file for a [trace provider](trace-provider.md), use [Tracepdb](tracepdb.md). Tracepdb extracts the formatting instructions from the PDB symbol file and creates a TMF file to store them. Many application and driver developers prefer shipping a TMF file, rather than a PDB symbol file.

The name of the TMF file is the [message GUID](message-guid.md) of the messages associated with that TMF file. ETW uses the message GUID to associate particular trace messages with the TMF file that holds their formatting instructions.

A TMF file contains the following data:

-   The name of the PDB file from which the TMF file data was extracted.

-   The [message GUID](message-guid.md) of the trace messages in the source file and the source file name.

-   For each trace message, an entry that specifies the message type, the source code file name, a line number, a message number, a message definition string, a trace flag name, and the name of the C function that contains the macro call.

-   A list of variables whose values appear in the trace messages and their associated internal type names. The variables are represented by the %*n* notation in a message definition string.

**Note**  The TMF file is reserved for internal use, and its format is subject to change between different versions of Windows.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Trace%20Message%20Format%20File%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




