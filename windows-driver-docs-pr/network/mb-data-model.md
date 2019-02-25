---
title: MB Data Model
description: MB Data Model
ms.assetid: 922b6b55-c332-4721-bbd1-571b0e154df3
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# MB Data Model


The MB driver model uses a data model that consists of a set of objects defined as abstractions of MB device features. Each object is identified by a unique object identifier (OID) and is defined by a set of corresponding attributes. The set of attributes is organized into a data structure. To manage the device, the MB Service and the MB miniport driver exchange OIDs and their associated data structures based on OID requests and indications provided by the Network Driver Interface Specification (NDIS).

In the MB driver model, only *set* and *query* operations are used for OID requests. The MB driver model does not use *method* operations. For indications, the MB driver model uses both event and transactional notifications to indicate state changes in the objects of the MB device. Transactional notifications also signal completion of an asynchronous transaction.

The following tables list the OIDs and status indications defined for MB miniport drivers, as well as the associated data structures. MB miniport drivers must implement all mandatory general OIDs that the NDIS 6.20 Specification requires. For a list of general OIDs for NDIS 6.x, see [General Operational OIDs](https://msdn.microsoft.com/library/windows/hardware/ff552474).

In addition, MB miniport drivers must implement OID\_GEN\_PHYSICAL\_MEDIUM even though the NDIS Specification describes it as optional to implement.

The syntax and semantics of the MB OIDs listed in the following table are described in [MB Operational Semantics](mb-operational-semantics.md). The interactions between the MB Service and the MB miniport driver are described in [MB Operation Flowcharts](mb-operation-flowcharts.md).

## WWAN-Specific OIDs

| OID and Corresponding Data Structure | Set operation |   | Query operation |   | GSM/CDMA |
| ---                                  | ---       | ---       | ---       | ---       |--- |
|                                      | Windows 7 | Windows 8 | Windows 7 | Windows 8 |    |
| [OID\_WWAN\_DRIVER\_CAPS](https://msdn.microsoft.com/library/windows/hardware/ff569825) uses [**NDIS\_WWAN\_DRIVER\_CAPS**](https://msdn.microsoft.com/library/windows/hardware/ff567908) | Not supported | Not supported |S | S | GSM, CDMA |
| [OID\_WWAN\_DEVICE\_CAPS](https://msdn.microsoft.com/library/windows/hardware/ff569824) has no corresponding structure | Not supported | Not supported | A | A | GSM, CDMA |
| [OID\_WWAN\_READY\_INFO](https://msdn.microsoft.com/library/windows/hardware/ff569833) has no corresponding structure | Not supported Not supported | A | A | GSM, CDMA |
| [OID\_WWAN\_SERVICE\_ACTIVATION](https://msdn.microsoft.com/library/windows/hardware/ff569835)† uses [**NDIS\_WWAN\_SERVICE\_ACTIVATION**](https://msdn.microsoft.com/library/windows/hardware/ff567918) | A | A | Not supported | Not supported | GSM, CDMA |
| [OID\_WWAN\_RADIO\_STATE](https://msdn.microsoft.com/library/windows/hardware/ff569832) uses [**NDIS\_WWAN\_SET\_RADIO\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff567925) | A | A | A | A | GSM, CDMA |
| [OID\_WWAN\_PIN](https://msdn.microsoft.com/library/windows/hardware/ff569828) uses [**NDIS\_WWAN\_SET\_PIN**](https://msdn.microsoft.com/library/windows/hardware/ff567922) | A | Not supported | A | Not supported | GSM, CDMA |
| [OID\_WWAN\_PIN\_LIST](https://msdn.microsoft.com/library/windows/hardware/ff569829) has no corresponding structure | Not supported | Not supported | A | A | GSM, CDMA |
| [OID\_WWAN\_PIN\_EX](https://msdn.microsoft.com/library/windows/hardware/hh440095) uses [**NDIS\_WWAN\_SET\_PIN\_EX**](https://msdn.microsoft.com/library/windows/hardware/hh439842) | Not supported | A | Not supported | A | GSM, CDMA |
| [OID\_WWAN\_HOME\_PROVIDER](https://msdn.microsoft.com/library/windows/hardware/ff569826) has no corresponding structure | Not supported | Not supported | A | A | GSM, CDMA |
| [OID\_WWAN\_PREFERRED\_PROVIDERS](https://msdn.microsoft.com/library/windows/hardware/ff569830)† uses [**NDIS\_WWAN\_SET\_PREFERRED\_PROVIDERS**](https://msdn.microsoft.com/library/windows/hardware/ff567923) | A | A | A | A | GSM only |
| [OID\_WWAN\_VISIBLE\_PROVIDERS](https://msdn.microsoft.com/library/windows/hardware/ff569843) has no corresponding structure | Not supported | Not supported | A | A | GSM |
| [OID\_WWAN\_REGISTER\_STATE](https://msdn.microsoft.com/library/windows/hardware/ff569834) uses [**NDIS\_WWAN\_SET\_REGISTER\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff567926) | A | A | A | A | CDMA |
| [OID\_WWAN\_SIGNAL\_STATE](https://msdn.microsoft.com/library/windows/hardware/ff569836) uses [**NDIS\_WWAN\_SET\_SIGNAL\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567928) | A | A | A | A | GSM, CDMA |
| [OID\_WWAN\_PACKET\_SERVICE](https://msdn.microsoft.com/library/windows/hardware/ff569827) uses [**NDIS\_WWAN\_SET\_PACKET\_SERVICE**](https://msdn.microsoft.com/library/windows/hardware/ff567921) | A | A | A | A | GSM, CDMA |
| [OID\_WWAN\_PROVISIONED\_CONTEXTS](https://msdn.microsoft.com/library/windows/hardware/ff569831)†† uses [**NDIS\_WWAN\_SET\_PROVISIONED\_CONTEXT**](https://msdn.microsoft.com/library/windows/hardware/ff567924) | A | A | A | A | GSM, CDMA |
| [OID\_WWAN\_CONNECT](https://msdn.microsoft.com/library/windows/hardware/ff569823) uses [**NDIS\_WWAN\_SET\_CONTEXT\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff567920) | A | A | A | A | GSM, CDMA |
| [OID\_WWAN\_SMS\_CONFIGURATION](https://msdn.microsoft.com/library/windows/hardware/ff569837) uses [**NDIS\_WWAN\_SET\_SMS\_CONFIGURATION**](https://msdn.microsoft.com/library/windows/hardware/ff567929) | A | A | A | A | GSM, CDMA | 
| [OID\_WWAN\_SMS\_READ](https://msdn.microsoft.com/library/windows/hardware/ff569839) uses [**NDIS\_WWAN\_SMS\_READ**](https://msdn.microsoft.com/library/windows/hardware/ff567941) | Not supported | A | A | A |GSM, CDMA | 
| [OID\_WWAN\_SMS\_SEND](https://msdn.microsoft.com/library/windows/hardware/ff569840) uses [**NDIS\_WWAN\_SMS\_SEND**](https://msdn.microsoft.com/library/windows/hardware/ff567943) | A | A | Not supported | Not supported | GSM, CDMA |
| [OID\_WWAN\_SMS\_DELETE](https://msdn.microsoft.com/library/windows/hardware/ff569838) uses [**NDIS\_WWAN\_SMS\_DELETE**](https://msdn.microsoft.com/library/windows/hardware/ff567938) | A | A | Not supported | Not supported |  GSM, CDMA |
| [OID\_WWAN\_SMS\_STATUS](https://msdn.microsoft.com/library/windows/hardware/ff569841) uses [**NDIS\_WWAN\_SMS\_STATUS**](https://msdn.microsoft.com/library/windows/hardware/ff567945) | Not supported | Not supported | A | A | GSM, CDMA |
| [OID\_WWAN\_VENDOR\_SPECIFIC](https://msdn.microsoft.com/library/windows/hardware/ff569842)† uses a vendor-defined structure | A | A | Not supported | Not supported | GSM, CDMA |
| [OID\_WWAN\_DEVICE\_SERVICES](https://msdn.microsoft.com/library/windows/hardware/hh440093) has no corresponding structure | Not supported | Not supported | Not supported | A | GSM, CDMA |
| [OID\_WWAN\_SUBSCRIBE\_DEVICE\_SERVICE\_EVENTS](https://msdn.microsoft.com/library/windows/hardware/hh440096) uses [**NDIS\_WWAN\_SUBSCRIBE\_DEVICE\_SERVICE\_EVENTS**](https://msdn.microsoft.com/library/windows/hardware/hh439843) | Not supported | A | Not supported | Not supported | GSM, CDMA |
| [OID\_WWAN\_AUTH\_CHALLENGE](https://msdn.microsoft.com/library/windows/hardware/hh440092) uses [**NDIS\_WWAN\_AUTH\_CHALLENGE**](https://msdn.microsoft.com/library/windows/hardware/hh439833) | Not supported | Not supported | Not supported | A | GSM, CDMA |
| [OID\_WWAN\_USSD](https://msdn.microsoft.com/library/windows/hardware/hh440100) uses [**NDIS\_WWAN\_USSD\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/hh439846) | Not supported | A | Not supported | Not supported | GSM |
| [OID\_WWAN\_DEVICE\_SERVICE\_COMMAND](https://msdn.microsoft.com/library/windows/hardware/hh440094) uses [**NDIS\_WWAN\_DEVICE\_SERVICE\_COMMAND**](https://msdn.microsoft.com/library/windows/hardware/hh439836) | Not supported | A | Not supported | A| GSM, CDMA |

> [!NOTE]
> The following notes apply to the preceding table:
> † represents optional OIDs that miniport drivers may support. Miniport drivers that do not support the optional OIDs must not return them in OID\_GEN\_SUPPORTED\_LIST.
>
> †† represents miniport drivers that support GSM-based devices which can optionally support OID\_WWAN\_PROVISIONED\_CONTEXTS set and query operations. Miniport drivers that support CDMA-based devices can optionally support OID\_WWAN\_PROVISIONED\_CONTEXTS query operations for CDMA-based devices that report Simple IP (WWAN\_CTRL\_CAPS\_CDMA\_SIMPLE\_IP).
>
> Miniport drivers must support all non-optional OIDs. The MB Service may ignore any miniport driver that does not report all of the mandatory OIDs.
> 
> "A" and "S" in the Set and Query operation columns in the preceding table reflect the nature of the transaction for completing the OID request: "A" stands for an asynchronous transaction and "S" for a synchronous transaction.
>
> The data structures in the preceding table correspond to set operation OIDs and to return data for synchronous query operation OIDs.
> 
> The following OIDs share a common variable length list data structure called [**WWAN\_LIST\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff571208) in their corresponding data structures:
> -   OID\_WWAN\_READY\_INFO
> -   OID\_WWAN\_PREFERRED\_PROVIDERS
> -   OID\_WWAN\_VISIBLE\_PROVIDERS
> -   OID\_WWAN\_PROVISIONED\_CONTEXTS
> -   OID\_WWAN\_SMS\_READ 

## WWAN-Specific Indications, Corresponding Data Structures, and OS Revisions

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Indication</strong> and <strong>Corresponding Data Structure</strong></p></td>
<td align="left"><p><strong>Windows 7 Revision</strong></p>
<p><strong>Windows 8 Revision</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567845" data-raw-source="[&lt;strong&gt;NDIS_STATUS_WWAN_DEVICE_CAPS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567845)"><strong>NDIS_STATUS_WWAN_DEVICE_CAPS</strong></a></p>
<p>uses <a href="https://msdn.microsoft.com/library/windows/hardware/ff567907" data-raw-source="[&lt;strong&gt;NDIS_WWAN_DEVICE_CAPS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567907)"><strong>NDIS_WWAN_DEVICE_CAPS</strong></a></p></td>
<td align="left"><p>NDIS_WWAN_DEVICE_CAPS_REVISION_1</p>
<p>NDIS_WWAN_DEVICE_CAPS_REVISION_2</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567856" data-raw-source="[&lt;strong&gt;NDIS_STATUS_WWAN_READY_INFO&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567856)"><strong>NDIS_STATUS_WWAN_READY_INFO</strong></a></p>
<p>uses <a href="https://msdn.microsoft.com/library/windows/hardware/ff567916" data-raw-source="[&lt;strong&gt;NDIS_WWAN_READY_INFO&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567916)"><strong>NDIS_WWAN_READY_INFO</strong></a></p></td>
<td align="left"><p>NDIS_WWAN_READY_INFO_REVISION_1</p>
<p>NDIS_WWAN_READY_INFO_REVISION_1</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567855" data-raw-source="[&lt;strong&gt;NDIS_STATUS_WWAN_RADIO_STATE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567855)"><strong>NDIS_STATUS_WWAN_RADIO_STATE</strong></a></p>
<p>uses <a href="https://msdn.microsoft.com/library/windows/hardware/ff567915" data-raw-source="[&lt;strong&gt;NDIS_WWAN_RADIO_STATE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567915)"><strong>NDIS_WWAN_RADIO_STATE</strong></a></p></td>
<td align="left"><p>NDIS_WWAN_RADIO_STATE_REVISION_1</p>
<p>NDIS_WWAN_RADIO_STATE_REVISION_1</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567851" data-raw-source="[&lt;strong&gt;NDIS_STATUS_WWAN_PIN_INFO&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567851)"><strong>NDIS_STATUS_WWAN_PIN_INFO</strong></a></p>
<p>uses <a href="https://msdn.microsoft.com/library/windows/hardware/ff567911" data-raw-source="[&lt;strong&gt;NDIS_WWAN_PIN_INFO&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567911)"><strong>NDIS_WWAN_PIN_INFO</strong></a></p></td>
<td align="left"><p>NDIS_WWAN_PIN_INFO_REVISION_1</p>
<p>NDIS_WWAN_PIN_INFO_REVISION_1</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567852" data-raw-source="[&lt;strong&gt;NDIS_STATUS_WWAN_PIN_LIST&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567852)"><strong>NDIS_STATUS_WWAN_PIN_LIST</strong></a></p>
<p>uses <a href="https://msdn.microsoft.com/library/windows/hardware/ff567912" data-raw-source="[&lt;strong&gt;NDIS_WWAN_PIN_LIST&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567912)"><strong>NDIS_WWAN_PIN_LIST</strong></a></p></td>
<td align="left"><p>NDIS_WWAN_PIN_LIST_REVISION_1</p>
<p>NDIS_WWAN_PIN_LIST_REVISION_1</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567858" data-raw-source="[&lt;strong&gt;NDIS_STATUS_WWAN_SERVICE_ACTIVATION&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567858)"><strong>NDIS_STATUS_WWAN_SERVICE_ACTIVATION</strong></a>†</p>
<p>uses <a href="https://msdn.microsoft.com/library/windows/hardware/ff567919" data-raw-source="[&lt;strong&gt;NDIS_WWAN_SERVICE_ACTIVATION_STATUS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567919)"><strong>NDIS_WWAN_SERVICE_ACTIVATION_STATUS</strong></a></p></td>
<td align="left"><p>NDIS_WWAN_SERVICE_ACTIVATION_STATUS_REVISION_1</p>
<p>NDIS_WWAN_SERVICE_ACTIVATION_STATUS_REVISION_1</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567848" data-raw-source="[&lt;strong&gt;NDIS_STATUS_WWAN_HOME_PROVIDER&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567848)"><strong>NDIS_STATUS_WWAN_HOME_PROVIDER</strong></a></p>
<p>uses <a href="https://msdn.microsoft.com/library/windows/hardware/ff567909" data-raw-source="[&lt;strong&gt;NDIS_WWAN_HOME_PROVIDER&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567909)"><strong>NDIS_WWAN_HOME_PROVIDER</strong></a></p></td>
<td align="left"><p>NDIS_WWAN_HOME_PROVIDER_REVISION_1</p>
<p>NDIS_WWAN_HOME_PROVIDER_REVISION_1</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567853" data-raw-source="[&lt;strong&gt;NDIS_STATUS_WWAN_PREFERRED_PROVIDERS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567853)"><strong>NDIS_STATUS_WWAN_PREFERRED_PROVIDERS</strong></a>†</p>
<p>uses <a href="https://msdn.microsoft.com/library/windows/hardware/ff567913" data-raw-source="[&lt;strong&gt;NDIS_WWAN_PREFERRED_PROVIDERS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567913)"><strong>NDIS_WWAN_PREFERRED_PROVIDERS</strong></a></p></td>
<td align="left"><p>NDIS_WWAN_PREFERRED_PROVIDERS_REVISION_1</p>
<p>NDIS_WWAN_PREFERRED_PROVIDERS_REVISION_1</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567866" data-raw-source="[&lt;strong&gt;NDIS_STATUS_WWAN_VISIBLE_PROVIDERS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567866)"><strong>NDIS_STATUS_WWAN_VISIBLE_PROVIDERS</strong></a></p>
<p>uses <a href="https://msdn.microsoft.com/library/windows/hardware/ff567948" data-raw-source="[&lt;strong&gt;NDIS_WWAN_VISIBLE_PROVIDERS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567948)"><strong>NDIS_WWAN_VISIBLE_PROVIDERS</strong></a></p></td>
<td align="left"><p>NDIS_WWAN_VISIBLE_PROVIDERS_REVISION_1</p>
<p>NDIS_WWAN_VISIBLE_PROVIDERS_REVISION_1</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567857" data-raw-source="[&lt;strong&gt;NDIS_STATUS_WWAN_REGISTER_STATE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567857)"><strong>NDIS_STATUS_WWAN_REGISTER_STATE</strong></a></p>
<p>uses <a href="https://msdn.microsoft.com/library/windows/hardware/ff567917" data-raw-source="[&lt;strong&gt;NDIS_WWAN_REGISTRATION_STATE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567917)"><strong>NDIS_WWAN_REGISTRATION_STATE</strong></a></p></td>
<td align="left"><p>NDIS_WWAN_REGISTRATION_STATE_REVISION_1</p>
<p>NDIS_WWAN_REGISTRATION_STATE_REVISION_2</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567859" data-raw-source="[&lt;strong&gt;NDIS_STATUS_WWAN_SIGNAL_STATE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567859)"><strong>NDIS_STATUS_WWAN_SIGNAL_STATE</strong></a></p>
<p>uses <a href="https://msdn.microsoft.com/library/windows/hardware/ff567931" data-raw-source="[&lt;strong&gt;NDIS_WWAN_SIGNAL_STATE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567931)"><strong>NDIS_WWAN_SIGNAL_STATE</strong></a></p></td>
<td align="left"><p>NDIS_WWAN_SIGNAL_STATE_REVISION_1</p>
<p>NDIS_WWAN_SIGNAL_STATE_REVISION_1</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567850" data-raw-source="[&lt;strong&gt;NDIS_STATUS_WWAN_PACKET_SERVICE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567850)"><strong>NDIS_STATUS_WWAN_PACKET_SERVICE</strong></a></p>
<p>uses <a href="https://msdn.microsoft.com/library/windows/hardware/ff567910" data-raw-source="[&lt;strong&gt;NDIS_WWAN_PACKET_SERVICE_STATE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567910)"><strong>NDIS_WWAN_PACKET_SERVICE_STATE</strong></a></p></td>
<td align="left"><p>NDIS_WWAN_PACKET_SERVICE_STATE_REVISION_1</p>
<p>NDIS_WWAN_PACKET_SERVICE_STATE_REVISION_1</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567854" data-raw-source="[&lt;strong&gt;NDIS_STATUS_WWAN_PROVISIONED_CONTEXTS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567854)"><strong>NDIS_STATUS_WWAN_PROVISIONED_CONTEXTS</strong></a></p>
<p>uses <a href="https://msdn.microsoft.com/library/windows/hardware/ff567914" data-raw-source="[&lt;strong&gt;NDIS_WWAN_PROVISIONED_CONTEXTS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567914)"><strong>NDIS_WWAN_PROVISIONED_CONTEXTS</strong></a></p></td>
<td align="left"><p>NDIS_WWAN_PROVISIONED_CONTEXTS_REVISION_1</p>
<p>NDIS_WWAN_PROVISIONED_CONTEXTS_REVISION_1</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567843" data-raw-source="[&lt;strong&gt;NDIS_STATUS_WWAN_CONTEXT_STATE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567843)"><strong>NDIS_STATUS_WWAN_CONTEXT_STATE</strong></a></p>
<p>uses <a href="https://msdn.microsoft.com/library/windows/hardware/ff567906" data-raw-source="[&lt;strong&gt;NDIS_WWAN_CONTEXT_STATE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567906)"><strong>NDIS_WWAN_CONTEXT_STATE</strong></a></p></td>
<td align="left"><p>NDIS_WWAN_CONTEXT_STATE_REVISION_1</p>
<p>NDIS_WWAN_CONTEXT_STATE_REVISION_1</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567860" data-raw-source="[&lt;strong&gt;NDIS_STATUS_WWAN_SMS_CONFIGURATION&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567860)"><strong>NDIS_STATUS_WWAN_SMS_CONFIGURATION</strong></a></p>
<p>uses <a href="https://msdn.microsoft.com/library/windows/hardware/ff567935" data-raw-source="[&lt;strong&gt;NDIS_WWAN_SMS_CONFIGURATION&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567935)"><strong>NDIS_WWAN_SMS_CONFIGURATION</strong></a></p></td>
<td align="left"><p>NDIS_WWAN_SMS_CONFIGURATION_REVISION_1</p>
<p>NDIS_WWAN_SMS_CONFIGURATION_REVISION_1</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567862" data-raw-source="[&lt;strong&gt;NDIS_STATUS_WWAN_SMS_RECEIVE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567862)"><strong>NDIS_STATUS_WWAN_SMS_RECEIVE</strong></a></p>
<p>uses <a href="https://msdn.microsoft.com/library/windows/hardware/ff567942" data-raw-source="[&lt;strong&gt;NDIS_WWAN_SMS_RECEIVE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567942)"><strong>NDIS_WWAN_SMS_RECEIVE</strong></a></p></td>
<td align="left"><p>NDIS_WWAN_SMS_RECEIVE_REVISION_1</p>
<p>NDIS_WWAN_SMS_RECEIVE_REVISION_1</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567863" data-raw-source="[&lt;strong&gt;NDIS_STATUS_WWAN_SMS_SEND&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567863)"><strong>NDIS_STATUS_WWAN_SMS_SEND</strong></a></p>
<p>uses <a href="https://msdn.microsoft.com/library/windows/hardware/ff567944" data-raw-source="[&lt;strong&gt;NDIS_WWAN_SMS_SEND_STATUS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567944)"><strong>NDIS_WWAN_SMS_SEND_STATUS</strong></a></p></td>
<td align="left"><p>NDIS_WWAN_SMS_SEND_STATUS_REVISION_1</p>
<p>NDIS_WWAN_SMS_SEND_STATUS_REVISION_1</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567861" data-raw-source="[&lt;strong&gt;NDIS_STATUS_WWAN_SMS_DELETE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567861)"><strong>NDIS_STATUS_WWAN_SMS_DELETE</strong></a></p>
<p>uses <a href="https://msdn.microsoft.com/library/windows/hardware/ff567940" data-raw-source="[&lt;strong&gt;NDIS_WWAN_SMS_DELETE_STATUS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567940)"><strong>NDIS_WWAN_SMS_DELETE_STATUS</strong></a></p></td>
<td align="left"><p>NDIS_WWAN_SMS_DELETE_STATUS_REVISION_1</p>
<p>NDIS_WWAN_SMS_DELETE_STATUS_REVISION_1</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567864" data-raw-source="[&lt;strong&gt;NDIS_STATUS_WWAN_SMS_STATUS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567864)"><strong>NDIS_STATUS_WWAN_SMS_STATUS</strong></a></p>
<p>uses <a href="https://msdn.microsoft.com/library/windows/hardware/ff567945" data-raw-source="[&lt;strong&gt;NDIS_WWAN_SMS_STATUS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567945)"><strong>NDIS_WWAN_SMS_STATUS</strong></a></p></td>
<td align="left"><p>NDIS_WWAN_SMS_STATUS_REVISION_1</p>
<p>NDIS_WWAN_SMS_STATUS_REVISION_1</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567865" data-raw-source="[&lt;strong&gt;NDIS_STATUS_WWAN_VENDOR_SPECIFIC&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567865)"><strong>NDIS_STATUS_WWAN_VENDOR_SPECIFIC</strong></a>†</p>
<p>uses a vendor-defined structure</p></td>
<td align="left"><p>N/A</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/hh439822" data-raw-source="[&lt;strong&gt;NDIS_STATUS_WWAN_USSD&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh439822)"><strong>NDIS_STATUS_WWAN_USSD</strong></a></p>
<p>uses <a href="https://msdn.microsoft.com/library/windows/hardware/hh439844" data-raw-source="[&lt;strong&gt;NDIS_WWAN_USSD_EVENT&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh439844)"><strong>NDIS_WWAN_USSD_EVENT</strong></a></p></td>
<td align="left"><p>NDIS_WWAN_USSD_EVENT_REVISION_1</p>
<p>NDIS_WWAN_USSD_EVENT_REVISION_1</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/hh846210" data-raw-source="[&lt;strong&gt;NDIS_STATUS_WWAN_DEVICE_SERVICE_SUPPORTED_COMMANDS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh846210)"><strong>NDIS_STATUS_WWAN_DEVICE_SERVICE_SUPPORTED_COMMANDS</strong></a></p>
<p>uses <a href="https://msdn.microsoft.com/library/windows/hardware/hh846214" data-raw-source="[&lt;strong&gt;NDIS_WWAN_DEVICE_SERVICE_SUPPORTED_COMMANDS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh846214)"><strong>NDIS_WWAN_DEVICE_SERVICE_SUPPORTED_COMMANDS</strong></a></p></td>
<td align="left"><p>NDIS_WWAN_DEVICE_SERVICES_REVISION_1</p>
<p>NDIS_WWAN_DEVICE_SERVICES_REVISION_1</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/hh846205" data-raw-source="[&lt;strong&gt;NDIS_STATUS_WWAN_DEVICE_SERVICE_RESPONSE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh846205)"><strong>NDIS_STATUS_WWAN_DEVICE_SERVICE_RESPONSE</strong></a></p>
<p>uses <a href="https://msdn.microsoft.com/library/windows/hardware/hh439838" data-raw-source="[&lt;strong&gt;NDIS_WWAN_DEVICE_SERVICE_RESPONSE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh439838)"><strong>NDIS_WWAN_DEVICE_SERVICE_RESPONSE</strong></a></p></td>
<td align="left"><p>NDIS_WWAN_DEVICE_SERVICE_RESPONSE_REVISION_1</p>
<p>NDIS_WWAN_DEVICE_SERVICE_RESPONSE_REVISION_1</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/hh846204" data-raw-source="[&lt;strong&gt;NDIS_STATUS_WWAN_DEVICE_SERVICE_EVENT&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh846204)"><strong>NDIS_STATUS_WWAN_DEVICE_SERVICE_EVENT</strong></a></p>
<p>uses <a href="https://msdn.microsoft.com/library/windows/hardware/hh439837" data-raw-source="[&lt;strong&gt;NDIS_WWAN_DEVICE_SERVICE_EVENT&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh439837)"><strong>NDIS_WWAN_DEVICE_SERVICE_EVENT</strong></a></p></td>
<td align="left"><p>NDIS_WWAN_DEVICE_SERVICE_EVENT_REVISION_1</p>
<p>NDIS_WWAN_DEVICE_SERVICE_EVENT_REVISION_1</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/hh846209" data-raw-source="[&lt;strong&gt;NDIS_STATUS_WWAN_DEVICE_SERVICE_SUBSCRIPTION&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh846209)"><strong>NDIS_STATUS_WWAN_DEVICE_SERVICE_SUBSCRIPTION</strong></a></p>
<p>uses <a href="https://msdn.microsoft.com/library/windows/hardware/hh439839" data-raw-source="[&lt;strong&gt;NDIS_WWAN_DEVICE_SERVICE_SUBSCRIPTION&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh439839)"><strong>NDIS_WWAN_DEVICE_SERVICE_SUBSCRIPTION</strong></a></p></td>
<td align="left"><p>NDIS_WWAN_DEVICE_SERVICE_SUBSCRIPTION_REVISION_1</p>
<p>NDIS_WWAN_DEVICE_SERVICE_SUBSCRIPTION_REVISION_1</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/hh439821" data-raw-source="[&lt;strong&gt;NDIS_STATUS_WWAN_AUTH_RESPONSE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh439821)"><strong>NDIS_STATUS_WWAN_AUTH_RESPONSE</strong></a></p>
<p>uses <a href="https://msdn.microsoft.com/library/windows/hardware/hh439834" data-raw-source="[&lt;strong&gt;NDIS_WWAN_AUTH_RESPONSE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh439834)"><strong>NDIS_WWAN_AUTH_RESPONSE</strong></a></p></td>
<td align="left"><p>NDIS_WWAN_AUTH_RESPONSE_REVISION_1</p>
<p>NDIS_WWAN_AUTH_RESPONSE_REVISION_1</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/hh846212" data-raw-source="[&lt;strong&gt;NDIS_STATUS_WWAN_SET_HOME_PROVIDER_COMPLETE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh846212)"><strong>NDIS_STATUS_WWAN_SET_HOME_PROVIDER_COMPLETE</strong></a></p>
<p>uses <a href="https://msdn.microsoft.com/library/windows/hardware/hh439841" data-raw-source="[&lt;strong&gt;NDIS_WWAN_SET_HOME_PROVIDER&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh439841)"><strong>NDIS_WWAN_SET_HOME_PROVIDER</strong></a></p></td>
<td align="left"><p>N/A</p>
<p>NDIS_WWAN_HOME_PROVIDER_REVISION_2</p></td>
</tr>
</tbody>
</table>

> [!NOTE]
> The following notes apply to the preceding table:
> † represents optional indications that miniport drivers may support. Be aware that if a miniport driver supports an optional OID, the miniport driver should also support the corresponding indication. 

## WWAN-Specific Indication Support for GSM, CDMA, and Unsolicited Indications

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Indication</strong></p></td>
<td align="left"><p><strong>GSM</strong></p></td>
<td align="left"><p><strong>CDMA</strong></p></td>
<td align="left"><p><strong>Unsolicited</strong></p>
<p><strong>indication</strong></p>
<p><strong>allowed?</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567845" data-raw-source="[&lt;strong&gt;NDIS_STATUS_WWAN_DEVICE_CAPS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567845)"><strong>NDIS_STATUS_WWAN_DEVICE_CAPS</strong></a></p></td>
<td align="left"><p>X</p></td>
<td align="left"><p>X</p></td>
<td align="left"><p>N</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567856" data-raw-source="[&lt;strong&gt;NDIS_STATUS_WWAN_READY_INFO&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567856)"><strong>NDIS_STATUS_WWAN_READY_INFO</strong></a></p></td>
<td align="left"><p>X</p></td>
<td align="left"><p>X</p></td>
<td align="left"><p>Y</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567855" data-raw-source="[&lt;strong&gt;NDIS_STATUS_WWAN_RADIO_STATE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567855)"><strong>NDIS_STATUS_WWAN_RADIO_STATE</strong></a></p></td>
<td align="left"><p>X</p></td>
<td align="left"><p>X</p></td>
<td align="left"><p>Y</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567851" data-raw-source="[&lt;strong&gt;NDIS_STATUS_WWAN_PIN_INFO&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567851)"><strong>NDIS_STATUS_WWAN_PIN_INFO</strong></a></p></td>
<td align="left"><p>X</p></td>
<td align="left"><p>X</p></td>
<td align="left"><p>N</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567852" data-raw-source="[&lt;strong&gt;NDIS_STATUS_WWAN_PIN_LIST&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567852)"><strong>NDIS_STATUS_WWAN_PIN_LIST</strong></a></p></td>
<td align="left"><p>X</p></td>
<td align="left"><p>X</p></td>
<td align="left"><p>N</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567858" data-raw-source="[&lt;strong&gt;NDIS_STATUS_WWAN_SERVICE_ACTIVATION&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567858)"><strong>NDIS_STATUS_WWAN_SERVICE_ACTIVATION</strong></a></p></td>
<td align="left"><p>X</p></td>
<td align="left"><p>X</p></td>
<td align="left"><p>N</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567848" data-raw-source="[&lt;strong&gt;NDIS_STATUS_WWAN_HOME_PROVIDER&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567848)"><strong>NDIS_STATUS_WWAN_HOME_PROVIDER</strong></a></p></td>
<td align="left"><p>X</p></td>
<td align="left"><p>X</p></td>
<td align="left"><p>N</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567853" data-raw-source="[&lt;strong&gt;NDIS_STATUS_WWAN_PREFERRED_PROVIDERS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567853)"><strong>NDIS_STATUS_WWAN_PREFERRED_PROVIDERS</strong></a></p></td>
<td align="left"><p>X</p></td>
<td align="left"></td>
<td align="left"><p>Y</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567866" data-raw-source="[&lt;strong&gt;NDIS_STATUS_WWAN_VISIBLE_PROVIDERS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567866)"><strong>NDIS_STATUS_WWAN_VISIBLE_PROVIDERS</strong></a></p></td>
<td align="left"><p>X</p></td>
<td align="left"><p>X</p></td>
<td align="left"><p>N</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567857" data-raw-source="[&lt;strong&gt;NDIS_STATUS_WWAN_REGISTER_STATE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567857)"><strong>NDIS_STATUS_WWAN_REGISTER_STATE</strong></a></p></td>
<td align="left"><p>X</p></td>
<td align="left"><p>X</p></td>
<td align="left"><p>Y</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567859" data-raw-source="[&lt;strong&gt;NDIS_STATUS_WWAN_SIGNAL_STATE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567859)"><strong>NDIS_STATUS_WWAN_SIGNAL_STATE</strong></a></p></td>
<td align="left"><p>X</p></td>
<td align="left"><p>X</p></td>
<td align="left"><p>Y</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567850" data-raw-source="[&lt;strong&gt;NDIS_STATUS_WWAN_PACKET_SERVICE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567850)"><strong>NDIS_STATUS_WWAN_PACKET_SERVICE</strong></a></p>
<p>uses <a href="https://msdn.microsoft.com/library/windows/hardware/ff567910" data-raw-source="[&lt;strong&gt;NDIS_WWAN_PACKET_SERVICE_STATE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567910)"><strong>NDIS_WWAN_PACKET_SERVICE_STATE</strong></a></p></td>
<td align="left"><p>X</p></td>
<td align="left"><p>X</p></td>
<td align="left"><p>Y</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567854" data-raw-source="[&lt;strong&gt;NDIS_STATUS_WWAN_PROVISIONED_CONTEXTS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567854)"><strong>NDIS_STATUS_WWAN_PROVISIONED_CONTEXTS</strong></a></p></td>
<td align="left"><p>X</p></td>
<td align="left"><p>X</p></td>
<td align="left"><p>Y</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567843" data-raw-source="[&lt;strong&gt;NDIS_STATUS_WWAN_CONTEXT_STATE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567843)"><strong>NDIS_STATUS_WWAN_CONTEXT_STATE</strong></a></p></td>
<td align="left"><p>X</p></td>
<td align="left"><p>X</p></td>
<td align="left"><p>Y</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567860" data-raw-source="[&lt;strong&gt;NDIS_STATUS_WWAN_SMS_CONFIGURATION&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567860)"><strong>NDIS_STATUS_WWAN_SMS_CONFIGURATION</strong></a></p></td>
<td align="left"><p>X</p></td>
<td align="left"><p>X</p></td>
<td align="left"><p>Y</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567862" data-raw-source="[&lt;strong&gt;NDIS_STATUS_WWAN_SMS_RECEIVE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567862)"><strong>NDIS_STATUS_WWAN_SMS_RECEIVE</strong></a></p></td>
<td align="left"><p>X</p></td>
<td align="left"><p>X</p></td>
<td align="left"><p>Y</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567863" data-raw-source="[&lt;strong&gt;NDIS_STATUS_WWAN_SMS_SEND&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567863)"><strong>NDIS_STATUS_WWAN_SMS_SEND</strong></a></p>
<p>uses <a href="https://msdn.microsoft.com/library/windows/hardware/ff567944" data-raw-source="[&lt;strong&gt;NDIS_WWAN_SMS_SEND_STATUS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567944)"><strong>NDIS_WWAN_SMS_SEND_STATUS</strong></a></p></td>
<td align="left"><p>X</p></td>
<td align="left"><p>X</p></td>
<td align="left"><p>N</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567861" data-raw-source="[&lt;strong&gt;NDIS_STATUS_WWAN_SMS_DELETE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567861)"><strong>NDIS_STATUS_WWAN_SMS_DELETE</strong></a></p></td>
<td align="left"><p>X</p></td>
<td align="left"><p>X</p></td>
<td align="left"><p>N</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567864" data-raw-source="[&lt;strong&gt;NDIS_STATUS_WWAN_SMS_STATUS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567864)"><strong>NDIS_STATUS_WWAN_SMS_STATUS</strong></a></p></td>
<td align="left"><p>X</p></td>
<td align="left"><p>X</p></td>
<td align="left"><p>Y</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567865" data-raw-source="[&lt;strong&gt;NDIS_STATUS_WWAN_VENDOR_SPECIFIC&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567865)"><strong>NDIS_STATUS_WWAN_VENDOR_SPECIFIC</strong></a></p></td>
<td align="left"><p>X</p></td>
<td align="left"><p>X</p></td>
<td align="left"><p>Y</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/hh439822" data-raw-source="[&lt;strong&gt;NDIS_STATUS_WWAN_USSD&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh439822)"><strong>NDIS_STATUS_WWAN_USSD</strong></a></p></td>
<td align="left"><p>X</p></td>
<td align="left"></td>
<td align="left"><p>Y</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/hh846210" data-raw-source="[&lt;strong&gt;NDIS_STATUS_WWAN_DEVICE_SERVICE_SUPPORTED_COMMANDS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh846210)"><strong>NDIS_STATUS_WWAN_DEVICE_SERVICE_SUPPORTED_COMMANDS</strong></a></p></td>
<td align="left"><p>X</p></td>
<td align="left"><p>X</p></td>
<td align="left"><p>N</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/hh846205" data-raw-source="[&lt;strong&gt;NDIS_STATUS_WWAN_DEVICE_SERVICE_RESPONSE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh846205)"><strong>NDIS_STATUS_WWAN_DEVICE_SERVICE_RESPONSE</strong></a></p></td>
<td align="left"><p>X</p></td>
<td align="left"><p>X</p></td>
<td align="left"><p>N</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/hh846204" data-raw-source="[&lt;strong&gt;NDIS_STATUS_WWAN_DEVICE_SERVICE_EVENT&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh846204)"><strong>NDIS_STATUS_WWAN_DEVICE_SERVICE_EVENT</strong></a></p></td>
<td align="left"><p>X</p></td>
<td align="left"><p>X</p></td>
<td align="left"><p>Y</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/hh846209" data-raw-source="[&lt;strong&gt;NDIS_STATUS_WWAN_DEVICE_SERVICE_SUBSCRIPTION&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh846209)"><strong>NDIS_STATUS_WWAN_DEVICE_SERVICE_SUBSCRIPTION</strong></a></p></td>
<td align="left"><p>X</p></td>
<td align="left"><p>X</p></td>
<td align="left"><p>N</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/hh439821" data-raw-source="[&lt;strong&gt;NDIS_STATUS_WWAN_AUTH_RESPONSE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh439821)"><strong>NDIS_STATUS_WWAN_AUTH_RESPONSE</strong></a></p></td>
<td align="left"><p>X</p></td>
<td align="left"><p>X</p></td>
<td align="left"><p>N</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/hh846212" data-raw-source="[&lt;strong&gt;NDIS_STATUS_WWAN_SET_HOME_PROVIDER_COMPLETE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh846212)"><strong>NDIS_STATUS_WWAN_SET_HOME_PROVIDER_COMPLETE</strong></a></p></td>
<td align="left"><p>X</p></td>
<td align="left"><p>X</p></td>
<td align="left"><p>N</p></td>
</tr>
</tbody>
</table> 

## Multi-carrier Specific OIDs

The following changes apply to NDIS 6.30 miniport drivers that support multi-carrier mode. If the miniport driver does not support multi-carrier mode then please refer to the preceding table.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>OID</strong> and <strong>Windows 8 Corresponding Data Structure</strong></p></td>
<td align="left"><p><strong>Query Operation</strong></p></td>
<td align="left"><p><strong>Set Operation</strong></p></td>
<td align="left"><p><strong>GSM/CDMA</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff569826" data-raw-source="[OID_WWAN_HOME_PROVIDER](https://msdn.microsoft.com/library/windows/hardware/ff569826)">OID_WWAN_HOME_PROVIDER</a></p>
<p>uses <a href="https://msdn.microsoft.com/library/windows/hardware/hh439841" data-raw-source="[&lt;strong&gt;NDIS_WWAN_SET_HOME_PROVIDER&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh439841)"><strong>NDIS_WWAN_SET_HOME_PROVIDER</strong></a></p></td>
<td align="left"><p>A</p></td>
<td align="left"><p>A</p></td>
<td align="left"><p>GSM, CDMA</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff569830" data-raw-source="[OID_WWAN_PREFERRED_MULTICARRIER_PROVIDERS](https://msdn.microsoft.com/library/windows/hardware/ff569830)">OID_WWAN_PREFERRED_MULTICARRIER_PROVIDERS</a></p>
<p>uses <a href="https://msdn.microsoft.com/library/windows/hardware/hh831866" data-raw-source="[&lt;strong&gt;NDIS_WWAN_SET_PREFERRED_MULTICARRIER_PROVIDERS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh831866)"><strong>NDIS_WWAN_SET_PREFERRED_MULTICARRIER_PROVIDERS</strong></a>. The <strong>PreferredListHeader.ElementType</strong> should be set to <strong>WwanStructProvider2</strong> and the structure is WWAN_PROVIDER2.</p></td>
<td align="left"><p>A</p></td>
<td align="left"><p>A</p></td>
<td align="left"><p>GSM, CDMA</p></td>
</tr>
</tbody>
</table> 

## Multi-carrier Specific Indications, Corresponding Data Structures, and OS Revisions

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Indication</strong> and <strong>Corresponding Data Structure</strong></p></td>
<td align="left"><p><strong>Windows 8 Revision</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567848" data-raw-source="[&lt;strong&gt;NDIS_STATUS_WWAN_HOME_PROVIDER&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567848)"><strong>NDIS_STATUS_WWAN_HOME_PROVIDER</strong></a></p>
<p>uses <a href="https://msdn.microsoft.com/library/windows/hardware/hh439840" data-raw-source="[&lt;strong&gt;NDIS_WWAN_HOME_PROVIDER2&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh439840)"><strong>NDIS_WWAN_HOME_PROVIDER2</strong></a></p></td>
<td align="left"><p>NDIS_WWAN_HOME_PROVIDER_REVISION_2</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/hh846211" data-raw-source="[&lt;strong&gt;NDIS_STATUS_WWAN_PREFERRED_MULTICARRIER_PROVIDERS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh846211)"><strong>NDIS_STATUS_WWAN_PREFERRED_MULTICARRIER_PROVIDERS</strong></a></p>
<p>uses <a href="https://msdn.microsoft.com/library/windows/hardware/hh831864" data-raw-source="[&lt;strong&gt;NDIS_WWAN_PREFERRED_MULTICARRIER_PROVIDERS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh831864)"><strong>NDIS_WWAN_PREFERRED_MULTICARRIER_PROVIDERS</strong></a></p></td>
<td align="left"><p>NDIS_WWAN_PREFERRED_MULTICARRIER_PROVIDERS_REVISION_1. The <strong>PreferredListHeader.ElementType</strong> should be set to <strong>WwanStructProvider2</strong> and the list should contain WWAN_PROVIDER2 structure.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567866" data-raw-source="[&lt;strong&gt;NDIS_STATUS_WWAN_VISIBLE_PROVIDERS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567866)"><strong>NDIS_STATUS_WWAN_VISIBLE_PROVIDERS</strong></a></p>
<p>uses <a href="https://msdn.microsoft.com/library/windows/hardware/ff567948" data-raw-source="[&lt;strong&gt;NDIS_WWAN_VISIBLE_PROVIDERS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567948)"><strong>NDIS_WWAN_VISIBLE_PROVIDERS</strong></a></p></td>
<td align="left"><p>NDIS_WWAN_VISIBLE_PROVIDERS_REVISION_1. The <strong>VisibleListHeader.ElementType</strong> should be set to <strong>WwanStructProvider2</strong> and the list should contain WWAN_PROVIDER2 structure.</p></td>
</tr>
</tbody>
</table> 

## Multi-carrier Specific Indication Support for GSM, CDMA, and Unsolicited Indications

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Indication</strong> and <strong>Corresponding Data Structure</strong></p></td>
<td align="left"><p><strong>GSM</strong></p></td>
<td align="left"><p><strong>CDMA</strong></p></td>
<td align="left"><p><strong>Unsolicited</strong></p>
<p><strong>indication</strong></p>
<p><strong>allowed?</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567848" data-raw-source="[&lt;strong&gt;NDIS_STATUS_WWAN_HOME_PROVIDER&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567848)"><strong>NDIS_STATUS_WWAN_HOME_PROVIDER</strong></a></p></td>
<td align="left"><p>X</p></td>
<td align="left"><p>X</p></td>
<td align="left"><p>N</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/hh846211" data-raw-source="[&lt;strong&gt;NDIS_STATUS_WWAN_PREFERRED_MULTICARRIER_PROVIDERS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh846211)"><strong>NDIS_STATUS_WWAN_PREFERRED_MULTICARRIER_PROVIDERS</strong></a></p></td>
<td align="left"><p>X</p></td>
<td align="left"><p>X</p></td>
<td align="left"><p>Y</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567866" data-raw-source="[&lt;strong&gt;NDIS_STATUS_WWAN_VISIBLE_PROVIDERS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567866)"><strong>NDIS_STATUS_WWAN_VISIBLE_PROVIDERS</strong></a></p>
<p>uses <a href="https://msdn.microsoft.com/library/windows/hardware/ff567948" data-raw-source="[&lt;strong&gt;NDIS_WWAN_VISIBLE_PROVIDERS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567948)"><strong>NDIS_WWAN_VISIBLE_PROVIDERS</strong></a></p></td>
<td align="left"><p>X</p></td>
<td align="left"><p>X</p></td>
<td align="left"><p>N</p></td>
</tr>
</tbody>
</table>
