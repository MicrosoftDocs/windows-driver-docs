---
title: WlanAssert rule (ndis)
description: The WlanAssert rule includes a set of checks validated inside the WDIWIFI driver.
ms.date: 04/08/2020
keywords: ["WlanAssert rule (ndis)"]
topic_type:
- apiref
api_name:
- WlanAssert
api_type:
- NA
ms.localizationpriority: medium
---

# WlanAssert rule (ndis)

The **WlanAssert** rule includes a set of checks validated inside the WDIWIFI driver.

The following violations are possible:

- *TxPeerBacklogStub: IHV WDI miniport called datapath after datapath deinitialization* - This rule applies to Peer-Queuing mode only. When the Miniport has been halted or reset, WDI will call the IHV driver's [CloseAdapterHandler](/windows-hardware/drivers/ddi/dot11wdi/nc-dot11wdi-miniport_wdi_close_adapter) function which will require the driver to cleanup its state and not call any data callbacks after that. These asserts will be invoked if the driver happens to call any of the data handlers such as [TxTransferCompleteIndication](/windows-hardware/drivers/ddi/dot11wdi/nc-dot11wdi-ndis_wdi_tx_transfer_complete_ind), [TxSendPauseIndication](/windows-hardware/drivers/ddi/dot11wdi/nc-dot11wdi-ndis_wdi_tx_send_pause_ind), or [TxReleaseFrameIndication](/windows-hardware/drivers/ddi/dot11wdi/nc-dot11wdi-ndis_wdi_tx_release_frames_ind) after the Close, or if there still any outstanding Tx frames after the Close.

- *TxAbortStub: IHV WDI miniport called datapath after datapath deinitialization* - This rule applies to Peer-Queuing mode only. When the Miniport has been halted or reset, WDI will call the IHV driver's [CloseAdapterHandler](/windows-hardware/drivers/ddi/dot11wdi/nc-dot11wdi-miniport_wdi_close_adapter) function which will require the driver to cleanup its state and not call any data callbacks after that. These asserts will be invoked if the driver happens to call any of the data handlers such as [TxTransferCompleteIndication](/windows-hardware/drivers/ddi/dot11wdi/nc-dot11wdi-ndis_wdi_tx_transfer_complete_ind), [TxSendPauseIndication](/windows-hardware/drivers/ddi/dot11wdi/nc-dot11wdi-ndis_wdi_tx_send_pause_ind), or [TxReleaseFrameIndication](/windows-hardware/drivers/ddi/dot11wdi/nc-dot11wdi-ndis_wdi_tx_release_frames_ind) after the Close, or if there still any outstanding Tx frames after the Close.

- *WDIWIFI driver being unloaded with mismatched calls to NdisMDeregisterWdiMiniportDriver and NdisMRegisterWdiMiniportDriver* - This Assert is invoked if the IHV driver's call to [NdisMRegisterWdiMiniportDriver](/windows-hardware/drivers/ddi/dot11wdi/nf-dot11wdi-ndismregisterwdiminiportdriver) failed, but the IHV driver still calls the [NdisMDeregisterWdiMiniportDriver](/windows-hardware/drivers/ddi/dot11wdi/nf-dot11wdi-ndismderegisterwdiminiportdriver) handler.

- *The IhvWdiVersion is too low for the passed MiniportDataHandler Revision* - WDI will get the IHV driver's WDI version by calling [OID_WDI_GET_ADAPTER_CAPABILITIES](../network/oid-wdi-get-adapter-capabilities.md), and it will then call the driver's [TalTxRxInitializeHandler](/windows-hardware/drivers/ddi/dot11wdi/nc-dot11wdi-miniport_wdi_tal_txrx_initialize) handler to get the [WdiCharacteristics](/windows-hardware/drivers/ddi/dot11wdi/ns-dot11wdi-_ndis_miniport_driver_wdi_characteristics), where the driver can update the WDI Handler Revision if needed. This Assert will be hit if the driver's WDI version is less than or equal to WDI_VERSION_1_1_0, but the driver's [WdiCharacteristics](/windows-hardware/drivers/ddi/dot11wdi/ns-dot11wdi-_ndis_miniport_driver_wdi_characteristics), Revision is set to a version greater than NDIS_OBJECT_TYPE_MINIPORT_WDI_DATA_HANDLERS_REVISION_1.

