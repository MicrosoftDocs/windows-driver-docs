---
title: Defining Custom Properties
author: windows-driver-content
description: Defining Custom Properties
ms.assetid: c3b69482-12ad-4b9f-8c0c-5ce315032d51
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Defining Custom Properties


## <a href="" id="ddk-defining-custom-properties-si"></a>


If it is necessary for the WIA minidriver to define custom properties, the WIA\_PRIVATE\_DEVPROP property should be used for custom root item properties, and the WIA\_PRIVATE\_ITEMPROP property should be used for other item properties. These constants are defined in *wiadef.h*.

The following example code shows definitions for three root item properties. The property ID for the first custom root item property, CUSTOM\_ROOT\_PROP\_1, is defined in terms of WIA\_PRIVATE\_DEVPROP. Property IDs for additional root item properties are defined in terms of WIA\_PRIVATE\_DEVPROP + 1, WIA\_PRIVATE\_DEVPROP + 2, and so on. The pattern can be continued if additional custom root item properties are needed.

```
#define CUSTOM_ROOT_PROP_1 WIA_PRIVATE_DEVPROP
#define CUSTOM_ROOT_PROP_2 (WIA_PRIVATE_DEVPROP + 1) 
#define CUSTOM_ROOT_PROP_3 (WIA_PRIVATE_DEVPROP + 2) 
```

The next example shows definitions for three custom child item properties and property IDs. The property ID for the first custom child item property, CUSTOM\_CHILD\_PROP\_1, is defined in terms of WIA\_PRIVATE\_ITEMPROP. Property IDs for additional child item properties are defined in terms of WIA\_PRIVATE\_ITEMPROP + 1, and so on. As before, the pattern can be continued if more of these custom child item properties are needed.

```
#define CUSTOM_CHILD_PROP_1 WIA_PRIVATE_ITEMPROP
#define CUSTOM_CHILD_PROP_2 (WIA_PRIVATE_ITEMPROP + 1) 
#define CUSTOM_CHILD_PROP_3 (WIA_PRIVATE_ITEMPROP + 2)
```

Custom WIA properties must have custom property names that are associated with the custom property IDs. The following example code shows definitions for three custom root item property names. (These property names are used with the custom property IDs that were created in a previous example, where the custom property name contained in CUSTOM\_ROOT\_PROP\_1\_STR is associated with the custom root item property ID CUSTOM\_ROOT\_PROP\_1.)

```
#define CUSTOM_ROOT_PROP_1_STR L"My First Custom Root Item Property"
#define CUSTOM_ROOT_PROP_2_STR L"My Second Custom Root Item Property"
#define CUSTOM_ROOT_PROP_3_STR L"My Third Custom Root Item Property"
```

**Note**   WIA property names are *not* localized in multiple languages. This is because WIA properties can be read by applications using the property ID or the property name. If the name is used, it must be a constant, just as the property ID is.

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Defining%20Custom%20Properties%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


