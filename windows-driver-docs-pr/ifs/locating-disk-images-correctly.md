---
title: Locating Disk Images Correctly
description: Locating Disk Images Correctly
ms.assetid: 7AC7DDDB-CDA3-4D0D-8D23-7BBA03536195
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Locating Disk Images Correctly


Disk imaging and volume management tools must be aware of where to locate the image data area on disk and the impact on user data when using a snapshot created by Volsnap. The snapshot will contain corrupted data when the disk image is located improperly.

Some imaging products make an incorrect assumption that the BIOS Parameter Block (BPB) on the disk is only 4K bytes when in fact it will always extend to the first 8K bytes of the disk. As a result, depending on cluster size of the volume, if an imaging tool locates user data in last 4K byte portion of the BPB, it can result in data loss after Volsnap snapshots are created for the volume. This is due to the fact that the imaging tool placed user data in a reserved area of the disk.

The logical sector size set for the device, such as 512 bytes or 4K bytes, does not determine the size of the BPB as it is always 8K bytes.

The following table describes the sector layout and byte offset requirements for the data area of a disk image.

BCB Reserved Area
Image Data Area
0 (512 byte sector)
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16 +
0 (byte offset)
4096
8192
 

 

 




