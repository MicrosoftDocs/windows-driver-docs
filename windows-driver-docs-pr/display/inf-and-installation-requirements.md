---
title: INF and Installation Requirements
description: INF and Installation Requirements
keywords:
- INF files WDK Windows 2000 display
ms.date: 04/20/2017
---

# INF and Installation Requirements


## <span id="ddk_inf_and_installation_requirements_gg"></span><span id="DDK_INF_AND_INSTALLATION_REQUIREMENTS_GG"></span>


NT-based operating system display and video miniport drivers must be installed using an INF file. To ensure that all registry entries associated with a video driver are properly initialized, this INF must be interpreted by the system-supplied display class installer and marked as **Class=Display**.

 

 





