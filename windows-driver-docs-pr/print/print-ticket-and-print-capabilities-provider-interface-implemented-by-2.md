---
title: Print Ticket and Print Capabilities Provider Interface
author: windows-driver-content
description: Print Ticket and Print Capabilities Provider Interface Implemented by Printer Drivers
ms.assetid: a14c1173-0419-44c7-bc8f-7197590083b3
keywords:
- printer interface DLL WDK , Print Ticket support
- printer interface DLL WDK , Print Capabilities support
- Print Capabilities WDK , printer interface DLL
- Print Tickets WDK , printer interface DLL
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Print Ticket and Print Capabilities Provider Interface Implemented by Printer Drivers


The Windows Vista operating system provides basic print ticket support for all drivers. However, that support is based only on information that is publicly exposed by the driver by means of Microsoft Win32 application programming interfaces (APIs) such as **DeviceCapabilities** and **GetDeviceCaps** and by the settings in the public portion of the [**DEVMODEW**](https://msdn.microsoft.com/library/windows/hardware/ff552837) structure. Drivers can provide a richer experience by implementing the driver print ticket and print capabilities provider interface, which is described in the following topics.

Implementations of the print ticket and print capabilities provider interface must be multithread safe, because calls into the provider are driven by the application and might be made concurrently.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Print%20Ticket%20and%20Print%20Capabilities%20Provider%20Interface%20Implemented%20by%20Printer%20Drivers%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


