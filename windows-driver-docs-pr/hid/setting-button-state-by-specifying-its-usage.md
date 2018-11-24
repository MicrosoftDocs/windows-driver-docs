---
title: Setting Button State by Specifying Its Usage
description: Setting Button State by Specifying Its Usage
ms.assetid: 0806f274-2b29-44f5-b487-4c0acb7a3e42
keywords: ["HID reports WDK , setting control data", "reports WDK HID , setting control data", "button usages WDK HID"]
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Setting Button State by Specifying Its Usage





An application or driver can set the state of buttons in a properly-initialized HID report by calling one of the following HID support routines:

<a href="" id="hidp-setbuttons--or-hidp-setusages-"></a>[**HidP\_SetButtons**](https://msdn.microsoft.com/library/windows/hardware/ff539779) (or [**HidP\_SetUsages**](https://msdn.microsoft.com/library/windows/hardware/ff539792))  
Sets a specified set of buttons to ON (1).

<a href="" id="hidp-unsetbuttons--or-hidp-unsetusages-"></a>[**HidP\_UnsetButtons**](https://msdn.microsoft.com/library/windows/hardware/ff539812) (or [**HidP\_UnsetUsages**](https://msdn.microsoft.com/library/windows/hardware/ff539819))  
Sets a specified set of buttons to OFF (zero).

<a href="" id="see-also-initializing-hid-reports-"></a>See also [Initializing HID Reports](initializing-hid-reports.md).  

 

 




