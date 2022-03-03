---
title: File systems driver design guide
description: File systems driver design guide
ms.assetid: 62DE75F7-0211-4173-AF45-84B2DDFDC95C
ms.date: 09/10/2020
ms.topic: article
---

# File systems driver design guide

This section of the WDK provides conceptual information related to file systems and filter drivers. For reference pages that describe the interfaces your driver can implement or call, see the [File System Programming Reference](/windows-hardware/drivers/ddi/_ifsk/).

## File systems

File systems in Windows are implemented as file system drivers working above the storage system.

Every system-supplied file system in Windows is designed to provide reliable data storage with varying features to meet the user's requirements. Standard file systems available in Windows include NTFS, ExFAT, UDF, and FAT32. A comparison of features for each of these file systems is shown in [File System Functionality Comparison](/windows/desktop/FileIO/filesystem-functionality-comparison). Additionally, the [Resilient File System](/windows-server/storage/refs/refs-overview) (ReFS), available on Windows Server 2012 and later versions, offers scalable large volume support and the ability to detect and correct data corruption on disk.

Developing a new file system driver is almost always unnecessary, and requirements/specifications for new file system drivers are not predictable. To that end, this design guide does not cover file system development. If you do need to develop a new file system driver beyond those available in Windows, sample code is available as a model (see below).

## File system filter drivers

A file system filter driver intercepts requests targeted at a file system or another file system filter driver. By intercepting the request before it reaches its intended target, the filter driver can extend or replace functionality provided by the original target of the request. Examples of filter drivers include:

- Anti-virus filters
- Backup agents
- Encryption products

Filter driver developers use the system-supplied [Filter Manager](./filter-manager-concepts.md), which provides a framework for developing filter drivers without having to manage all the complexities of file I/O. The Filter Manager simplifies the development of third-party filter drivers and solves many of the problems with the legacy filter driver model, such as the ability to control load order through an assigned altitude.

## File system and filter sample code

A number of Windows driver samples are available, including samples for file system development and file system filter driver development. See [Windows driver samples](../samples/index.md) for a complete list.

## File system filter driver certification

Certification information for File Systems and File System Filter Drivers is found in the [Windows Hardware Lab Kit (HLK)](https://go.microsoft.com/fwlink/p/?LinkId=733613). Tests for File Systems and File System Filter Drivers are found in the [Filter.Driver](/previous-versions/windows/hardware/hck/jj124779(v=vs.85)) category of the HCK.

## Additional resources

Along with this documentation and the sample code mentioned above, [OSR](https://go.microsoft.com/fwlink/p/?linkid=50692) offers a variety of resources for file system filter development, including seminars and community discussion forums such as the NTFDS forum.