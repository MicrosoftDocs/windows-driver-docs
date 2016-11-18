---
title: Setting Button State by Specifying Its Usage
author: windows-driver-content
description: Setting Button State by Specifying Its Usage
MS-HAID:
- 'hidclass\_25448ae4-0b7e-4f64-b1c5-ab6fccbc1e84.xml'
- 'hid.setting\_button\_state\_by\_specifying\_its\_usage'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 0806f274-2b29-44f5-b487-4c0acb7a3e42
keywords: ["HID reports WDK , setting control data", "reports WDK HID , setting control data", "button usages WDK HID"]
---

# Setting Button State by Specifying Its Usage


## <a href="" id="ddk-setting-button-state-by-specifying-its-usage-kg"></a>


An application or driver can set the state of buttons in a properly-initialized HID report by calling one of the following HID support routines:

<a href="" id="hidp-setbuttons--or-hidp-setusages-"></a>[**HidP\_SetButtons**](https://msdn.microsoft.com/library/windows/hardware/ff539779) (or [**HidP\_SetUsages**](https://msdn.microsoft.com/library/windows/hardware/ff539792))  
Sets a specified set of buttons to ON (1).

<a href="" id="hidp-unsetbuttons--or-hidp-unsetusages-"></a>[**HidP\_UnsetButtons**](https://msdn.microsoft.com/library/windows/hardware/ff539812) (or [**HidP\_UnsetUsages**](https://msdn.microsoft.com/library/windows/hardware/ff539819))  
Sets a specified set of buttons to OFF (zero).

<a href="" id="see-also-initializing-hid-reports-"></a>See also [Initializing HID Reports](initializing-hid-reports.md).  

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhid\hid%5D:%20Setting%20Button%20State%20by%20Specifying%20Its%20Usage%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


