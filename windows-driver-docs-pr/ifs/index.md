---
title: File System and File System Filter Drivers
description: Introduces file system drivers and file system filter drivers.
ms.date: 04/30/2025
keywords:
- file system filter drivers , Windows , WDK
- file system drivers , Windows , WDK
ms.topic: concept-article
---

# File System and File System Filter Drivers

The documentation under this node contains developer-related information for the following types of drivers:

* [File system drivers](about-file-system-drivers.md). Developing a new file system is almost always unnecessary and requirements/specifications for new file system drivers aren't predictable. For this reason, the documentation is limited to [INF creation](creating-an-inf-file-for-a-file-system-driver.md) and [sample code](file-system-sample-code.md).

* [File system (FS) filter drivers](about-file-system-filter-drivers.md), also known as *minifilter drivers* or *minifilters*.

## Other resources

* For DDI reference pages, see the [programming reference](/windows-hardware/drivers/ddi/_ifsk/).

* For driver certification information, see the [Windows Hardware Lab Kit (HLK)](/windows-hardware/test/hlk/). Tests for file systems and minifilter drivers are found under [Filter.Driver](/windows-hardware/test/hlk/testref/filter-driver).

* For community support, [OSR](https://community.osr.com/) offers various training resources for file system filter developers. They also host community discussion forums such as the [Windows File Systems and Minifilters Devs Interest List](https://community.osr.com/c/ntfsd/6). These forums enable you to ask questions and communicate with filter driver developers from around the world.
