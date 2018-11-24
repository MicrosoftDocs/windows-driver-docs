---
title: EMF Data Type
description: EMF Data Type
ms.assetid: d5a05778-3637-4dba-b036-5f0fc236d52d
keywords:
- print processors WDK , data types
- data types WDK print processor
- EMF data type WDK print processor
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# EMF Data Type





Enhanced Metafile (EMF) data consists of instructions to call GDI functions. The print processor must call the GDI functions to render printable images. The GDI functions make calls to the printer driver's [printer graphics DLL](printer-graphics-dll.md), which renders the image and sends it to the spooler as RAW data (by calling [**EngWritePrinter**](https://msdn.microsoft.com/library/windows/hardware/ff565467)).

NT-based operating system clients send EMF data to NT-based operating system print servers. EMF data is device independent and can be sent to a server more quickly than RAW data. A print job is also spooled as EMF data when the requesting application is local to the server, allowing a quick return to the application while the EMF data is subsequently rendered by a background spooler thread.

For more information about the EMF data type, see the *Windows 2000 Professional Resource Kit* or the *Windows 2000 Server Resource Kit*. For more information about enhanced metafiles, see the Windows SDK documentation. (These resources may not be available in some languages and countries.)

 

 




