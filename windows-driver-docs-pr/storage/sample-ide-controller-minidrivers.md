---
title: Sample IDE Controller Minidrivers
description: Sample IDE Controller Minidrivers
ms.assetid: 3c8779ae-30d7-4ab8-b6d8-a711f917564c
keywords:
- IDE controller minidrivers WDK storage , samples
- storage IDE controller minidrivers WDK , samples
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Sample IDE Controller Minidrivers


## <span id="ddk_sample_ide_controller_minidrivers_kg"></span><span id="DDK_SAMPLE_IDE_CONTROLLER_MINIDRIVERS_KG"></span>


This section identifies the sample IDE controller minidriver included with the Microsoft Windows Driver Kit (WDK).

The WDK includes the source code for the *pciide.sys* generic controller minidriver. See the sample code in the \\src\\storage directory of the WDK.

This sample is 64-bit compliant. It builds with Microsoft Visual C 6.0 and does not implement Plug and Play or Power Management.

The *pciide.sys* sample is binary compatible between Windows 95/98/Me and NT-based versions of the operating system, provided no Windows 95/98/Me VxD calls nor any NT-based system calls are embedded in the minidriver.

 

 




