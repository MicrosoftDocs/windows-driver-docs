---
title: INF and Installation Requirements
description: INF and Installation Requirements
ms.assetid: d3b21de9-5eb0-4278-91b1-c49c4368c047
keywords:
- INF files WDK Windows 2000 display
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# INF and Installation Requirements


## <span id="ddk_inf_and_installation_requirements_gg"></span><span id="DDK_INF_AND_INSTALLATION_REQUIREMENTS_GG"></span>


NT-based operating system display and video miniport drivers must be installed using an INF file. To ensure that all registry entries associated with a video driver are properly initialized, this INF must be interpreted by the system-supplied display class installer and marked as **Class=Display**.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20INF%20and%20Installation%20Requirements%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




