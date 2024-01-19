---
title: '[SourceDiskNames] Section Directives'
description: On Windows Vista and later, in-box INFs use the [SourceDisksXxx] directives. 
ms.date: 01/12/2024
---

# \[SourceDiskNames\] section directives

On Windows Vista and later, in-box INFs use the *\[SourceDisksXxx\]* directives. However, the values of these sections were changed from what had previously typically been noted in an independent hardware vendor (IHV) production driver package.

## *\[SourceDisksNames\]* and *\[SourceDisksFiles\]* section directives

For example, for IHV production drivers:

``` syntax
For example, IHV production drivers:
[SourceDisksNames]
1 = %DiskID1%

[SourceDisksFiles]
r200.sys    = 1
r200umd.dll = 1
```

This is the Windows inbox INF requirement:

``` syntax
[SourceDisksNames]
3426=windows cd

[SourceDisksFiles]
IHVKDM.sys      = 3426
IHVUMD.dll      = 3426
IHVVID.dll      = 3426
```

## *\[SignatureAttributes\]* section directives

On Windows Vista and later, inbox INFs use the *\[SignatureAttributes\]* directives.

There is no need to reference the miniport (.sys) file.

For example:

``` syntax
[SignatureAttributes]
IHVUMD1.dll=SignatureAttributes.PETrust
IHVUMD2.dll=SignatureAttributes.PETrust

[SignatureAttributes.PETrust]
PETrust=true
```
