---
title: Example 4 Sequence Numbers
description: Example 4 Sequence Numbers
ms.assetid: 5b498267-c495-4a25-abb9-aa83a51559e1
keywords:
- Tracefmt WDK , sequence numbers
- sequence numbers WDK Tracefmt
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Example 4: Sequence Numbers


The following command includes the local or global sequence number of the message in the output file. If sequence numbers were not generated, the sequence field contains zeros.

```
tracefmt mytrace.etl -p c:\tracing -o mytrace.txt -seq
```

This command formats messages from the mytrace.etl log file by using a TMF file in the c:\\tracing directory. It writes the formatted messages to the mytrace.txt file. The command uses the **-seq** parameter to direct Tracefmt to include sequence numbers in the output file.

An excerpt of the output file appears as follows:

```
[0]0AF4.0C64::07/25/2003-13:55:39.998 00004ea4 [tracedrv]IOCTL = 1
[0]0AF4.0C64::07/25/2003-13:55:39.998 000047d0 [tracedrv]Hello, 1 Hi
[0]0AF4.0C64::07/25/2003-13:55:39.998 63966c89 [tracedrv]Hello, 2 Hi
...
```

**Note**   If you view a trace message file on a computer running Windows XP, the display might show trace messages that are out of sequence trace messages. To correct this problem, you can use the sequence number option when you start the trace session and view the trace using Tracefmt. You can then view the trace with Traceview and sort according to sequence number. You can also view the trace on a computer running Windows Server 2003 or later versions of Windows.

 

 

 





