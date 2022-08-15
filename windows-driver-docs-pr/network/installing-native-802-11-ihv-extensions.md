---
title: Installing Native 802.11 IHV Extensions
description: Installing Native 802.11 IHV Extensions
keywords:
- IHV extensions WDK Native 802.11 , installing
- installing Native 802.11 IHV extensions
- Native 802.11 IHV Extensions WDK , installing
ms.date: 06/17/2022
---

# Installing Native 802.11 IHV Extensions




 

To install the [Native 802.11 IHV Extensions DLL](native-802-11-ihv-extensions-dll4.md) and [Native 802.11 IHV UI Extensions DLL](native-802-11-ihv-ui-extensions-dll2.md), the independent hardware vendor (IHV) must make the following changes to the DDInstall section within the INF file that is used for the installation of the IHV's wireless LAN (WLAN) adapter.

-   Add a CopyFiles directive, with an associated *file-list-section*, to the INF file. The name of each DLL developed by the IHV must be within the *file-list-section*.

    For example, if the IHV is installing IhvExt.dll and IhvUIExt.dll, the INF file would have the following CopyFiles directive and *file-list-section*:

    ```
    CopyFiles = Sample-File-List-Section

    [Sample-File-List-Section]
    IhvExt.dll,,,2
    IhvUIExt.dll,,,2
    ```

    For more information about the CopyFiles directive, see [**INF CopyFiles Directive**](../install/inf-copyfiles-directive.md).

-   Make sure that a DestinationDirs section declares the destination of the *file-list-section* used in the CopyFiles directive.

    In the previous example, the DestinationDirs section would have the following values:

    ```
    [DestinationDirs]
    DefaultDestDir = 13
    Sample-File-List-Section = 13
    ```

    For more information about the DestinationDirs section, see [**INF DestinationDirs Section**](../install/inf-destinationdirs-section.md).

-   Make sure that an AddReg directive, with an associated *add-registry-section*, is added to the INF file for each WLAN adapter. For more information about the AddReg directive, see [**INF AddReg Directive**](../install/inf-addreg-directive.md).

    Within the *add-registry-section*, the following keys must be declared.

    <a href="" id="hkr--ndi-ihvextensions--extensibilitydll--0----------destination-file-name"></a>HKR, Ndi\\IHVExtensions, ExtensibilityDLL, 0, *destination-file-name*  
    This key identifies the name of the IHV Extensions DLL. For example, to associate the IhvExt.dll with the management of the WLAN adapter, the following key would be declared.

    ```
    HKR,Ndi\IHVExtensions, ExtensibilityDLL, 0, %13%\IhvExt.dll
    ```

    <a href="" id="hkr--ndi-ihvextensions--uiextensibilityclsid--0----------clsid"></a>HKR, Ndi\\IHVExtensions, UIExtensibilityCLSID, 0, *CLSID*  
    This key identifies the COM class identifier (CLSID), which was registered on the target system for the IHV UI Extensions DLL. The *CLSID* value must be enclosed in quotation marks. This key associates the IHV UI Extensions DLL with the IHV Extensions DLL installed through the **ExtensibilityDLL** key.

    **Note**  The **UIExtensibilityCLSID** key is required only if the IHV installs an IHV UI Extensions DLL.

     

    <a href="" id="hkr--ndi-ihvextensions--adapteroui--0x00010001----------oui"></a>HKR, Ndi\\IHVExtensions, AdapterOUI, 0x00010001, *OUI*  
    This key identifies the IEEE-assigned organizationally unique identifier (OUI), which identifies the IHV. The OUI value must be declared as a 24-bit hexadecimal value.

    The AdapterOUI key is used to verify that the OUI of the WLAN adapter matches the value of the **OUI** attribute of the **IHV** XML element. For more information about the **IHV** element and the Native 802.11 XML schema, refer to the Microsoft Windows SDK documentation.

For more information about the INF file and its sections, see [Creating an INF File](../install/overview-of-inf-files.md).

 

 
