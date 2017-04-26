---
title: Installed display drivers directive
description: The installed display drivers directive is a software device setting that gives the proper name for the UMD that is installed as part of the driver package.
ms.assetid: 7104129C-57B1-4F37-B1E0-D86529C9866E
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Installed display drivers directive


The installed display drivers directive is a software device setting that gives the proper name for the UMD that is installed as part of the driver package.

``` syntax
HKR,, InstalledDisplayDrivers,              %REG_MULTI_SZ%, 
UserModeDriverName1, UserModeDriverName2, UserModeDriverNameWow1, UserModeDriverNameWow2
```

For example:

``` syntax
For example:
X86:
HKR,, InstalledDisplayDrivers,              %REG_MULTI_SZ%, r200umd

X64:
HKR,, InstalledDisplayDrivers,              %REG_MULTI_SZ%, r200umd, r200umdva, r200umd64, r200umd64va
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Installed%20display%20drivers%20directive%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




