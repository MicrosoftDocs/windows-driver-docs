---
title: OID\_WWAN\_SYS\_CAPS\_INFO
author: windows-driver-content
description: OID\_WWAN\_SYS\_CAPS\_INFO retrieves information about the modem. It can be sent on any of the NDIS instances exposed by the modem.
ms.assetid: D158432A-A715-4ABB-969C-F8F80D2DB845
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_WWAN_SYS_CAPS_INFO Network Drivers Starting with Windows Vista
---

# OID\_WWAN\_SYS\_CAPS\_INFO


OID\_WWAN\_SYS\_CAPS\_INFO retrieves information about the modem. It can be sent on any of the NDIS instances exposed by the modem.

Miniport drivers must process query requests asynchronously, initially returning NDIS\_STATUS\_INDICATION\_REQUIRED to the original request before later sending an [**NDIS\_STATUS\_WWAN\_SYS\_CAPS\_INFO**](https://msdn.microsoft.com/library/windows/hardware/mt782400) status notification containing an [**NDIS\_WWAN\_SYS\_CAPS\_INFO**](https://msdn.microsoft.com/library/windows/hardware/mt782410) structure, which in turn contains a [**WWAN\_SYS\_CAPS\_INFO**](https://msdn.microsoft.com/library/windows/hardware/mt799893) structure, to provide information about the overall modem system capability.

The following diagram illustrates a query request.

![system capability query](images/multi-sim-5-systemcapabilityquery.png)

Set requests are not applicable.

Remarks
-------

The host uses OID\_WWAN\_SYS\_CAPS\_INFO to query the number of devices (executors) and slots in the modem as well as the number of executors that may be active concurrently. A dual-standby modem would have a concurrency of 1; a dual-active modem would have a concurrency of 2. This OID is not executor-specific and may be sent to any NDIS instance.

The modem may expose multiple configurations with differing numbers of executors and slots. Regardless of which configuration is selected, this query will return the maximum number of devices and slots that the modem can support as currently configured.

A modem supporting OID\_WWAN\_SYS\_CAPS\_INFO is expected to also support [OID\_WWAN\_DEVICE\_CAPS\_EX](oid-wwan-device-caps-ex.md). Versions of Windows that support multi-executor modems will not use the legacy [OID\_WWAN\_DEVICE\_CAPS](oid-wwan-device-caps.md) if the underlying modem supports OID\_WWAN\_SYS\_CAPS\_INFO. For legacy versions of the OS (any version before Windows 10 Version 1703 for the purposes of this OID), a multi-executor modem would be represented as multiple independent modems and the existing OID\_WWAN\_DEVICE\_CAPS, available starting in Windows 8, will be used.

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
<td><p>Windows 10, version 1703</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_STATUS\_WWAN\_SYS\_CAPS\_INFO**](https://msdn.microsoft.com/library/windows/hardware/mt782400)

[**NDIS\_WWAN\_SYS\_CAPS\_INFO**](https://msdn.microsoft.com/library/windows/hardware/mt782410)

[**WWAN\_SYS\_CAPS\_INFO**](https://msdn.microsoft.com/library/windows/hardware/mt799893)

[OID\_WWAN\_DEVICE\_CAPS\_EX](oid-wwan-device-caps-ex.md)

[OID\_WWAN\_DEVICE\_CAPS](oid-wwan-device-caps.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_WWAN_SYS_CAPS_INFO%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


