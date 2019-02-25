---
title: NDIS_STATUS_WWAN_PREFERRED_MULTICARRIER_PROVIDERS
description: Miniport drivers use the NDIS_STATUS_WWAN_PREFERRED_MULTICARRIER_PROVIDERS notification to respond to a previous OID_WWAN_PREFERRED_MULTICARRIER_PROVIDERSquery request.Miniport drivers may also use this notification to inform the MB Service about the update as a result of a OID_WWAN_PREFERRED_MULTICARRIER_PROVIDERS set request from the MB Service. A response to an OID_WWAN_PREFERRED_MULTICARRIER_PROVIDERS set request must contain zero elements in the PreferredListHeader member. Miniport drivers can also send unsolicited events with this notification to inform the MB Service that the Preferred Multi-Carrier Provider List (PMCPL) has changed.This notification uses the NDIS_WWAN_PREFERRED_MULTICARRIER_PROVIDERS structure.
ms.assetid: DBE8911D-1A92-40BC-94EB-BED3B8B82CB0
ms.date: 07/18/2017
keywords:
 - NDIS_STATUS_WWAN_PREFERRED_MULTICARRIER_PROVIDERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_WWAN\_PREFERRED\_MULTICARRIER\_PROVIDERS


Miniport drivers use the NDIS\_STATUS\_WWAN\_PREFERRED\_MULTICARRIER\_PROVIDERS notification to respond to a previous [OID\_WWAN\_PREFERRED\_MULTICARRIER\_PROVIDERS](https://msdn.microsoft.com/library/windows/hardware/hh831868)*query* request.

Miniport drivers may also use this notification to inform the MB Service about the update as a result of a OID\_WWAN\_PREFERRED\_MULTICARRIER\_PROVIDERS *set* request from the MB Service. A response to an OID\_WWAN\_PREFERRED\_MULTICARRIER\_PROVIDERS *set* request must contain zero elements in the **PreferredListHeader** member. Miniport drivers can also send unsolicited events with this notification to inform the MB Service that the Preferred Multi-Carrier Provider List (PMCPL) has changed.

This notification uses the [**NDIS\_WWAN\_PREFERRED\_MULTICARRIER\_PROVIDERS**](https://msdn.microsoft.com/library/windows/hardware/hh831864) structure.

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
<td><p>Supported starting with Windows 8.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ndis.h</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_WWAN\_PREFERRED\_MULTICARRIER\_PROVIDERS**](https://msdn.microsoft.com/library/windows/hardware/hh831864)

 

 




