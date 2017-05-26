---
title: Mapping PTP Objects to WIA Items
author: windows-driver-content
description: Mapping PTP Objects to WIA Items
ms.assetid: 3ee88c09-7f36-403a-ae7b-41d08c11c52f
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Mapping PTP Objects to WIA Items


## <a href="" id="ddk-mapping-ptp-objects-to-wia-items-si"></a>


A WIA item is created for each PTP object present on a device. The driver displays the objects in the same hierarchy as they were reported in. For example, if all of the objects are reported under a folder named "XYZ", the pictures are displayed in Explorer under a folder named "XYZ".

One exception to this rule is for devices that report their FilesystemType as DCF in the StorageInfo dataset. In that case, the top level folder is called "DCIM" (if it exists), and the next level of folders down is hidden by the Microsoft PTP class WIA minidriver. All of the objects in the subfolders are promoted to the top level. File name extensions (for example, .JPG) are stripped from the object names before they are sent to WIA.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Mapping%20PTP%20Objects%20to%20WIA%20Items%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


