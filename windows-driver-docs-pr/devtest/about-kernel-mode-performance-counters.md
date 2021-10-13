---
title: About Kernel Mode Performance Counters
description: About Kernel Mode Performance Counters
ms.date: 08/05/2020
ms.localizationpriority: medium
---

# About Kernel Mode Performance Counters

Performance counters are values published by a component to allow system administrators and developers to understand the status of the component. For example, a networking component might publish the number of packets sent over a network connection.

The Windows Performance Counter system allows various different components to publish performance counters through a consistent and discoverable interface. Windows Performance Counter publishers are consumed through GUI tools (e.g. perfmon), command-line tools (e.g. typeperf), and APIs (e.g. PDH and WMI). For more information, see [Performance Counters](/windows/win32/perfctrs/performance-counters-portal). A component that publishes performance counters is called a performance counter provider.

Performance counter values can be published in three ways.

1. A user-mode component (e.g. a service) can publish counters via the [PerfLib APIs](/windows/win32/perfctrs/providing-counter-data-using-version-2-0).
2. A kernel-mode component (e.g. a driver) can publish counters via the [PCW APIs](using-kernel-mode-performance-counters.md).
3. An in-process [performance extension DLL](/windows/win32/perfctrs/providing-counter-data-using-a-performance-dll) can perform custom collection. Note that in-process performance extension DLLs are **deprecated and should not be used** by new components due to performance and reliability issues.

Performance Counters for Windows (PCW) keeps track of countersets provided by kernel-mode components. It routes consumer data collection requests to the appropriate kernel-mode component and returns the requested data to the user-mode consumer.

## Related topics

[Using Kernel Mode Performance Counters](using-kernel-mode-performance-counters.md)

[Performance Counters Portal](/windows/win32/perfctrs/performance-counters-portal)
