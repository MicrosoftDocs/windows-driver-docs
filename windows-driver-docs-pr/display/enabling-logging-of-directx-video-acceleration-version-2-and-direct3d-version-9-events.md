---
title: Enabling Logging of DirectX Video Acceleration Version 2 and Direct3D Version 9 Events
description: "To enable logging of DirectX VA version 2 events, you will need to add the following registry key."
ms.date: 05/10/2022
---

# Enabling Logging of DirectX Video Acceleration Version 2 and Direct3D Version 9 Events

To enable logging of DirectX VA version 2 events, you will need to add the following registry key.


**[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows Media Foundation] "WmiInstrumentation"=dword:00000001**


Direct3D version 9 events are defined under the Microsoft Media Foundation provider GUID, which is provided in the Log.cmd and Circularlog.cmd files.