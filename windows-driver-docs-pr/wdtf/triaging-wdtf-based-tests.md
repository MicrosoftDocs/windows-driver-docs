---
title: Triaging WDTF-based tests
description: To help you better understand what is going on in your WDTF-based tests, you can use the built-in support for WDTF Object Logging and WPP Software Tracing.
ms.assetid: C2F7AA74-7A74-4EA4-AD2D-8143252380C8
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Triaging WDTF-based tests


To help you better understand what is going on in your WDTF-based tests, you can use the built-in support for [WDTF Object Logging](logging-and-tracing.md) and [WPP Software Tracing](https://msdn.microsoft.com/library/windows/hardware/ff556204).

WDTF object logging causes WDTF objects to automatcially write log messages to a common log file, which can simplify test authoring and can help you diagnose test problems. The Device Fundamental tests and other tests that ship in the WDK are examples of WDTF-based tests. For information about those tests, see [How to select and configure the Device Fundamental tests](https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests).

WDTF provides support for [WPP Software Tracing](https://msdn.microsoft.com/library/windows/hardware/ff556204). All WDTF objects produce tracing information as they run. You can read the trace information by using WDK tools, including [TraceView](https://msdn.microsoft.com/library/windows/hardware/ff556063).

## In this section


-   [WDTF Object Logging](logging-and-tracing.md)
-   [Enabling and Viewing WDTF Traces](viewing-wdtf-traces.md)
-   [Diagnosing problems running WDTF-based tests](diagnosing-problems-running-wdtf-based-tests.md)

 

 




