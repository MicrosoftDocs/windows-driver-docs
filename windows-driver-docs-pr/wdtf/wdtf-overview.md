---
title: WDTF Architecture and Overview
author: windows-driver-content
description: The Microsoft Windows Device Testing Framework (WDTF) enables you to create, manage, reuse, and extend device-centric, scenario-based automated tests.
ms.assetid: 7e7660ec-1f17-4987-82c0-f62cca3a99b9
keywords:
- Windows Device Testing Framework WDK
- WDTF WDK
- scripts WDK WDTF
- Windows Device Testing Framework WDK , about WDTF
- WDTF WDK , about Windows Device Testing Framework
- test scripts WDK WDTF
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# WDTF Architecture and Overview


The Microsoft Windows Device Testing Framework (WDTF) enables you to create, manage, reuse, and extend device-centric, scenario-based automated tests.

The following illustration shows the typical WDTF model for creating scenarios at a very high-level.

![diagram illustrating the typical wdtf model for creating scenarios at a very high level ](images/wdtf-scenariomodel.gif)

Test scripts use WDTF objects through Component Object Model (COM) interfaces. You can use any programming language that supports COM automation to write these scenarios. This documentation provides code examples in VBScript, C++, and JScript.

Additionally, you can use some WDTF samples through Driver Test Manager (DTM) without any additional coding.

**Note**  DTM is part of the [Windows Hardware Certification Kit (HCK)](http://go.microsoft.com/fwlink/p/?linkid=254893) and Microsoft Windows Logo Kit (WLK). When you run WDTF-based tests in DTM, WDTF is installed for you.

 

The preceding figure shows a model for creating component-based scenarios that lets you focus on the common capabilities of a group of devices instead of individual devices. Even though many devices require special implementations for some of these interfaces, they are quite easy to add. When a scenario involves using a new feature, you can [add](extending-the-framework.md) a simple COM automation interface that wraps that feature to WDTF.

## In this section


-   [WDTF Architecture](wdtf-architecture.md)
-   [Extending the Framework](extending-the-framework.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdtf\dtf%5D:%20WDTF%20Architecture%20and%20Overview%20%20RELEASE:%20%289/13/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


