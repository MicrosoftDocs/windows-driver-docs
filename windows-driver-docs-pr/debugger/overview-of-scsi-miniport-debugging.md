---
title: Overview of SCSI Miniport Debugging
description: Overview of SCSI Miniport Debugging
keywords: ["SCSI Miniport Debugging, overview"]
ms.date: 05/23/2017
---

# Overview of SCSI Miniport Debugging

## <span id="overview_of_scsi"></span><span id="OVERVIEW_OF_SCSI"></span> SCSI Verification

Small computer system interface (SCSI) debugging extensions can be found in two extension modules: Scsikd.dll and Minipkd.dll. For an overview of the most important extension commands in these modules, see [Extensions for Debugging SCSI Miniport Drivers](extensions-for-debugging-scsi-miniport-drivers.md). For a complete list, see [SCSI Miniport Extensions](../debuggercmds/scsi-miniport-extensions--scsikd-dll-and-minipkd-dll-.md).

The SCSIkd.dll extension commands can be used in any version of Windows. The Minipkd.dll extension commands can only be used in Windows XP and later versions of Windows. Commands in Minipkd.dll are only applicable to miniport drivers that work with the SCSI Port driver.

To test a SCSI miniport driver, use the SCSI Verification feature of Driver Verifier. For information about Driver Verifier, see [Driver Verifier](../devtest/driver-verifier.md) in the Windows Driver Kit (WDK) documentation.
