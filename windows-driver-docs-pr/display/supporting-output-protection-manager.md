---
title: Supporting Output Protection Manager
description: Supporting Output Protection Manager
ms.assetid: 2c138dbd-55ca-4c71-8c8b-b2efd1ca80f2
keywords:
- COPP WDK DirectX VA , Output Protection Manager
- Output Protection Manager WDK display
- OPM WDK display
- copy protection WDK display
- video copy protection WDK display
- protected video WDK display
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Supporting Output Protection Manager


The [Output Protection Manager (OPM) device driver interface (DDI)](https://msdn.microsoft.com/library/windows/hardware/ff568627) enables the copy protection of video signals that are output by various connectors of the graphics adapter. To learn more about how Windows Vista protects the content that graphics adapters output, download the Output Content Protection document at the [Output Content Protection and Windows Vista](http://go.microsoft.com/fwlink/p/?linkid=204788) website.

OPM is the successor to the [Certified Output Protection Protocol (COPP)](copp-processing.md) that the [Windows 2000 display driver model](windows-2000-display-driver-model-design-guide.md) provides. OPM supports all of COPP's features. For information about COPP's features, see [Introduction to COPP](introduction-to-copp.md). OPM also supports new features.

The [OPM DDI](https://msdn.microsoft.com/library/windows/hardware/ff568627) is semantically similar to the [COPP DDI](https://msdn.microsoft.com/library/windows/hardware/ff540449) because OPM is essentially COPP 1.1 for the Windows Vista display driver model. However, the OPM DDI is much simpler than the COPP DDI because the OPM DDI consists of a set of functions while the COPP DDI is mapped through the DirectDraw and DirectX Video Acceleration (VA) DDI.

If a display miniport driver supports the passing of protected commands, information, and status between applications and the driver, the Microsoft DirectX graphics kernel subsystem (*Dxgkrnl.sys*) can successfully open the driver's OPM DDI.

The following topics describe the new features of OPM and how to support and use the OPM DDI:

[OPM Terminology](opm-terminology.md)

[OPM Features](opm-features.md)

[Performing a Hardware Functionality Scan](performing-a-hardware-functionality-scan.md)

[Retrieving the OPM DDI](retrieving-the-opm-ddi.md)

[Using the OPM DDI](using-the-opm-ddi.md)

[Handling Protection Levels with OPM](handling-protection-levels-with-opm.md)

[Handling the Loss of a Display Device](handling-the-loss-of-a-display-device.md)

[Retrieving Information About a Protected Output](retrieving-information-about-a-protected-output.md)

[Retrieving COPP-Compatible Information about a Protected Output](retrieving-copp-compatible-information-about-a-protected-output.md)

[Configuring a Protected Output](configuring-a-protected-output.md)

[Reporting Status of a Protected Output](reporting-status-of-a-protected-output.md)

[Implementation Tips and Requirements for OPM](implementation-tips-and-requirements-for-opm.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Supporting%20Output%20Protection%20Manager%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




