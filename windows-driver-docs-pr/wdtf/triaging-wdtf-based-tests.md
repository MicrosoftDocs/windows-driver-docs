---
title: Triaging WDTF-based tests
author: windows-driver-content
description: To help you better understand what is going on in your WDTF-based tests, you can use the built-in support for WDTF Object Logging and WPP Software Tracing.
ms.assetid: C2F7AA74-7A74-4EA4-AD2D-8143252380C8
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Triaging WDTF-based tests


To help you better understand what is going on in your WDTF-based tests, you can use the built-in support for [WDTF Object Logging](logging-and-tracing.md) and [WPP Software Tracing](https://msdn.microsoft.com/library/windows/hardware/ff556204).

WDTF object logging causes WDTF objects to automatcially write log messages to a common log file, which can simplify test authoring and can help you diagnose test problems. The Device Fundamental tests and other tests that ship in the WDK are examples of WDTF-based tests. For information about those tests, see [How to select and configure the Device Fundamental tests](https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests).

WDTF provides support for [WPP Software Tracing](https://msdn.microsoft.com/library/windows/hardware/ff556204). All WDTF objects produce tracing information as they run. You can read the trace information by using WDK tools, including [TraceView](https://msdn.microsoft.com/library/windows/hardware/ff556063).

## In this section


-   [WDTF Object Logging](logging-and-tracing.md)
-   [Enabling and Viewing WDTF Traces](viewing-wdtf-traces.md)
-   [Diagnosing problems running WDTF-based tests](diagnosing-problems-running-wdtf-based-tests.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdtf\dtf%5D:%20Triaging%20WDTF-based%20tests%20%20RELEASE:%20%289/13/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


