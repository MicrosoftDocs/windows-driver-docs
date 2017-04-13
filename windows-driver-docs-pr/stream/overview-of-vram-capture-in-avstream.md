---
title: Overview of VRAM Capture in AVStream
author: windows-driver-content
description: Overview of VRAM Capture in AVStream
ms.assetid: b5fd026f-75e3-49e0-a39e-4883dd6cacf2
keywords: ["VRAM capture WDK AVStream , about VRAM capture"]
---

# Overview of VRAM Capture in AVStream


To support capture to VRAM, the vendor adds functionality within the Windows Vista display driver stack. Specifically, the vendor supplies a pin-centric AVStream minidriver that supports specific KS properties. While it is possible to include the AVStream functionality within the display miniport driver, Microsoft recommends that the minidriver instead be subordinate to the display miniport driver. To view a diagram that explains how the display miniport driver fits into the Windows Vista display driver stack, go to the Windows Vista Display Driver Model Architecture topic.

This documentation describes how to implement such a separate stand-alone capture minidriver.

A capture driver can send data to any DXVA2-aware downstream filter, for example, a renderer or an encoder.

The following diagram shows how a VRAM capture-enabled AVStream minidriver interacts with the display miniport driver and with other modules.

![diagram illustrating how a vram capture-enabled avstream minidriver interacts with the display miniport driver and other modules](images/lddmcapturearchitectureoverview.gif)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Overview%20of%20VRAM%20Capture%20in%20AVStream%20%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


