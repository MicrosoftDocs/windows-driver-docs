---
title: Installing an Image Processing Filter
description: Installing an Image Processing Filter
ms.assetid: bce6405f-0377-4e50-b898-28c6cdb962be
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Installing an Image Processing Filter





The image processing filter is typically installed together with the WIA driver. In order to install the driver's image processing filter together with the driver, a small number of additions must be done to the driver's INF file. The following example shows an example of how an existing driver INF file can be modified to include the image processing filter.

```INF
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

 

 

 




