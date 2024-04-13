---
title: Supporting Rotation in a Display Miniport Driver
description: Supporting Rotation in a Display Miniport Driver
keywords:
- miniport drivers WDK display , rotation
- rotation WDK display
- clone mode WDK video present network
- surface rotation WDK display
ms.date: 04/20/2017
---

# Supporting Rotation in a Display Miniport Driver


A display miniport driver's [**DxgkDdiEnumVidPnCofuncModality**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_enumvidpncofuncmodality) function calls the [**pfnUpdatePathSupportInfo**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_vidpntopology_updatepathsupportinfo) function to report rotation support for each path in a video present network (VidPN) topology. For more information about reporting rotation support, see [Enumerating Cofunctional VidPN Source and Target Modes](enumerating-cofunctional-vidpn-source-and-target-modes.md).

The Microsoft DirectX graphics kernel subsystem uses non-rotated surface dimensions to create the shared primary surface. To notify a display miniport driver to rotate the surface, the DirectX graphics kernel subsystem specifies [**D3DKMDT\_VIDPN\_PRESENT\_PATH\_ROTATION**](/windows-hardware/drivers/ddi/d3dkmdt/ne-d3dkmdt-_d3dkmdt_vidpn_present_path_rotation)-typed values in the **Rotation** member of the [**D3DKMDT\_VIDPN\_PRESENT\_PATH\_TRANSFORMATION**](/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_d3dkmdt_vidpn_present_path_transformation) structure that is specified in the **ContentTransformation** member of the [**D3DKMDT\_VIDPN\_PRESENT\_PATH**](/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_d3dkmdt_vidpn_present_path) structure in calls to the display miniport driver's [**DxgkDdiCommitVidPn**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_commitvidpn) and [**DxgkDdiUpdateActiveVidPnPresentPath**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_updateactivevidpnpresentpath) functions.

**Note**   All rotation degrees are defined in the counter-clockwise direction, which is consistent with how GDI defines rotation.

 

When the DirectX subsystem notifies the display miniport driver to rotate the surface, the driver should rotate the surface data only if the **Rotate** bit-field flag was set in the **Flags** member of the [**DXGKARG\_PRESENT**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgkarg_present) structure that the *pPresent* parameter points to in a call to the driver's [**DxgkDdiPresent**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_present) function. Even if the driver determines that the current orientation of the screen is rotated from the presentation data and **Rotate** was not set, the driver should not rotate the data.

### <span id="Clone-mode_behavior"></span><span id="clone-mode_behavior"></span><span id="CLONE-MODE_BEHAVIOR"></span>Clone-mode behavior

*Clone mode* is a mode in which a video present source connects to multiple video present targets through multiple paths in a video present network. (For more information about video present networks, see [Multiple Monitors and Video Present Networks](multiple-monitors-and-video-present-networks.md).)

A display miniport driver handles rotation differently if it operates in clone mode because each target might require a different rotation. The operating system, various versions of Microsoft DirectX runtimes, and user-mode clients detect only the orientation of the primary video present target. Therefore, the content in the video present source will always match the orientation of the primary video present target.

The following table shows how a display miniport driver behaves in clone mode for all of the relevant situations. The setting of the **Rotate** flag is the setting of the **Rotate** bit-field in the **Flags** member of the [**DXGKARG\_PRESENT**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgkarg_present) structure.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Primary target</th>
<th align="left">Secondary target</th>
<th align="left">Rotate flag</th>
<th align="left">Driver behavior</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Not rotated</p></td>
<td align="left"><p>Not rotated</p></td>
<td align="left"><p>Not set</p></td>
<td align="left"><p>The driver performs no rotation.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Not rotated</p></td>
<td align="left"><p>Rotated</p></td>
<td align="left"><p>Not set</p></td>
<td align="left"><p>The driver rotates the secondary target even though the <strong>Rotate</strong> flag is not set.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Rotated</p></td>
<td align="left"><p>Not rotated</p></td>
<td align="left"><p>Set</p></td>
<td align="left"><p>The driver rotates the primary target but not the secondary target.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Rotated</p></td>
<td align="left"><p>Not rotated</p></td>
<td align="left"><p>Not set</p></td>
<td align="left"><p>Because <strong>Rotate</strong> is not set, the driver does not rotate the primary target. Because the secondary target does not match the orientation of the content in the source, the driver must rotate the secondary target.</p>
<p>This situation occurs when the client is rotation-aware, and it already has properly oriented the content of the source. Therefore, the operating system does not set <strong>Rotate</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Rotated</p></td>
<td align="left"><p>Rotated</p></td>
<td align="left"><p>Set</p></td>
<td align="left"><p>The driver rotates both the primary and secondary targets.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Rotated</p></td>
<td align="left"><p>Rotated</p></td>
<td align="left"><p>Not set</p></td>
<td align="left"><p>The rotation-aware client has already properly oriented the content of the source. Therefore, no additional rotation is required.</p></td>
</tr>
</tbody>
</table>

 

