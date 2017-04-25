---
title: Using the OPM DDI
description: Using the OPM DDI
ms.assetid: cd3c78a4-0241-48ab-9005-c544db199eb5
keywords:
- OPM WDK display , about DDI
- OPM WDK display , creating protected outputs
- OPM WDK display , destroying protected outputs
- OPM WDK display , getting certificates
- OPM WDK display , configuring protected outputs
- OPM WDK display , getting protected output information
- OPM WDK display , getting graphics adapter information
- protection levels WDK display , changing
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Using the OPM DDI


The Microsoft DirectX graphics kernel subsystem (*Dxgkrnl.sys*) uses the OPM DDI to create OPM protected outputs, destroy OPM protected outputs, get certificates, configure protected outputs, get information about protected outputs, and get information about the graphics adapter. The DirectX graphics kernel subsystem gets pointers to the OPM DDI functions when it calls the display miniport driver's [**DxgkDdiQueryInterface**](https://msdn.microsoft.com/library/windows/hardware/ff559764) function to query for the interface that is identified by GUID\_DEVINTERFACE\_OPM and DXGK\_OPM\_INTERFACE\_VERSION\_1. The following sequence describes how the OPM DDI is typically used to create, manipulate, and destroy OPM protected outputs:

1.  The DirectX graphics kernel subsystem calls the [**DxgkDdiOPMCreateProtectedOutput**](https://msdn.microsoft.com/library/windows/hardware/ff559705) function to create an OPM protected output. An OPM protected output always corresponds to exactly one physical video output. *DxgkDdiOPMCreateProtectedOutput* returns a handle to the newly created output.

2.  The DirectX graphics kernel subsystem calls the [**DxgkDdiOPMGetCertificateSize**](https://msdn.microsoft.com/library/windows/hardware/ff559715) and [**DxgkDdiOPMGetCertificate**](https://msdn.microsoft.com/library/windows/hardware/ff559711) functions to get the display miniport driver's OPM certificate or COPP certificate and its size.
    **Note**  *DxgkDdiOPMCreateProtectedOutput*, *DxgkDdiOPMGetCertificateSize*, and *DxgkDdiOPMGetCertificate* are the only OPM DDI functions that the DirectX graphics kernel subsystem does not pass a protected output handle to.

     

3.  The DirectX graphics kernel subsystem calls the [**DxgkDdiOPMGetRandomNumber**](https://msdn.microsoft.com/library/windows/hardware/ff559730) function to get the protected output's random number.

4.  The DirectX graphics kernel subsystem passes a 256-byte buffer in a call to the [**DxgkDdiOPMSetSigningKeyAndSequenceNumbers**](https://msdn.microsoft.com/library/windows/hardware/ff559735) function. The buffer contains data that is encrypted with one of the display miniport driver's public keys. For more information about public keys, download the Output Content Protection document from the [Output Content Protection and Windows Vista](http://go.microsoft.com/fwlink/p/?linkid=204788) website. The public key that is used depends on the semantics of the protected output. The public key in the display miniport driver's OPM certificate is used if the protected output has OPM semantics. The public key in the display miniport driver's COPP certificate is used if the protected output has COPP semantics. The encryption scheme that is used to encrypt the data also depends on the protected output's semantics. The data is encrypted with the standard RSA algorithm if the protected output has COPP semantics and with the RSAES-OAEP encryption scheme if the protected output has OPM semantics. For information about RSA, AES, and RSAES-OAEP, see the [RSA Laboratories](http://go.microsoft.com/fwlink/p/?linkid=70411) website. The display miniport driver uses the appropriate private key and decryption method to decrypt the data. A random number, two random sequence numbers, and a 128-bit AES key are in the decrypted data. The display miniport drive ensures that the random number matches the random number that the driver returned when its [**DxgkDdiOPMGetRandomNumber**](https://msdn.microsoft.com/library/windows/hardware/ff559730) function was called. The driver then stores the two sequence numbers and the 128-bit AES key.

5.  The DirectX graphics kernel subsystem can now call the [**DxgkDdiOPMGetInformation**](https://msdn.microsoft.com/library/windows/hardware/ff559725) or [**DxgkDdiOPMGetCOPPCompatibleInformation**](https://msdn.microsoft.com/library/windows/hardware/ff559720) function to get information from a protected output. The DirectX graphics kernel subsystem can also call [**DxgkDdiOPMConfigureProtectedOutput**](https://msdn.microsoft.com/library/windows/hardware/ff559701) to configure a protected output. *DxgkDdiOPMGetInformation* can be called only if the output has OPM semantics and *DxgkDdiOPMGetCOPPCompatibleInformation* can be called only if the output has COPP semantics. Typically, the DirectX graphics kernel subsystem calls *DxgkDdiOPMGetInformation* or *DxgkDdiOPMGetCOPPCompatibleInformation* to get information about the output and then calls *DxgkDdiOPMConfigureProtectedOutput* one or more times to configure the output. Then, the DirectX graphics kernel subsystem calls *DxgkDdiOPMGetInformation* or *DxgkDdiOPMGetCOPPCompatibleInformation* again. The DirectX graphics kernel subsystem can get the following types of information by calling *DxgkDdiOPMGetInformation* or *DxgkDdiOPMGetCOPPCompatibleInformation*:

    -   The output's connector type.
    -   The types of content protection that the output supports. Outputs can currently support Analog Copy Protection (ACP), [Content Generation Management System Analog (CGMS-A)](cgms-a-standards.md), High-bandwidth Digital Content Protection (HDCP), and DisplayPort Content Protection (DPCP). For more information about ACP, see the [Rovi (formerly Macrovision)](http://go.microsoft.com/fwlink/p/?linkid=71273) website. For more information about HDCP, see the [HDCP Specification Revision 1.1](http://go.microsoft.com/fwlink/p/?linkid=38728). For more information about DisplayPort, see the [DisplayPort](http://go.microsoft.com/fwlink/p/?linkid=71382) Web article.
    -   The output's current virtual protection level for a particular protection type.
    -   The physical output's actual protection level for a particular protection type.
    -   The version of the HDCP System Renewability Message (SRM) that the output currently uses. For more information about HDCP SRM, see the [HDCP Specification Revision 1.1](http://go.microsoft.com/fwlink/p/?linkid=38728). Only [**DxgkDdiOPMGetInformation**](https://msdn.microsoft.com/library/windows/hardware/ff559725) can get this information.
    -   The connected HDCP device's key-selection vector (KSV) and whether the HDCP device is a repeater. Only [**DxgkDdiOPMGetCOPPCompatibleInformation**](https://msdn.microsoft.com/library/windows/hardware/ff559720) can get this information. For more information about HDCP repeaters and KSVs, see the [HDCP Specification Revision 1.1](http://go.microsoft.com/fwlink/p/?linkid=38728).
    -   The type of expansion bus that the graphics adapter uses. PCI and AGP are examples of expansion buses.
    -   The format of the images that are sent from the physical connector that is associated with the protected output to a monitor.
    -   The CGMS-A and ACP signaling standards that the protected output supports. Only [**DxgkDdiOPMGetCOPPCompatibleInformation**](https://msdn.microsoft.com/library/windows/hardware/ff559720) can get this information.
    -   The identifier of the output.
    -   The electrical characteristics of a Digital Video Interface (DVI) output connector.

    The DirectX graphics kernel subsystem can change the following settings by calling [**DxgkDdiOPMConfigureProtectedOutput**](https://msdn.microsoft.com/library/windows/hardware/ff559701):

    -   The current protection level of one of the output's protection types. For example, *DxgkDdiOPMConfigureProtectedOutput* can enable or disable HDCP and can turn off ACP protection or change the current ACP protection level.
    -   The current HDCP SRM that the protected output uses.
    -   The current signaling standard that the protected output uses. This change can be done only if the output has COPP semantics.

6.  The DirectX graphics kernel subsystem calls [**DxgkDdiOPMDestroyProtectedOutput**](https://msdn.microsoft.com/library/windows/hardware/ff559708) when it finishes using the protected output object.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Using%20the%20OPM%20DDI%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




