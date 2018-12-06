---
title: UE hang detection Steps 1-14
description: Steps 1 through 14 of UE hang detection are described below. The steps correspond to the diagram shown in UE hang detection and recovery flow.
ms.assetid: 0F6F9B31-27FB-44B1-8C0E-A270E8BAF295
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# UE hang detection: Steps 1-14


Steps 1 through 14 of UE hang detection are described below. The steps correspond to the diagram shown in [UE hang detection and recovery flow](wdi-ue-hang-detection-and-recovery-flow.md).

This example uses OID\_SET\_POWER.

1.  NDIS receives a system power IRP or the NIC active references drop to 0.
2.  NDIS generates an OID\_SET\_POWER D3 to the WDI driver.
3.  WDI sets a timer for a WDI command (M1), including a task before it sends the WDI OID down to the LE. If the command is a task, an additional timer for the task is also set. Both timers can time out, but at most, only one can trigger a reset recovery.
4.  WDI sends the WDI command to the LE. The recommendation for the LE is to remember the WDI OID in the adapter structure if it needs a firmware command to complete the OID. When the firmware completes the job for the WDI OID, the LE completes the OID and removes it from the adapter structure. Since WDI serializes OIDs to the LE, the LE needs only one slot to remember the pending WDI OID. If the firmware command is hung, the LE can return the OID at any time but no later than at surprise-remove (it can be in the context of surprise-remove) at Step 17 when the firmware has been disabled. For any other cases, the LE simply completes the WDI OID when the firmware completes the corresponding job, regardless of if it is before or after a diagnose callback. If the LE needs to remember the WDI OID after Diagnose, it needs another slot to remember it. However, for the OIDs received after Diagnose, the LE should not touch the firmware to avoid cascaded hangs.
5.  The LE sends a command to the firmware.
6.  If the firmware command timed out, it may be due to a firmware hanging or taking too long.
    -   If the firmware is simply taking too long to complete the command after a time out, the LE can complete the WDI command. The UE handles it appropriately.
    -   If the firmware is hung, the WDI command is not completed soon. The LE must complete it at surprise-remove at Step 16 when the hardware has been reset, so it is safe to complete without special handling for a potential race condition.

7.  The WDI timer fires to generate a WDI Diagnose command. This WDI command is a call to the LE driver, [*MiniportWdiAdapterHangDiagnose*](https://msdn.microsoft.com/library/windows/hardware/mt297558), rather than a WDI OID.
8.  LE collects hardware control register states, and optionally, the full firmware state.
    -   The IHV driver is expected to collect hardware register content which is limited to 1KB, and return it in the function return. Additionally, in the pre-production environment, the LE should also try to dump the firmware context into files so that the IHV can do post-mortem debug thoroughly. The switch can be implemented as a registry key to control the collection of hardware registers and the firmware image.
    -   The LE also marks the current command for cancellation. If command completion races to beat the diagnosis, it is acceptable if the LE does nothing for this command.
    -   With this command pending, the UE may send further WDI commands as the consequence of Reset. These are in-flight commands or clean-up commands. After the diagnose call, the LE should process them without touching the firmware.

9.  WDI receives the control register state.
10. WDI marks the hang WDI command so that it is indicated later by the LE.
11. WDI returns (completes) the NDIS command without the WDI completion. This is safe because WDI double-buffers NDIS commands.
12. WDI calls NDIS to reset and calls [**NdisWriteErrorLogEntry**](https://msdn.microsoft.com/library/windows/hardware/ff564663) with *Error Code* of **NDIS\_ERROR\_CODE\_HARDWARE\_FAILURE** (0xc000138a). This results in an event recorded in the system event log with the module name of LE. The error event ID automatically pops up as (0xc000138a | 0xffff) – 0n5002. If the LE also uses the same error code to write error logs, the first DWORD of the data should contain the high bit set (0x80000000) to easily separate events by the LE. WDI uses 0x00000000 to 0x7fffffff for the first DWORD data.
13. The call returns.
14. NDIS completes the IRP.

After this point, NDIS calls the bus to surprise remove and re-enumerate us. It is important to note that WDI double-buffers NDIS commands so that it does not have to wait for the WDI command to return to complete the NDIS command. This eliminates the need for the LE to do cancel logics, which are notoriously complex to do.

The completion of NDIS OID\_SET\_POWER is necessary to avoid a deadlock of PnP operations. All PnP and power state changing events are serialized. This means that if a Set power OID does not return, NDIS is not able to return the Set power IRP, which means the Reset Recovery locks up with the Surprise-Remove IRP.

## Related topics


[*MiniportWdiAdapterHangDiagnose*](https://msdn.microsoft.com/library/windows/hardware/mt297558)

[Reset (surprise remove): steps 15-20](wdi-reset--surprise-remove---steps-15-20.md)

[UE hang detection and recovery flow](wdi-ue-hang-detection-and-recovery-flow.md)

 

 






