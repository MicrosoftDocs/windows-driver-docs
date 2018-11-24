---
ms.assetid: 602bf657-7ae4-4610-b4c0-9d7260c42063
title: Distributing a driver package
description: Distributing a driver package
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Distributing a driver package

## <span id="ddk_distributing_a_driver_pg"></span><span id="DDK_DISTRIBUTING_A_DRIVER_PG"></span>


This topic describes how to securely distribute your driver package. This information includes how to distribute a driver package through the Microsoft Windows Update program. This topic also describes how Windows protects system files.

## <span id="ddk_windows_update_pg"></span><span id="DDK_WINDOWS_UPDATE_PG"></span>Windows Update


* [Driver packages](https://msdn.microsoft.com/Library/Windows/Hardware/Ff544840) that pass [Windows Hardware Certification Kit (HCK)](http://go.microsoft.com/fwlink/p/?linkid=254893) testing can be digitally-signed by WHQL. If your driver package is digitally-signed by WHQL, it can be distributed through the Windows Update program or other Microsoft-supported distribution mechanisms.

Obtaining a WHQL release signature is part of the [Windows Hardware Certification Kit (HCK)](http://go.microsoft.com/fwlink/p/?linkid=254893). A WHQL release signature consists of a digitally-signed [catalog file](https://msdn.microsoft.com/Library/Windows/Hardware/Ff537872). The digital signature does not change the driver binary files or the INF file that you submit for testing.

You can distribute a driver package through the Windows Update program if the driver package:

-   Passes the WHQL test program and receives a [WHQL release signature](https://msdn.microsoft.com/Library/Windows/Hardware/Ff553976).

-   Qualifies for the Windows Certification Program.

-   Meets additional requirements that ensure that Windows Update can determine the correct driver package for the user's device, can legally distribute it, and can automatically download it.

Because the requirements of the Windows Update program are frequently updated, you should regularly check the [Windows Update driver publishing](http://go.microsoft.com/fwlink/p/?linkid=8712) Web site.

## <span id="ddk_protection_for_system_files_pg"></span><span id="DDK_PROTECTION_FOR_SYSTEM_FILES_PG"></span>Protection for System Files


Windows File Protection (WFP) protects Windows operating system files from being replaced with unknown or incompatible versions.

WFP prevents programs from replacing critical Windows system files. Programs must not overwrite these files because they are used by the operating system and by other programs. Protecting these files prevents problems with programs and the operating system.

The types of system files that WFP protects include .sys, .exe, .ocx, and .dll files that ship "in the box" with the operating system.

During WHQL testing, the [**Signability**](https://msdn.microsoft.com/Library/Windows/Hardware/Ff547089) program checks a driver's INF file to ensure that it does not attempt to replace system files. A driver package that attempts to replace system files cannot receive a digital signature. A driver package can, however, contain updated versions of files that the vendor supplied to Microsoft to ship with Windows 2000 or later versions of the operating system.

For additional information about Windows File Protection, see the Windows SDK documentation.

 

 





