---
title: RAW Data Type
description: RAW Data Type
ms.assetid: f53264c1-97aa-42f0-8bab-76bf984f2c79
keywords:
- print processors WDK , data types
- data types WDK print processor
- RAW data type WDK print processor
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# RAW Data Type





RAW data can be sent to a print monitor without further processing. The print processor just sends this data back to the spooler (by calling **WritePrinter**, described in the Microsoft Windows SDK documentation), sometimes inserting form feeds. An example of a RAW data file is one consisting of [*printer control language (PCL)*](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-printer-control-language--pcl-) commands. Print jobs are sent from client to server in RAW format if either the client or the server does not support NT-based-operating system EMF, or if a server administrator has disabled EMF support. In such cases, image rendering is performed on the client before the job is sent to the server.

Postscript commands can be considered RAW data if the target printer supports Postscript. On the other hand, the Sfmpsprt.dll print processor takes Postscript input and interprets it for non-Postscript printers, so in that case the Postscript is not RAW data.

For more information about the RAW data type, see the *Windows 2000 Professional Resource Kit* or the *Windows 2000 Server Resource Kit*. (These resources may not be available in some languages and countries.)

 

 




