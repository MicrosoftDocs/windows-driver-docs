---
title: Performing a Hardware Functionality Scan
description: Performing a Hardware Functionality Scan
ms.assetid: 966b30b7-2f08-4611-9f4d-f85b301de414
keywords:
- OPM WDK display , HFS
- OPM WDK display , hardware functionality scan
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Performing a Hardware Functionality Scan


A display miniport driver's Hardware Functionality Scan (HFS) ensures that the miniport driver communicates with the required hardware. For more information about HFS, download the Output Content Protection document at the [Output Content Protection and Windows Vista](http://download.microsoft.com/download/5/D/6/5D6EAF2B-7DDF-476B-93DC-7CF0072878E6/output_protect.doc) website.

A display miniport driver must start performing an HFS whenever the Microsoft DirectX graphics kernel subsystem (*Dxgkrnl.sys*) calls the following driver functions:

-   [**DxgkDdiStartDevice**](https://msdn.microsoft.com/library/windows/hardware/ff560775)

-   [**DxgkDdiSetPowerState**](https://msdn.microsoft.com/library/windows/hardware/ff560764) with the graphics adapter's power state set to D0.

The HFS can be asynchronous and is not required to complete before [**DxgkDdiStartDevice**](https://msdn.microsoft.com/library/windows/hardware/ff560775) or [**DxgkDdiSetPowerState**](https://msdn.microsoft.com/library/windows/hardware/ff560764) returns. However, no [OPM DDI](https://msdn.microsoft.com/library/windows/hardware/ff568627) function can return until the HFS completes.

 

 





