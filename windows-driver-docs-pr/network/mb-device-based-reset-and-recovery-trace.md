---
title: MB Device-based Reset and Recovery trace
description: MB Device-based Reset and Recovery trace
keywords:
- MB Device-based Reset and Recovery, Mobile Broadband Device-based Reset and Recovery, Mobile Broadband miniport driver Device-based Reset and Recovery
ms.date: 03/01/2021
ms.localizationpriority: medium
---

# MBB Device Reset and Recovery (RnR) trace
## Useful keywords/regexp for filtering traces
- Attempt connection reset
- current RnR state
- OnConnectionStateInfoChanged
- EvaluateAndTryHighImpactRnRMethod
- CWwanResetRecovery::Trigger
- CWwanResetRecovery::Initialize
- CWwanResetRecovery::OnNdisNotification
- CWwanResetRecovery::OnWwanNotification
- CWwanResetRecovery::OnInterfaceReArrival
- CWwanResetRecovery::OnInterfaceRemoval
- CWwanResetRecovery::fsmEventHandler:
- CWwanResetRecovery::OnWwanNotification
- CWwanResetRecovery::fsmEventHandler: 
- CWwanDeviceEnumerator::
- CWwanResetRecovery
- SET OID_WWAN_RADIO_STATE (e010103), RequestId 
- : OID_WWAN_CONNECT (
- [NH] Dispatch WwanNotificationSourceMsm\WwanMsmEventTypeConnectionIStreamUpdated
- ]RouteManagement::BadConnectionState
- WNF_WCM_INTERFACE_CONNECTION_STATE
- WNF_PHN_CALL_STATUS
- L3ConnnectivityGood
- WaitL3ConnnectivityGood
- CONTEXT_STATE Resp (Set)
- ound valid
- _ReadRnRPolicies
- Opportunistic Internet
- Active probe result code on interface

## Investigation tips

* Ensure the necessary ETW providers are included in log:

  1. netsh trace start wireless_dbg,provisioning persist=yes
  2. repro the scenario 
  3. netsh trace stop
  4. Collect the files generated and attach them to the bug 
       
* Follow the [RnR trigger guidelines](mb-device-based-reset-and-recovery.md#rnr-triggers) to identify the case that caused the RnR trigger.

