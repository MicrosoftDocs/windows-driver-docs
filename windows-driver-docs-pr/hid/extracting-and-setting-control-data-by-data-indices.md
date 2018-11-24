---
title: Extracting and Setting Control Data by Data Indices
description: Extracting and Setting Control Data by Data Indices
ms.assetid: d26d169f-4116-4d81-94c7-63c92d22877d
keywords: ["HID reports WDK , setting control data", "reports WDK HID , setting control data", "HID reports WDK , extracting control data", "reports WDK HID , extracting control data", "extracting HID control data", "data index WDK HID", "index WDK HID data"]
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Extracting and Setting Control Data by Data Indices





To use [data indices](data-indices.md) to extract and set control data in a HID report, an application or driver can use the following HID support routines:

[**HidP\_GetData**](https://msdn.microsoft.com/library/windows/hardware/ff539718)

[**HidP\_SetData**](https://msdn.microsoft.com/library/windows/hardware/ff539783)

These routines are particularly useful to an application or driver that provides a "value-added" service. For example, one that provides a custom interface to all the controls supported by a HIDClass device. Microsoft DirectInput is one example.

By calling these routines, an application or driver can most efficiently obtain and set all values in a report. For example, to obtain all value data by their [HID usages](hid-usages.md), it has to call [**HidP\_GetUsageValue**](https://msdn.microsoft.com/library/windows/hardware/ff539748) for each usage. However, to obtain all value data by data index, it only has to call **HidP\_GetData** once.

An application or driver uses the data indices specified in a collection's [button capability arrays](button-capability-arrays.md) and [value capability arrays](value-capability-arrays.md) to identify HID usages.

 

 




