---
title: COPP Commands
description: COPP Commands
ms.assetid: c745b7d9-be59-45f9-90f5-0a7ecef0a292
keywords:
- copy protection WDK COPP , commands
- video copy protection WDK COPP , commands
- COPP WDK DirectX VA , commands
- protected video WDK COPP , commands
- commands WDK COPP
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# COPP Commands


## <span id="ddk_copp_command_gg"></span><span id="DDK_COPP_COMMAND_GG"></span>


This section applies only to Windows Server 2003 SP1 and later, and Windows XP SP2 and later.

The video miniport driver can receive a request to perform an operation on the physical connector associated with the DirectX VA COPP device. The video miniport driver's [*COPPCommand*](https://msdn.microsoft.com/library/windows/hardware/ff539642) function is passed a pointer to a [**DXVA\_COPPCommand**](https://msdn.microsoft.com/library/windows/hardware/ff563141) structure that specifies the operation to perform. The **guidCommandID** and **CommandData** members of DXVA\_COPPCommand specify the operation. The following operations are supported:

-   [Setting the protection level](setting-the-protection-level.md)

-   [Instructing how to protect the signal](instructing-how-to-protect-the-signal.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20COPP%20Commands%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




