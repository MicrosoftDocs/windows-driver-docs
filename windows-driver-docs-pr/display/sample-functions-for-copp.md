---
title: Sample Functions for COPP
description: Sample Functions for COPP
keywords:
- copy protection WDK COPP , sample functions
- video copy protection WDK COPP , sample functions
- COPP WDK DirectX VA , sample functions
- protected video WDK COPP , sample functions
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Sample Functions for COPP


## <span id="ddk_sample_functions_for_copp_gg"></span><span id="DDK_SAMPLE_FUNCTIONS_FOR_COPP_GG"></span>


**This section applies only to Windows Server 2003 SP1 and later, and Windows XP SP2 and later.**

The sample COPP functions show how to implement COPP processing functionality. These sample functions map to the [motion compensation callback functions](motion-compensation-callbacks.md) defined in the [**DD\_MOTIONCOMPCALLBACKS**](/windows/win32/api/ddrawint/ns-ddrawint-dd_motioncompcallbacks) structure. You can implement each sample function and a corresponding COPP I/O control (IOCTL) request, and then use a motion-compensation code template and a video miniport driver template to complete the implementation. For more information, see [Example Code for DirectX VA Devices](example-code-for-directx-va-devices.md).

### <span id="COPP_Sample_Functions"></span><span id="copp_sample_functions"></span><span id="COPP_SAMPLE_FUNCTIONS"></span>COPP Sample Functions

The sample COPP functions in the following table are called by using the COPP device. For more information about the COPP device, see [COPP Device Definition Template Code](copp-device-definition-template-code.md) and [Defining the COPP Device Class](defining-the-copp-device-class.md).

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Member Function</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/display/coppopenvideosession" data-raw-source="[&lt;em&gt;COPPOpenVideoSession&lt;/em&gt;](./coppopenvideosession.md)"><em>COPPOpenVideoSession</em></a></p></td>
<td align="left"><p>Initializes the COPP device used for the current video session.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/display/coppgetcertificatelength" data-raw-source="[&lt;em&gt;COPPGetCertificateLength&lt;/em&gt;](./coppgetcertificatelength.md)"><em>COPPGetCertificateLength</em></a></p></td>
<td align="left"><p>Retrieves the size, in bytes, of the certificate used by the graphics hardware.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/display/coppkeyexchange" data-raw-source="[&lt;em&gt;COPPKeyExchange&lt;/em&gt;](./coppkeyexchange.md)"><em>COPPKeyExchange</em></a></p></td>
<td align="left"><p>Retrieves the digital certificate used by the graphics hardware.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/display/coppsequencestart" data-raw-source="[&lt;em&gt;COPPSequenceStart&lt;/em&gt;](./coppsequencestart.md)"><em>COPPSequenceStart</em></a></p></td>
<td align="left"><p>Sets the current video session to protected mode.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/display/coppcommand" data-raw-source="[&lt;em&gt;COPPCommand&lt;/em&gt;](./coppcommand.md)"><em>COPPCommand</em></a></p></td>
<td align="left"><p>Sets the protection level on the physical connector associated with the COPP device.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/display/coppquerystatus" data-raw-source="[&lt;em&gt;COPPQueryStatus&lt;/em&gt;](./coppquerystatus.md)"><em>COPPQueryStatus</em></a></p></td>
<td align="left"><p>Retrieves status on a protected video session that is associated with a COPP device.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/display/coppclosevideosession" data-raw-source="[&lt;em&gt;COPPCloseVideoSession&lt;/em&gt;](./coppclosevideosession.md)"><em>COPPCloseVideoSession</em></a></p></td>
<td align="left"><p>Closes the COPP device object and instructs the driver to release hardware resources associated with the COPP device.</p></td>
</tr>
</tbody>
</table>

 

### <span id="Mapping_Sample_Functions_to_DD_MOTIONCOMPCALLBACKS"></span><span id="mapping_sample_functions_to_dd_motioncompcallbacks"></span><span id="MAPPING_SAMPLE_FUNCTIONS_TO_DD_MOTIONCOMPCALLBACKS"></span>Mapping Sample Functions to DD\_MOTIONCOMPCALLBACKS

