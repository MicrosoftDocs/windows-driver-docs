---
title: Introduction to Printer Graphics DLLs
description: Introduction to Printer Graphics DLLs
keywords:
- printer graphics DLL WDK , about printer graphics DLL
- graphics DLL WDK printer , about printer graphics DLL
- graphics DLL WDK printer
- printer graphics DLL WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Introduction to Printer Graphics DLLs


Printer graphics DLLs implement Drv-prefixed graphics DDI functions that are described in [Using the Graphics DDI](../display/using-the-graphics-ddi.md). These DLLs have the following two responsibilities:

-   Assist GDI in rendering a print job.

    A printer graphics DLL can provide graphics DDI drawing functions to handle drawing operations that must be performed in a device-specific manner and thus cannot be handled exclusively by GDI's rendering engine.

-   Deliver a rendered data stream to the spooler.

    Printer graphics DLLs typically produce an output stream in a [RAW data type](raw-data-type.md) (including command sequences) that the spooler can send to printer hardware through *print monitors*.

The amount of rendering assistance that a printer graphics DLL must provide is printer type-specific, depending on the hardware's drawing capabilities, and includes the following scenarios:

-   The GDI rendering engine does all rendering, using a GDI-managed surface. The graphics DLL does not provide any DDI drawing functions.

-   The graphics DLL provides some graphics DDI drawing functions to work in conjunction with GDI's rendering engine, using a GDI-managed surface. The graphics DDI drawing functions provided by the graphics DLL can optionally call back to the GDI rendering engine's [GDI support services](../display/gdi-support-services.md).

-   The graphics DLL does all rendering by providing graphics DDI drawing functions and using a device-managed surface.

For example, the [Microsoft Universal Printer Driver](microsoft-universal-printer-driver.md) (Unidrv) uses a GDI-managed surface and provides some graphics DDI drawing functions, while the [Microsoft PostScript Printer Driver](microsoft-postscript-printer-driver.md) uses a device-managed surface.

For more information about providing rendering assistance in graphics drivers, see [Surface Types](../display/surface-types.md) and [Using the Graphics DDI](../display/using-the-graphics-ddi.md).

The following two figures illustrate the data flow that occurs when an application creates a print job using GDI. EMF recording and playback are combined in these figures.

The first diagram depicts a user-mode printer graphics DLL.

**Note**   In Windows Vista printer graphics DLLs can only execute in user mode. For more information, see [Choosing User Mode or Kernel Mode](choosing-user-mode-or-kernel-mode.md).

 

![diagram illustrating a user-mode printer graphics dll.](images/usrmdprt.png)

The second diagram depicts a kernel-mode printer graphics DLL.

![print job data flow, using a kernel-mode printer graphics dll.](images/gdiprint.png)

Note in these diagrams that if the output format from GDI is *enhanced metafile (EMF)*, the printer graphics DLL does not receive the job until the EMF print processor plays back EMF records. Note also that the EMF Print Processor changes output format to non-EMF.

The diagrams illustrate an entirely local environment. If the printer is connected to a server, EMF records are typically produced by the client's copy of the GDI rendering engine (GRE) and then spooled to a local file that is sent to the server. The server's copy of the spooler reads the file and sends the records to the server's EMF print processor, and the server's copy of the GRE calls the server's printer graphics DLL.

 

