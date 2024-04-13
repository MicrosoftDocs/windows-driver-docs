---
title: RAW Data Type
description: Provides information about the RAW data type.
keywords:
- print processors WDK, data types
- data types WDK print processor
- RAW data type WDK print processor
ms.date: 09/16/2022
---

# RAW data type

RAW data can be sent to a print monitor without further processing. The print processor just sends this data back to the spooler by calling [**WritePrinter**](/windows/win32/printdocs/writeprinter), sometimes inserting form feeds. An example of a RAW data file is one consisting of *printer control language (PCL)* commands. Print jobs are sent from client to server in RAW format if either the client or the server does not support NT-based-operating system EMF, or if a server administrator has disabled EMF support. In such cases, image rendering is performed on the client before the job is sent to the server.

Postscript commands can be considered RAW data if the target printer supports Postscript. On the other hand, the Sfmpsprt.dll print processor takes Postscript input and interprets it for non-Postscript printers, so in that case the Postscript is not RAW data.
