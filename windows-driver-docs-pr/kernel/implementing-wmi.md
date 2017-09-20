---
title: Implementing WMI
author: windows-driver-content
description: Implementing WMI
ms.assetid: 5c2ed322-0fc9-4004-9a5f-f4d3c6a59fe9
keywords: ["WMI WDK kernel", "Windows Management Instrumentation WDK kernel", "extensions WDK WMI", "measurement data WDK WMI", "instrumentation data WDK WMI", "user-mode WMI WDK", "WMI WDK user-mode", "Windows Management Instrumentation WDK user-mode", "kernel-mode drivers WDK , WMI"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Implementing WMI


## <a href="" id="ddk-windows-management-instrumentation-kg"></a>


This section describes kernel-mode Windows Management Instrumentation (WMI) extensions to WDM. When you add these extensions to your kernel-mode driver, your driver becomes a WMI provider. A WMI provider makes measurement and instrumentation data available to WMI consumers, such as user-mode applications.

For more information about the user-mode WMI API, refer to [Windows Management Instrumentation](http://msdn.microsoft.com/library/aa394582(VS.85).aspx) in the Windows SDK.

If you are implementing a KMDF-based driver, refer to [Supporting WMI in Framework-Based Drivers](https://msdn.microsoft.com/library/windows/hardware/ff544711).

This section includes the following information about kernel-mode WMI:

[Introduction to WMI](introduction-to-wmi.md)

[WMI Architecture](wmi-architecture.md)

[WMI Requirements for WDM Drivers](wmi-requirements-for-wdm-drivers.md)

[MOF Syntax for WMI Data and Event Blocks](mof-syntax-for-wmi-data-and-event-blocks.md)

[Designing WMI Data and Event Blocks](designing-wmi-data-and-event-blocks.md)

[Publishing a WMI Schema](publishing-a-wmi-schema.md)

[Registering as a WMI Data Provider](registering-as-a-wmi-data-provider.md)

[Handling WMI Requests](handling-wmi-requests.md)

[Sending WMI Events](sending-wmi-events.md)

[WMI Property Sheets](wmi-property-sheets.md)

[Using wmimofck.exe](using-wmimofck-exe.md)

[WMI Event Tracing](wmi-event-tracing.md)

[Testing and Troubleshooting WMI Driver Support](testing-and-troubleshooting-wmi-driver-support.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Implementing%20WMI%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


