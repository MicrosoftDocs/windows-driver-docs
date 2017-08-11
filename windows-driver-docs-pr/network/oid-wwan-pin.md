---
title: OID\_WWAN\_PIN
author: windows-driver-content
description: OID\_WWAN\_PIN sets or returns information related to Personal Identification Numbers (PINs).
ms.assetid: 5c93ffe0-8067-4022-ba8e-e528e44692e6
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_WWAN_PIN Network Drivers Starting with Windows Vista
---

# OID\_WWAN\_PIN


OID\_WWAN\_PIN sets or returns information related to Personal Identification Numbers (PINs).

Miniport drivers must process set and query requests asynchronously, initially returning NDIS\_STATUS\_INDICATION\_REQUIRED to the original request, and later sending an [**NDIS\_STATUS\_WWAN\_PIN\_INFO**](ndis-status-wwan-pin-info.md) status notification when they have completed the set or query request.

Miniport drivers should send [**NDIS\_STATUS\_WWAN\_PIN\_INFO**](ndis-status-wwan-pin-info.md) status notifications containing an [**NDIS\_WWAN\_PIN\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff567911) structure to return PIN-type and PIN-entry state information, primarily to indicate whether a PIN is required to unlock the MB device or Subscriber Identity Module (SIM card) when completing query requests.

Callers requesting to set information related to PINs provide an [**NDIS\_WWAN\_SET\_PIN**](https://msdn.microsoft.com/library/windows/hardware/ff567922) structure to the miniport driver to send a PIN to the MB device, enable or disable PIN settings, or to change a PIN on the SIM.

Remarks
-------

See [WWAN Pin Operations](https://msdn.microsoft.com/library/windows/hardware/ff559093) for more information about using this OID.

Windows 7 miniport drivers should use OID\_WWAN\_PIN. Windows 8 miniport drivers should use [OID\_WWAN\_PIN\_EX](oid-wwan-pin-ex.md).

Miniport drivers can access the Subscriber Identity Module (SIM card) when processing query operations, but should not access the provider network.

During the miniport driver initialization process, the MB Service does not proceed to registration until PIN1 is successfully unlocked, if enabled.

Miniport drivers provide a PIN value, entered by the end user, in the **PinAction.Pin** member of the NDIS\_WWAN\_SET\_PIN structure when processing set requests. Only when the PIN value matches the value stored in the SIM card should the request be processed by the miniport driver. Otherwise, miniport drivers should fail the set request with status code WWAN\_STATUS\_FAILURE.

CDMA-based devices must report the power-on device lock as PIN1.

For all supported PIN types, miniport drivers must support the *WwanPinOperationEnter* operation. Additionally, if PIN1 is supported, miniport drivers must support the *WwanPinOperationEnable*, *WwanPinOperationDisable*, and *WwanPinOperationChange* operations.

If a PIN disable operation for a PIN type is tried when that PIN type is locked, miniport drivers can either fail the request with WWAN\_STATUS\_PIN\_REQUIRED or they can successfully complete the request. If the miniport driver completes the request successfully, the disable operation should also unlock the PIN.

If reporting multiple PINs are enabled, and only one PIN can be reported at a time, then miniport drivers are expected to report PIN1 first. For example, if reporting of SubsidyLock and SIM PIN1 are enabled, then the SubsidyLock PIN should be reported (in a subsequent query request) only after PIN1 has been successfully verified.

The MB API supports other PINs in addition to PIN1. However, a 3rd-party connection manager/GUI would need to be installed because the Windows Connection Manager/GUI supports only PIN1.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Available in Windows 7 and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_WWAN\_PIN\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff567911)

[**NDIS\_WWAN\_SET\_PIN**](https://msdn.microsoft.com/library/windows/hardware/ff567922)

[**NDIS\_STATUS\_WWAN\_PIN\_INFO**](ndis-status-wwan-pin-info.md)

[WWAN Pin Operations](https://msdn.microsoft.com/library/windows/hardware/ff559093)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_WWAN_PIN%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


