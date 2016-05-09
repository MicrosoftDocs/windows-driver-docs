---
title: Locating Disk Images Correctly
description: Locating Disk Images Correctly
ms.assetid: 7AC7DDDB-CDA3-4D0D-8D23-7BBA03536195
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
 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Locating%20Disk%20Images%20Correctly%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




