---
title: '[SourceDiskNames] section directives'
description: On Windows Vista and later, in-box INFs use the [SourceDisksXxx] directives. 
ms.date: 04/20/2017
---

# \[SourceDiskNames\] section directives


On Windows Vista and later, in-box INFs use the *\[SourceDisksXxx\]* directives. However, the values of these sections were changed from what had previously typically been noted in an independent hardware vendor (IHV) production driver package.

## <span id="_SourceDisksNames__and__SourceDisksFiles__section_directives"></span><span id="_sourcedisksnames__and__sourcedisksfiles__section_directives"></span><span id="_SOURCEDISKSNAMES__AND__SOURCEDISKSFILES__SECTION_DIRECTIVES"></span>*\[SourceDisksNames\]* and *\[SourceDisksFiles\]* section directives


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

## <span id="_SignatureAttributes__section_directives"></span><span id="_signatureattributes__section_directives"></span><span id="_SIGNATUREATTRIBUTES__SECTION_DIRECTIVES"></span>*\[SignatureAttributes\]* section directives


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

 

 





