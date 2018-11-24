---
title: Specifying the Source and Target Locations for Device Files
description: Specifying the Source and Target Locations for Device Files
ms.assetid: e44961e2-e9fb-43d3-aeb9-a625021e56e6
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Specifying the Source and Target Locations for Device Files





When Windows processes copy, rename, and delete file statements in an INF file, it determines the source and target locations for the files. To determine these locations, it assesses whether the driver ships with the operating system or separately and examines various INF file sections and entries, including **SourceDisksNames**, **SourceDisksFiles**, **Include**, **Needs**, and **DestinationDirs**.

This section describes how Windows determines source and target locations, and provides guidelines to help you correctly specify these locations, and describes how to copy INF files from one location to another. It contains the following topics:

[Source Media for INF Files](source-media-for-inf-files.md)

[Target Media for INF Files](target-media-for-inf-files.md)

[Copying INF Files](copying-inf-files.md)

 

 





