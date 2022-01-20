---
title: Windows Device Testing Framework (WDTF) design guide
description: The Microsoft Windows Device Testing Framework (WDTF) enables you to create, manage, reuse, and extend device-centric, scenario-based automated tests.
ms.assetid: cff552f0-5dde-4fe7-996c-0a496d845edc
ms.date: 04/20/2017
ms.topic: article
---

# Windows Device Testing Framework (WDTF) design guide

The Microsoft Windows Device Testing Framework (WDTF) enables you to create, manage, reuse, and extend device-centric, scenario-based automated tests.

## In this section

|Topic|Description|
|----|----|
|[Writing a WDTF SimpleIO plug-in for your device](writing-a-wdtf-simpleio-plug-in-for-your-device.md)|To get the most benefit from the [Device Fundamental tests](/windows-hardware/drivers), your device should have a Simple I/O plug-in that can perform simple I/O to your device. This can be one of the default Simple I/O plugs that come with WDTF or one that you wrote. To see if your device type is supported and to determine if there are specific requirements for testing, refer to [Provided WDTF Simple I/O plug-ins](provided-wdtf-simpleio-plug-ins.md).|
|[Writing tests with WDTF](writing-tests-with-wdtf.md)|Whether you start writing driver tests with the templates provided in the Windows Driver Kit (WDK), or whether you create the tests on your own, the Microsoft Windows Device Testing Framework (WDTF) enables you to create and extend device-centric, scenario-based automated tests.|
|[Triaging WDTF-based tests](triaging-wdtf-based-tests.md)|To help you better understand what is going on in your WDTF-based tests, you can use the built-in support for [WDTF Object Logging](logging-and-tracing.md) and [WPP Software Tracing](../devtest/wpp-software-tracing.md).|
|[WDTF Architecture and Overview](wdtf-overview.md)|The Microsoft Windows Device Testing Framework (WDTF) enables you to create, manage, reuse, and extend device-centric, scenario-based automated tests.|