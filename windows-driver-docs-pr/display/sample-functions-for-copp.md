---
title: Sample Functions for COPP
description: Sample Functions for COPP
ms.assetid: 73c9cf1c-c20d-456c-8029-5316fd8979d5
keywords: ["copy protection WDK COPP , sample functions", "video copy protection WDK COPP , sample functions", "COPP WDK DirectX VA , sample functions", "protected video WDK COPP , sample functions"]
---

# Sample Functions for COPP


## <span id="ddk_sample_functions_for_copp_gg"></span><span id="DDK_SAMPLE_FUNCTIONS_FOR_COPP_GG"></span>


**This section applies only to Windows Server 2003 SP1 and later, and Windows XP SP2 and later.**

The sample COPP functions show how to implement COPP processing functionality. These sample functions map to the [motion compensation callback functions](motion-compensation-callbacks.md) defined in the [**DD\_MOTIONCOMPCALLBACKS**](https://msdn.microsoft.com/library/windows/hardware/ff551660) structure. You can implement each sample function and a corresponding COPP I/O control (IOCTL) request, and then use a motion-compensation code template and a video miniport driver template to complete the implementation. For more information, see [Example Code for DirectX VA Devices](example-code-for-directx-va-devices.md).

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
<td align="left"><p>[<em>COPPOpenVideoSession</em>](https://msdn.microsoft.com/library/windows/hardware/ff539650)</p></td>
<td align="left"><p>Initializes the COPP device used for the current video session.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>COPPGetCertificateLength</em>](https://msdn.microsoft.com/library/windows/hardware/ff539644)</p></td>
<td align="left"><p>Retrieves the size, in bytes, of the certificate used by the graphics hardware.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>COPPKeyExchange</em>](https://msdn.microsoft.com/library/windows/hardware/ff539646)</p></td>
<td align="left"><p>Retrieves the digital certificate used by the graphics hardware.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>COPPSequenceStart</em>](https://msdn.microsoft.com/library/windows/hardware/ff540421)</p></td>
<td align="left"><p>Sets the current video session to protected mode.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>COPPCommand</em>](https://msdn.microsoft.com/library/windows/hardware/ff539642)</p></td>
<td align="left"><p>Sets the protection level on the physical connector associated with the COPP device.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>COPPQueryStatus</em>](https://msdn.microsoft.com/library/windows/hardware/ff539652)</p></td>
<td align="left"><p>Retrieves status on a protected video session that is associated with a COPP device.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>COPPCloseVideoSession</em>](https://msdn.microsoft.com/library/windows/hardware/ff539638)</p></td>
<td align="left"><p>Closes the COPP device object and instructs the driver to release hardware resources associated with the COPP device.</p></td>
</tr>
</tbody>
</table>

 

### <span id="Mapping_Sample_Functions_to_DD_MOTIONCOMPCALLBACKS"></span><span id="mapping_sample_functions_to_dd_motioncompcallbacks"></span><span id="MAPPING_SAMPLE_FUNCTIONS_TO_DD_MOTIONCOMPCALLBACKS"></span>Mapping Sample Functions to DD\_MOTIONCOMPCALLBACKS

The sample functions in this section map to the motion compensation callback functions by using a COPP IOCTL, as follows; that is, each sample function is called within its respective COPP IOCTL, and each COPP IOCTL is passed to the [**EngDeviceIoControl**](https://msdn.microsoft.com/library/windows/hardware/ff564838) function within its respective motion-compensation callback function.

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
<td align="left"><p>[<em>COPPOpenVideoSession</em>](https://msdn.microsoft.com/library/windows/hardware/ff539650)</p></td>
<td align="left"><p>[<strong>IOCTL_COPP_OpenDevice</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567768)</p></td>
<td align="left"><p><strong>CreateMoComp</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>COPPGetCertificateLength</em>](https://msdn.microsoft.com/library/windows/hardware/ff539644)</p></td>
<td align="left"><p>[<strong>IOCTL_COPP_GetCertificateLength</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567765)</p></td>
<td align="left"><p><strong>RenderMoComp</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>COPPKeyExchange</em>](https://msdn.microsoft.com/library/windows/hardware/ff539646)</p></td>
<td align="left"><p>[<strong>IOCTL_COPP_KeyExchange</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567766)</p></td>
<td align="left"><p><strong>RenderMoComp</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>COPPSequenceStart</em>](https://msdn.microsoft.com/library/windows/hardware/ff540421)</p></td>
<td align="left"><p>[<strong>IOCTL_COPP_StartSequence</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567781)</p></td>
<td align="left"><p><strong>RenderMoComp</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>COPPCommand</em>](https://msdn.microsoft.com/library/windows/hardware/ff539642)</p></td>
<td align="left"><p>[<strong>IOCTL_COPP_Command</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567762)</p></td>
<td align="left"><p><strong>RenderMoComp</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>COPPQueryStatus</em>](https://msdn.microsoft.com/library/windows/hardware/ff539652)</p></td>
<td align="left"><p>[<strong>IOCTL_COPP_Status</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567783)</p></td>
<td align="left"><p><strong>RenderMoComp</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>COPPCloseVideoSession</em>](https://msdn.microsoft.com/library/windows/hardware/ff539638)</p></td>
<td align="left"><p>[<strong>IOCTL_COPP_CloseDevice</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567759)</p></td>
<td align="left"><p><strong>DestroyMoComp</strong></p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Sample%20Functions%20for%20COPP%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




