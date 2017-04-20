---
title: Interpreting HID Reports
author: windows-driver-content
description: Interpreting HID Reports
ms.assetid: 10f8c3a1-ad60-4c99-a425-fa8c9a3be0e1
keywords:
- HID reports WDK , interpreting
- reports WDK HID , interpreting
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Interpreting HID Reports


## <a href="" id="ddk-interpreting-hid-reports-kg"></a>


This section describes how user-mode applications and kernel-mode drivers use the HidP\_*Xxx* [HIDClass support routines](https://msdn.microsoft.com/library/windows/hardware/ff538865) to interpret control data in a HID report.

For information about extracting control data from a report, see the following:

[Extracting Value Data by Specifying Its Usage](extracting-value-data-by-specifying-its-usage.md)

[Extracting Button Usages That Are Set to ON](extracting-button-usages-that-are-set-to-on.md)

[Extracting and Setting Control Data by Data Indices](extracting-and-setting-control-data-by-data-indices.md)

For information about how to set control data in a report, see the following:

[Setting Value Data by Specifying Its Usage](setting-value-data-by-specifying-its-usage.md)

[Setting Button State by Specifying Its Usage](setting-button-state-by-specifying-its-usage.md)

[Extracting and Setting Control Data by Data Indices](extracting-and-setting-control-data-by-data-indices.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhid\hid%5D:%20Interpreting%20HID%20Reports%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


