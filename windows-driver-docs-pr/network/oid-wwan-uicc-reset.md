---
title: OID_WWAN_UICC_RESET
description: OID_WWAN_UICC_RESET
ms.assetid: D6654B8D-8700-437B-A944-BB273C7D31A1
keywords:
- MB UICC reset, Mobile Broadband UICC reset, Mobile Broadband miniport driver UICC reset
ms.author: windowsdriverdev
ms.date: 08/17/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# OID_WWAN_UICC_RESET

OID_WWAN_UICC_RESET is sent by the mobile broadband host to a modem miniport driver instance to reset its UICC smart card and specify the UICC's passthrough status after reset, or query the passthrough state of the driver instance.

For query requests, the miniport driver responds with the [NDIS_WWAN_UICC_RESET_INFO](TBD) structure, which in turn contains a [WWAN_UICC_RESET_INFO](TBD) structure that represents the passthrough status of the driver instance.

For Set requests, OID_WWAN_UICC_RESET uses the [NDIS_WWAN_SET_UICC_RESET](TBD) structure, which in turn contains a [WWAN_SET_UICC_RESET](TBD) structure that represents the passthrough action the host specifies for the driver after it resets the UICC. After reset is complete, the driver responds with **NDIS_WWAN_UICC_RESET_INFO** to indicate its passthrough status.

For more info about passthrough actions and passthrough status, see [MB UICC reset operations](mb-uicc-reset-operations.md).

## Requirements

| | |
| --- | --- |
| Version | Windows 10, version 1709 |
| Header | Ntddndis.h (include Ndis.h) |

## See also

[NDIS_WWAN_UICC_RESET_INFO](TBD)

[WWAN_UICC_RESET_INFO](TBD)

[NDIS_WWAN_SET_UICC_RESET](TBD)

[WWAN_SET_UICC_RESET](TBD)

[MB UICC reset operations](mb-uicc-reset-operations.md)

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Slicer%20settings%20%20RELEASE:%20%289/2/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")