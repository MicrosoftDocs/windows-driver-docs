---
title: Example 9 Customizing the Trace Log File
description: Example 9 Customizing the Trace Log File
ms.assetid: b65b4d15-f058-425a-b2b2-b040265d48ac
keywords:
- trace logs WDK
- logs WDK tracing
- custom trace logs WDK
- event trace logs WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Example 9: Customizing the Trace Log File


## <span id="ddk_customizing_the_trace_log_file_tools"></span><span id="DDK_CUSTOMIZING_THE_TRACE_LOG_FILE_TOOLS"></span>


The commands in this example demonstrate different methods for customizing the event trace log file that Tracelog produces.

**Circular file.** The following command starts a trace log session with a circular log file. It uses the **-cir** parameter to specify a circular log file with a maximum size of 2 MB.

If you omit the maximum file size value (in this case, **2**), Tracelog ignores the parameter and starts a session with a sequential trace log file.

```
tracelog -start MyTrace -guid MyProvider.guid -f testtrace.etl -cir 2
```

**Preallocated file.** The following command starts a trace log session with a preallocated file. In this case, the file was preallocated to make sure that its large size could be accommodated before the trace session started.

This command uses the **-seq** parameter to specify a sequential event trace log file with a maximum file size of 128 MB and it uses the **-prealloc** parameter to request a preallocated file. Sequential files are the default, but the **-seq** parameter was used to specify a maximum file size, which is required for preallocated files. The **-cir** parameter can also be used to specify a maximum files size for **-prealloc**, if circular files are preferred.

```
tracelog -start MyTrace -guid MyProvider.guid -f testtrace.etl -seq 128 -prealloc
```

**Multiple files.** The following command starts a trace log session that generates a series of smaller, sequential event trace log files, instead of one large file.

The command uses the **-newfile** parameter with a maximum file size value of 1 to start a new trace log file whenever the current log file reaches 1 MB. Also, the file name specified by the **-f** parameter includes the characters **%d**, as is required when using **-newfile**. The system substitutes a file counter value for **%d** when it creates each file.

```
tracelog -start MyTrace −guid MyProvider.guid -f testtrace%d.etl -newfile 1
```

The resulting 1 MB files are numbered in the order that they are created, for example testtrace1.etl.

 

 





