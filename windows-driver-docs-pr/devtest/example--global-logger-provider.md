---
title: Example Global Logger Provider
description: Example Global Logger Provider
keywords:
- Global Logger trace session WDK , logging
- boot-time Global Logger trace session WDK , logging
- logs WDK tracing during boot
ms.date: 04/20/2017
---

# Example: Global Logger Provider

The following screen shot shows the **GlobalLogger** subkey, which contains entries that configure the [Global Logger trace session](global-logger-trace-session.md). Under the **GlobalLogger** subkey is a **ControlGUID** subkey that represents a trace provider that logs to the Global Logger trace session. The **ControlGUID** subkey is selected, and the entries in the subkey appear in the right pane.

:::image type="content" source="images/globallogger.png" alt-text="Screenshot of a trace provider's subkey that logs to the Global Logger trace session on Windows XP.":::

In this example, the **ControlGUID** subkey represents the TraceDrv sample driver. The subkey is named for the Tracedrv [control GUID](control-guid.md), d58c126f-b309-11d1-969e-0000f875a5bc. Because the trace session is running on Windows XP, the GUID is not enclosed in braces.

The [TraceDrv](https://github.com/Microsoft/Windows-driver-samples/tree/main/general/tracing/tracedriver) sample driver is available in the [Windows driver samples](https://github.com/Microsoft/Windows-driver-samples) repository available on GitHub.

This **ControlGUID** subkey contains a **Flags** entry and a **Level** entry. These entries are optional and their value is defined by the provider.
