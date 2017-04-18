---
title: Sending HID Reports by User-Mode Applications
author: windows-driver-content
description: Sending HID Reports by User-Mode Applications
ms.assetid: 265d7393-62be-41ad-8f87-efcfa462de1f
---

# Sending HID Reports by User-Mode Applications


A user-mode application should use WriteFile (as described in the Microsoft Windows SDK) as its main approach to continuously send output reports to a HID collection. An application can also use **HidD\_Set***Xxx* routines to send output reports and feature reports to a collection. However, an application should only use these routines to set the current state of a collection. Some devices might not support **HidD\_SetOutputReport** and will become unresponsive if this routine is used.

For more information, see [Using WriteFile](#using-writefile) and [Using HidD\_SetXxx Routines](#using-hidd-setxxx-routines).

### Using WriteFile

An application should use write requests to send output reports to a HID collection. After a user-mode application has created an output report, it can send an output report to a collection using WriteFile.

### <a href="" id="using-hidd-setxxx-routines"></a>Using HidD\_SetXxx Routines

An application can use the following [HIDClass support routines](https://msdn.microsoft.com/library/windows/hardware/ff538865) to send HID reports to a HID collection:

<a href="" id="hidd-setoutputreport"></a>[**HidD\_SetOutputReport**](https://msdn.microsoft.com/library/windows/hardware/ff539690)  
Sends an output report to a HID collection (Windows XP and later versions).

<a href="" id="hidd-setfeature"></a>[**HidD\_SetFeature**](https://msdn.microsoft.com/library/windows/hardware/ff539684)  
Sends a feature report to a HID collection.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhid\hid%5D:%20Sending%20HID%20Reports%20by%20User-Mode%20Applications%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


