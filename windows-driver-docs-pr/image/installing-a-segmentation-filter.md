---
title: Installing a Segmentation Filter
author: windows-driver-content
description: Installing a Segmentation Filter
ms.assetid: 39f96c16-2408-460c-8aa3-08b6a6584bef
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Installing a Segmentation Filter


## <a href="" id="ddk-installing-a-segmentation-filter-si"></a>


The segmentation filter should be installed together with the WIA driver. In order to do this, a small number of additions must be made to the driver's INF file. The following INF example shows how an existing driver INF file can be modified to include a segmentation filter.

```
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Installing%20a%20Segmentation%20Filter%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


