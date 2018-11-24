---
title: Installed display drivers directive
description: The installed display drivers directive is a software device setting that gives the proper name for the UMD that is installed as part of the driver package.
ms.assetid: 7104129C-57B1-4F37-B1E0-D86529C9866E
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 





