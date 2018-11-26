---
title: Obtaining HID Reports by User-Mode Applications
description: This topic discusses the obtaining of HID input reports or HID feature reports, by user-mode applications using ReadFile or the HidD_GetXxx routines.
ms.assetid: 28f560dd-b919-4652-93f6-691051a0ffbe
ms.localizationpriority: medium
ms.date: 10/17/2018
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

 

 




