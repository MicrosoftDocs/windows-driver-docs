---
title: Retrieving the OPM DDI
description: Retrieving the OPM DDI
keywords:
- OPM WDK display , retrieving DDI
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Retrieving the OPM DDI


The following sequence shows how the Microsoft DirectX graphics kernel subsystem (Dxgkrnl.sys) retrieves the display miniport driver's [OPM DDI](supporting-output-protection-manager.md):

1. The DirectX graphics kernel subsystem calls the display miniport driver's [**DxgkDdiAddDevice**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_add_device) function to create a context block for a graphics adapter and to return a handle to that graphics adapter.

2. The DirectX graphics kernel subsystem initializes a [**QUERY\_INTERFACE**](/windows-hardware/drivers/ddi/video/ns-video-_query_interface) structure with the values in the following table.

   <table>
   <colgroup>
   <col width="33%" />
   <col width="33%" />
   <col width="33%" />
   </colgroup>
   <thead>
   <tr class="header">
   <th align="left">Member name</th>
   <th align="left">Member type</th>
   <th align="left">Value</th>
   </tr>
   </thead>
   <tbody>
   <tr class="odd">
   <td align="left"><p><strong>InterfaceType</strong></p></td>
   <td align="left"><p>CONST PGUID</p></td>
   <td align="left"><p>A pointer to GUID_DEVINTERFACE_OPM</p>
   <p>(BF4672DE-6B4E-4BE4-A325-68A91EA49C09)</p></td>
   </tr>
   <tr class="even">
   <td align="left"><p><strong>Size</strong></p></td>
   <td align="left"><p>USHORT</p></td>
   <td align="left"><p>sizeof(DXGK_OPM_INTERFACE)</p></td>
   </tr>
   <tr class="odd">
   <td align="left"><p><strong>Version</strong></p></td>
   <td align="left"><p>USHORT</p></td>
   <td align="left"><p>DXGK_OPM_INTERFACE_VERSION_1</p></td>
   </tr>
   <tr class="even">
   <td align="left"><p><strong>Interface</strong></p></td>
   <td align="left"><p>PINTERFACE</p></td>
   <td align="left"><p>A pointer to a <a href="/windows-hardware/drivers/ddi/dispmprt/ns-dispmprt-_dxgk_opm_interface" data-raw-source="[&lt;strong&gt;DXGK_OPM_INTERFACE&lt;/strong&gt;](/windows-hardware/drivers/ddi/dispmprt/ns-dispmprt-_dxgk_opm_interface)"><strong>DXGK_OPM_INTERFACE</strong></a> structure</p></td>
   </tr>
   <tr class="odd">
   <td align="left"><p><strong>InterfaceSpecificData</strong></p></td>
   <td align="left"><p>PVOID</p></td>
   <td align="left"><p>NULL</p></td>
   </tr>
   </tbody>
   </table>

     

3. The DirectX graphics kernel subsystem passes the initialized QUERY\_INTERFACE in a call to the display miniport driver's [**DxgkDdiQueryInterface**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_query_interface) function.

