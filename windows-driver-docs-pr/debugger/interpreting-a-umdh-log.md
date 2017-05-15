---
title: Interpreting a UMDH Log
description: Interpreting a UMDH Log
ms.assetid: c5c74a3a-9598-4d89-8c5b-445138ae845f
keywords: ["UMDH, interpreting a UMDH log"]
---

# Interpreting a UMDH Log


## <span id="ddk_interpreting_a_umdh_log_dtools"></span><span id="DDK_INTERPRETING_A_UMDH_LOG_DTOOLS"></span>


User-Mode Dump Heap (UMDH) log files display the list of heap allocations in the process and the stacks where the allocations were made.

This example shows how to generate a log for a process that has ID 1204. The log is written to the file log1.txt.

```
umdh -p:1204 -f:log1.txt
```

The log file is not readable because the symbols are not resolved. UMDH resolves symbols when you analyze the log. This example shows how to analyze log1.txt and store the result in result.txt.

```
umdh -v log1.txt  > result.txt
```

## <span id="Symbol_Files_for_Analyzing_a_Log_File"></span><span id="symbol_files_for_analyzing_a_log_file"></span><span id="SYMBOL_FILES_FOR_ANALYZING_A_LOG_FILE"></span>Symbol Files for Analyzing a Log File


Suppose you have two computers: a *logging computer* where you create a UMDH log and an *analysis computer* where you analyze the UMDH log. The symbol path on your analysis computer must point to the symbols for the version of Windows that was loaded on the logging computer at the time the log was made. Do not point the symbol path on the analysis computer to a symbol server. If you do, UMDH will retrieve symbols for the version of Windows that is running on the analysis computer, and UMDH will not display meaningful results.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Interpreting%20a%20UMDH%20Log%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




