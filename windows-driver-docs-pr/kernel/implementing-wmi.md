---
title: Implementing WMI
description: Implementing WMI
keywords: ["WMI WDK kernel", "Windows Management Instrumentation WDK kernel", "extensions WDK WMI", "measurement data WDK WMI", "instrumentation data WDK WMI", "user-mode WMI WDK", "WMI WDK user-mode", "Windows Management Instrumentation WDK user-mode", "kernel-mode drivers WDK , WMI"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Implementing WMI





This section describes kernel-mode Windows Management Instrumentation (WMI) extensions to WDM. When you add these extensions to your kernel-mode driver, your driver becomes a WMI provider. A WMI provider makes measurement and instrumentation data available to WMI consumers, such as user-mode applications.

For more information about the user-mode WMI API, refer to [Windows Management Instrumentation](/windows/desktop/WmiSdk/wmi-start-page) in the Windows SDK.

If you are implementing a KMDF-based driver, refer to [Supporting WMI in Framework-Based Drivers](../wdf/introduction-to-wmi-for-kmdf-drivers.md).

This section includes the following information about kernel-mode WMI:

[Introduction to WMI](introduction-to-wmi.md)

[WMI Architecture](wmi-architecture.md)

[WMI Requirements for WDM Drivers](wmi-requirements-for-wdm-drivers.md)

[MOF Syntax for WMI Data and Event Blocks](mof-syntax-for-wmi-data-and-event-blocks.md)

[Designing WMI Data and Event Blocks](designing-wmi-data-and-event-blocks.md)

[Publishing a WMI Schema](publishing-a-wmi-schema.md)

[Registering as a WMI Data Provider](registering-as-a-wmi-data-provider.md)

[Handling WMI Requests](handling-wmi-requests.md)

[Sending WMI Events](sending-wmi-events.md)

[WMI Property Sheets](wmi-property-sheets.md)

[Using wmimofck.exe](using-wmimofck-exe.md)

[WMI Event Tracing](wmi-event-tracing.md)

[Testing and Troubleshooting WMI Driver Support](general-techniques-for-testing-wmi-driver-support.md)

