---
title: IoSpy and IoAttack
description: IoSpy and IoAttack
ms.assetid: 4cc5bf5c-f9e4-43d4-8532-dd7813b6f2a0
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# IoSpy and IoAttack


IoSpy and IoAttack are tools that perform IOCTL and WMI fuzz tests on kernel-mode drivers. By using these tools, you can ensure that drivers' IOCTL and WMI code validate data buffers and buffer lengths correctly. By doing this, you avoid buffer overruns that can lead to system instability.

*Fuzz testing* presents a driver with random data, referred to as *fuzz*, in order to determine defects within the driver. Fuzz testing over an IOCTL or WMI interface is not new. However, most test suites are either generic *black box* fuzz tests, which only verify the external access to a driver's IOCTL or WMI interfaces, or are written to test the specific IOCTL and WMI paths within a driver.

IoSpy and IoAttack use more of a *white box* approach to fuzz testing. When a device is enabled for fuzz testing, IoSpy captures the IOCTL and WMI requests sent to the driver of the device, and records the attributes of these requests within a data file. IoAttack then reads the attributes from this data file, and uses these attributes to *fuzz*, or randomly change, the IOCTL or WMI requests in various ways before sending them to the driver. This allows further entry into the driver's buffer validation code without writing IOCTL- or WMI-specific tests.

IoSpy and IoAttack are supported on systems that run Windows Vista or later versions of the Windows operating system. These tools are included in the WDK as part of the as part of the [Device Fundamentals Tests](device-fundamentals-tests.md), see [Penetration Tests (Device Fundamentals)](coverage-tests--device-fundamentals-.md). You can select these tests from the **Add or Remove Driver tests** dialog box, under Basic\\Device Fundamentals\\Penetration\\IoSpy & Attack folder.

**Important**   IoSpy and IoAttack should be run on test systems that have been previously prepared for kernel-mode debugging.

 

This section includes the following topics:

[IoSpy](iospy.md)

[IoAttack](ioattack.md)

[How to Perform Fuzz tests with IoSpy and IoAttack](how-to-perform-fuzz-tests-with-iospy-and-ioattack.md)

 

 





