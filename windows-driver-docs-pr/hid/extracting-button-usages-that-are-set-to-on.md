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

<a href="" id="hidp-getbuttons--or-hidp-getusages-"></a>[**HidP\_GetButtons**](https://msdn.microsoft.com/library/windows/hardware/ff539708) (or [**HidP\_GetUsages**](https://msdn.microsoft.com/library/windows/hardware/ff539742))  
Returns the usage ID of all buttons on a specified usage page that are set to ON.

<a href="" id="hidp-getbuttonsex--or-hidp-getusagesex-"></a>[**HidP\_GetButtonsEx**](https://msdn.microsoft.com/library/windows/hardware/ff539712) (or [**HidP\_GetUsagesEx**](https://msdn.microsoft.com/library/windows/hardware/ff539745))  
Returns the usage page and usage ID of all buttons that are set to ON.

These routines return an array of all usage information for all buttons that are currently set to ON. Implicitly, buttons whose usage is not returned by these routines are set to OFF (zero).

To call these routines, applications and drivers must first allocate and zero-initialize the buffer used to return the array of button usages. An application or driver calls [**HidP\_MaxUsageListLength**](https://msdn.microsoft.com/library/windows/hardware/ff539770) to determine the number of button usages in a specified usage page in the report. If the application or driver specifies a usage page of zero, the routine returns the number of all the button usages in the report.

The required buffer size, in bytes, is the following:

-   (For [**HidP\_GetButtons**](https://msdn.microsoft.com/library/windows/hardware/ff539708)) The value returned by **HidP\_MaxUsageListLength** times sizeof(USAGE)

-   (For [**HidP\_GetButtonsEx**](https://msdn.microsoft.com/library/windows/hardware/ff539712)) The value returned by **HidP\_MaxUsageListLength** times sizeof(USAGE\_AND\_PAGE)

After an application or driver has used these routines to obtain information about which buttons are currently set to ON, it can determine the difference between the current state and the previous state of the buttons by calling one of the following [HIDClass support routines](https://msdn.microsoft.com/library/windows/hardware/ff538865). These routines return the difference between two arrays of usage information:

[**HidP\_UsageListDifference**](https://msdn.microsoft.com/library/windows/hardware/ff539826)

[**HidP\_UsageAndPageListDifference**](https://msdn.microsoft.com/library/windows/hardware/ff539824)

 

 




