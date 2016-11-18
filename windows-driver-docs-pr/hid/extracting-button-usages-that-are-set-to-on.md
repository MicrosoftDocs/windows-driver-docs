---
title: Extracting Button Usages That Are Set to ON
author: windows-driver-content
description: Extracting Button Usages That Are Set to ON
MS-HAID:
- 'hidclass\_ca7b48f4-c7f1-4541-b702-c77d378719a9.xml'
- 'hid.extracting\_button\_usages\_that\_are\_set\_to\_on'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 700cdb18-f570-4189-a33c-f57af56a52fd
keywords: ["HID reports WDK , extracting control data", "reports WDK HID , extracting control data", "extracting HID control data", "button usages WDK HID"]
---

# Extracting Button Usages That Are Set to ON


## <a href="" id="ddk-extracting-button-usages-that-are-set-to-on-kg"></a>


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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhid\hid%5D:%20Extracting%20Button%20Usages%20That%20Are%20Set%20to%20ON%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


