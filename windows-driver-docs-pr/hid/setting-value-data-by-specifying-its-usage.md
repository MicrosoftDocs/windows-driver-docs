---
title: Setting Value Data by Specifying Its Usage
author: windows-driver-content
description: Setting Value Data by Specifying Its Usage
MS-HAID:
- 'hidclass\_346ca1e8-4649-468c-b3dd-fe7c33e50f48.xml'
- 'hid.setting\_value\_data\_by\_specifying\_its\_usage'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 69dc3bb4-8999-4990-950c-8581328030eb
keywords: ["HID reports WDK , setting control data", "reports WDK HID , setting control data", "data usage settings WDK HID"]
---

# Setting Value Data by Specifying Its Usage


## <a href="" id="ddk-setting-value-data-by-specifying-its-usage-kg"></a>


An application or driver can set a value in a properly-initialized HID report by calling one of the following HID support routines:

<a href="" id="hidp-setscaledusagevalue"></a>[**HidP\_SetScaledUsageValue**](https://msdn.microsoft.com/library/windows/hardware/ff539787)  
Sets a signed and scaled value in a report.

<a href="" id="hidp-setusagevalue"></a>[**HidP\_SetUsageValue**](https://msdn.microsoft.com/library/windows/hardware/ff539797)  
Sets a value in a report.

<a href="" id="hidp-setusagevaluearray"></a>[**HidP\_SetUsageValueArray**](https://msdn.microsoft.com/library/windows/hardware/ff539801)  
Sets a usage value array in a report.

<a href="" id="see-also-initializing-hid-reports-"></a>See also [Initializing HID Reports](initializing-hid-reports.md).  

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhid\hid%5D:%20Setting%20Value%20Data%20by%20Specifying%20Its%20Usage%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


