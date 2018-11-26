---
title: Sending HID Reports by User-Mode Applications
description: Sending HID Reports by User-Mode Applications
ms.assetid: 265d7393-62be-41ad-8f87-efcfa462de1f
ms.localizationpriority: medium
ms.date: 10/17/2018
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

 

 




