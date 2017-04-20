---
title: '\ SourceDiskNames\ section directives'
description: On Windows Vista and later, in-box INFs use the \ SourceDisksXxx\ directives. However, the values of these sections were changed from what had previously typically been noted in an independent hardware vendor (IHV) production driver package.
ms.assetid: 0AC01548-3E53-41ED-9C7E-E33FC2DD14FD
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# \[SourceDiskNames\] section directives


On Windows Vista and later, in-box INFs use the *\[SourceDisksXxx\]* directives. However, the values of these sections were changed from what had previously typically been noted in an independent hardware vendor (IHV) production driver package.

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


On Windows Vista and later, inbox INFs use the *\[SignatureAttributes\]* directives.

There is no need to reference the miniport (.sys) file.

For example:

``` syntax
[SignatureAttributes]
IHVUMD1.dll=SignatureAttributes.PETrust
IHVUMD2.dll=SignatureAttributes.PETrust

[SignatureAttributes.PETrust]
PETrust=true
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20[SourceDiskNames]%20section%20directives%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




