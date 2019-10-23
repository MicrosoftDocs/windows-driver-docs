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

<a href="" id="hidp-setbuttons--or-hidp-setusages-"></a>[**HidP\_SetButtons**](https://docs.microsoft.com/windows-hardware/drivers/hid/hdpi-h-macros) (or [**HidP\_SetUsages**](https://docs.microsoft.com/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_setusages))  
Sets a specified set of buttons to ON (1).

<a href="" id="hidp-unsetbuttons--or-hidp-unsetusages-"></a>[**HidP\_UnsetButtons**](https://docs.microsoft.com/windows-hardware/drivers/hid/hdpi-h-macros) (or [**HidP\_UnsetUsages**](https://docs.microsoft.com/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_unsetusages))  
Sets a specified set of buttons to OFF (zero).

<a href="" id="see-also-initializing-hid-reports-"></a>See also [Initializing HID Reports](initializing-hid-reports.md).  

 

 




