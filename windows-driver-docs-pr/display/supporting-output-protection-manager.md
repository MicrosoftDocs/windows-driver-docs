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
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supporting Output Protection Manager


The [Output Protection Manager (OPM) device driver interface (DDI)](https://msdn.microsoft.com/library/windows/hardware/ff568627) enables the copy protection of video signals that are output by various connectors of the graphics adapter. To learn more about how Windows Vista protects the content that graphics adapters output, download the Output Content Protection document at the [Output Content Protection and Windows Vista](http://download.microsoft.com/download/5/D/6/5D6EAF2B-7DDF-476B-93DC-7CF0072878E6/output_protect.doc) website.

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

 

 





