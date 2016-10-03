---
title: WHEA Changes for Windows Server 2008 and Windows Vista SP1
author: windows-driver-content
description: WHEA Changes for Windows Server 2008 and Windows Vista SP1
MS-HAID:
- 'whea\_cefe16bf-1089-406e-af6e-86fd89138679.xml'
- 'whea.whea\_changes\_for\_windows\_server\_2008\_and\_windows\_vista\_sp1'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: fd66ee01-e262-45c2-bced-549192b0eca3
keywords: ["Windows Hardware Error Architecture WDK , Windows Server 2008 changes", "Windows Hardware Error Architecture WDK , Windows Vista SP1 changes", "WHEA WDK , Windows Server 2008 changes", "WHEA WDK , Windows Vista SP1 changes", "Windows Server 2008 WDK WHEA", "Windows Server 2008 WDK WHEA , WHEA changes", "Windows Vista SP1 WDK WHEA", "Windows Vista SP1 WDK WHEA , WHEA changes"]
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwhea\whea%5D:%20WHEA%20Changes%20for%20Windows%20Server%202008%20and%20Windows%20Vista%20SP1%20%20RELEASE:%20%289/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


