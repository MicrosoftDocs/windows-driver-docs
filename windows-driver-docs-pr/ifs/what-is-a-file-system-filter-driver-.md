---
title: What Is a File System Filter Driver
description: What Is a File System Filter Driver
ms.assetid: 4bff8ad6-624a-429d-b9ec-3f96c3c7c99d
keywords:
- filter drivers WDK file system , about file system filter drivers
- file system filter drivers WDK , about file system filter drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# What Is a File System Filter Driver?


## <span id="ddk_what_is_a__file_system_filter_driver_if"></span><span id="DDK_WHAT_IS_A__FILE_SYSTEM_FILTER_DRIVER_IF"></span>


A *file system filter driver* is an optional driver that adds value to or modifies the behavior of a file system. A file system filter driver is a kernel-mode component that runs as part of the Windows executive.

A file system filter driver can filter I/O operations for one or more file systems or file system volumes. Depending on the nature of the driver, *filter* can mean *log*, *observe*, *modify*, or even *prevent*. Typical applications for file system filter drivers include antivirus utilities, encryption programs, and hierarchical storage management systems.

 

 




