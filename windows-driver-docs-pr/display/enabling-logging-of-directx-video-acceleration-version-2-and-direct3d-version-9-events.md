---
title: Enabling Logging of DirectX Video Acceleration Version 2 and Direct3D Events
description: "How to enable logging of DXVA version 2 and Direct3D events in GPUView"
ms.date: 06/30/2022
---

# Enabling Logging of DirectX Video Acceleration Version 2 and Direct3D Events

To enable logging of DirectX VA version 2 events, you will need to add the following registry key.

``` registry
[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows Media Foundation] "WmiInstrumentation"=dword:00000001
```

Direct3D events are defined under the Microsoft Media Foundation provider GUID, which is provided in the *Log.cmd* file.
