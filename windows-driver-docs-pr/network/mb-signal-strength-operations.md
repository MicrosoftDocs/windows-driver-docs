---
title: MB Signal Strength Operations
description: MB Signal Strength Operations
ms.date: 03/01/2021
ms.localizationpriority: medium
---

# MB Signal Strength Operations


This topic describes the operations to report signal strength.

These operations require access to the network provider, but not to the Subscriber Identity Module (SIM card).

Be aware that in case of GSM-based devices, miniport drivers should send signal strength notifications only after the miniport driver has successfully registered with a network provider. For CDMA-based devices, miniport drivers can send signal strength notifications before the miniport driver has successfully registered with a network provider.

## Signal Strength Indication Semantics


The following diagram shows the process that miniport drivers should follow to process signal strength indications. The MB Service adjusts the signal strength-reporting threshold and interval, based on the current device signal strength and how long the device has been idle. These actions are usually performed as part of the power management features provided by the MB Service. The labels in bold are OID identifiers or transactional flow control. The labels in regular text are the important flags within the OID structure.

![diagram illustrating the process that miniport drivers should follow to process signal strength indications.](images/wwansignalstrength.png)

To update signal strength indications, use the following procedure:

1.  The miniport driver sends [**NDIS\_WWAN\_SIGNAL\_STATE**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_signal_state) to the MB Service.

2.  The MB Service sends [OID\_WWAN\_SIGNAL\_STATE](oid-wwan-signal-state.md) to the miniport driver. The miniport driver responds with a provisional acknowledgement (NDIS\_STATUS\_INDICATION\_REQUIRED) that it has received the request, and it will send a notification with the requested information in the future.

3.  The miniport driver sends NDIS\_STATUS\_WWAN\_SUCCESS to the MB Service.

4.  The miniport driver sends [**NDIS\_WWAN\_SIGNAL\_STATE**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_signal_state) to the MB Service.

5.  The MB Service sends [OID\_WWAN\_SIGNAL\_STATE](oid-wwan-signal-state.md) to the miniport driver. The miniport driver responds with a provisional acknowledgement (NDIS\_STATUS\_INDICATION\_REQUIRED) that it has received the request, and it will send a notification with the requested information in the future.

6.  The miniport driver sends NDIS\_STATUS\_WWAN\_SUCCESS to the MB Service.

7.  The MB Service sends [OID\_WWAN\_SIGNAL\_STATE](oid-wwan-signal-state.md) to the miniport driver. The miniport driver responds with a provisional acknowledgement (NDIS\_STATUS\_INDICATION\_REQUIRED) that it has received the request, and it will send a notification with the requested information in the future.

8.  The miniport driver sends NDIS\_STATUS\_WWAN\_SUCCESS to the MB Service.

9.  The miniport driver sends [**NDIS\_WWAN\_SIGNAL\_STATE**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_signal_state) to the MB Service.

 

