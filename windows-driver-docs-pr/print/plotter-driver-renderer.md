---
title: Plotter Driver Renderer
description: Plotter Driver Renderer
ms.assetid: 54aac978-6344-41b3-97ea-e78816fb94dc
keywords:
- Plotter Driver WDK print , renderer
- MSPlot WDK print , renderer
- renderer WDK MSPlot
- graphics DDI functions WDK print
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Plotter Driver Renderer





The plotter driver renderer is implemented as a [printer graphics DLL](printer-graphics-dll.md) and thus exports functions defined by the Microsoft Device Driver Interface (DDI) for graphics drivers. When an application calls Graphics Device Interface (GDI) functions to send images to a plotter, the kernel-mode graphics engine calls the renderer's graphics DDI functions. These graphics DDI functions assist GDI in drawing a print job's page images.

The renderer is also responsible for sending rendered image data, along with plotter command sequences, to the print spooler, which then directs the images and commands to plotter hardware.

 

 




