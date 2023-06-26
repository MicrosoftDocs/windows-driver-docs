---
title: Introduction to print processors
description: Introduction to print processors
keywords:
- print processors WDK , about print processors
- customized print processors WDK
- print processors WDK , data types
- data types WDK print processor
ms.date: 06/26/2023
---

# Introduction to print processors

Print processors are user-mode DLLs that are responsible for converting a print job's spooled data into a format that can be sent to a *print monitor*. They are also responsible for handling application requests to pause, resume and cancel print jobs.

The print job's spooled data is contained in a spool file. The print processor reads the file, performs conversion operations on the data stream, and writes the converted data to the spooler. The spooler then sends the data stream to the appropriate print monitor.

Windows includes the print processors listed in the following table.

| Print processor | Input data types | Output data types |
|--|--|--|
| Localspl.dll | EMF<br><br>RAW<br><br>TEXT | RAW |
| Sfmpsprt.dll | PSCRIPT1 | RAW |

For information about the data types, see the following topics:

[EMF Data Type](emf-data-type.md)

[RAW Data Type](raw-data-type.md)

[TEXT Data Type](text-data-type.md)

[PSCRIPT1 Data Type](pscript1-data-type.md)

You can create a customized print processor to support a data type that is not supported by Windows 2000 or later operating system versions. You can also provide a customized print processor that supports one or more of the supported data types, thus allowing you to modify the capabilities provided by the supplied print processors.

Print processors are associated with printer drivers during driver installation, so multiple print processors supporting the same data type can coexist. For more information, see [Installing a Print Processor](installing-a-print-processor.md).

When you compile a print processor, set the Unicode flag with \#define UNICODE. Print processor code should use only wide strings, of type LPWSTR, for example.
