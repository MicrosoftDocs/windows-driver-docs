---
title: Example 1 No Parameters
description: Example 1 No Parameters
keywords:
- Tracefmt WDK , parameters
ms.date: 04/20/2017
---

# Example 1: No Parameters

Tracefmt has no required parameters. Therefore, the simplest Tracefmt command is as follows:

```
tracefmt
```

In response, Tracefmt formats the trace messages in the default C:\\logfile.etl file by using a TMF file in the path specified by the %TRACE\_FORMAT\_SEARCH\_PATH% environment variable. It creates an output file named Fmtfile.txt and a summary message file named Fmtfile.txt.sum in the local directory.
