---
title: Target Media for INF Files
description: Target Media for INF Files
ms.assetid: f1aaea38-e500-40a9-89c1-9c4447054fb1
keywords: ["INF files WDK device installations , target media", "target media WDK INF files", "locations WDK INF files", "media WDK INF files"]
---

# Target Media for INF Files


## <a href="" id="ddk-target-media-for-infs-dg"></a>


An INF file specifies the target location for device files that have a [**DestinationDirs**](inf-destinationdirs-section.md) section. This section should always be specified in the same INF file as the section with the copy, rename, or delete statements.

A **DestinationDirs** section should include a **DefaultDestDir** entry.

If an INF has copy, rename, or delete sections but no **DestinationDirs** section and the INF includes other INF files, Windows searches the included INF files for target location information. However, the order in which Windows searches the included files is not predictable. Therefore, there is a risk that Windows will, for example, copy files to a location not intended by the INF writer. To avoid such confusion, always specify a **DestinationDirs** section in an INF that contains copy, rename, or delete sections. The **DestinationDirs** section should include at least a **DefaultDestDir** entry and can list sections in the INF that copy, rename, or delete files.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Target%20Media%20for%20INF%20Files%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




