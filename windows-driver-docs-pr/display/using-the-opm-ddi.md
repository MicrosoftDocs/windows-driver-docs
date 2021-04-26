---
title: Using the OPM DDI
description: Using the OPM DDI
keywords:
- OPM WDK display , about DDI
- OPM WDK display , creating protected outputs
- OPM WDK display , destroying protected outputs
- OPM WDK display , getting certificates
- OPM WDK display , configuring protected outputs
- OPM WDK display , getting protected output information
- OPM WDK display , getting graphics adapter information
- protection levels WDK display , changing
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using the OPM DDI

The Microsoft DirectX graphics kernel subsystem (*Dxgkrnl.sys*) uses the OPM DDI to create OPM protected outputs, destroy OPM protected outputs, get certificates, configure protected outputs, get information about protected outputs, and get information about the graphics adapter. The DirectX graphics kernel subsystem gets pointers to the OPM DDI functions when it calls the display miniport driver's [**DxgkDdiQueryInterface**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_query_interface) function to query for the interface that is identified by GUID_DEVINTERFACE_OPM and DXGK_OPM_INTERFACE_VERSION_1. The following sequence describes how the OPM DDI is typically used to create, manipulate, and destroy OPM protected outputs:

1. The DirectX graphics kernel subsystem calls the [**DxgkDdiOPMCreateProtectedOutput**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_opm_create_protected_output) function to create an OPM protected output. An OPM protected output always corresponds to exactly one physical video output. *DxgkDdiOPMCreateProtectedOutput* returns a handle to the newly created output.

2. The DirectX graphics kernel subsystem calls the [**DxgkDdiOPMGetCertificateSize**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_opm_get_certificate_size) and [**DxgkDdiOPMGetCertificate**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_opm_get_certificate) functions to get the display miniport driver's OPM certificate or COPP certificate and its size.

   > [!NOTE]
   > *DxgkDdiOPMCreateProtectedOutput*, *DxgkDdiOPMGetCertificateSize*, and *DxgkDdiOPMGetCertificate* are the only OPM DDI functions that the DirectX graphics kernel subsystem does not pass a protected output handle to.

3. The DirectX graphics kernel subsystem calls the [**DxgkDdiOPMGetRandomNumber**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_opm_get_random_number) function to get the protected output's random number.

4. The DirectX graphics kernel subsystem passes a 256-byte buffer in a call to the [**DxgkDdiOPMSetSigningKeyAndSequenceNumbers**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_opm_set_signing_key_and_sequence_numbers) function. The buffer contains data that is encrypted with one of the display miniport driver's public keys. For more information about public keys, download the Output Content Protection document from the [Output Content Protection and Windows Vista](https://download.microsoft.com/download/5/D/6/5D6EAF2B-7DDF-476B-93DC-7CF0072878E6/output_protect.doc) website. The public key that is used depends on the semantics of the protected output. The public key in the display miniport driver's OPM certificate is used if the protected output has OPM semantics. The public key in the display miniport driver's COPP certificate is used if the protected output has COPP semantics. The encryption scheme that is used to encrypt the data also depends on the protected output's semantics. The data is encrypted with the standard RSA algorithm if the protected output has COPP semantics and with the RSAES-OAEP encryption scheme if the protected output has OPM semantics. For information about RSA, AES, and RSAES-OAEP, see the [RSA Laboratories](https://www.rsa.com/) website. The display miniport driver uses the appropriate private key and decryption method to decrypt the data. A random number, two random sequence numbers, and a 128-bit AES key are in the decrypted data. The display miniport drive ensures that the random number matches the random number that the driver returned when its [**DxgkDdiOPMGetRandomNumber**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_opm_get_random_number) function was called. The driver then stores the two sequence numbers and the 128-bit AES key.

5. The DirectX graphics kernel subsystem can now call the [**DxgkDdiOPMGetInformation**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_opm_get_information) or [**DxgkDdiOPMGetCOPPCompatibleInformation**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_opm_get_copp_compatible_information) function to get information from a protected output. The DirectX graphics kernel subsystem can also call [**DxgkDdiOPMConfigureProtectedOutput**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_opm_configure_protected_output) to configure a protected output. *DxgkDdiOPMGetInformation* can be called only if the output has OPM semantics and *DxgkDdiOPMGetCOPPCompatibleInformation* can be called only if the output has COPP semantics. Typically, the DirectX graphics kernel subsystem calls *DxgkDdiOPMGetInformation* or *DxgkDdiOPMGetCOPPCompatibleInformation* to get information about the output and then calls *DxgkDdiOPMConfigureProtectedOutput* one or more times to configure the output. Then, the DirectX graphics kernel subsystem calls *DxgkDdiOPMGetInformation* or *DxgkDdiOPMGetCOPPCompatibleInformation* again. The DirectX graphics kernel subsystem can get the following types of information by calling *DxgkDdiOPMGetInformation* or *DxgkDdiOPMGetCOPPCompatibleInformation*:

    - The output's connector type.
    - The types of content protection that the output supports. Outputs can currently support:
      - [Analog Copy Protection (ACP)](https://business.tivo.com/services/acp-technology)
      - [Content Generation Management System Analog (CGMS-A)](cgms-a-standards.md)
      - [High-bandwidth Digital Content Protection (HDCP)](https://www.digital-cp.com/hdcp-specifications)
      - [DisplayPort](https://go.microsoft.com/fwlink/p/?linkid=71382) Content Protection (DPCP)
    - The output's current virtual protection level for a particular protection type.
    - The physical output's actual protection level for a particular protection type.
    - The version of the HDCP System Renewability Message (SRM) that the output currently uses. For more information about HDCP SRM, see the [HDCP Specification Revision 1.1](https://go.microsoft.com/fwlink/p/?linkid=38728). Only [**DxgkDdiOPMGetInformation**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_opm_get_information) can get this information.
    - The connected HDCP device's key-selection vector (KSV) and whether the HDCP device is a repeater. Only [**DxgkDdiOPMGetCOPPCompatibleInformation**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_opm_get_copp_compatible_information) can get this information. For more information about HDCP repeaters and KSVs, see the [HDCP Specification Revision 1.1](https://go.microsoft.com/fwlink/p/?linkid=38728).
    - The type of expansion bus that the graphics adapter uses. PCI and AGP are examples of expansion buses.
    - The format of the images that are sent from the physical connector that is associated with the protected output to a monitor.
    - The CGMS-A and ACP signaling standards that the protected output supports. Only [**DxgkDdiOPMGetCOPPCompatibleInformation**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_opm_get_copp_compatible_information) can get this information.
    - The identifier of the output.
    - The electrical characteristics of a Digital Video Interface (DVI) output connector.

    The DirectX graphics kernel subsystem can change the following settings by calling [**DxgkDdiOPMConfigureProtectedOutput**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_opm_configure_protected_output):

    - The current protection level of one of the output's protection types. For example, *DxgkDdiOPMConfigureProtectedOutput* can enable or disable HDCP and can turn off ACP protection or change the current ACP protection level.
    - The current HDCP SRM that the protected output uses.
    - The current signaling standard that the protected output uses. This change can be done only if the output has COPP semantics.

6. The DirectX graphics kernel subsystem calls [**DxgkDdiOPMDestroyProtectedOutput**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_opm_destroy_protected_output) when it finishes using the protected output object.
