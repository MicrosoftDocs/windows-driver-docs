---
title: Obtaining Collection Information
author: windows-driver-content
description: Obtaining Collection Information
ms.assetid: 0568993b-ff50-48ac-a875-95ab643d6c28
keywords: ["collections WDK HID , informatin gathering", "HID collections WDK , information gathering"]
---

# Obtaining Collection Information


## <a href="" id="ddk-obtaining-collection-information-kg"></a>


This section addresses obtaining information that user-mode applications and kernel-mode drivers use to operate a [HID collection](hid-collections.md).

After an application or driver has connected to a HID collection, it can obtain the following information:

-   [Collection's capabilities](collection-capability.md).

-   [Button capability arrays](button-capability-arrays.md) and [value capability arrays](value-capability-arrays.md), which describe the capabilities of buttons and values supported by the collection.

-   Link collection array, which describes the internal organization of its [link collections](link-collections.md).

This information includes the [HID usage](hid-usages.md) of the collection and all the controls supported by the collection. If an application or driver does not use these controls, it should immediately close its connection to the collection.

After obtaining this information, an application or driver has the information it requires to access control data in HID reports.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhid\hid%5D:%20Obtaining%20Collection%20Information%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


