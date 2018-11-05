---
title: Analyze UMDH Logs
description: Use the following commands to analyze User-Mode Dump Heap (UMDH) logs that were created by running UMDH with the syntax described in Analyze a Running Process.
ms.assetid: 66e559b2-0335-4a1d-ba6c-dde6b826dc5f
keywords: ["Analyze UMDH Logs Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- Analyze UMDH Logs
api_type:
- NA
ms.localizationpriority: medium
---

# Analyze UMDH Logs


Use the following commands to analyze User-Mode Dump Heap (UMDH) logs that were created by running UMDH with the syntax described in [**Analyze a Running Process**](analyze-a-running-process.md). This analysis focuses on allocations, instead of stack traces.

You can analyze a single log file or compare logs from different runs to detect the changes in the program or driver's memory dump allocations over time.

```dbgcmd
umdh [-d] [-v] [-l] File1 [File2] [-h | ?]
```

## <span id="ddk_analyze_umdh_logs_dtools"></span><span id="DDK_ANALYZE_UMDH_LOGS_DTOOLS"></span>Parameters


<span id="_______-d______"></span><span id="_______-D______"></span> **-d**   
Displays numeric data in decimal numbers. The default is hexadecimal.

<span id="_______-v______"></span><span id="_______-V______"></span> **-v**   
Verbose mode. Includes the traces, as well as summary information. The traces are most helpful when analyzing a single log file.

<span id="_______-l______"></span><span id="_______-L______"></span> **-l**   
Includes file names and line numbers in the log. (Please note that the parameter is the lowercased letter "L," not the number one.)

<span id="_______File1__File2_"></span><span id="_______file1__file2_"></span><span id="_______FILE1__FILE2_"></span> *File1* \[*File2*\]  
Specifies the UMDH log files to analyze.

UMDH creates log files when you run it in the [**analyze a running process**](analyze-a-running-process.md) mode and save the log content in a text file (**-f**).

When you specify one log file, UMDH analyzes the file and displays the function calls in each trace in descending order of bytes allocated.

When you specify two log files, UMDH compares the files and displays in descending order the function calls whose allocations have grown the most between the two trials.

<span id="_______-h____"></span><span id="_______-H____"></span> **-h | ?**  
Displays help.

### <span id="sample_usage"></span><span id="SAMPLE_USAGE"></span>Sample Usage

```dbgcmd
umdh dump.txt
umdh -d -v dump.txt
umdh dump1.txt dump2.txt
```

Remarks
-------

Suppose you have two computers: a *logging computer* where you create a UMDH log and an *analysis computer* where you analyze the UMDH log. The symbol path on your analysis computer must point to the symbols for the version of Windows that was loaded on the logging computer at the time the log was made. Do not point the symbol path on the analysis computer to a symbol server. If you do, UMDH will retrieve symbols for the version of Windows that is running on the analysis computer, and UMDH will not display meaningful results.

 

 





