---
title: Introduction to Print Processors
description: Introduction to Print Processors
ms.assetid: a34d8daa-b000-4501-8799-5f38cdf38ba4
keywords:
- print processors WDK , about print processors
- customized print processors WDK
- print processors WDK , data types
- data types WDK print processor
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Introduction to Print Processors





Print processors are user-mode DLLs that are responsible for converting a print job's spooled data into a format that can be sent to a [*print monitor*](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-print-monitor). They are also responsible for handling application requests to pause, resume and cancel print jobs.

The print job's spooled data is contained in a spool file. The print processor reads the file, performs conversion operations on the data stream, and writes the converted data to the spooler. The spooler then sends the data stream to the appropriate print monitor.

Microsoft Windows 2000 and later includes the print processors listed in the following table.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Print processor</th>
<th>Input data types</th>
<th>Output data types</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Localspl.dll *</p></td>
<td><p>EMF</p>
<p>RAW</p>
<p>TEXT</p></td>
<td><p>RAW</p></td>
</tr>
<tr class="even">
<td><p>Sfmpsprt.dll</p></td>
<td><p>PSCRIPT1</p></td>
<td><p>RAW</p></td>
</tr>
</tbody>
</table>

 

\* Beginning with Windows 2000, Localmon.dll and Winprint.dll are included in Localspl.dll.

For information about the data types, see the following topics:

[EMF Data Type](emf-data-type.md)

[RAW Data Type](raw-data-type.md)

[TEXT Data Type](text-data-type.md)

[PSCRIPT1 Data Type](pscript1-data-type.md)

You can create a customized print processor to support a data type that is not supported by Windows 2000 or later operating system versions. You can also provide a customized print processor that supports one or more of the supported data types, thus allowing you to modify the capabilities provided by the supplied print processors.

Print processors are associated with printer drivers during driver installation, so multiple print processors supporting the same data type can coexist. For more information, see [Installing a Print Processor](installing-a-print-processor.md).

**Note**   When you compile a print processor, set the Unicode flag with \#define UNICODE. Print processor code should use only wide strings, of type LPWSTR, for example.

 

 

 




