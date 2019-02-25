---
title: DirectX VA COPP Device
description: DirectX VA COPP Device
ms.assetid: f9268b38-3317-4c4f-b9c1-e0ad3c88f92e
keywords:
- COPP device WDK DirectX VA
- copy protection WDK COPP , COPP device
- video copy protection WDK COPP , COPP device
- COPP WDK DirectX VA , COPP device
- protected video WDK COPP , COPP device
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# DirectX VA COPP Device


## <span id="ddk_directx_va_copp_device_gg"></span><span id="DDK_DIRECTX_VA_COPP_DEVICE_GG"></span>


This section applies only to Windows Server 2003 SP1 and later, and Windows XP SP2 and later.

The display driver should be implemented so that a DirectX VA COPP device is created for each video session. The COPP device represents an end point to receive COPP commands and status requests. The COPP device also stores the protection settings of its associated physical connector. A physical connector can support multiple content protection types. For example, an S-Video connector can support analog content protection (ACP) in addition to Content Generation Management System for Analog (CGMS-A) protection. For more information, see [Defining the COPP Device Class](defining-the-copp-device-class.md).

Multiple instances of the COPP device are required so that different processes can configure the settings of the graphics adapter's output through COPP. Therefore, you should implement the COPP device class so that each COPP device acts appropriately when multiple video sessions are active on the system.

**Note**   A video session consists of a video stream possibly combined with one or more video substreams. A video session is tied to a particular graphics adapter's output connector. Several video sessions can be active on a system and within a single process.

 

 

 





