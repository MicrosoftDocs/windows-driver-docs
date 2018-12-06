---
title: Pscript Renderer
description: Pscript Renderer
ms.assetid: b1707a83-c5c9-4578-8603-7c19de4960ed
keywords:
- PostScript Printer Driver WDK print , renderer
- Pscript WDK print , renderer
- renderer WDK Pscript
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Pscript Renderer





The Pscript renderer is implemented as a [printer graphics DLL](printer-graphics-dll.md) and thus exports functions defined by the Microsoft Device Driver Interface (DDI) for graphics drivers. When an application calls Graphics Device Interface (GDI) functions to send text and images to a printer device, the kernel-mode graphics engine calls the renderer's graphics DDI functions. These graphics DDI functions assist GDI in drawing a print job's page images.

The renderer is also responsible for sending text rendered image data, along with printer command sequences, to the print spooler, which then directs the data stream and commands to printer hardware.

You can modify Pscript's rendering operations by providing a [rendering plug-in](rendering-plug-ins.md), which is described in the section entitled [Customizing Microsoft's Printer Drivers](customizing-microsoft-s-printer-drivers.md).

 

 




