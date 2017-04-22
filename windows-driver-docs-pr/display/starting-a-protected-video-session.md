---
title: Starting a Protected Video Session
description: Starting a Protected Video Session
ms.assetid: c92f2d1a-ac15-49d4-858b-ff207ff4810c
keywords:
- copy protection WDK COPP , starting protected video session
- video copy protection WDK COPP , starting protected video session
- COPP WDK DirectX VA , starting protected video session
- protected video WDK COPP , starting session
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Starting%20a%20Protected%20Video%20Session%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




