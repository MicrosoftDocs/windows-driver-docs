---
title: Performing a Hardware Functionality Scan
description: Performing a Hardware Functionality Scan
keywords:
- OPM WDK display , HFS
- OPM WDK display , hardware functionality scan
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Performing a Hardware Functionality Scan


A display miniport driver's Hardware Functionality Scan (HFS) ensures that the miniport driver communicates with the required hardware. For more information about HFS, download the Output Content Protection document at the [Output Content Protection and Windows Vista](https://download.microsoft.com/download/5/D/6/5D6EAF2B-7DDF-476B-93DC-7CF0072878E6/output_protect.doc) website.

A display miniport driver must start performing an HFS whenever the Microsoft DirectX graphics kernel subsystem (*Dxgkrnl.sys*) calls the following driver functions:

-   [**DxgkDdiStartDevice**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_start_device)

-   [**DxgkDdiSetPowerState**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_set_power_state) with the graphics adapter's power state set to D0.

The HFS can be asynchronous and is not required to complete before [**DxgkDdiStartDevice**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_start_device) or [**DxgkDdiSetPowerState**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_set_power_state) returns. However, no [OPM DDI](supporting-output-protection-manager.md) function can return until the HFS completes.
