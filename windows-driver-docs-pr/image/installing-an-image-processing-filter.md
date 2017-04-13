---
title: Installing an Image Processing Filter
author: windows-driver-content
description: Installing an Image Processing Filter
ms.assetid: bce6405f-0377-4e50-b898-28c6cdb962be
---

# Installing an Image Processing Filter


## <a href="" id="ddk-installing-an-image-processing-filter-si"></a>


The image processing filter is typically installed together with the WIA driver. In order to install the driver's image processing filter together with the driver, a small number of additions must be done to the driver's INF file. The following example shows an example of how an existing driver INF file can be modified to include the image processing filter.

```
[MyDriver.AddReg]
...
HKCR,CLSID\<UiClassId>\shellex\ImageProcessingFilter\<FilterClassId>
...
HKCR,CLSID\<FilterClassId>,,,"My Image Processing Filter"
HKCR,CLSID\<FilterClassId>\InProcServer32,,,%11%\Myimgfilter.dll
HKCR,CLSID\<FilterClassId>\InProcServer32,ThreadingModel,,"Apartment"
...

[MyDriver.CopyFiles]
...
Myimgfilter.dll
...

[SourceDisksFiles.x86]
...
Myimgfilter.dll=1
...
```

The *&lt;UiClassId&gt;* value is the class ID that the driver returns for the WIA\_DIP\_UI\_CLSID property, and *&lt;FilterClassId&gt;* is the class ID of the image processing filter implementation. In this example, *Myimgfilter.dll* contains the implementation of the image processing filter.

The first entry in the **AddReg** section is to register the image processing filter as an extension for the driver, and the following three entries register the image processing filter as a COM component.

As shown in the preceding example INF snippet, the recommended **ThreadingModel** value in the image processing filter's INF file is **Apartment**.

**Note**   It is possible to install a filter after the installation of the driver is complete--for example, as a value-added component.

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Installing%20an%20Image%20Processing%20Filter%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


