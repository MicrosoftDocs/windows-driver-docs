---
title: Example 8 Using the CSV File Format
description: Example 8 Using the CSV File Format
ms.assetid: 225365dd-57f8-4d35-a859-b881a104201f
keywords: ["Tracefmt WDK , CSV format", "CSV format WDK Tracefmt"]
---

# Example 8: Using the CSV File Format


The following command directs Tracefmt to format the trace message output file (**-o**) as a comma-separated, variable-length (CSV) format file:

```
tracefmt mytrace.etl -p c:\tracing -o mytrace.csv -csv -csvheader
```

This command formats the trace messages in the mytrace.etl trace log file. It uses the **-p** parameter to specify the location of the TMF file.

The command uses the **-o** parameter to specify the name and location of the output file and uses a .csv file name extension for the file. It uses the **-csv** parameter to specify the CSV format, and the **-csvheader** parameter to add a row of column headers to the file. By default, the file has no column headers.

In response, Tracefmt formats the trace messages by using commas between the prefix and message fields, and saves them in the mytrace.csv file.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Example%208:%20Using%20the%20CSV%20File%20Format%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




