---
title: Kernel Mode Performance Monitoring
description: Kernel Mode Performance Monitoring
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Kernel Mode Performance Monitoring

The Microsoft Windows operating system allows system components and third parties to expose performance metrics in a standard way by using [performance counters](/windows/win32/perfctrs/performance-counters-portal).

The section includes the following topics:

[About Kernel Mode Performance Counters](about-kernel-mode-performance-counters.md)

[Using Kernel Mode Performance Counters](using-kernel-mode-performance-counters.md)

Kernel Mode Performance Counter makes use of the following DDIs:

## Kernel Mode Performance Counter Provider Functions

[PcwAddInstance](/windows-hardware/drivers/ddi/wdm/nf-wdm-pcwaddinstance)

[PcwCallback](/windows-hardware/drivers/ddi/wdm/nc-wdm-pcw_callback)

[PcwCloseInstance](/windows-hardware/drivers/ddi/wdm/nf-wdm-pcwcloseinstance)

[PcwCreateInstance](/windows-hardware/drivers/ddi/wdm/nf-wdm-pcwcreateinstance)

[PcwRegister](/windows-hardware/drivers/ddi/wdm/nf-wdm-pcwregister)

[PcwUnregister](/windows-hardware/drivers/ddi/wdm/nf-wdm-pcwunregister)

## Kernel Mode Performance Counter Structures and Enumerations

[PCW_CALLBACK_INFORMATION](/windows-hardware/drivers/ddi/wdm/ns-wdm-_pcw_callback_information)

[PCW_CALLBACK_TYPE](/windows-hardware/drivers/ddi/wdm/ne-wdm-_pcw_callback_type)

[PCW_COUNTER_DESCRIPTOR](/windows-hardware/drivers/ddi/wdm/ns-wdm-_pcw_counter_descriptor)

[PCW_COUNTER_INFORMATION](/windows-hardware/drivers/ddi/wdm/ns-wdm-_pcw_counter_information)

[PCW_DATA](/windows-hardware/drivers/ddi/wdm/ns-wdm-_pcw_counter_information)

[PCW_MASK_INFORMATION](/windows-hardware/drivers/ddi/wdm/ns-wdm-_pcw_mask_information)

[PCW_REGISTRATION_INFORMATION](/windows-hardware/drivers/ddi/wdm/ns-wdm-_pcw_registration_information)
