---
title: Specifying the Source and Target Locations for Device Files
description: Specifying the Source and Target Locations for Device Files
ms.assetid: e44961e2-e9fb-43d3-aeb9-a625021e56e6
---

# Specifying the Source and Target Locations for Device Files


## <a href="" id="ddk-specifying-the-source-and-target-locations-for-device-files-dg"></a>


When Windows processes copy, rename, and delete file statements in an INF file, it determines the source and target locations for the files. To determine these locations, it assesses whether the driver ships with the operating system or separately and examines various INF file sections and entries, including **SourceDisksNames**, **SourceDisksFiles**, **Include**, **Needs**, and **DestinationDirs**.

This section describes how Windows determines source and target locations, and provides guidelines to help you correctly specify these locations, and describes how to copy INF files from one location to another. It contains the following topics:

[Source Media for INF Files](source-media-for-inf-files.md)

[Target Media for INF Files](target-media-for-inf-files.md)

[Copying INF Files](copying-inf-files.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Specifying%20the%20Source%20and%20Target%20Locations%20for%20Device%20Files%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




