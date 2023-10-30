---
title: Kernel Mode Performance Monitoring
description: Kernel Mode Performance Monitoring
ms.date: 08/24/2023
---

# Kernel Mode Performance Monitoring

The Microsoft Windows operating system allows system components and third parties to expose performance metrics in a standard way by using [performance counters](/windows/win32/perfctrs/performance-counters-portal).

For information on adding a new performance counter provider to your code, see [Using Kernel Mode Performance Counters](using-kernel-mode-performance-counters.md).

## About Kernel Mode Performance Counters

Performance counters are values published by a component to allow system administrators and developers to understand the status of the component. For example, a networking component might publish the number of packets sent over a network connection.

The Windows Performance Counter system allows various different components to publish performance counters through a consistent and discoverable interface. Windows Performance Counter publishers are consumed through GUI tools (e.g. perfmon), command-line tools (e.g. typeperf), and APIs (e.g. PDH and WMI). For more information, see [Performance Counters](/windows/win32/perfctrs/performance-counters-portal). A component that publishes performance counters is called a performance counter provider.

Performance counter values can be published in three ways.

1. A user-mode component (e.g. a service) can publish counters via the [PerfLib APIs](/windows/win32/perfctrs/providing-counter-data-using-version-2-0).

2. A kernel-mode component (e.g. a driver) can publish counters via the [PCW APIs](using-kernel-mode-performance-counters.md).

3. An in-process [performance extension DLL](/windows/win32/perfctrs/providing-counter-data-using-a-performance-dll) can perform custom collection. Note that in-process performance extension DLLs are **deprecated and should not be used** by new components due to performance and reliability issues.

Performance Counters for Windows (PCW) keeps track of countersets provided by kernel-mode components. It routes consumer data collection requests to the appropriate kernel-mode component and returns the requested data to the user-mode consumer.

## Kernel Mode Performance Counter Provider Functions

Kernel Mode Performance Counter makes use of the following DDIs:

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

## See also

[Using Kernel Mode Performance Counters](using-kernel-mode-performance-counters.md)

[Win32 Performance Counters](/windows/win32/perfctrs/performance-counters-portal)
