---
title: Obtaining HID Reports by User-Mode Applications
description: This topic discusses the obtaining of HID input reports or HID feature reports, by user-mode applications using ReadFile or the HidD_GetXxx routines.
ms.assetid: 28f560dd-b919-4652-93f6-691051a0ffbe
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Obtaining HID Reports by User-Mode Applications


This topic discusses the obtaining of HID input reports or HID feature reports, by user-mode applications using [ReadFile](https://docs.microsoft.com/windows/desktop/api/fileapi/nf-fileapi-readfile) or the **HidD\_Get**_Xxx_ routines.

However, an application should only use the **HidD\_Get**_Xxx_ routines to obtain the current state of a device. If an application attempts to use [**HidD\_GetInputReport**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/hidsdi/nf-hidsdi-hidd_getinputreport) to continuously obtain input reports, the reports can be lost. In addition, some devices might not support **HidD\_GetInputReport**, and will become unresponsive if this routine is used.

The following sections provide more information.

### Using ReadFile

An application uses the open file handle it obtained by using CreateFile to open a file on the collection. When the application calls [ReadFile](https://docs.microsoft.com/windows/desktop/api/fileapi/nf-fileapi-readfile), it does not have to specify overlapped I/O because the [HID Client Drivers](hid-client-drivers.md) buffers reports in a ring buffer. However, an application can use overlapped I/O to have more than one outstanding read request.

### <a href="" id="using-hid-getxx-routines"></a>Using HidD\_GetXxx Routines

An application can use the following [HIDClass support routines](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/index) to obtain the most current input reports and feature reports from a HID collection:

<a href="" id="hidd-getinputreport"></a>[**HidD\_GetInputReport**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/hidsdi/nf-hidsdi-hidd_getinputreport)  
Returns an input report from a HID collection (Windows XP and later versions).

<a href="" id="hidd-getfeature"></a>[**HidD\_GetFeature**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/hidsdi/nf-hidsdi-hidd_getfeature)  
Returns a feature report from a HID collection.

An application can request the return of a specific report. To retrieve a specific report using these routines, the application allocates the report output buffer, zero-initializes the buffer, and sets the first byte in the buffer to the specific report ID. For more information, see [Initializing HID Reports](initializing-hid-reports.md).

 

 




