---
title: Obtaining HID Reports by User-Mode Applications
author: windows-driver-content
description: This topic discusses the obtaining of HID input reports or HID feature reports, by user-mode applications using ReadFile or the HidD\_GetXxx routines.
ms.assetid: 28f560dd-b919-4652-93f6-691051a0ffbe
---

# Obtaining HID Reports by User-Mode Applications


This topic discusses the obtaining of HID input reports or HID feature reports, by user-mode applications using [ReadFile](https://msdn.microsoft.com/library/windows/desktop/aa365467.aspx) or the **HidD\_Get***Xxx* routines.

However, an application should only use the **HidD\_Get***Xxx* routines to obtain the current state of a device. If an application attempts to use [**HidD\_GetInputReport**](https://msdn.microsoft.com/library/windows/hardware/ff538945) to continuously obtain input reports, the reports can be lost. In addition, some devices might not support **HidD\_GetInputReport**, and will become unresponsive if this routine is used.

The following sections provide more information.

### Using ReadFile

An application uses the open file handle it obtained by using CreateFile to open a file on the collection. When the application calls [ReadFile](https://msdn.microsoft.com/library/windows/desktop/aa365467.aspx), it does not have to specify overlapped I/O because the [HID Client Drivers](hid-client-drivers.md) buffers reports in a ring buffer. However, an application can use overlapped I/O to have more than one outstanding read request.

### <a href="" id="using-hid-getxx-routines"></a>Using HidD\_GetXxx Routines

An application can use the following [HIDClass support routines](https://msdn.microsoft.com/library/windows/hardware/ff538865) to obtain the most current input reports and feature reports from a HID collection:

<a href="" id="hidd-getinputreport"></a>[**HidD\_GetInputReport**](https://msdn.microsoft.com/library/windows/hardware/ff538945)  
Returns an input report from a HID collection (Windows XP and later versions).

<a href="" id="hidd-getfeature"></a>[**HidD\_GetFeature**](https://msdn.microsoft.com/library/windows/hardware/ff538910)  
Returns a feature report from a HID collection.

An application can request the return of a specific report. To retrieve a specific report using these routines, the application allocates the report output buffer, zero-initializes the buffer, and sets the first byte in the buffer to the specific report ID. For more information, see [Initializing HID Reports](initializing-hid-reports.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhid\hid%5D:%20Obtaining%20HID%20Reports%20by%20User-Mode%20Applications%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


