---
title: Extracting Value Data by Specifying Its Usage
author: windows-driver-content
description: Extracting Value Data by Specifying Its Usage
MS-HAID:
- 'hidclass\_822d63d4-d5e0-4f9f-a403-59574805bb1a.xml'
- 'hid.extracting\_value\_data\_by\_specifying\_its\_usage'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 043cdb68-ead8-4ccf-ae00-1165fe2988f4
keywords: ["HID reports WDK , extracting control data", "reports WDK HID , extracting control data", "extracting HID control data", "data usage extractions WDK HID"]
---

# Extracting Value Data by Specifying Its Usage


## <a href="" id="ddk-extracting-value-data-by-specifying-its-usage-kg"></a>


To extract value data from a HID report, an application or driver can use one of the following HID support routines:

<a href="" id="hidp-getscaledusagevalue"></a>[**HidP\_GetScaledUsageValue**](https://msdn.microsoft.com/library/windows/hardware/ff539729)  
Returns a signed and scaled value.

<a href="" id="hidp-getusagevalue"></a>[**HidP\_GetUsageValue**](https://msdn.microsoft.com/library/windows/hardware/ff539748)  
Returns a nonscaled value in an unsigned format or a scaled value that is out of its **Normal** range.

<a href="" id="hidp-getusagevaluearray"></a>[**HidP\_GetUsageValueArray**](https://msdn.microsoft.com/library/windows/hardware/ff539750)  
Returns a usage value array.

To use **HidP\_GetUsageValueArray**, applications and drivers must allocate a zero-initialized buffer, which is large enough to hold the usage value array. The required size, in bytes, is the product of the **BitSize** and **ReportCount** members of the usage value array's [**HIDP\_VALUE\_CAPS**](https://msdn.microsoft.com/library/windows/hardware/ff539832) structure, rounded up to the nearest byte.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhid\hid%5D:%20Extracting%20Value%20Data%20by%20Specifying%20Its%20Usage%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


