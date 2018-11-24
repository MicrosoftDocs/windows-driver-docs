---
title: OID_WWAN_DEVICE_CAPS_EX
description: OID_WWAN_DEVICE_CAPS_EX is a similar but different OID from OID_WWAN_DEVICE_CAPS.
ms.assetid: BE664B41-3FE7-4E93-8739-12BD2F0AE5B8
keywords:
- OID_WWAN_DEVICE_CAPS_EX, OID per executor, device capability ex
ms.date: 08/08/2017
ms.localizationpriority: medium
---

# OID\_WWAN\_DEVICE\_CAPS\_EX


OID\_WWAN\_DEVICE\_CAPS\_EX is a similar but different OID from [OID\_WWAN\_DEVICE\_CAPS](oid-wwan-device-caps.md). OID\_WWAN\_DEVICE\_CAPS\_EX is a per-executor OID. This OID serves to indicate the hardware’s device/executor capability, including the capability on extended optional features such as LTE attach APN configuration.

Miniport drivers must process query requests asynchronously, initially returning NDIS\_STATUS\_INDICATION\_REQUIRED to the original request before later sending an [**NDIS\_STATUS\_WWAN\_DEVICE\_CAPS\_EX**](https://msdn.microsoft.com/library/windows/hardware/mt782396) status notification containing an [**NDIS\_WWAN\_DEVICE\_CAPS\_EX**](https://msdn.microsoft.com/library/windows/hardware/mt782401) structure, which in turn contains a [**WWAN\_DEVICE\_CAPS\_EX**](https://msdn.microsoft.com/library/windows/hardware/mt799889) structure, to provide information about the device's capability.

The following diagram illustrates a query request.

![executor capability query](images/multi-SIM_6_executorCapabilityQuery.png)

Set requests are not applicable.

Remarks
-------

It is critical for the driver to report service extension capability as a whole including from the driver to the actual device. If a driver supports a service but it is not supported by the underlying hardware, then the service capabilities should be marked as FALSE.

OID\_WWAN\_DEVICE\_CAPS\_EX is also used to retrieve each executor’s capability. This OID is the same in structure as existing [OID\_WWAN\_DEVICE\_CAPS](oid-wwan-device-caps.md) but with the addition of **Executor ID**. A miniport driver should report the highest OID version it supports.

Just as with [OID\_WWAN\_DEVICE\_CAPS](oid-wwan-device-caps.md), the parameters in this OID are not expected to change due to SIM cards but rather represent the modem’s RF capability of the selected executor. A physical hardware modem may have multiple executors and thus may have multiple interfaces that support OID\_WWAN\_DEVICE\_CAPS\_EX.

For possible future updates, if the OS’s requested version is newer than the device-supported version, the device should return the newest version of the OID structure it supports. If the OS’s requested version is older than the latest one supported by the device, then the device should return the version matching the OS’s specification. It is a requirement for IHVs to make sure all revisions of OID\_WWAN\_DEVICE\_CAPS\_EX are supported for backwards compatibility and legacy support.

Unlike other OIDs new to Windows 10 Version 1703 that are only required if the modem supports multi-SIM/multi-executors, this OID must be implemented for modems that would like to support any Microsoft-defined service extensions starting in Windows 10 Version 1703.

Versions of Windows prior to Windows 10 Version 1703 may still use the existing [OID\_WWAN\_DEVICE\_CAPS](oid-wwan-device-caps.md); their behavior with multi-executor capable modems is not a supported scenario. IHVs must define this behavior.

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


[OID\_WWAN\_DEVICE\_CAPS](oid-wwan-device-caps.md)

[**NDIS\_STATUS\_WWAN\_DEVICE\_CAPS\_EX**](https://msdn.microsoft.com/library/windows/hardware/mt782396)

[**NDIS\_WWAN\_DEVICE\_CAPS\_EX**](https://msdn.microsoft.com/library/windows/hardware/mt782401)

[**WWAN\_DEVICE\_CAPS\_EX**](https://msdn.microsoft.com/library/windows/hardware/mt799889)



