---
title: Extensible Access Point Indications
description: Extensible Access Point Indications
ms.assetid: 0339DD41-C4F4-4E09-B348-A15EFB101B45
keywords:
- ExtAP status indications WDK Native 802.11
- Extensible Access Point status indications WDK Native 802.11
ms.author: windowsdriverdev
ms.date: 04/26/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Extensible Access Point Indications


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

When a miniport driver operates in Extensible Access Point (ExtAP) mode, it can make the following status indications that are specific to ExtAP mode:

| Name | Description |
| --- | --- |
| [NDIS_STATUS_DOT11_CAN_SUSTAIN_AP](https://msdn.microsoft.com/library/windows/hardware/ff567323) | The driver makes this indication after the NIC stops an 802.11 access point (AP). |
| [NDIS_STATUS_DOT11_INCOMING_ASSOC_COMPLETION](https://msdn.microsoft.com/library/windows/hardware/ff567338) | The driver makes this indication after either a successful or failed incoming association request from a peer station. For more information about Association operations in ExtAP mode, see [Association Operation Guidelines for Extensible Access Point (ExtAP) Mode](association-operation-guidelines-for-extensible-access-point--extap--m.md). |
| [NDIS_STATUS_DOT11_INCOMING_ASSOC_REQUEST_RECEIVED](https://msdn.microsoft.com/library/windows/hardware/ff567339) | The driver makes this indication after the NIC receives an incoming association request frame from a peer station. For more information about Association operations in ExtAP mode, see [Association Operation Guidelines for Extensible Access Point (ExtAP) Mode](association-operation-guidelines-for-extensible-access-point--extap--m.md). |
| [NDIS_STATUS_DOT11_INCOMING_ASSOC_STARTED](https://msdn.microsoft.com/library/windows/hardware/ff567342) | The driver makes this indication when the NIC receives the first valid 802.11 authentication request from a peer station. For more information about Association operations in ExtAP mode, see [Association Operation Guidelines for Extensible Access Point (ExtAP) Mode](association-operation-guidelines-for-extensible-access-point--extap--m.md). |
| [NDIS_STATUS_DOT11_PHY_FREQUENCY_ADOPTED](https://msdn.microsoft.com/library/windows/hardware/ff567351) | The driver makes this indication after it has adopted a channel or frequency to communicate with a peer station.|
| [NDIS_STATUS_DOT11_STOP_AP](https://msdn.microsoft.com/library/windows/hardware/ff567366) | The driver makes this indication when the NIC cannot sustain 802.11 access point (AP) functionality on any of the available PHYs.|

Additionally, a miniport driver operating in ExtAP mode can makethe following status indications:

| Name | Description |
| --- | --- |
| [NDIS_STATUS_DOT11_DISASSOCIATION](https://msdn.microsoft.com/library/windows/hardware/ff567334) | The driver makes this indication after the 802.11 station completes a disassociation operation with an AP or peer station. For more information about this operation, see [Disassociation Operations](disassociation-operations.md). |
| [NDIS_STATUS_DOT11_LINK_QUALITY](https://msdn.microsoft.com/library/windows/hardware/ff567344) | The driver makes this indication whenever the 802.11 station determines the link quality for an association with an AP or peer station that has changed significantly. For more information about link quality and link quality indications, see [Link Quality Operations](link-quality-operations.md). |
| [NDIS_STATUS_DOT11_PHY_STATE_CHANGED](https://msdn.microsoft.com/library/windows/hardware/ff567354) | The driver makes this indication whenever the power state changes on a PHY that is supported by the 802.11 station. |
| [NDIS_STATUS_DOT11_TKIPMIC_FAILURE](https://msdn.microsoft.com/library/windows/hardware/ff567368) | The driver makes this indication whenever a received packet that has been successfully decrypted by the TKIP cipher algorithm fails the message integrity code (MIC) verification. |

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Planning%20your%20APN%20database%20submission%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")
