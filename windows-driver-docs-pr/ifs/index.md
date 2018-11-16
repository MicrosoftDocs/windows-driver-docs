---
title: Introduction to File System Filters
description: The file systems in Windows are implemented as file system drivers working above the storage system.
ms.assetid: 62DE75F7-0211-4173-AF45-84B2DDFDC95C
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Installable file systems driver design guide


The file systems in Windows are implemented as file system drivers working above the storage system. Each of the file systems in Windows are designed to provide reliable data storage with varying features to meet the user’s requirements. A comparison of features for each of the standard file systems in Windows is shown in [File System Functionality Comparison](https://msdn.microsoft.com/library/windows/desktop/ee681827). New for Windows Server 2012 is ReFS. ReFS is a file system with scalable large volume support and the ability detect and correct data corruption on disk.

Creating a new file system driver in addition to those supplied in Windows is likely unnecessary. File Systems and File System Filter Drivers can provide any customized behavior required to modify the operation of existing file systems.

## <span id="File_System_Filter_Driver_Development"></span><span id="file_system_filter_driver_development"></span><span id="FILE_SYSTEM_FILTER_DRIVER_DEVELOPMENT"></span>File System Filter Driver Development


A file system filter driver intercepts requests targeted at a file system or another file system filter driver. By intercepting the request before it reaches its intended target, the filter driver can extend or replace functionality provided by the original target of the request. Examples of File Systems and File System Filter Drivers include anti-virus filters, backup agents, and encryption products.

File system filtering services are available through the [Filter Manager](filter-manager-and-minifilter-driver-architecture.md) in Windows. The Filter Manager provides a framework for developing File Systems and File System Filter Drivers without having to manage all the complexities of file I/O. The Filter Manager simplifies the development of third-party filter drivers and solves many of the problems with the existing legacy filter driver model, such as the ability to control load order through an assigned altitude. A filter driver developed to the Filter Manager model is called a minifilter. Every minifilter driver has an assigned altitude, which is a unique identifier that determines where the minifilter is loaded relative to other minifilters in the I/O stack. Altitudes are allocated and managed by Microsoft.

## <span id="File_System_Filter_Driver_Certification"></span><span id="file_system_filter_driver_certification"></span><span id="FILE_SYSTEM_FILTER_DRIVER_CERTIFICATION"></span>File System Filter Driver Certification


Certification information for File Systems and File System Filter Drivers is found in the [Windows Hardware Certification Kit (HCK)](https://go.microsoft.com/fwlink/p/?LinkId=733613). Tests for File Systems and File System Filter Drivers are found in the [Filter.Driver](https://msdn.microsoft.com/library/windows/hardware/jj124779) category of the HCK.

## <span id="File_System_Filter_Driver_Developer_Resources"></span><span id="file_system_filter_driver_developer_resources"></span><span id="FILE_SYSTEM_FILTER_DRIVER_DEVELOPER_RESOURCES"></span>File System Filter Driver Developer Resources


To request an altitude allocation from Microsoft, send an e-mail asking for an altitude assignment for your minifilter. Follow the instructions in [Minifilter Altitude Request](minifilter-altitude-request.md) to submit a request.

To obtain an ID for a filter driver that uses reparse points follow the steps in [Reparse Point Request](reparse-point-tag-request.md).

You can subscribe to the NTFSD newsgroup for details about developing file systems and filter drivers. The group is found at [NT File System Drivers Newsgroup](http://go.microsoft.com/fwlink/p/?LinkId=620898).

OSR's "Developing File Systems for Windows" seminar explores developing file systems and File Systems and File System Filter Drivers. See [Training for IFS Developers](http://go.microsoft.com/fwlink/p/?linkid=50692).



## In this section
This design guide includes the following sections:  

* [File System Drivers](file-system-drivers.md)  
* [File System Filter Drivers](file-system-filter-drivers.md)  
* [File System Minifilter Drivers](file-system-minifilter-drivers.md)  
* [Network Redirector Drivers](network-redirector-drivers.md)  
* [Security Considerations for File Systems](security-considerations-for-file-systems.md)  
* [Miscellaneous Information](miscellaneous-information.md)



