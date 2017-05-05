---
title: RunAs
description: RunAs
ms.assetid: 47183A50-513C-4bc5-8DC4-33065323F584
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# RunAs


TAEF provides a mechanism to execute tests Elevated, Restricted, as Local System or within a Low Integrity process.

## <span id="Prerequisites"></span><span id="prerequisites"></span><span id="PREREQUISITES"></span>Prerequisites


-   [Te.Service](te-service.md) must be installed and running on the machine in order to run elevated tests from a non-elevated process, run non-elevated tests from an elevated process, or to run tests as Local System.

## <span id="RunAs_Types"></span><span id="runas_types"></span><span id="RUNAS_TYPES"></span>RunAs Types


TAEF supports the following RunAs types, which are specified via test metadata or the command prompt.

-   [RunAs Elevated](runas-elevated.md)
-   [RunAs LowIL](runas-lowil.md)
-   [RunAs Restricted](runas-restricted.md)
-   [RunAs System](runas-system.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[taef\taef]:%20RunAs%20%20RELEASE:%20%289/12/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




