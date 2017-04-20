---
title: Using Multiple Multiple-Head Adapters
description: Using Multiple Multiple-Head Adapters
ms.assetid: 632652f9-8d21-4a2f-91a6-03e3ba47d632
keywords:
- multiple-head hardware WDK DirectX 9.0 , adapters
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Using Multiple Multiple-Head Adapters


## <span id="ddk_using_multiple_multiple_head_adapters_gg"></span><span id="DDK_USING_MULTIPLE_MULTIPLE_HEAD_ADAPTERS_GG"></span>


The driver can provide multiple-head support if the system is equipped with more than one multiple-head card. If the driver owns more than one multiple-head card, then the driver must ensure that the separate multiple-head cards remain independent.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Using%20Multiple%20Multiple-Head%20Adapters%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