The sample functions in this section map to the motion compensation callback functions by using a COPP IOCTL, as follows; that is, each sample function is called within its respective COPP IOCTL, and each COPP IOCTL is passed to the [**EngDeviceIoControl**](/windows/win32/api/winddi/nf-winddi-engdeviceiocontrol) function within its respective motion-compensation callback function.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Function</th>
<th align="left">IOCTL</th>
<th align="left">DD_MOTIONCOMPCALLBACKS member</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/display/coppopenvideosession" data-raw-source="[&lt;em&gt;COPPOpenVideoSession&lt;/em&gt;](./coppopenvideosession.md)"><em>COPPOpenVideoSession</em></a></p></td>
<td align="left"><p><a href="/windows-hardware/drivers/display/" data-raw-source="[&lt;strong&gt;IOCTL_COPP_OpenDevice&lt;/strong&gt;](./index.md)"><strong>IOCTL_COPP_OpenDevice</strong></a></p></td>
<td align="left"><p><strong>CreateMoComp</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/display/coppgetcertificatelength" data-raw-source="[&lt;em&gt;COPPGetCertificateLength&lt;/em&gt;](./coppgetcertificatelength.md)"><em>COPPGetCertificateLength</em></a></p></td>
<td align="left"><p><a href="/windows-hardware/drivers/display/ioctl-copp-getcertificatelength" data-raw-source="[&lt;strong&gt;IOCTL_COPP_GetCertificateLength&lt;/strong&gt;](./ioctl-copp-getcertificatelength.md)"><strong>IOCTL_COPP_GetCertificateLength</strong></a></p></td>
<td align="left"><p><strong>RenderMoComp</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/display/coppkeyexchange" data-raw-source="[&lt;em&gt;COPPKeyExchange&lt;/em&gt;](./coppkeyexchange.md)"><em>COPPKeyExchange</em></a></p></td>
<td align="left"><p><a href="/windows-hardware/drivers/display/ioctl-copp-keyexchange" data-raw-source="[&lt;strong&gt;IOCTL_COPP_KeyExchange&lt;/strong&gt;](./ioctl-copp-keyexchange.md)"><strong>IOCTL_COPP_KeyExchange</strong></a></p></td>
<td align="left"><p><strong>RenderMoComp</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/display/coppsequencestart" data-raw-source="[&lt;em&gt;COPPSequenceStart&lt;/em&gt;](./coppsequencestart.md)"><em>COPPSequenceStart</em></a></p></td>
<td align="left"><p><a href="/windows-hardware/drivers/display/ioctl-copp-startsequence" data-raw-source="[&lt;strong&gt;IOCTL_COPP_StartSequence&lt;/strong&gt;](./ioctl-copp-startsequence.md)"><strong>IOCTL_COPP_StartSequence</strong></a></p></td>
<td align="left"><p><strong>RenderMoComp</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/display/coppcommand" data-raw-source="[&lt;em&gt;COPPCommand&lt;/em&gt;](./coppcommand.md)"><em>COPPCommand</em></a></p></td>
<td align="left"><p><a href="/windows-hardware/drivers/display/ioctl-copp-command" data-raw-source="[&lt;strong&gt;IOCTL_COPP_Command&lt;/strong&gt;](./ioctl-copp-command.md)"><strong>IOCTL_COPP_Command</strong></a></p></td>
<td align="left"><p><strong>RenderMoComp</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/display/coppquerystatus" data-raw-source="[&lt;em&gt;COPPQueryStatus&lt;/em&gt;](./coppquerystatus.md)"><em>COPPQueryStatus</em></a></p></td>
<td align="left"><p><a href="/windows-hardware/drivers/display/ioctl-copp-status" data-raw-source="[&lt;strong&gt;IOCTL_COPP_Status&lt;/strong&gt;](./ioctl-copp-status.md)"><strong>IOCTL_COPP_Status</strong></a></p></td>
<td align="left"><p><strong>RenderMoComp</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/display/coppclosevideosession" data-raw-source="[&lt;em&gt;COPPCloseVideoSession&lt;/em&gt;](./coppclosevideosession.md)"><em>COPPCloseVideoSession</em></a></p></td>
<td align="left"><p><a href="/windows-hardware/drivers/display/" data-raw-source="[&lt;strong&gt;IOCTL_COPP_CloseDevice&lt;/strong&gt;](./index.md)"><strong>IOCTL_COPP_CloseDevice</strong></a></p></td>
<td align="left"><p><strong>DestroyMoComp</strong></p></td>
</tr>
</tbody>
</table>

 