4. If the display miniport driver does not support the OPM interface, [**DxgkDdiQueryInterface**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_query_interface) must return STATUS\_NOT\_SUPPORTED.

   If the display miniport driver supports OPM, [**DxgkDdiQueryInterface**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_query_interface) initializes the [**DXGK\_OPM\_INTERFACE**](/windows-hardware/drivers/ddi/dispmprt/ns-dispmprt-_dxgk_opm_interface) structure that was received in the **Interface** member of [**QUERY\_INTERFACE**](/windows-hardware/drivers/ddi/video/ns-video-_query_interface) with the values in the following table.

   **Member name, type, and value:**

   <span id="Size"></span><span id="size"></span><span id="SIZE"></span>**Size**  
   Type USHORT

   sizeof(DXGK\_OPM\_INTERFACE)

   <span id="Version"></span><span id="version"></span><span id="VERSION"></span>**Version**  
   Type USHORT

   DXGK\_OPM\_INTERFACE\_VERSION\_1

   <span id="InterfaceReference"></span><span id="interfacereference"></span><span id="INTERFACEREFERENCE"></span>**InterfaceReference**  
   Type PINTERFACE\_REFERENCE

   A pointer to the display miniport driver's **InterfaceReference** routine (For information about **InterfaceReference**, see the Remarks section of the [**INTERFACE**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_interface) structure.)

   <span id="InterfaceDereference"></span><span id="interfacedereference"></span><span id="INTERFACEDEREFERENCE"></span>**InterfaceDereference**  
   Type PINTERFACE\_DEREFERENCE

   A pointer to the display miniport driver's **InterfaceDereference** routine (For information about **InterfaceDereference**, see the Remarks section of the [**INTERFACE**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_interface) structure.)

   <span id="DxgkDdiOPMGetCertificateSize"></span><span id="dxgkddiopmgetcertificatesize"></span><span id="DXGKDDIOPMGETCERTIFICATESIZE"></span>**DxgkDdiOPMGetCertificateSize**  
   Type DXGKDDI\_OPM\_GET\_CERTIFICATE\_SIZE

   A pointer to the display miniport driver's [**DxgkDdiOPMGetCertificateSize**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_opm_get_certificate_size) function

   <span id="DxgkDdiOPMGetCertificate"></span><span id="dxgkddiopmgetcertificate"></span><span id="DXGKDDIOPMGETCERTIFICATE"></span>**DxgkDdiOPMGetCertificate**  
   Type DXGKDDI\_OPM\_GET\_CERTIFICATE

   A pointer to the display miniport driver's [**DxgkDdiOPMGetCertificate**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_opm_get_certificate) function

   <span id="DxgkDdiOPMCreateProtectedOutput"></span><span id="dxgkddiopmcreateprotectedoutput"></span><span id="DXGKDDIOPMCREATEPROTECTEDOUTPUT"></span>**DxgkDdiOPMCreateProtectedOutput**  
   Type DXGKDDI\_OPM\_CREATE\_PROTECTED\_OUTPUT

   A pointer to the display miniport driver's [**DxgkDdiOPMCreateProtectedOutput**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_opm_create_protected_output) function

   <span id="DxgkDdiOPMGetRandomNumber"></span><span id="dxgkddiopmgetrandomnumber"></span><span id="DXGKDDIOPMGETRANDOMNUMBER"></span>**DxgkDdiOPMGetRandomNumber**  
   Type DXGKDDI\_OPM\_GET\_RANDOM\_NUMBER

   A pointer to the display miniport driver's [**DxgkDdiOPMGetRandomNumber**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_opm_get_random_number) function

   <span id="DxgkDdiOPMSetSigningKeyAndSequenceNumbers"></span><span id="dxgkddiopmsetsigningkeyandsequencenumbers"></span><span id="DXGKDDIOPMSETSIGNINGKEYANDSEQUENCENUMBERS"></span>**DxgkDdiOPMSetSigningKeyAndSequenceNumbers**  
   DXGKDDI\_OPM\_SET\_SIGNING\_KEY\_AND\_SEQUENCE\_NUMBERS

   A pointer to the display miniport driver's [**DxgkDdiOPMSetSigningKeyAndSequenceNumbers**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_opm_set_signing_key_and_sequence_numbers) function

   <span id="DxgkDdiOPMGetInformation"></span><span id="dxgkddiopmgetinformation"></span><span id="DXGKDDIOPMGETINFORMATION"></span>**DxgkDdiOPMGetInformation**  
   DXGKDDI\_OPM\_GET\_INFORMATION

   A pointer to the display miniport driver's [**DxgkDdiOPMGetInformation**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_opm_get_information) function

   <span id="DxgkDdiOPMGetCOPPCompatibleInformation"></span><span id="dxgkddiopmgetcoppcompatibleinformation"></span><span id="DXGKDDIOPMGETCOPPCOMPATIBLEINFORMATION"></span>**DxgkDdiOPMGetCOPPCompatibleInformation**  
   DXGKDDI\_OPM\_GET\_COPP\_COMPATIBLE\_INFORMATION

   A pointer to the display miniport driver's [**DxgkDdiOPMGetCOPPCompatibleInformation**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_opm_get_copp_compatible_information) function

   <span id="DxgkDdiOPMConfigureProtectedOutput"></span><span id="dxgkddiopmconfigureprotectedoutput"></span><span id="DXGKDDIOPMCONFIGUREPROTECTEDOUTPUT"></span>**DxgkDdiOPMConfigureProtectedOutput**  
   DXGKDDI\_OPM\_CONFIGURE\_PROTECTED\_OUTPUT

   A pointer to the display miniport driver's [**DxgkDdiOPMConfigureProtectedOutput**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_opm_configure_protected_output) function

   <span id="DxgkDdiOPMDestroyProtectedOutput"></span><span id="dxgkddiopmdestroyprotectedoutput"></span><span id="DXGKDDIOPMDESTROYPROTECTEDOUTPUT"></span>**DxgkDdiOPMDestroyProtectedOutput**  
   DXGKDDI\_OPM\_DESTROY\_PROTECTED\_OUTPUT

   A pointer to the display miniport driver's [**DxgkDdiOPMDestroyProtectedOutput**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_opm_destroy_protected_output) function

5. When the display miniport driver is finished using the OPM interface, the driver calls its **InterfaceDereference** routine. The driver should call **InterfaceDereference** before its [**DxgkDdiRemoveDevice**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_remove_device) function is called.

