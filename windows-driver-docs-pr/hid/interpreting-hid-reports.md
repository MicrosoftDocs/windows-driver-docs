---
title: Interpreting HID Reports
author: windows-driver-content
description: Interpreting HID Reports
MS-HAID:
- 'hidclass\_ee7f8c3a-31b7-4ed9-a47d-d2f3ca31d600.xml'
- 'hid.interpreting\_hid\_reports'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 10f8c3a1-ad60-4c99-a425-fa8c9a3be0e1
keywords: ["HID reports WDK , interpreting", "reports WDK HID , interpreting"]
---

# Interpreting HID Reports


## <a href="" id="ddk-interpreting-hid-reports-kg"></a>


This section describes how user-mode applications and kernel-mode drivers use the HidP\_*Xxx* [HIDClass support routines](https://msdn.microsoft.com/library/windows/hardware/ff538865) to interpret control data in a HID report.


## Extracting Value Data by Specifying Its Usage

## <a href="" id="ddk-extracting-value-data-by-specifying-its-usage-kg"></a>


To extract value data from a HID report, an application or driver can use one of the following HID support routines:

<a href="" id="hidp-getscaledusagevalue"></a>[**HidP\_GetScaledUsageValue**](https://msdn.microsoft.com/library/windows/hardware/ff539729)  
Returns a signed and scaled value.

<a href="" id="hidp-getusagevalue"></a>[**HidP\_GetUsageValue**](https://msdn.microsoft.com/library/windows/hardware/ff539748)  
Returns a nonscaled value in an unsigned format or a scaled value that is out of its **Normal** range.

<a href="" id="hidp-getusagevaluearray"></a>[**HidP\_GetUsageValueArray**](https://msdn.microsoft.com/library/windows/hardware/ff539750)  
Returns a usage value array.

To use **HidP\_GetUsageValueArray**, applications and drivers must allocate a zero-initialized buffer, which is large enough to hold the usage value array. The required size, in bytes, is the product of the **BitSize** and **ReportCount** members of the usage value array's [**HIDP\_VALUE\_CAPS**](https://msdn.microsoft.com/library/windows/hardware/ff539832) structure, rounded up to the nearest byte.

 

## Extracting Button Usages That Are Set to ON

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

## Extracting and Setting Control Data by Data Indices


## <a href="" id="ddk-extracting-and-setting-control-data-by-data-indices-kg"></a>


To use [data indices](data-indices.md) to extract and set control data in a HID report, an application or driver can use the following HID support routines:

[**HidP\_GetData**](https://msdn.microsoft.com/library/windows/hardware/ff539718)

[**HidP\_SetData**](https://msdn.microsoft.com/library/windows/hardware/ff539783)

These routines are particularly useful to an application or driver that provides a "value-added" service. For example, one that provides a custom interface to all the controls supported by a HIDClass device. Microsoft DirectInput is one example.

By calling these routines, an application or driver can most efficiently obtain and set all values in a report. For example, to obtain all value data by their [HID usages](hid-usages.md), it has to call [**HidP\_GetUsageValue**](https://msdn.microsoft.com/library/windows/hardware/ff539748) for each usage. However, to obtain all value data by data index, it only has to call **HidP\_GetData** once.

An application or driver uses the data indices specified in a collection's [button capability arrays](button-capability-arrays.md) and [value capability arrays](value-capability-arrays.md) to identify HID usages.

 
## Setting Value Data by Specifying Its Usage


## <a href="" id="ddk-setting-value-data-by-specifying-its-usage-kg"></a>


An application or driver can set a value in a properly-initialized HID report by calling one of the following HID support routines:

<a href="" id="hidp-setscaledusagevalue"></a>[**HidP\_SetScaledUsageValue**](https://msdn.microsoft.com/library/windows/hardware/ff539787)  
Sets a signed and scaled value in a report.

<a href="" id="hidp-setusagevalue"></a>[**HidP\_SetUsageValue**](https://msdn.microsoft.com/library/windows/hardware/ff539797)  
Sets a value in a report.

<a href="" id="hidp-setusagevaluearray"></a>[**HidP\_SetUsageValueArray**](https://msdn.microsoft.com/library/windows/hardware/ff539801)  
Sets a usage value array in a report.

<a href="" id="see-also-initializing-hid-reports-"></a>See also [Initializing HID Reports](initializing-hid-reports.md).  

 
## Setting Button State by Specifying Its Usage


## <a href="" id="ddk-setting-button-state-by-specifying-its-usage-kg"></a>


An application or driver can set the state of buttons in a properly-initialized HID report by calling one of the following HID support routines:

<a href="" id="hidp-setbuttons--or-hidp-setusages-"></a>[**HidP\_SetButtons**](https://msdn.microsoft.com/library/windows/hardware/ff539779) (or [**HidP\_SetUsages**](https://msdn.microsoft.com/library/windows/hardware/ff539792))  
Sets a specified set of buttons to ON (1).

<a href="" id="hidp-unsetbuttons--or-hidp-unsetusages-"></a>[**HidP\_UnsetButtons**](https://msdn.microsoft.com/library/windows/hardware/ff539812) (or [**HidP\_UnsetUsages**](https://msdn.microsoft.com/library/windows/hardware/ff539819))  
Sets a specified set of buttons to OFF (zero).

<a href="" id="see-also-initializing-hid-reports-"></a>See also [Initializing HID Reports](initializing-hid-reports.md).  

 
## Extracting and Setting Control Data by Data Indices


## <a href="" id="ddk-extracting-and-setting-control-data-by-data-indices-kg"></a>


To use [data indices](data-indices.md) to extract and set control data in a HID report, an application or driver can use the following HID support routines:

[**HidP\_GetData**](https://msdn.microsoft.com/library/windows/hardware/ff539718)

[**HidP\_SetData**](https://msdn.microsoft.com/library/windows/hardware/ff539783)

These routines are particularly useful to an application or driver that provides a "value-added" service. For example, one that provides a custom interface to all the controls supported by a HIDClass device. Microsoft DirectInput is one example.

By calling these routines, an application or driver can most efficiently obtain and set all values in a report. For example, to obtain all value data by their [HID usages](hid-usages.md), it has to call [**HidP\_GetUsageValue**](https://msdn.microsoft.com/library/windows/hardware/ff539748) for each usage. However, to obtain all value data by data index, it only has to call **HidP\_GetData** once.

An application or driver uses the data indices specified in a collection's [button capability arrays](button-capability-arrays.md) and [value capability arrays](value-capability-arrays.md) to identify HID usages.


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhid\hid%5D:%20Interpreting%20HID%20Reports%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


