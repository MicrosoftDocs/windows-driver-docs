---
title: About the DirectInput Control Panel
description: About the DirectInput Control Panel
ms.assetid: d6845778-1203-4b5a-8a7b-7d4eecbcc59e
keywords: ["property sheets WDK DirectInput , about control panel", "game controllers WDK DirectInput , about control panel", "control panels WDK DirectInput , about control panel", "Joy.cpl"]
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# About the DirectInput Control Panel





DirectInput provides support for game controllers such as game pads, joysticks, and force-feedback devices. In Microsoft DirectX 5.0 and later versions, DirectInput provides a new game controller control panel called Joy.cpl. This version of Control Panel is the first to allow extensibility in that the property sheets that are displayed for each controller can be replaced with property pages that are specific to that controller. This is done through the creation of a DLL that contains information about these property sheets. This DLL exposes a COM interface that is called into by the DirectInput control panel.

Game controller hardware vendors are encouraged to use this extensibility feature to provide customized property sheets for their game controllers instead of creating a separate control panel. This allows the user to open a single control panel to configure and test their game controllers.

 

 




