---
title: Starting a Protected Video Session
description: Starting a Protected Video Session
ms.assetid: c92f2d1a-ac15-49d4-858b-ff207ff4810c
keywords:
- copy protection WDK COPP , starting protected video session
- video copy protection WDK COPP , starting protected video session
- COPP WDK DirectX VA , starting protected video session
- protected video WDK COPP , starting session
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Starting a Protected Video Session


## <span id="ddk_starting_a_protected_video_session_gg"></span><span id="DDK_STARTING_A_PROTECTED_VIDEO_SESSION_GG"></span>


**This section applies only to Windows Server 2003 SP1 and later, and Windows XP SP2 and later.**

To start a protected video session, the VMR should initiate operations on the DirectX VA COPP device in a specific order. If this order is not followed, the video miniport driver should return error code E\_UNEXPECTED. The video miniport driver can determine that the correct operation order is followed by assigning a unique device-state constant to the COPP device when an operation is performed, and then by verifying the device-state constant before performing a subsequent operation.

To start the protected video session, calls should be made to the COPP device's functions in the following order:

1.  The [*COPPOpenVideoSession*](https://msdn.microsoft.com/library/windows/hardware/ff539650) function to initialize the COPP device. Before returning, the driver should set the device-state constant to COPP\_OPENED.

2.  The [*COPPGetCertificateLength*](https://msdn.microsoft.com/library/windows/hardware/ff539644) function to retrieve the size, in bytes, of the certificate used by the graphics hardware. The driver should first verify that the device-state constant is currently set to COPP\_OPENED. If it is not, the driver should return E\_UNEXPECTED. Before returning, the driver should set the device-state constant to COPP\_CERT\_LENGTH\_RETURNED.

3.  The [*COPPKeyExchange*](https://msdn.microsoft.com/library/windows/hardware/ff539646) function to retrieve the digital certificate used by the graphics hardware. The driver should first verify that the device-state constant is currently set to COPP\_CERT\_LENGTH\_RETURNED. If it is not, the driver should return E\_UNEXPECTED. Before returning, the driver should set the device-state constant to COPP\_KEY\_EXCHANGED.

4.  The [*COPPSequenceStart*](https://msdn.microsoft.com/library/windows/hardware/ff540421) function to set the video session to protected mode. The driver should first verify that the device-state constant is currently set to COPP\_KEY\_EXCHANGED. If it is not, the driver should return E\_UNEXPECTED. Before returning, the driver should set the device-state constant to COPP\_SESSION\_ACTIVE to show that the video session is in the protected mode.

After the video session is set to protected mode, the video miniport driver can process [COPP commands](copp-commands.md) and requests for [COPP status](copp-status.md), and pass [COPP status events](copp-status-events.md).

 

 