## <span id="clone-mode_requirements"></span><span id="CLONE-MODE_REQUIREMENTS"></span>Clone-mode requirements starting with Windows 8.1 Update


Starting with Windows 8.1 Update, drivers must meet these requirements. If test signing is enabled, a system bugcheck will occur if a driver fails to meet these requirements.

<span id="Primary_clone_path"></span><span id="primary_clone_path"></span><span id="PRIMARY_CLONE_PATH"></span>*Primary clone path*  
**Definition:** The path that includes the target monitor that duplicates the source display—for example, an external monitor that duplicates the display on a laptop computer.

**Requirement:** In the primary clone path, the driver must set **Offset0** to **TRUE** and the other 3 offset values in [**D3DKMDT\_VIDPN\_PRESENT\_PATH\_ROTATION\_SUPPORT**](/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_d3dkmdt_vidpn_present_path_rotation_support) to **FALSE**.

In the case of a portrait-first source display, the primary clone path is not rotationally offset. This means that the primary clone path always has an offset of zero ([**D3DKMDT\_VIDPN\_PRESENT\_PATH\_ROTATION\_SUPPORT**](/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_d3dkmdt_vidpn_present_path_rotation_support).**Offset0** is **TRUE**), and the Desktop Window Manager (DWM) rotates its content in advance to match the proper orientation.

The primary clone path determines the monitor refresh rate for all primary and secondary clone targets.

<span id="Secondary_clone_path"></span><span id="secondary_clone_path"></span><span id="SECONDARY_CLONE_PATH"></span>*Secondary clone path*  
**Definition:** The path that includes any additional target monitor, not part of the primary clone path, that also duplicates the source display.

**Requirement:** In the secondary clone path, the driver must set at least one of the 4 offset values in [**D3DKMDT\_VIDPN\_PRESENT\_PATH\_ROTATION\_SUPPORT**](/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_d3dkmdt_vidpn_present_path_rotation_support) to **TRUE**. If the driver doesn't support path-independent rotation, it should set **Offset0** to **TRUE** in all secondary clone paths.

Here are two examples of settings the driver should make if it supports path-independent rotation:

<span id="Landscape-first_example"></span><span id="landscape-first_example"></span><span id="LANDSCAPE-FIRST_EXAMPLE"></span>**Landscape-first example**  
If the source display and the target in the secondary clone path are both landscape-first monitors, in the secondary clone path the driver would set [**D3DKMDT\_VIDPN\_PRESENT\_PATH\_ROTATION\_SUPPORT**](/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_d3dkmdt_vidpn_present_path_rotation_support).**Offset0** to **TRUE** and the other 3 offset values in **D3DKMDT\_VIDPN\_PRESENT\_PATH\_ROTATION\_SUPPORT** to **FALSE**. Alternately in this case, in the secondary clone path the driver would set both **Offset0** and **Offset180** to **TRUE** and the other offset values to **FALSE**.

<span id="Portrait-first_example"></span><span id="portrait-first_example"></span><span id="PORTRAIT-FIRST_EXAMPLE"></span>**Portrait-first example**  
If the source display is a portrait-first device and connects to a landscape-first external monitor, in the secondary clone path the driver would set either **Offset270** or **Offset90** to **TRUE**.

For more info, see [Supporting Path-Independent Rotation](supporting-path-independent-rotation.md).

 

