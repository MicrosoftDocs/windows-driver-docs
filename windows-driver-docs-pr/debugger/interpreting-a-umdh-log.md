---
title: Interpreting a UMDH Log
description: Interpreting a UMDH Log
ms.assetid: c5c74a3a-9598-4d89-8c5b-445138ae845f
keywords: ["UMDH, interpreting a UMDH log"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Interpreting a UMDH Log


## <span id="ddk_interpreting_a_umdh_log_dtools"></span><span id="DDK_INTERPRETING_A_UMDH_LOG_DTOOLS"></span>


User-Mode Dump Heap (UMDH) log files display the list of heap allocations in the process and the stacks where the allocations were made.

This example shows how to generate a log for a process that has ID 1204. The log is written to the file log1.txt.

```console
umdh -p:1204 -f:log1.txt
```

The log file is not readable because the symbols are not resolved. UMDH resolves symbols when you analyze the log. This example shows how to analyze log1.txt and store the result in result.txt.

```console
umdh -v log1.txt  > result.txt
```

## <span id="Symbol_Files_for_Analyzing_a_Log_File"></span><span id="symbol_files_for_analyzing_a_log_file"></span><span id="SYMBOL_FILES_FOR_ANALYZING_A_LOG_FILE"></span>Symbol Files for Analyzing a Log File


Suppose you have two computers: a *logging computer* where you create a UMDH log and an *analysis computer* where you analyze the UMDH log. The symbol path on your analysis computer must point to the symbols for the version of Windows that was loaded on the logging computer at the time the log was made. Do not point the symbol path on the analysis computer to a symbol server. If you do, UMDH will retrieve symbols for the version of Windows that is running on the analysis computer, and UMDH will not display meaningful results.

 

 





