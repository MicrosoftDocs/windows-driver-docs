---
title: Reporting Status of a Protected Output
description: Reporting Status of a Protected Output
keywords:
- OPM WDK display , status of protected output
ms.date: 04/20/2017
---

# Reporting Status of a Protected Output


External events can alter the nature of the protection that is applied to a connector or even modify the type of the connector. The display miniport driver must report these events to OPM applications whenever the driver receives a call to its [**DxgkDdiOPMGetInformation**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_opm_get_information) or [**DxgkDdiOPMGetCOPPCompatibleInformation**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_opm_get_copp_compatible_information) function. The display miniport driver must report the following external events by returning the specified status flags from the [**DXGKMDT\_OPM\_STATUS**](/windows-hardware/drivers/ddi/d3dkmdt/ne-d3dkmdt-_dxgkmdt_opm_status) enumeration only on the next call to *DxgkDdiOPMGetInformation* or *DxgkDdiOPMGetCOPPCompatibleInformation* after the events occur:

<span id="Connection_working_properly"></span><span id="connection_working_properly"></span><span id="CONNECTION_WORKING_PROPERLY"></span>Connection working properly  
If the connection between the computer and the display device is working properly, the display miniport driver should set the DXGKMDT\_OPM\_STATUS\_NORMAL status flag in the **ulStatusFlags** member of the [**DXGKMDT\_OPM\_STANDARD\_INFORMATION**](/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_dxgkmdt_opm_standard_information), [**DXGKMDT\_OPM\_ACTUAL\_OUTPUT\_FORMAT**](/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_dxgkmdt_opm_actual_output_format), [**DXGKMDT\_OPM\_ACP\_AND\_CGMSA\_SIGNALING**](/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_dxgkmdt_opm_acp_and_cgmsa_signaling), or [**DXGKMDT\_OPM\_CONNECTED\_HDCP\_DEVICE\_INFORMATION**](/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_dxgkmdt_opm_connected_hdcp_device_information) structure.

<span id="Connection_integrity"></span><span id="connection_integrity"></span><span id="CONNECTION_INTEGRITY"></span>Connection integrity  
If the computer and the display device become disconnected, the display miniport driver should set the DXGKMDT\_OPM\_STATUS\_LINK\_LOST status flag in the **ulStatusFlags** member of the DXGKMDT\_OPM\_STANDARD\_INFORMATION, DXGKMDT\_OPM\_ACTUAL\_OUTPUT\_FORMAT, DXGKMDT\_OPM\_ACP\_AND\_CGMSA\_SIGNALING, or DXGKMDT\_OPM\_CONNECTED\_HDCP\_DEVICE\_INFORMATION structure.

<span id="Connector_reconfigurations"></span><span id="connector_reconfigurations"></span><span id="CONNECTOR_RECONFIGURATIONS"></span>Connector reconfigurations  
If the end-user causes the configuration of the physical connector to change, the display miniport driver should set the DXGKMDT\_OPM\_STATUS\_RENEGOTIATION\_REQUIRED status flag in the **ulStatusFlags** member of the DXGKMDT\_OPM\_STANDARD\_INFORMATION, DXGKMDT\_OPM\_ACTUAL\_OUTPUT\_FORMAT, DXGKMDT\_OPM\_ACP\_AND\_CGMSA\_SIGNALING, or DXGKMDT\_OPM\_CONNECTED\_HDCP\_DEVICE\_INFORMATION structure.

<span id="Tampering"></span><span id="tampering"></span><span id="TAMPERING"></span>Tampering  
If tampering with the graphics adapter or the adapter's display miniport driver has occurred, the display miniport driver should set the DXGKMDT\_OPM\_STATUS\_TAMPERING\_DETECTED status flag in the **ulStatusFlags** member of the DXGKMDT\_OPM\_STANDARD\_INFORMATION, DXGKMDT\_OPM\_ACTUAL\_OUTPUT\_FORMAT, DXGKMDT\_OPM\_ACP\_AND\_CGMSA\_SIGNALING, or DXGKMDT\_OPM\_CONNECTED\_HDCP\_DEVICE\_INFORMATION structure.

<span id="Revoked_HDCP_device"></span><span id="revoked_hdcp_device"></span><span id="REVOKED_HDCP_DEVICE"></span>Revoked HDCP device  
If a revoked High-bandwidth Digital Content Protection (HDCP) device is directly or indirectly attached to a connector and if HDCP is enabled, the display miniport driver should set the DXGKMDT\_OPM\_STATUS\_REVOKED\_HDCP\_DEVICE\_ATTACHED status flag in the **ulStatusFlags** member of the DXGKMDT\_OPM\_STANDARD\_INFORMATION or DXGKMDT\_OPM\_ACTUAL\_OUTPUT\_FORMAT structure. If HDCP is not enabled, the driver is not required to set this status flag. The driver sets this status value only from a call to its [**DxgkDdiOPMGetInformation**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_opm_get_information) function to determine if HDCP is enabled.

The display miniport driver returns a pointer to a DXGKMDT\_OPM\_STANDARD\_INFORMATION, DXGKMDT\_OPM\_ACTUAL\_OUTPUT\_FORMAT, DXGKMDT\_OPM\_ACP\_AND\_CGMSA\_SIGNALING, or DXGKMDT\_OPM\_CONNECTED\_HDCP\_DEVICE\_INFORMATION structure in the **abRequestedInformation** member of the [**DXGKMDT\_OPM\_REQUESTED\_INFORMATION**](/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_dxgkmdt_opm_requested_information) structure. A pointer to DXGKMDT\_OPM\_REQUESTED\_INFORMATION is returned through the *RequestedInformation* parameter of *DxgkDdiOPMGetInformation* or *DxgkDdiOPMGetCOPPCompatibleInformation*.

For example, consider two media playback applications, A and B. Each application controls, via OPM, the HDCP protection level of the connector that attaches the computer to the display monitor. Each application controls its own unique protected output. If the connector becomes unplugged, the next time either application initiates a *DxgkDdiOPMGetInformation* or *DxgkDdiOPMGetCOPPCompatibleInformation* request to its protected output, the display miniport driver should return the DXGKMDT\_OPM\_STATUS\_LINK\_LOST status flag.

Assume application A is the first to initiate a call to *DxgkDdiOPMGetInformation* or *DxgkDdiOPMGetCOPPCompatibleInformation* on its protected output. Application A then receives the DXGKMDT\_OPM\_STATUS\_LINK\_LOST flag and acts accordingly. If application A initiates a subsequent *DxgkDdiOPMGetInformation* or *DxgkDdiOPMGetCOPPCompatibleInformation* call, it should not receive the DXGKMDT\_OPM\_STATUS\_LINK\_LOST flag, unless the connector becomes unplugged again. When application B initiates a call to *DxgkDdiOPMGetInformation* or *DxgkDdiOPMGetCOPPCompatibleInformation* on its protected output, it receives the DXGKMDT\_OPM\_STATUS\_LINK\_LOST flag and acts accordingly. Again, application B should not receive the DXGKMDT\_OPM\_STATUS\_LINK\_LOST flag again until the connector becomes unplugged again.

 

