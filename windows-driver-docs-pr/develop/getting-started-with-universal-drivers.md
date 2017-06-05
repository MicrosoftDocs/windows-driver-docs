---
ms.assetid: E109BD80-F9CB-4F1F-A6FD-1142E27EC6AD
title: Getting Started with Universal Windows drivers
description: Universal Windows drivers allow you to create one driver that runs on multiple device types, from embedded systems to tablets and PCs.
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Getting Started with Universal Windows drivers

Universal Windows drivers enable developers to create a single driver that runs across multiple different device types, from embedded systems to tablets and desktop PCs.

Universal Windows drivers run on Windows 10 for desktop editions (Home, Pro, and Enterprise), Windows 10 Mobile, Windows 10 IoT Core, Windows Server 2016 Technical Preview, as well as other Windows 10 editions that share a common set of interfaces.

## Introduction to Universal Windows drivers

Windows 10 provides a set of API and DDI interfaces that are common to multiple editions of Windows. This set of interfaces is called the Universal Windows Platform (UWP).

A Universal Windows driver is a kernel-mode or user-mode driver binary that installs and runs on UWP-based editions of Windows 10.

A Universal Windows driver calls only device driver interfaces (DDIs) that are part of UWP. These DDIs are marked as **Universal** on the corresponding MSDN reference pages.

A Universal Windows driver can use [KMDF](../wdf/index.md), [UMDF 2](../wdf/getting-started-with-umdf-version-2.md) or the Windows Driver Model (WDM).

## Requirements

The following are required when writing a universal driver:

*  Create a universal INF file for your driver:
    1.  Review the list of INF sections and directives that are valid in universal drivers in [Using a Universal INF File](../install/using-a-universal-inf-file.md).
    2.  Use the [InfVerif](../devtest/infverif.md) tool to verify that your driver's INF file is universal.
*  Use the ApiValidator tool to verify that the APIs your driver calls are valid for a universal driver.  See [Validating Universal Windows drivers](validating-universal-drivers.md).

## Best Practices

Use the following optional best practices:

*  If your INF performs any custom setup actions that depend on the target platform, consider separating them out into an extension INF.  You can update an extension INF independently from the primary INF to improve robustness and servicing.  See [Using an Extension INF File](../install/creating-an-extensible-inf-file.md).
*  Provide a UWP app that works with your device.  For details, see [Hardware access for Universal Windows Platform apps](../devapps/hardware-access-for-universal-windows-platform-apps.md).  In Windows 10, version 1703, the OEM needs to pre-load such an app.  Alternatively, users can manually download the app from the Windows Store.
