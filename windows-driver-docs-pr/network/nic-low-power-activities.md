---
title: NIC Low-Power Activities
description: NIC Low-Power Activities
ms.assetid: 9973b28f-f0ef-4a22-a29f-91f3e771f1c4
keywords: ["low-power activities WDK Native 802.11", "wake-on-wireless LAN WDK Native 802.11 , low-power activities"]
---

# NIC Low-Power Activities


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

This section applies only to NDIS 6.20 and later.

After it receives an [OID\_PM\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff569768) set request, the 802.11 miniport driver should enable the wake-on-LAN (WOL) packet and WOL magic pattern wake-up procedure. After the host computer resumes operation from a low-power state, the NIC should clear the WOL packet and WOL magic pattern from the hardware.

After the driver receives an [OID\_PNP\_SET\_POWER](https://msdn.microsoft.com/library/windows/hardware/ff569780) request to put the NIC into a low-power state, and if WOL is enabled from a set request of [OID\_PM\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff569768), the driver should enable low-power protocol offload on the NIC. This 802.11 low-power protocol offload specifies a Robust Security Network (RSN) WPA2-GTK (group transient key) rekey operation. When the system resumes operation from a low-power state and the driver receives an OID\_PNP\_SET\_POWER request to put the NIC into a D0 state, the driver should disable the low-power protocol offload. However, the NIC should store this low-power protocol offload state in software. The operating system will query this state when it uploads the protocol at a later time.

While the NIC is in a low-power state (D1, D2, or D3), it should be able to perform the following activities:

### Keep AP Association Alive

To minimize spurious wake-up events, the NIC must keep alive the association with the current AP. The hardware vendor must decide how to implement the keep-alive mechanism.

### Wake Up Host Computer

The NIC should wake up the host computer if any of the events described in [Wake-Up Events](wake-up-events.md) are triggered. If the NIC wakes up the host computer in response to a WOL packet or WOL magic pattern, it should also indicate the packet to the operating system.

### Handle WPA2-GTK Rekey Requests

If the NIC is not using infrastructure-assisted wake-up, it must handle WPA2-GTK rekey requests from the current AP. The operating system provides initial values for a key confirmation key ( **KCK** ), EAPOL key encryption key ( **KEK** ), and key replay counter ( **KeyReplayCounter** ) in the **Dot11RSNRekeyParameters** structure within the [**NDIS\_PM\_PROTOCOL\_OFFLOAD**](https://msdn.microsoft.com/library/windows/hardware/ff566760) structure. The NIC should update the replay counter as appropriate.

When the NIC is in a low-power state, it must maintain the GTK key if the key is critical to complete a WOL event. For example, in the case of an infrastructure assisted wake-up procedure, a GTK might not be necessary for completing WOL. In that case, the NIC is not required to maintain a GTK.

If rekeying a GTK is not required for completing WOL, the NIC must make an [**NDIS\_STATUS\_PM\_OFFLOAD\_REJECTED**](https://msdn.microsoft.com/library/windows/hardware/ff567412) status indication when GTK rotation is not required to support WOL.

When the operating system calls [OID\_PM\_ADD\_PROTOCOL\_OFFLOAD](https://msdn.microsoft.com/library/windows/hardware/ff569763), it provides the initial values of a key confirmation key ( **KCK** ) and EAPOL key encryption key ( **KEK** ) in the **Dot11RSNRekeyParameters** structure within the [**NDIS\_PM\_PROTOCOL\_OFFLOAD**](https://msdn.microsoft.com/library/windows/hardware/ff566760) structure. After the miniport driver receives this data, it should not attempt to associate to a new AP. While the NIC is in a low-power state, the driver should not change AP association. Also while the NIC is in a low-power state, the NIC must update the **KeyReplayCounter** member of the **Dot11RSNRekeyParameters** structure.

When the NIC wakes up, the operating system calls [OID\_PM\_GET\_PROTOCOL\_OFFLOAD](https://msdn.microsoft.com/library/windows/hardware/ff569766) to upload RSN rekeying information from the NIC. In response to this OID method request, the NIC should return the value of **KeyReplayCounter**, but it must not return values for **KCK** and **KEK** . If the NIC is performing GTK rekeying while the miniport driver is waking up, the NIC should complete its processing of an [OID\_PNP\_SET\_POWER](https://msdn.microsoft.com/library/windows/hardware/ff569780) request after the GTK exchange reaches its final state.

After the NIC completes processing an [OID\_PNP\_SET\_POWER](https://msdn.microsoft.com/library/windows/hardware/ff569780) request to wake up to state D0, it must stop processing the miniport driver M1 message.

 

 





