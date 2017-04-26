---
title: COPP and ChangeDisplaySettingsEx
description: COPP and ChangeDisplaySettingsEx
ms.assetid: 5c729bfd-0758-4de5-9e81-a3279f8aab56
keywords:
- copy protection WDK COPP , ChangeDisplaySettingsEx
- video copy protection WDK COPP , ChangeDisplaySettingsEx
- COPP WDK DirectX VA , ChangeDisplaySettingsEx
- protected video WDK COPP , ChangeDisplaySettingsEx
- ChangeDisplaySettingsEx
- analog content protection WDK COPP
- ACP protection type WDK COPP
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# COPP and ChangeDisplaySettingsEx


## <span id="ddk_copp_and_changedisplaysettingsex_gg"></span><span id="DDK_COPP_AND_CHANGEDISPLAYSETTINGSEX_GG"></span>


**This section applies only to Windows Server 2003 SP1 and later, and Windows XP SP2 and later.**

Because applications can alter analog content protection (ACP) levels by calling the Microsoft Win32 **ChangeDisplaySettingsEx** function, the video miniport driver should ensure that adjustments to the ACP protection type through **ChangeDisplaySettingsEx** are independent of adjustments made by the **IAMCertifiedOutputProtection** interface. In other words, if the ACP protection type is set on the physical connector through the video miniport driver's [*COPPCommand*](https://msdn.microsoft.com/library/windows/hardware/ff539642) function, the video miniport driver should not permit disabling the ACP protection type on the physical connector through a [**IOCTL\_VIDEO\_HANDLE\_VIDEOPARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567805) request. Note that user-mode calls to **ChangeDisplaySettingsEx** initiate IOCTL\_VIDEO\_HANDLE\_VIDEOPARAMETERS requests to the video miniport driver.

For more information about the **ChangeDisplaySettingsEx** function, see the Windows SDK documentation.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20COPP%20and%20ChangeDisplaySettingsEx%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




