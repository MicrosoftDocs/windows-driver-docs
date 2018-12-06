---
title: Code Integrity Diagnostic System Log Events
description: Code Integrity Diagnostic System Log Events
ms.assetid: 4aa8db3e-033c-4f38-a813-623518e36485
keywords:
- Code Integrity WDK driver signing
- events WDK driver signing
- status information WDK driver signing
- verbose diagnostic events WDK driver signing
- audit events WDK driver signing
- logs WDK driver signing
- diagnostic log events WDK Code Integrity
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 





