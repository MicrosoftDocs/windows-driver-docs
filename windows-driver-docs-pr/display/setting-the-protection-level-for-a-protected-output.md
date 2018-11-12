---
title: Setting the Protection Level for a Protected Output
description: Setting the Protection Level for a Protected Output
ms.assetid: 2f041190-8001-4e79-8398-8b642884f751
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Setting the Protection Level for a Protected Output


OPM configuration can set the protection level of a protection type on a protected output. To set the protection level, the display miniport driver's [**DxgkDdiOPMConfigureProtectedOutput**](https://msdn.microsoft.com/library/windows/hardware/ff559701) function receives a pointer to a [**DXGKMDT\_OPM\_CONFIGURE\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff560849) structure with the **guidSetting** member set to the DXGKMDT\_OPM\_SET\_PROTECTION\_LEVEL GUID and the **abParameters** member set to a pointer to a [**DXGKMDT\_OPM\_SET\_PROTECTION\_LEVEL\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff560921) structure that specifies the type of protection to set and the level at which to set the protection. The following protection levels can be set for the indicated protection types:

-   For DXGKMDT\_OPM\_PROTECTION\_TYPE\_ACP specified in the **ulProtectionType** member of DXGKMDT\_OPM\_SET\_PROTECTION\_LEVEL\_PARAMETERS, one of the protection-level values from the [**DXGKMDT\_OPM\_ACP\_PROTECTION\_LEVEL**](https://msdn.microsoft.com/library/windows/hardware/ff560834) enumeration can be specified in the **ulProtectionLevel** member of DXGKMDT\_OPM\_SET\_PROTECTION\_LEVEL\_PARAMETERS.

-   For DXGKMDT\_OPM\_PROTECTION\_TYPE\_CGMSA specified in the **ulProtectionType** member of DXGKMDT\_OPM\_SET\_PROTECTION\_LEVEL\_PARAMETERS, one of the protection-level values from the [**DXGKMDT\_OPM\_CGMSA**](https://msdn.microsoft.com/library/windows/hardware/ff560846) enumeration can be specified in the **ulProtectionLevel** member of DXGKMDT\_OPM\_SET\_PROTECTION\_LEVEL\_PARAMETERS.

-   For DXGKMDT\_OPM\_PROTECTION\_TYPE\_HDCP or DXGKMDT\_OPM\_PROTECTION\_TYPE\_COPP\_COMPATIBLE\_HDCP specified in the **ulProtectionType** member of DXGKMDT\_OPM\_SET\_PROTECTION\_LEVEL\_PARAMETERS, one of the protection-level values from the [**DXGKMDT\_OPM\_HDCP\_PROTECTION\_LEVEL**](https://msdn.microsoft.com/library/windows/hardware/ff560878) enumeration can be specified in the **ulProtectionLevel** member of DXGKMDT\_OPM\_SET\_PROTECTION\_LEVEL\_PARAMETERS.

-   For DXGKMDT\_OPM\_PROTECTION\_TYPE\_DPCP specified in the **ulProtectionType** member of DXGKMDT\_OPM\_SET\_PROTECTION\_LEVEL\_PARAMETERS, one of the protection-level values from the [**DXGKMDT\_OPM\_DPCP\_PROTECTION\_LEVEL**](https://msdn.microsoft.com/library/windows/hardware/ff560861) enumeration can be specified in the **ulProtectionLevel** member of DXGKMDT\_OPM\_SET\_PROTECTION\_LEVEL\_PARAMETERS.

**Note**   The DXGKMDT\_OPM\_SET\_PROTECTION\_LEVEL\_ACCORDING\_TO\_CSS\_DVD GUID is new for Windows 7 and is used to indicate that the driver should enable HDCP according to the new CSS rules. Setting the DXGKMDT\_OPM\_SET\_PROTECTION\_LEVEL\_ACCORDING\_TO\_CSS\_DVD command is identical to setting the existing DXGKMDT\_OPM\_SET\_PROTECTION\_LEVEL command except that DXGKMDT\_OPM\_SET\_PROTECTION\_LEVEL\_ACCORDING\_TO\_CSS\_DVD has no absolute requirement to enable the requested protection.

 

 

 





