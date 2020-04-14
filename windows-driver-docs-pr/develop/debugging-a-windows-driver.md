---
title: Debugging a Universal Windows driver
ms.assetid: d2d168fe-8be2-4a3d-bc29-4ab3a306296e
description: Describes debugging techniques you can use with a Universal Windows driver, in particular the Inflight Trace Recorder.
ms.date: 04/28/2020
ms.localizationpriority: medium
---

# Debugging a Windows Driver 

For general information about debugging drivers, see [Getting Started with Windows Debugging](https://docs.microsoft.com/windows-hardware/drivers/debugger/getting-started-with-windows-debugging).

## Inflight Trace Recorder

Starting in Windows 10, you can build your KMDF or UMDF driver binary so that it gets additional driver debugging information through the [Inflight Trace Recorder](https://docs.microsoft.com/windows-hardware/drivers/devtest/using-wpp-recorder). Windows Drivers can take advantage of this feature.

In addition, if you used the Visual Studio KMDF template, your driver uses Windows software trace preprocessor (WPP) to write trace messages. Your driver binary is an ETW provider with a provider GUID.

To send a trace message from your driver binary, use this code:

   ```cpp
   TraceEvents(TRACE_LEVEL_INFORMATION, TRACE_DRIVER, "%!FUNC! Entry");
   ```

You can access the ETW logs using Tracelog by using [!wmitrace](https://docs.microsoft.com/windows-hardware/drivers/debugger/wmi-tracing-extensions--wmitrace-dll-) in a debugger session.

