---
title: Querying for an HD Audio DDI
description: Querying for an HD Audio DDI
ms.assetid: 972bce92-0ecd-486a-a9a8-fcd434ad12a5
keywords:
- HD Audio, querying
- High Definition Audio (HD Audio), querying
- queries WDK audio
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Querying for an HD Audio DDI


To obtain a counted reference to an object with an HD Audio DDI, the function driver for an audio or modem codec sends an [**IRP\_MN\_QUERY\_INTERFACE**](https://msdn.microsoft.com/library/windows/hardware/ff551687) IOCTL to the HD Audio bus driver.

In Windows Vista and later, the HD Audio bus driver supports the [**HDAUDIO\_BUS\_INTERFACE**](https://msdn.microsoft.com/library/windows/hardware/ff536413) and the [**HDAUDIO\_BUS\_INTERFACE\_V2**](https://msdn.microsoft.com/library/windows/hardware/ff536418) versions of the DDI. It does not support the [**HDAUDIO\_BUS\_INTERFACE\_BDL**](https://msdn.microsoft.com/library/windows/hardware/ff536416) version.

An HD Audio bus driver can be installed as an upgrade in Windows Server 2003 and Windows XP. This bus driver supports both DDI versions.

The procedures for obtaining references to the HDAUDIO\_BUS\_INTERFACE, the HDAUDIO\_BUS\_INTERFACE\_V2 and the HDAUDIO\_BUS\_INTERFACE\_BDL versions of the DDI are described in the following sections:

[Obtaining an HDAUDIO\_BUS\_INTERFACE DDI Object](obtaining-an-hdaudio-bus-interface-ddi-object.md)

[Obtaining an HDAUDIO\_BUS\_INTERFACE\_V2 DDI Object](obtaining-an-hdaudio-bus-interface-v2-ddi-object.md)

[Obtaining an HDAUDIO\_BUS\_INTERFACE\_BDL DDI Object](obtaining-an-hdaudio-bus-interface-bdl-ddi-object.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Querying%20for%20an%20HD%20Audio%20DDI%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


