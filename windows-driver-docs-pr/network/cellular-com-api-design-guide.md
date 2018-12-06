---
title: Cellular COM API design guide
description: This section provides information on the cellular COM API.
ms.assetid: 93aa20d0-d8c3-40ec-baf1-fab56ff5686d
keywords:
- Cellular COM API design guide network drivers
ms.date: 11/07/2017
ms.localizationpriority: medium
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