- *The MiniportDataHandler Revision is too low for the IhvWdiVersion* - WDI will get the IHV driver's WDI version by calling [OID_WDI_GET_ADAPTER_CAPABILITIES](../network/oid-wdi-get-adapter-capabilities.md), and it will then call the driver's [TalTxRxInitializeHandler](/windows-hardware/drivers/ddi/dot11wdi/nc-dot11wdi-miniport_wdi_tal_txrx_initialize) handler to get the [WdiCharacteristics](/windows-hardware/drivers/ddi/dot11wdi/ns-dot11wdi-_ndis_miniport_driver_wdi_characteristics), where the driver can update the WDI Handler Revision if needed. This Assert will be hit if the driver's WDI version is greater than WDI_VERSION_1_1_0, but the driver's [WdiCharacteristics](/windows-hardware/drivers/ddi/dot11wdi/ns-dot11wdi-_ndis_miniport_driver_wdi_characteristics), Revision is set to a version less than NDIS_OBJECT_TYPE_MINIPORT_WDI_DATA_HANDLERS_REVISION_2.

The *violation text* will be provided as parameter two in the 0xC4 bug check.

**Driver model: NDIS**

**Bug check(s) found with this rule**: [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](../debugger/bug-check-0xc4--driver-verifier-detected-violation.md) ( 0x00093004)


## How to test

<table>
<colgroup>
<col width="100%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">At run time</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Run <a href="/windows-hardware/drivers/devtest/driver-verifier" data-raw-source="[Driver Verifier](./driver-verifier.md)">Driver Verifier</a> and select the <a href="/windows-hardware/drivers/devtest/ndis-wifi-verification" data-raw-source="[NDIS/WIFI verification](./ndis-wifi-verification.md)">NDIS/WIFI verification</a> option.</p></td>
</tr>
</tbody>
</table>

## Applies to

[TxTransferCompleteIndication](/windows-hardware/drivers/ddi/dot11wdi/nc-dot11wdi-ndis_wdi_tx_transfer_complete_ind)

[TxSendPauseIndication](/windows-hardware/drivers/ddi/dot11wdi/nc-dot11wdi-ndis_wdi_tx_send_pause_ind)

[TxReleaseFrameIndication](/windows-hardware/drivers/ddi/dot11wdi/nc-dot11wdi-ndis_wdi_tx_release_frames_ind) 

[OID_WDI_GET_ADAPTER_CAPABILITIES](../network/oid-wdi-get-adapter-capabilities.md)

[MINIPORT_HALT callback function](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_halt)

[MINIPORT_SHUTDOWN callback function](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_shutdown)

[NdisMRegisterWdiMiniportDriver](/windows-hardware/drivers/ddi/dot11wdi/nf-dot11wdi-ndismregisterwdiminiportdriver)

[NdisMDeregisterWdiMiniportDriver](/windows-hardware/drivers/ddi/dot11wdi/nf-dot11wdi-ndismderegisterwdiminiportdriver)

## See also

[WDI IHV driver interfaces](../network/wdi-ihv-driver-interfaces.md)

[General Connection Operation Guidelines](/previous-versions/windows/hardware/wireless/general-connection-operation-guidelines)

[OID\_DOT11\_RESET\_REQUEST](/previous-versions/windows/hardware/wireless/oid-dot11-reset-request)

[NDIS\_STATUS\_DOT11\_ASSOCIATION\_START](/previous-versions/windows/hardware/wireless/ndis-status-dot11-association-start)
