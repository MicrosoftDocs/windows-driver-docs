---
title: Lists
author: windows-driver-content
description: Lists
ms.assetid: 69b928fa-8348-437a-ac4d-677f272615dd
keywords:
- GPD file entries WDK Unidrv , lists
- listing attributes WDK GPD files
- LIST keyword
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Lists


## <a href="" id="ddk-lists-gg"></a>


To assign a set of values to an attribute, use the LIST keyword. The format is:

**LIST** ( *Value1* , *Value2* , *Value3* , ..., *ValueN*)

where *Value1*, *Value2*, *Value3*, ..., *ValueN* represent a set of one or more values, all of the type specified for the attribute. For example, the order in which a printer's color plane data should be sent can be specified as follows:

```
*ColorPlaneOrder: LIST(YELLOW, MAGENTA, CYAN, BLACK)
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Lists%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


