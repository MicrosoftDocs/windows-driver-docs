---
title: Configuring a Protected Output
description: Configuring a Protected Output
ms.assetid: ff740b37-6e4a-4243-8e83-97dc2a46e3f1
keywords:
- OPM WDK display , configuring protected outputs
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Configuring a Protected Output


The display miniport driver can receive requests to configure the protected output that is associated with a graphics adapter's physical output connector. The display miniport driver's [**DxgkDdiOPMConfigureProtectedOutput**](https://msdn.microsoft.com/library/windows/hardware/ff559701) function is passed a pointer to a [**DXGKMDT\_OPM\_CONFIGURE\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff560849) structure that specifies how to configure the protected output. The **guidSetting** and **abParameters** members of DXGKMDT\_OPM\_CONFIGURE\_PARAMETERS specify the configuration request.

**Note**   Before **DxgkDdiOPMConfigureProtectedOutput** returns, the display miniport driver must verify that the One-key Cipher Block Chaining (CBC)-mode message authentication code (OMAC) that is specified in the **omac** member of DXGKMDT\_OPM\_CONFIGURE\_PARAMETERS is correct. For more information about verifying OMAC, see [OMAC-1 algorithm](http://go.microsoft.com/fwlink/p/?linkid=70417). The driver must also verify that the sequence number that is specified in the **ulSequenceNumber** member of DXGKMDT\_OPM\_CONFIGURE\_PARAMETERS matches the sequence number that the driver currently has stored. The driver must then increment the stored sequence number.

 

The display miniport driver should support the following configuration requests:

-   [Setting the Protection Level for a Protected Output](setting-the-protection-level-for-a-protected-output.md)

-   [Configuring Protection for the Video Signal](configuring-protection-for-the-video-signal.md)

-   [Setting the HDCP SRM Version](setting-the-hdcp-srm-version.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Configuring%20a%20Protected%20Output%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




