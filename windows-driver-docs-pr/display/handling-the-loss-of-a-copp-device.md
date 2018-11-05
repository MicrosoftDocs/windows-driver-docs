---
title: Handling the Loss of a COPP Device
description: Handling the Loss of a COPP Device
ms.assetid: 7e74b249-34be-44cc-a022-ba6574f2f841
keywords:
- copy protection WDK COPP , loss of device
- video copy protection WDK COPP , loss of device
- COPP WDK DirectX VA , loss of device
- protected video WDK COPP , loss of device
- lost COPP devices WDK DirectX VA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling the Loss of a COPP Device


## <span id="ddk_handling_the_loss_of_a_copp_device_gg"></span><span id="DDK_HANDLING_THE_LOSS_OF_A_COPP_DEVICE_GG"></span>


**This section applies only to Windows Server 2003 SP1 and later, and Windows XP SP2 and later.**

A video session that is set to protected mode must handle scenarios that cause the destruction of a DirectX VA COPP device that is associated with the video session. The following scenarios initiate a call to the display driver's [*DdMoCompDestroy*](https://msdn.microsoft.com/library/windows/hardware/ff549664) callback function while content protection on the certified output connector for the video session is possibly enabled:

-   Changing the display mode

-   Attaching or detaching a monitor from the Windows desktop

-   Entering a full-screen Command Prompt window

-   Starting any DirectDraw or Direct3D exclusive-mode application

-   Performing Fast User Switching

-   Locking the workstation or pressing CTRL+ALT+DELETE

-   Attaching to the workstation by using Remote Desktop Connection

-   Entering a power-saving mode--for example, suspend or hibernate

-   Terminating the application unexpectedly--for example, through a page fault

If one of the preceding scenarios occurs while output content protection for the video session is enabled, the display driver's *DdMoCompDestroy* function should initiate a call to the video miniport driver's [*COPPCloseVideoSession*](https://msdn.microsoft.com/library/windows/hardware/ff539638) function to decrement the global protection-level count by the current local protection-level count for the COPP device. The video miniport driver should then examine the modified global protection level and adjust the protection level applied to the output connector accordingly.

 

 





