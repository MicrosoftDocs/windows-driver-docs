---
title: Plotter Driver Capabilities
description: Plotter Driver Capabilities
keywords:
- Plotter Driver WDK print , capabilities
- MSPlot WDK print , capabilities
ms.date: 01/30/2023
---

# Plotter Driver Capabilities

[!include[Print Support Apps](../includes/print-support-apps.md)]

The Microsoft Plotter Driver (MSPlot) provides the following capabilities:

- Support for all plotters that use the HPGL/2 version of the Hewlett-Packard Graphics Language, by means of plotter model-specific [plotter driver minidrivers](plotter-driver-minidrivers.md).

- A [plotter driver user interface](plotter-driver-user-interface.md), based on the TreeView control and property sheets, that is consistent for all plotters.

- A [plotter driver renderer](plotter-driver-renderer.md) that, along with the GDI graphics engine, converts Win32 GDI calls from applications into printer commands that can be sent to the print spooler.

To provide support for a new HPGL/2-compliant device type, all you need to do is provide a minidriver that describes the device.
