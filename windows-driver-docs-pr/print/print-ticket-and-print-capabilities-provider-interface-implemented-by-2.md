---
title: Print Ticket and Print Capabilities Provider Interface
description: Print Ticket and Print Capabilities Provider Interface Implemented by Printer Drivers
ms.assetid: a14c1173-0419-44c7-bc8f-7197590083b3
keywords:
- printer interface DLL WDK , Print Ticket support
- printer interface DLL WDK , Print Capabilities support
- Print Capabilities WDK , printer interface DLL
- Print Tickets WDK , printer interface DLL
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Print Ticket and Print Capabilities Provider Interface Implemented by Printer Drivers


The Windows Vista operating system provides basic print ticket support for all drivers. However, that support is based only on information that is publicly exposed by the driver by means of Microsoft Win32 application programming interfaces (APIs) such as **DeviceCapabilities** and **GetDeviceCaps** and by the settings in the public portion of the [**DEVMODEW**](https://msdn.microsoft.com/library/windows/hardware/ff552837) structure. Drivers can provide a richer experience by implementing the driver print ticket and print capabilities provider interface, which is described in the following topics.

Implementations of the print ticket and print capabilities provider interface must be multithread safe, because calls into the provider are driven by the application and might be made concurrently.

 

 




