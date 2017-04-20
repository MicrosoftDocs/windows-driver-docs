---
title: Setting the Protection Level for a Protected Output
description: Setting the Protection Level for a Protected Output
ms.assetid: 2f041190-8001-4e79-8398-8b642884f751
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Setting the Protection Level for a Protected Output


OPM configuration can set the protection level of a protection type on a protected output. To set the protection level, the display miniport driver's [**DxgkDdiOPMConfigureProtectedOutput**](https://msdn.microsoft.com/library/windows/hardware/ff559701) function receives a pointer to a [**DXGKMDT\_OPM\_CONFIGURE\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff560849) structure with the **guidSetting** member set to the DXGKMDT\_OPM\_SET\_PROTECTION\_LEVEL GUID and the **abParameters** member set to a pointer to a [**DXGKMDT\_OPM\_SET\_PROTECTION\_LEVEL\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff560921) structure that specifies the type of protection to set and the level at which to set the protection. The following protection levels can be set for the indicated protection types:

-   For DXGKMDT\_OPM\_PROTECTION\_TYPE\_ACP specified in the **ulProtectionType** member of DXGKMDT\_OPM\_SET\_PROTECTION\_LEVEL\_PARAMETERS, one of the protection-level values from the [**DXGKMDT\_OPM\_ACP\_PROTECTION\_LEVEL**](https://msdn.microsoft.com/library/windows/hardware/ff560834) enumeration can be specified in the **ulProtectionLevel** member of DXGKMDT\_OPM\_SET\_PROTECTION\_LEVEL\_PARAMETERS.

-   For DXGKMDT\_OPM\_PROTECTION\_TYPE\_CGMSA specified in the **ulProtectionType** member of DXGKMDT\_OPM\_SET\_PROTECTION\_LEVEL\_PARAMETERS, one of the protection-level values from the [**DXGKMDT\_OPM\_CGMSA**](https://msdn.microsoft.com/library/windows/hardware/ff560846) enumeration can be specified in the **ulProtectionLevel** member of DXGKMDT\_OPM\_SET\_PROTECTION\_LEVEL\_PARAMETERS.

-   For DXGKMDT\_OPM\_PROTECTION\_TYPE\_HDCP or DXGKMDT\_OPM\_PROTECTION\_TYPE\_COPP\_COMPATIBLE\_HDCP specified in the **ulProtectionType** member of DXGKMDT\_OPM\_SET\_PROTECTION\_LEVEL\_PARAMETERS, one of the protection-level values from the [**DXGKMDT\_OPM\_HDCP\_PROTECTION\_LEVEL**](https://msdn.microsoft.com/library/windows/hardware/ff560878) enumeration can be specified in the **ulProtectionLevel** member of DXGKMDT\_OPM\_SET\_PROTECTION\_LEVEL\_PARAMETERS.

-   For DXGKMDT\_OPM\_PROTECTION\_TYPE\_DPCP specified in the **ulProtectionType** member of DXGKMDT\_OPM\_SET\_PROTECTION\_LEVEL\_PARAMETERS, one of the protection-level values from the [**DXGKMDT\_OPM\_DPCP\_PROTECTION\_LEVEL**](https://msdn.microsoft.com/library/windows/hardware/ff560861) enumeration can be specified in the **ulProtectionLevel** member of DXGKMDT\_OPM\_SET\_PROTECTION\_LEVEL\_PARAMETERS.

**Note**   The DXGKMDT\_OPM\_SET\_PROTECTION\_LEVEL\_ACCORDING\_TO\_CSS\_DVD GUID is new for Windows 7 and is used to indicate that the driver should enable HDCP according to the new CSS rules. Setting the DXGKMDT\_OPM\_SET\_PROTECTION\_LEVEL\_ACCORDING\_TO\_CSS\_DVD command is identical to setting the existing DXGKMDT\_OPM\_SET\_PROTECTION\_LEVEL command except that DXGKMDT\_OPM\_SET\_PROTECTION\_LEVEL\_ACCORDING\_TO\_CSS\_DVD has no absolute requirement to enable the requested protection.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Setting%20the%20Protection%20Level%20for%20a%20Protected%20Output%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




