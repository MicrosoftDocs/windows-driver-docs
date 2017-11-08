---
title: Cellular COM API design guide
author: windows-driver-content
description: This section provides information on the cellular COM API.
ms.assetid: 93aa20d0-d8c3-40ec-baf1-fab56ff5686d
keywords:
- Cellular COM API design guide network drivers
ms.author: windowsdriverdev
ms.date: 11/07/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Cellular COM API design guide

> [!WARNING]
> The Cellular COM API is deprecated in Windows 10. This content is provided to support maintenance of OEM and mobile operator created Windows Phone 8.1 applications.

This section provides information on the cellular COM API.

The interfaces are provided by two Microsoft Interface Definition Language (MIDL) files:

- cellularapi_oem.idl
- rilapitypes.idl

Use the MIDL compiler to generate header files. For more information, see [Microsoft Interface Definition Language](https://msdn.microsoft.com/library/windows/desktop/aa367091) on the Windows Dev Center.

You must declare appropriate capabilities in the package that contains the cellular application. For more information, see [Cellular COM API capabilities](cellular-com-api-capabilities.md).

## In this section

[Cellular COM API capabilities](cellular-com-api-capabilities.md)

[Communicate with the RIL driver by using the IOemCellularModem interface](communicate-with-the-ril-driver-by-using-the-ioemcellularmodem-interface.md)

## Related topics

[Cellular COM API reference](https://msdn.microsoft.com/library/windows/hardware/dn946508)

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Planning%20your%20APN%20database%20submission%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")