---
title: WHEA Changes for Windows Server 2008 and Windows Vista SP1
description: WHEA Changes for Windows Server 2008 and Windows Vista SP1
ms.assetid: fd66ee01-e262-45c2-bced-549192b0eca3
keywords:
- Windows Hardware Error Architecture WDK , Windows Server 2008 changes
- Windows Hardware Error Architecture WDK , Windows Vista SP1 changes
- WHEA WDK , Windows Server 2008 changes
- WHEA WDK , Windows Vista SP1 changes
- Windows Server 2008 WDK WHEA
- Windows Server 2008 WDK WHEA , WHEA changes
- Windows Vista SP1 WDK WHEA
- Windows Vista SP1 WDK WHEA , WHEA changes
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WHEA Changes for Windows Server 2008 and Windows Vista SP1


Starting with Windows Server 2008 and Windows Vista SP1, the following changes have been made to Windows Hardware Error Architecture (WHEA):

-   Vendors of hardware platforms can supplement the default WHEA platform-specific hardware error driver (PSHED) functionality by providing PSHED plug-ins that use platform-specific capabilities. A PSHED plug-in is a specialized Windows device driver that implements a callback interface that is called by the PSHED. The purpose of a PSHED plug-in is to augment or override the default behavior of the PSHED that is provided by Microsoft.

    For more information about PSHED plug-ins, see [Platform-Specific Hardware Error Driver Plug-Ins](platform-specific-hardware-error-driver-plug-ins2.md).

-   WHEA supports an error record persistence mechanism that allows [error records](error-records.md) to be stored in nonvolatile storage. As a result, error records are retained if the operating system must restart because of a fatal hardware error condition. This mechanism preserves the error records so that none of the captured error data related to the fatal hardware error condition is lost when the system is restarted.

    For more information about error record persistence, see [Error Record Persistence Mechanism](error-record-persistence-mechanism.md).

-   WHEA raises an Event Tracing for Windows (ETW) event whenever a hardware error occurs. Starting with Windows Server 2008, the WHEA hardware error events and the data templates that describe those hardware error events are different from the events and templates that are supported on Windows Vista.

    For more information about ETW support within WHEA, see [Hardware Error Events](https://msdn.microsoft.com/library/windows/hardware/ff559387).

-   [WHEA hardware error event processing applications](whea-hardware-error-event-processing-applications.md) can retrieve hardware error events from the system event log by querying for any events that were logged by WHEA. However, starting with Windows Server 2008, the name of the provider that logs the WHEA hardware error events has changed. These applications have to access error events through the new provider. For more information, see [Querying the System Event Log for Hardware Error Events](querying-the-system-event-log-for-hardware-error-events.md).

-   In addition to WHEA hardware error event processing applications, [WHEA management applications](whea-management-applications.md) are now supported in Windows Server 2008, Windows Vista SP1 and later versions of Windows. Through a WMI interface that is provided by WHEA, user-mode applications can perform WHEA management operations, such as enabling or disabling an error source and injecting hardware errors for testing purposes.

 

 




