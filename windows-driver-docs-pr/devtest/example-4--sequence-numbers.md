---
title: Example 4 Sequence Numbers
description: Example 4 Sequence Numbers
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

```text
[0]0AF4.0C64::07/25/2003-13:55:39.998 00004ea4 [tracedrv]IOCTL = 1
[0]0AF4.0C64::07/25/2003-13:55:39.998 000047d0 [tracedrv]Hello, 1 Hi
[0]0AF4.0C64::07/25/2003-13:55:39.998 63966c89 [tracedrv]Hello, 2 Hi
...
```
