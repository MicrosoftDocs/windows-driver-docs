---
title: Triaging WDTF-based tests
description: To help you better understand what is going on in your WDTF-based tests, you can use the built-in support for WDTF Object Logging and WPP Software Tracing.
ms.date: 04/20/2017
---

# Triaging WDTF-based tests


To help you better understand what is going on in your WDTF-based tests, you can use the built-in support for [WDTF Object Logging](logging-and-tracing.md) and [WPP Software Tracing](../devtest/wpp-software-tracing.md).

WDTF object logging causes WDTF objects to automatcially write log messages to a common log file, which can simplify test authoring and can help you diagnose test problems. The Device Fundamental tests and other tests that ship in the WDK are examples of WDTF-based tests. For information about those tests, see [How to select and configure the Device Fundamental tests](/windows-hardware/drivers).

WDTF provides support for [WPP Software Tracing](../devtest/wpp-software-tracing.md). All WDTF objects produce tracing information as they run. You can read the trace information by using WDK tools, including [TraceView](../devtest/using-traceview.md).

## In this section


-   [WDTF Object Logging](logging-and-tracing.md)
-   [Enabling and Viewing WDTF Traces](viewing-wdtf-traces.md)
-   [Diagnosing problems running WDTF-based tests](diagnosing-problems-running-wdtf-based-tests.md)

 

