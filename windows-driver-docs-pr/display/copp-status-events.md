---
title: COPP Status Events
description: COPP Status Events
ms.assetid: e9d6bb04-9abd-4864-b359-3c8331843968
keywords:
- copy protection WDK COPP , status
- video copy protection WDK COPP , status
- COPP WDK DirectX VA , status
- protected video WDK COPP , status
- status information WDK COPP
- status events WDK COPP
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# COPP Status Events


## <span id="ddk_copp_status_events_gg"></span><span id="DDK_COPP_STATUS_EVENTS_GG"></span>


This section applies only to Windows Server 2003 SP1 and later, and Windows XP SP2 and later.

External events can alter the nature of the protection that is applied to a connector or even modify the type of the connector. The video miniport driver must report these events to COPP applications whenever the driver receives a call to its [*COPPQueryStatus*](https://msdn.microsoft.com/library/windows/hardware/ff539652) function. The video miniport driver must report the following external events by returning the specified flags only on the next call to *COPPQueryStatus* after the events occur:

-   Connection integrity: If the connection between the computer and the display device becomes unplugged, the video miniport driver should set the COPP\_LinkLost flag in the **dwFlags** member of the [**DXVA\_COPPStatusData**](https://msdn.microsoft.com/library/windows/hardware/ff563154) structure, the [**DXVA\_COPPStatusDisplayData**](https://msdn.microsoft.com/library/windows/hardware/ff563157) structure, the [**DXVA\_COPPStatusHDCPKeyData**](https://msdn.microsoft.com/library/windows/hardware/ff563896) structure, or the [**DXVA\_COPPStatusSignalingCmdData**](https://msdn.microsoft.com/library/windows/hardware/ff563905) structure.

-   Connector reconfigurations: If the user causes the configuration of the physical connector to change, the video miniport driver should set the COPP\_RenegotiationRequired flag in the **dwFlags** member of the DXVA\_COPPStatusData, DXVA\_COPPStatusDisplayData, DXVA\_COPPStatusHDCPKeyData, or DXVA\_COPPStatusSignalingCmdData structure.

The video miniport driver returns a pointer to a DXVA\_COPPStatusData, DXVA\_COPPStatusDisplayData, DXVA\_COPPStatusHDCPKeyData, or DXVA\_COPPStatusSignalingCmdData structure in the **COPPStatus** array member of the [**DXVA\_COPPStatusOutput**](https://msdn.microsoft.com/library/windows/hardware/ff563903) structure. A pointer to DXVA\_COPPStatusOutput is returned through the *pOutput* parameter of [*COPPQueryStatus*](https://msdn.microsoft.com/library/windows/hardware/ff539652).

For example, consider two media playback applications, A and B, each controlling, via COPP, the HDCP protection level of the connector that attaches the computer to the display monitor. Each application controls its own unique COPP DirectX VA device. If the connector becomes unplugged, then the next time either application initiates a [*COPPQueryStatus*](https://msdn.microsoft.com/library/windows/hardware/ff539652) request to its COPP device, the video miniport driver should return the COPP\_LinkLost flag.

Assume application A is the first to initiate a call to [*COPPQueryStatus*](https://msdn.microsoft.com/library/windows/hardware/ff539652) on its COPP device. Application A then receives the COPP\_LinkLost flag and acts accordingly. If application A initiates a subsequent *COPPQueryStatus* call, it should not receive the COPP\_LinkLost flag, unless the connector becomes unplugged again. When application B initiates a call to *COPPQueryStatus* on its COPP device, it receives the COPP\_LinkLost flag and acts accordingly. Again, application B should not receive the COPP\_LinkLost flag again until the connector becomes unplugged again.

 

 





