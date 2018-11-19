---
title: Installing a Segmentation Filter
description: Installing a Segmentation Filter
ms.assetid: 39f96c16-2408-460c-8aa3-08b6a6584bef
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Installing a Segmentation Filter





The segmentation filter should be installed together with the WIA driver. In order to do this, a small number of additions must be made to the driver's INF file. The following INF example shows how an existing driver INF file can be modified to include a segmentation filter.

```INF
[MyDriver.AddReg]
...
HKCR,CLSID\<UiClassId>\shellex\SegmentationFilter\<FilterClassId>
...
HKCR,CLSID\<FilterClassId>,,,"My Segmentation Filter"
HKCR,CLSID\<FilterClassId>\InProcServer32,,,%11%\Mysegfilter.dll
HKCR,CLSID\<FilterClassId>\InProcServer32,ThreadingModel,,"Both"
...
 
[MyDriver.CopyFiles]
...
Mysegfilter.dll
...
 
[SourceDisksFiles.x86]
...
Mysegfilter.dll=1
...
```

*&lt;UiClassId&gt;* is the value that the driver returns for the WIA\_DIP\_UI\_CLSID property. *&lt;FilterClassId&gt;* is the class ID of the segmentation filter implementation. *Mysegfilter.dll* is the DLL that contains the implementation of the segmentation filter.

The first entry in the device's [**INF AddReg Directive**](https://msdn.microsoft.com/library/windows/hardware/ff546320) registers the segmentation filter as an extension for the driver, the next three entries register the segmentation filter as a COM component.

If the driver uses the WIA segmentation filter provided by Microsoft , neither the device's [**INF CopyFiles Directive**](https://msdn.microsoft.com/library/windows/hardware/ff546346), [**INF SourceDisksFiles Section**](https://msdn.microsoft.com/library/windows/hardware/ff547472), nor the last three registry entries will be required. The only requirement is that the minidriver implements the WIA\_IPS\_SEGMENTATION property.

The COM **ThreadingModel** must be **Both**.

For more information about INF files, see [INF Files for WIA Devices](inf-files-for-wia-devices.md).

 

 




