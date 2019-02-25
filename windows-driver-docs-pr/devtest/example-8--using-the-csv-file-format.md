---
title: Example 8 Using the CSV File Format
description: Example 8 Using the CSV File Format
ms.assetid: 225365dd-57f8-4d35-a859-b881a104201f
keywords:
- Tracefmt WDK , CSV format
- CSV format WDK Tracefmt
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Example 8: Using the CSV File Format


The following command directs Tracefmt to format the trace message output file (**-o**) as a comma-separated, variable-length (CSV) format file:

```
tracefmt mytrace.etl -p c:\tracing -o mytrace.csv -csv -csvheader
```

This command formats the trace messages in the mytrace.etl trace log file. It uses the **-p** parameter to specify the location of the TMF file.

The command uses the **-o** parameter to specify the name and location of the output file and uses a .csv file name extension for the file. It uses the **-csv** parameter to specify the CSV format, and the **-csvheader** parameter to add a row of column headers to the file. By default, the file has no column headers.

In response, Tracefmt formats the trace messages by using commas between the prefix and message fields, and saves them in the mytrace.csv file.

 

 





