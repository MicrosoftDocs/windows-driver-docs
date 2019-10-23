---
title: Extracting Value Data by Specifying Its Usage
description: Extracting Value Data by Specifying Its Usage
ms.assetid: 043cdb68-ead8-4ccf-ae00-1165fe2988f4
keywords: ["HID reports WDK , extracting control data", "reports WDK HID , extracting control data", "extracting HID control data", "data usage extractions WDK HID"]
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Extracting Value Data by Specifying Its Usage





To extract value data from a HID report, an application or driver can use one of the following HID support routines:

<a href="" id="hidp-getscaledusagevalue"></a>[**HidP\_GetScaledUsageValue**](https://docs.microsoft.com/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_getscaledusagevalue)  
Returns a signed and scaled value.

<a href="" id="hidp-getusagevalue"></a>[**HidP\_GetUsageValue**](https://docs.microsoft.com/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_getusagevalue)  
Returns a nonscaled value in an unsigned format or a scaled value that is out of its **Normal** range.

<a href="" id="hidp-getusagevaluearray"></a>[**HidP\_GetUsageValueArray**](https://docs.microsoft.com/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_getusagevaluearray)  
Returns a usage value array.

To use **HidP\_GetUsageValueArray**, applications and drivers must allocate a zero-initialized buffer, which is large enough to hold the usage value array. The required size, in bytes, is the product of the **BitSize** and **ReportCount** members of the usage value array's [**HIDP\_VALUE\_CAPS**](https://docs.microsoft.com/windows-hardware/drivers/ddi/hidpi/ns-hidpi-_hidp_value_caps) structure, rounded up to the nearest byte.

 

 




