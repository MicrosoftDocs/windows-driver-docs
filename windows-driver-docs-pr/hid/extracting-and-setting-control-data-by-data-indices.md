---
title: Extracting and Setting Control Data by Data Indices
author: windows-driver-content
description: Extracting and Setting Control Data by Data Indices
MS-HAID:
- 'hidclass\_fa9f249b-4866-481c-9f7f-c96b19442606.xml'
- 'hid.extracting\_and\_setting\_control\_data\_by\_data\_indices'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: d26d169f-4116-4d81-94c7-63c92d22877d
keywords: ["HID reports WDK , setting control data", "reports WDK HID , setting control data", "HID reports WDK , extracting control data", "reports WDK HID , extracting control data", "extracting HID control data", "data index WDK HID", "index WDK HID data"]
---

# Extracting and Setting Control Data by Data Indices


## <a href="" id="ddk-extracting-and-setting-control-data-by-data-indices-kg"></a>


To use [data indices](data-indices.md) to extract and set control data in a HID report, an application or driver can use the following HID support routines:

[**HidP\_GetData**](https://msdn.microsoft.com/library/windows/hardware/ff539718)

[**HidP\_SetData**](https://msdn.microsoft.com/library/windows/hardware/ff539783)

These routines are particularly useful to an application or driver that provides a "value-added" service. For example, one that provides a custom interface to all the controls supported by a HIDClass device. Microsoft DirectInput is one example.

By calling these routines, an application or driver can most efficiently obtain and set all values in a report. For example, to obtain all value data by their [HID usages](hid-usages.md), it has to call [**HidP\_GetUsageValue**](https://msdn.microsoft.com/library/windows/hardware/ff539748) for each usage. However, to obtain all value data by data index, it only has to call **HidP\_GetData** once.

An application or driver uses the data indices specified in a collection's [button capability arrays](button-capability-arrays.md) and [value capability arrays](value-capability-arrays.md) to identify HID usages.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhid\hid%5D:%20Extracting%20and%20Setting%20Control%20Data%20by%20Data%20Indices%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


