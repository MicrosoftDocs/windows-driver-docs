---
title: Retrieving the OPM DDI
description: Retrieving the OPM DDI
ms.assetid: 84218245-f5f3-4a6f-88ed-9cd5db224e30
keywords:
- OPM WDK display , retrieving DDI
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Retrieving the OPM DDI


The following sequence shows how the Microsoft DirectX graphics kernel subsystem (Dxgkrnl.sys) retrieves the display miniport driver's [OPM DDI](https://msdn.microsoft.com/library/windows/hardware/ff568627):

1.  The DirectX graphics kernel subsystem calls the display miniport driver's [**DxgkDdiAddDevice**](https://msdn.microsoft.com/library/windows/hardware/ff559586) function to create a context block for a graphics adapter and to return a handle to that graphics adapter.

2.  The DirectX graphics kernel subsystem initializes a [**QUERY\_INTERFACE**](https://msdn.microsoft.com/library/windows/hardware/ff569225) structure with the values in the following table.

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
    <td align="left"><p>A pointer to a [<strong>DXGK_OPM_INTERFACE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561986) structure</p></td>
    </tr>
    <tr class="odd">
    <td align="left"><p><strong>InterfaceSpecificData</strong></p></td>
    <td align="left"><p>PVOID</p></td>
    <td align="left"><p>NULL</p></td>
    </tr>
    </tbody>
    </table>

     

3.  The DirectX graphics kernel subsystem passes the initialized QUERY\_INTERFACE in a call to the display miniport driver's [**DxgkDdiQueryInterface**](https://msdn.microsoft.com/library/windows/hardware/ff559764) function.

4.  If the display miniport driver does not support the OPM interface, [**DxgkDdiQueryInterface**](https://msdn.microsoft.com/library/windows/hardware/ff559764) must return STATUS\_NOT\_SUPPORTED.

    If the display miniport driver supports OPM, [**DxgkDdiQueryInterface**](https://msdn.microsoft.com/library/windows/hardware/ff559764) initializes the [**DXGK\_OPM\_INTERFACE**](https://msdn.microsoft.com/library/windows/hardware/ff561986) structure that was received in the **Interface** member of [**QUERY\_INTERFACE**](https://msdn.microsoft.com/library/windows/hardware/ff569225) with the values in the following table.

    **Member name, type, and value:**

    <span id="Size"></span><span id="size"></span><span id="SIZE"></span>**Size**  
    Type USHORT

    sizeof(DXGK\_OPM\_INTERFACE)

    <span id="Version"></span><span id="version"></span><span id="VERSION"></span>**Version**  
    Type USHORT

    DXGK\_OPM\_INTERFACE\_VERSION\_1

    <span id="InterfaceReference"></span><span id="interfacereference"></span><span id="INTERFACEREFERENCE"></span>**InterfaceReference**  
    Type PINTERFACE\_REFERENCE

    A pointer to the display miniport driver's **InterfaceReference** routine (For information about **InterfaceReference**, see the Remarks section of the [**INTERFACE**](https://msdn.microsoft.com/library/windows/hardware/ff547825) structure.)

    <span id="InterfaceDereference"></span><span id="interfacedereference"></span><span id="INTERFACEDEREFERENCE"></span>**InterfaceDereference**  
    Type PINTERFACE\_DEREFERENCE

    A pointer to the display miniport driver's **InterfaceDereference** routine (For information about **InterfaceDereference**, see the Remarks section of the [**INTERFACE**](https://msdn.microsoft.com/library/windows/hardware/ff547825) structure.)

    <span id="DxgkDdiOPMGetCertificateSize"></span><span id="dxgkddiopmgetcertificatesize"></span><span id="DXGKDDIOPMGETCERTIFICATESIZE"></span>**DxgkDdiOPMGetCertificateSize**  
    Type DXGKDDI\_OPM\_GET\_CERTIFICATE\_SIZE

    A pointer to the display miniport driver's [**DxgkDdiOPMGetCertificateSize**](https://msdn.microsoft.com/library/windows/hardware/ff559715) function

    <span id="DxgkDdiOPMGetCertificate"></span><span id="dxgkddiopmgetcertificate"></span><span id="DXGKDDIOPMGETCERTIFICATE"></span>**DxgkDdiOPMGetCertificate**  
    Type DXGKDDI\_OPM\_GET\_CERTIFICATE

    A pointer to the display miniport driver's [**DxgkDdiOPMGetCertificate**](https://msdn.microsoft.com/library/windows/hardware/ff559711) function

    <span id="DxgkDdiOPMCreateProtectedOutput"></span><span id="dxgkddiopmcreateprotectedoutput"></span><span id="DXGKDDIOPMCREATEPROTECTEDOUTPUT"></span>**DxgkDdiOPMCreateProtectedOutput**  
    Type DXGKDDI\_OPM\_CREATE\_PROTECTED\_OUTPUT

    A pointer to the display miniport driver's [**DxgkDdiOPMCreateProtectedOutput**](https://msdn.microsoft.com/library/windows/hardware/ff559705) function

    <span id="DxgkDdiOPMGetRandomNumber"></span><span id="dxgkddiopmgetrandomnumber"></span><span id="DXGKDDIOPMGETRANDOMNUMBER"></span>**DxgkDdiOPMGetRandomNumber**  
    Type DXGKDDI\_OPM\_GET\_RANDOM\_NUMBER

    A pointer to the display miniport driver's [**DxgkDdiOPMGetRandomNumber**](https://msdn.microsoft.com/library/windows/hardware/ff559730) function

    <span id="DxgkDdiOPMSetSigningKeyAndSequenceNumbers"></span><span id="dxgkddiopmsetsigningkeyandsequencenumbers"></span><span id="DXGKDDIOPMSETSIGNINGKEYANDSEQUENCENUMBERS"></span>**DxgkDdiOPMSetSigningKeyAndSequenceNumbers**  
    DXGKDDI\_OPM\_SET\_SIGNING\_KEY\_AND\_SEQUENCE\_NUMBERS

    A pointer to the display miniport driver's [**DxgkDdiOPMSetSigningKeyAndSequenceNumbers**](https://msdn.microsoft.com/library/windows/hardware/ff559735) function

    <span id="DxgkDdiOPMGetInformation"></span><span id="dxgkddiopmgetinformation"></span><span id="DXGKDDIOPMGETINFORMATION"></span>**DxgkDdiOPMGetInformation**  
    DXGKDDI\_OPM\_GET\_INFORMATION

    A pointer to the display miniport driver's [**DxgkDdiOPMGetInformation**](https://msdn.microsoft.com/library/windows/hardware/ff559725) function

    <span id="DxgkDdiOPMGetCOPPCompatibleInformation"></span><span id="dxgkddiopmgetcoppcompatibleinformation"></span><span id="DXGKDDIOPMGETCOPPCOMPATIBLEINFORMATION"></span>**DxgkDdiOPMGetCOPPCompatibleInformation**  
    DXGKDDI\_OPM\_GET\_COPP\_COMPATIBLE\_INFORMATION

    A pointer to the display miniport driver's [**DxgkDdiOPMGetCOPPCompatibleInformation**](https://msdn.microsoft.com/library/windows/hardware/ff559720) function

    <span id="DxgkDdiOPMConfigureProtectedOutput"></span><span id="dxgkddiopmconfigureprotectedoutput"></span><span id="DXGKDDIOPMCONFIGUREPROTECTEDOUTPUT"></span>**DxgkDdiOPMConfigureProtectedOutput**  
    DXGKDDI\_OPM\_CONFIGURE\_PROTECTED\_OUTPUT

    A pointer to the display miniport driver's [**DxgkDdiOPMConfigureProtectedOutput**](https://msdn.microsoft.com/library/windows/hardware/ff559701) function

    <span id="DxgkDdiOPMDestroyProtectedOutput"></span><span id="dxgkddiopmdestroyprotectedoutput"></span><span id="DXGKDDIOPMDESTROYPROTECTEDOUTPUT"></span>**DxgkDdiOPMDestroyProtectedOutput**  
    DXGKDDI\_OPM\_DESTROY\_PROTECTED\_OUTPUT

    A pointer to the display miniport driver's [**DxgkDdiOPMDestroyProtectedOutput**](https://msdn.microsoft.com/library/windows/hardware/ff559708) function

5.  When the display miniport driver is finished using the OPM interface, the driver calls its **InterfaceDereference** routine. The driver should call **InterfaceDereference** before its [**DxgkDdiRemoveDevice**](https://msdn.microsoft.com/library/windows/hardware/ff559789) function is called.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Retrieving%20the%20OPM%20DDI%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




