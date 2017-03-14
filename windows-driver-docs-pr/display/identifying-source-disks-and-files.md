---
title: Identifying Source Disks and Files
description: Identifying Source Disks and Files
ms.assetid: 0eb8fe7f-1e44-4f3d-8567-31a2cd659805
keywords: ["INF files WDK display , identifying source disks or files", "source disks WDK display", "source files WDK display", "identifying display source disks or files"]
---

# Identifying Source Disks and Files


You must specify all in-box display drivers in the **SourceDisksNames** and **SourceDisksFiles** sections. The following example shows how to identify the CD-ROM discs and the names of the source files that are contained on the disks. The source files are transferred to the target computer during installation.

```
[SourceDisksNames]
3426=windows cd

[SourceDisksFiles]
DisplayMiniportDriverName.sys  = 3426
UserModeDriverName1.dll  = 3426
UserModeDriverName2.dll  = 3426
```

For more information about the **SourceDisksNames** and **SourceDisksFiles** sections, see [**INF SourceDisksNames Section**](https://msdn.microsoft.com/library/windows/hardware/ff547478) and [**INF SourceDisksFiles Section**](https://msdn.microsoft.com/library/windows/hardware/ff547472).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Identifying%20Source%20Disks%20and%20Files%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




