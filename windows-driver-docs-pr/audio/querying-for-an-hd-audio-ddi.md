---
title: Querying for an HD Audio DDI
description: Querying for an HD Audio DDI
ms.assetid: 972bce92-0ecd-486a-a9a8-fcd434ad12a5
keywords:
- HD Audio, querying
- High Definition Audio (HD Audio), querying
- queries WDK audio
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Querying for an HD Audio DDI


To obtain a counted reference to an object with an HD Audio DDI, the function driver for an audio or modem codec sends an [**IRP\_MN\_QUERY\_INTERFACE**](https://msdn.microsoft.com/library/windows/hardware/ff551687) IOCTL to the HD Audio bus driver.

In Windows Vista and later, the HD Audio bus driver supports the [**HDAUDIO\_BUS\_INTERFACE**](https://msdn.microsoft.com/library/windows/hardware/ff536413) and the [**HDAUDIO\_BUS\_INTERFACE\_V2**](https://msdn.microsoft.com/library/windows/hardware/ff536418) versions of the DDI. It does not support the [**HDAUDIO\_BUS\_INTERFACE\_BDL**](https://msdn.microsoft.com/library/windows/hardware/ff536416) version.

An HD Audio bus driver can be installed as an upgrade in Windows Server 2003 and Windows XP. This bus driver supports both DDI versions.

The procedures for obtaining references to the HDAUDIO\_BUS\_INTERFACE, the HDAUDIO\_BUS\_INTERFACE\_V2 and the HDAUDIO\_BUS\_INTERFACE\_BDL versions of the DDI are described in the following sections:

[Obtaining an HDAUDIO\_BUS\_INTERFACE DDI Object](obtaining-an-hdaudio-bus-interface-ddi-object.md)

[Obtaining an HDAUDIO\_BUS\_INTERFACE\_V2 DDI Object](obtaining-an-hdaudio-bus-interface-v2-ddi-object.md)

[Obtaining an HDAUDIO\_BUS\_INTERFACE\_BDL DDI Object](obtaining-an-hdaudio-bus-interface-bdl-ddi-object.md)

 

 




