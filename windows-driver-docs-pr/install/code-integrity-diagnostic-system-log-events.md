---
title: Code Integrity Diagnostic System Log Events
description: Code Integrity Diagnostic System Log Events
ms.assetid: 4aa8db3e-033c-4f38-a813-623518e36485
keywords: ["Code Integrity WDK driver signing", "events WDK driver signing", "status information WDK driver signing", "verbose diagnostic events WDK driver signing", "audit events WDK driver signing", "logs WDK driver signing", "diagnostic log events WDK Code Integrity"]
---

# Code Integrity Diagnostic System Log Events


The Code Integrity component of Windows Vista and later versions of Windows enforces the requirement that kernel-mode drivers be signed in order to load. Windows Vista and later versions of Windows always generate Code Integrity operational events and optionally will generate additional system audit events and verbose diagnostic events that provide information about the status of driver signing, as follows:

-   The Code Integrity operational log includes warning events that indicate that a kernel-mode driver failed to load because the driver signature could not be verified. Signature verification can fail for the following reasons:
    -   An administrator preinstalled an unsigned driver, but Code Integrity subsequently blocked loading the unsigned driver.
    -   The driver is signed, but the signature is invalid because the driver file has been altered.
    -   The system disk device might have device errors when reading the file for the driver from bad disk sectors.
-   If system audit policy is enabled, Code Integrity generates System Audit log events that correspond to the Operational warning events that indicate that signature verification of driver file failed. System audit policy is not enabled by default.

-   If verbose logging for Code Integrity is enabled, Code Integrity logs analytic and debug events that provide information about successful verification checks that occur prior to loading kernel-mode driver files. Verbose logging for Code Integrity is not enabled by default.

You can use Event Viewer to view Code Integrity events, as described in [Viewing Code Integrity Events](viewing-code-integrity-events.md). For more information about these event log messages, see [Code Integrity Event Log Messages](code-integrity-event-log-messages.md).

For more information about how to enable the system audit log and verbose logging, see [Enabling the System Event Audit Log](enabling-the-system-event-audit-log.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Code%20Integrity%20Diagnostic%20System%20Log%20Events%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




