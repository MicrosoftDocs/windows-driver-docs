---
title: 32-Bit and 64-Bit WIA Interoperability
description: 32-Bit and 64-Bit WIA Interoperability
ms.assetid: f7f7a42a-590e-4f81-b325-ba9f9ffa9664
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# 32-Bit and 64-Bit WIA Interoperability


On systems that run Windows 64-Bit Edition for Extended Processors, all WIA components are 64-bit so the WIA infrastructure was changed to allow interoperability between these 64-bit drivers and existing 32-bit applications.

On 64-bit editions of the Windows operating system, the 64-bit WIA minidriver is loaded in the WIA service's 64-bit process. However, WIA minidriver UI extensions are loaded in the application's process space. A Microsoft Win32 application's unmodified 32-bit process that runs on an x64-based machine would not be able to load the 64-bit UI extension.

To mitigate the 32-bit to 64-bit problem, Microsoft provides a 64-bit extension host, *wiawow64.exe*. This host ensures transparent interoperability between 32-bit applications and 64-bit WIA UI extensions. The *wiawow64.exe* extension host will be available in Windows Server 2003 64-Bit Edition for Extended Processors, Windows XP 64-Bit Edition for Extended Processors, Windows Vista, and later operating system versions.

The WIA service will determine where UI extensions get physically loaded, depending on whether the application is 64-bit or 32-bit:

-   *64-bit application*. The 64-bit WIA minidriver UI extension is loaded directly into the process space of the application. This is similar to what happens when you run a 32-bit application on 32-bit versions of the Windows operating system.

-   *32-bit application*. WIA launches the *wiawow64.exe* extension host that UI extensions will be loaded into. A separate instance of *wiawow64.exe* is created and launched each time a call to any of the interface methods comes in from a 32-bit application. The *wiawow64.exe* host runs in the same context as the application and communicates with the application through the existing COM interfaces.

    **Note**   Even though *wiawow64.exe* is completely transparent to both WIA application writers and WIA driver developers, driver developers have to debug the *wiawow64.exe* process rather than the 32-bit application to debug 64-bit UI extensions.

     

 

 




