---
title: Extracting Button Usages That Are Set to ON
description: Extracting Button Usages That Are Set to ON
ms.assetid: 700cdb18-f570-4189-a33c-f57af56a52fd
keywords: ["HID reports WDK , extracting control data", "reports WDK HID , extracting control data", "extracting HID control data", "button usages WDK HID"]
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Extracting Button Usages That Are Set to ON





To extract the [HID usages](hid-usages.md) of buttons that are set to ON (1), applications and drivers call one of the following HID support routines:

<a href="" id="hidp-getbuttons--or-hidp-getusages-"></a>[**HidP\_GetButtons**](https://docs.microsoft.com/windows-hardware/drivers/hid/hdpi-h-macros) (or [**HidP\_GetUsages**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/hidpi/nf-hidpi-hidp_getusages))  
Returns the usage ID of all buttons on a specified usage page that are set to ON.

<a href="" id="hidp-getbuttonsex--or-hidp-getusagesex-"></a>[**HidP\_GetButtonsEx**](https://docs.microsoft.com/windows-hardware/drivers/hid/hdpi-h-macros) (or [**HidP\_GetUsagesEx**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/hidpi/nf-hidpi-hidp_getusagesex))  
Returns the usage page and usage ID of all buttons that are set to ON.

These routines return an array of all usage information for all buttons that are currently set to ON. Implicitly, buttons whose usage is not returned by these routines are set to OFF (zero).

To call these routines, applications and drivers must first allocate and zero-initialize the buffer used to return the array of button usages. An application or driver calls [**HidP\_MaxUsageListLength**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/hidpi/nf-hidpi-hidp_maxusagelistlength) to determine the number of button usages in a specified usage page in the report. If the application or driver specifies a usage page of zero, the routine returns the number of all the button usages in the report.

The required buffer size, in bytes, is the following:

-   (For [**HidP\_GetButtons**](https://docs.microsoft.com/windows-hardware/drivers/hid/hdpi-h-macros)) The value returned by **HidP\_MaxUsageListLength** times sizeof(USAGE)

-   (For [**HidP\_GetButtonsEx**](https://docs.microsoft.com/windows-hardware/drivers/hid/hdpi-h-macros)) The value returned by **HidP\_MaxUsageListLength** times sizeof(USAGE\_AND\_PAGE)

After an application or driver has used these routines to obtain information about which buttons are currently set to ON, it can determine the difference between the current state and the previous state of the buttons by calling one of the following [HIDClass support routines](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/index). These routines return the difference between two arrays of usage information:

[**HidP\_UsageListDifference**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/hidpi/nf-hidpi-hidp_usagelistdifference)

[**HidP\_UsageAndPageListDifference**](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff539824(v=vs.85))

 

 




