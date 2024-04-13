---
title: Unidrv Renderer
description: Unidrv Renderer
keywords:
- Unidrv, renderer
- renderer WDK Unidrv
- Unidrv WDK print
ms.date: 01/30/2023
---

# Unidrv Renderer

[!include[Print Support Apps](../includes/print-support-apps.md)]

The Unidrv renderer is implemented as a [printer graphics DLL](printer-graphics-dll.md) and thus exports functions defined by the Microsoft Device Driver Interface (DDI) for graphics drivers. When an application calls Graphics Device Interface (GDI) functions to send images to a printer device, the kernel-mode graphics engine calls the renderer's graphics DDI functions. These graphics DDI functions assist GDI in drawing a print job's page images.

The renderer is also responsible for sending rendered image data, along with printer command sequences, to the print spooler, which then directs the images and commands to printer hardware. The printer commands that the renderer sends are specified in [Unidrv Minidrivers](unidrv-minidrivers.md).

You can modify Unidrv's rendering operations by providing a [rendering plug-in](rendering-plug-ins.md).
