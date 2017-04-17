---
title: Initializing HID Reports
author: windows-driver-content
description: Initializing HID Reports
ms.assetid: 14229315-3928-4421-a8d8-c3f7837bf1c3
keywords: ["HID reports WDK , initializing", "reports WDK HID , initializing", "initializing reports", "controls WDK HID"]
---

# Initializing HID Reports


## <a href="" id="ddk-initializing-hid-reports-kg"></a>


This section describes how user-mode applications and kernel-mode drivers initialize a HID report before using the [HIDClass support routines](https://msdn.microsoft.com/library/windows/hardware/ff538865) or the HID class driver IOCTLs.

To initialize a report buffer, an application or driver creates a zero-initialized buffer of the required size, in bytes, for the report type. The *Xxx*ReportByteLength members of a HID collection's [**HIDP\_CAPS**](https://msdn.microsoft.com/library/windows/hardware/ff539697) structure specify the required size of input, output, and feature reports. After initializing a report buffer, an application or driver can use **HidP\_Set***Xxx* routines to set control data in the report. On the first use of a report, the **HidP\_Set***Xxx* routines set the report ID to the one associated with a specified [HID usage](hid-usages.md). If the application or driver subsequently attempts to set a usage that is incompatible with the report ID, the **HidP\_Set***Xxx* routines return a status of HIDP\_STATUS\_INCOMPATIBLE\_REPORT\_ID.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhid\hid%5D:%20Initializing%20HID%20Reports%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


