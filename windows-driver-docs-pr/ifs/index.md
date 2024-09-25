---
title: File Systems and Filter Driver Design Guide
description: File systems driver design guide
ms.date: 09/25/2024
keywords:
- file system filter driver design, Windows, WDK
- file system information, Windows, WDK
ms.topic: article
---

# File Systems and Filter Driver Design Guide

The File Systems and Filter Driver Design Guide describes how to design and implement a file system filter driver for Windows. It also provides driver-relevant information about Windows file systems. See the [programming reference](/windows-hardware/drivers/ddi/_ifsk/) for reference pages.

## File systems

Windows file systems are implemented as file system drivers working above the storage system.

Every system-supplied file system in Windows is designed to provide reliable data storage with varying features to meet the user's requirements.

* Standard file systems available in Windows include NTFS, ExFAT, UDF, and FAT32. A comparison of features for each of these file systems is shown in [File System Functionality Comparison](/windows/desktop/FileIO/filesystem-functionality-comparison).
* The [Resilient File System](/windows-server/storage/refs/refs-overview) (ReFS) is available on Windows Server 2012 and later versions. ReFS offers scalable large volume support and the ability to detect and correct data corruption on disk.

Developing a new file system driver is almost always unnecessary, and requirements/specifications for new file system drivers aren't predictable. To that end, this design guide doesn't cover file system development. If you do need to develop a new file system driver beyond those available in Windows, sample code is available as a model.

## File system filter drivers

A file system filter driver, or minifilter, intercepts requests targeted at a file system or another file system filter driver. By intercepting the request before it reaches its intended target, a minifilter can extend or replace functionality provided by the original target of the request. Examples of filter drivers include:

* Anti-virus filters
* Backup agents
* Encryption products

Filter driver developers use the [Filter Manager](./filter-manager-concepts.md) (*FltMgr.sys*). This system-supplied module provides developers a framework to implement filter drivers without having to manage all the complexities of file I/O. *FltMgr* simplifies filter driver development and solves many of the problems with the legacy filter driver model, such as *FltMgr* having the ability to control load order through an assigned altitude.

## File system and filter sample code

Microsoft provides several [file system filter driver samples](../samples/file-system-driver-samples.md). Anyone who decides to develop their own file system can file system driver sample code as well.

## File system filter driver certification

Certification information for File Systems and File System Filter Drivers is found in the [Windows Hardware Lab Kit (HLK)](/windows-hardware/test/hlk/). Tests for file systems and filter drivers are found under [Filter.Driver](/windows-hardware/test/hlk/testref/filter-driver).

## Other resources

[OSR](https://community.osr.com/) offers various training resources for file system filter developers. They also host community discussion forums such as the [Windows File Systems and Minifilters Devs Interest List](https://community.osr.com/c/ntfsd/6), where you can ask questions and communicate with filter driver developers from around the world.
