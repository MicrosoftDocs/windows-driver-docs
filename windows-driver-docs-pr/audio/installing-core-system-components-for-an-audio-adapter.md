---
title: Installing Core System Components for an Audio Adapter
description: Installing Core System Components for an Audio Adapter
keywords:
- audio adapters WDK , system components
- adapter drivers WDK audio , system components
- Port Class audio adapters WDK , system components
ms.date: 10/27/2017
ms.localizationpriority: medium
---

# Installing Core System Components for an Audio Adapter


## <span id="installing_core_system_components_for_an_audio_adapter"></span><span id="INSTALLING_CORE_SYSTEM_COMPONENTS_FOR_AN_AUDIO_ADAPTER"></span>


This section includes the following topics about installing the core system components for a port-class audio adapter:

[Installing in Windows](installing-in-windows.md)

The [**INF DDInstall section**](../install/inf-ddinstall-section.md) for each hardware ID specified in the manufacture's **MODEL** section should specify the inclusion of the **KS.Registration** section in Ks.inf and the **WDMAUDIO.Registration** section in Wdmaudio.inf. The Ks.inf file installs the core kernel streaming components. The Wdmaudio.inf file installs the core WDM audio components. Vendors should not modify or replace these system INF files.

 

