---
title: Setting the HDCP SRM Version
description: Setting the HDCP SRM Version
ms.assetid: 23f99f8f-7d13-4868-84fb-49245a81958b
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Setting the HDCP SRM Version


OPM configuration can set the version of the High-bandwidth Digital Content Protection (HDCP) System Renewability Message (SRM) for the protected output. To set the version, the display miniport driver's [**DxgkDdiOPMConfigureProtectedOutput**](https://msdn.microsoft.com/library/windows/hardware/ff559701) function receives a pointer to a [**DXGKMDT\_OPM\_CONFIGURE\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff560849) structure with the **guidSetting** member set to the DXGKMDT\_OPM\_SET\_HDCP\_SRM GUID and the **abParameters** member set to a pointer to a [**DXGKMDT\_OPM\_SET\_HDCP\_SRM\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff560915) structure. The DXGKMDT\_OPM\_SET\_HDCP\_SRM\_PARAMETERS structure contains a ULONG that specifies the version number. The least significant bits (bits 0 through 15) contain the SRM's version number in little-endian format. For more information about the SRM version number, see the [HDCP Specification Revision 1.1](http://go.microsoft.com/fwlink/p/?linkid=38728).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Setting%20the%20HDCP%20SRM%20Version%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




