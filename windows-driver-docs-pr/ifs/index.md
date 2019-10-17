---
title: File Systems Driver Design Guide
description: File Systems Driver Design Guide
ms.assetid: 62DE75F7-0211-4173-AF45-84B2DDFDC95C
ms.date: 10/16/2019
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# File Systems Driver Design Guide

This section of the WDK provides conceptual information related to file systems and filter drivers (minifilters). For reference pages that describe the interfaces your driver can implement or call, see the [File System Programming Reference](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/_ifsk/).

## File Systems

File systems in Windows are implemented as file system drivers working above the storage system. Every system-supplied file system in Windows is designed to provide reliable data storage with varying features to meet the user’s requirements.

Standard file systems available in Windows include NTFS, ExFAT, UDF, and FAT32. A comparison of features for each of these file systems is shown in [File System Functionality Comparison](https://docs.microsoft.com/windows/desktop/FileIO/filesystem-functionality-comparison). Additionally, the [Resilient File System](https://docs.microsoft.com/windows-server/storage/refs/refs-overview) (ReFS), available on Windows Server 2012 and later versions, offers scalable large volume support and the ability to detect and correct data corruption on disk.

Creating a new file system driver in addition to those supplied in Windows is likely unnecessary, and requirements/specifications for new file system drivers are not predictable. To that end, this design guide does not cover file system development. That said, [sample code](#file-system-sample-code) is available as a model to write new file systems.

## File System Filter Driver Development

A file system filter driver intercepts requests targeted at a file system or another file system filter driver. By intercepting the request before it reaches its intended target, the filter driver can extend or replace functionality provided by the original target of the request. Examples of filter drivers include anti-virus filters, backup agents, and encryption products.

File system filtering services are available through the system-supplied [Filter Manager](filter-manager-and-minifilter-driver-architecture.md) in Windows. The Filter Manager provides a framework for developing filter drivers without having to manage all the complexities of file I/O. The Filter Manager simplifies the development of third-party filter drivers and solves many of the problems with the legacy filter driver model, such as the ability to control load order through an assigned altitude. A filter driver developed to the Filter Manager model is called a minifilter. Every minifilter driver has an assigned altitude, which is a unique identifier that determines where the minifilter is loaded relative to other minifilters in the I/O stack. Altitudes are allocated and managed by Microsoft.

## File System Sample Code

A number of Windows driver samples are available, including samples for file system development and file system filter driver development. See [Windows driver samples](https://docs.microsoft.com/windows-hardware/drivers/samples/) for a complete list.

## File System Filter Driver Certification

Certification information for File Systems and File System Filter Drivers is found in the [Windows Hardware Lab Kit (HLK)](https://go.microsoft.com/fwlink/p/?LinkId=733613). Tests for File Systems and File System Filter Drivers are found in the [Filter.Driver](https://docs.microsoft.com/previous-versions/windows/hardware/hck/jj124779(v=vs.85)) category of the HCK.

## File System Filter Driver Developer Resources

Along with the sample code mentioned above, the following additional resources are available:

- To request an altitude allocation from Microsoft, send an e-mail asking for an altitude assignment for your minifilter. Follow the instructions in [Minifilter Altitude Request](minifilter-altitude-request.md) to submit a request.

- To obtain an ID for a filter driver that uses reparse points follow the steps in [Reparse Point Request](reparse-point-tag-request.md).

- [OSR](https://go.microsoft.com/fwlink/p/?linkid=50692) offers a variety of resources for file system minifilter development, including seminars and community discussion forums such as the NTFDS forum.
