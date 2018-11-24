---
title: Initializing HID Reports
description: Initializing HID Reports
ms.assetid: 14229315-3928-4421-a8d8-c3f7837bf1c3
keywords:
- HID reports WDK , initializing
- reports WDK HID , initializing
- initializing reports
- controls WDK HID
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Initializing HID Reports





This section describes how user-mode applications and kernel-mode drivers initialize a HID report before using the [HIDClass support routines](https://msdn.microsoft.com/library/windows/hardware/ff538865) or the HID class driver IOCTLs.

To initialize a report buffer, an application or driver creates a zero-initialized buffer of the required size, in bytes, for the report type. The *Xxx*ReportByteLength members of a HID collection's [**HIDP\_CAPS**](https://msdn.microsoft.com/library/windows/hardware/ff539697) structure specify the required size of input, output, and feature reports. After initializing a report buffer, an application or driver can use **HidP\_Set***Xxx* routines to set control data in the report. On the first use of a report, the **HidP\_Set***Xxx* routines set the report ID to the one associated with a specified [HID usage](hid-usages.md). If the application or driver subsequently attempts to set a usage that is incompatible with the report ID, the **HidP\_Set***Xxx* routines return a status of HIDP\_STATUS\_INCOMPATIBLE\_REPORT\_ID.

 

 




