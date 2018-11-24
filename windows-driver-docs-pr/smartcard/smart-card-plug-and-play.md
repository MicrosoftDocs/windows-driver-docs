---
title: Smart Card Plug and Play
description: Smart Card Plug and Play
ms.assetid: AE65A450-62A4-4774-A935-B7CB4301CCF4
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Smart Card Plug and Play


## <span id="_Pairing_Process"></span><span id="_pairing_process"></span><span id="_PAIRING_PROCESS"></span> Pairing Process


The operating system follows these steps to pair a smart card with an already installed minidriver:

-   Get the ATR from the smart card.
-   Iterate through entries in the HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\Cryptography\\Calais\\SmartCards registry key and do the following:

    -   Apply ATRMask subkey value that is stored in the registry to the ATR that was acquired from the smart card.
    -   Compare the masked ATR value to the ATR subkey value that is stored in the registry.
    -   If the two ATR values match, stop processing and pair the corresponding minidriver with the smart card.

Smart card ATR and ATRMask values must be carefully chosen to avoid the erroneous pairing of a minidriver with a smart card. The smart card ATR value that is stored in the registry should be the expected value after the ATRMask has been applied to an ATR read from a smart card. Otherwise, the masked ATR values from the card and the registry do not match and the pairing fails.

Beginning with Windows 7, the first time a smart card is inserted into a card reader triggers Plug and Play events that result in a search for an appropriate minidriver on the Windows Update site. The device ID that Windows generates to locate the driver on Windows Update depends upon the following factors:

-   Historical bytes from the ATR. For more information about ATR historical bytes, see section 8 of the ISO/IEC 7816-4:2005(E) standard.
-   Presence of the Microsoft Plug and Play AID application with a list of GUIDS in tag 0x7F68.
-   Presence of a PIV application on the card which will be paired with an inbox driver.
-   Presence of a GIDS (Generic Identity Device Specification) application with Microsoft Generic Profile on the card which will be paired with an inbox driver.

For more detailed information on the smart card discovery process for Plug and Play and Winscard, see [Smart Card Discovery Process](discovery-process.md). These processes result in the generation of a unique device ID for the smart card.

**Note**  To determine the device ID that Windows generates for a smart card, the recommended approach is to insert the smart card in a smart card reader that is attached to a computer that is running Windows 7 or later versions of Windows. The device ID can then be found by looking at the “Hardware Ids” property of the smart card device in Device Manager.

 

## <span id="Sample_INF_for_x86_and_amd64"></span><span id="sample_inf_for_x86_and_amd64"></span><span id="SAMPLE_INF_FOR_X86_AND_AMD64"></span>Sample INF for x86 and amd64


The following is a sample INF file for smart card installation in Windows 8 and earlier versions of Windows. This INF file is decorated for installation in X86 and AMD64 CPU platforms.

**Note**  To avoid problems with deployments, it is strongly advised to test your driver package on clean installations of all targeted operating systems prior to submitting the driver package to Winqual.

 

``` syntax
;
;FabrikamVendor Smartcard Minidriver for an x86 and x64 based package.
;

[Version]
Signature="$Windows NT$"
Class=SmartCard
ClassGuid={990A2BD7-E738-46c7-B26F-1CF8FB9F1391}
Provider=%FABRIKAMVENDOR%
CatalogFile=delta.cat
DriverVer=10/03/2008,7.0.0.4

[Manufacturer]
%FABRIKAMVENDOR%=FabrikamVendor,NTamd64,NTamd64.6.1,NTx86,NTx86.6.1

[FabrikamVendor.NTamd64]
%FabrikamCardDeviceName%=FabrikamVendor64_Install,SCFILTER\CID_51FF0800

[FabrikamVendor.NTx86]
%FabrikamCardDeviceName%=FabrikamVendor32_Install,SCFILTER\CID_51FF0800

[FabrikamVendor.NTamd64.6.1]
%FabrikamCardDeviceName%=FabrikamVendor64_61_Install,SCFILTER\CID_51FF0800

[FabrikamVendor.NTx86.6.1]
%FabrikamCardDeviceName%=FabrikamVendor32_61_Install,SCFILTER\CID_51FF0800

[DefaultInstall]
CopyFiles=x86_CopyFiles
AddReg=AddRegDefault

[DefaultInstall.ntamd64]
CopyFiles=amd64_CopyFiles
CopyFiles=wow64_CopyFiles
AddReg=AddRegWOW64
AddReg=AddRegDefault

[DefaultInstall.NTx86]
CopyFiles=x86_CopyFiles
AddReg=AddRegDefault

[SourceDisksFiles]
Fabrikamcm64.dll=1
Fabrikamcm.dll=1

[SourceDisksNames]
1 = %MediaDescription%

[FabrikamVendor64_Install.NT]
CopyFiles=amd64_CopyFiles
CopyFiles=wow64_CopyFiles
AddReg=AddRegWOW64
AddReg=AddRegDefault

[FabrikamVendor64_61_Install.NT]
CopyFiles=amd64_CopyFiles
CopyFiles=wow64_CopyFiles
AddReg=AddRegWOW64
AddReg=AddRegDefault
Include=umpass.inf
Needs=UmPass

[FabrikamVendor32_Install.NT]
CopyFiles=x86_CopyFiles
AddReg=AddRegDefault

[FabrikamVendor32_61_Install.NT]
CopyFiles=x86_CopyFiles
AddReg=AddRegDefault
Include=umpass.inf
Needs=UmPass

[FabrikamVendor64_61_Install.NT.Services]
Include=umpass.inf
Needs=UmPass.Services

[FabrikamVendor32_61_Install.NT.Services]
Include=umpass.inf
Needs=UmPass.Services


[FabrikamVendor64_61_Install.NT.HW]
Include=umpass.inf
Needs=UmPass.HW

[FabrikamVendor64_61_Install.NT.CoInstallers]
Include=umpass.inf
Needs=UmPass.CoInstallers


[FabrikamVendor64_61_Install.NT.Interfaces]
Include=umpass.inf
Needs=UmPass.Interfaces


[FabrikamVendor32_61_Install.NT.HW]
Include=umpass.inf
Needs=UmPass.HW

[FabrikamVendor32_61_Install.NT.CoInstallers]
Include=umpass.inf
Needs=UmPass.CoInstallers


[FabrikamVendor32_61_Install.NT.Interfaces]
Include=umpass.inf
Needs=UmPass.Interfaces


[amd64_CopyFiles]
Fabrikamcm.dll,Fabrikamcm64.dll

[x86_CopyFiles]
Fabrikamcm.dll

[wow64_CopyFiles]
Fabrikamcm.dll

[AddRegWOW64]
HKLM, %SmartCardNameWOW64%,"ATR",0x00000001,3b,04,51,ff,08,00
HKLM, %SmartCardNameWOW64%,"ATRMask",0x00000001,ff,ff,ff,ff,ff,ff
HKLM, %SmartCardNameWOW64%,"Crypto Provider",0x00000000,"Microsoft Base Smart Card Crypto Provider"
HKLM, %SmartCardNameWOW64%,"Smart Card Key Storage Provider",0x00000000,"Microsoft Smart Card Key Storage Provider"
HKLM, %SmartCardNameWOW64%,"80000001",0x00000000,%SmartCardCardModule%

[AddRegDefault]
HKLM, %SmartCardName%,"ATR",0x00000001,3b,04,51,ff,08,00
HKLM, %SmartCardName%,"ATRMask",0x00000001,ff,ff,ff,ff,ff,ff
HKLM, %SmartCardName%,"Crypto Provider",0x00000000,"Microsoft Base Smart Card Crypto Provider"
HKLM, %SmartCardName%,"Smart Card Key Storage Provider",0x00000000,"Microsoft Smart Card Key Storage Provider"
HKLM, %SmartCardName%,"80000001",0x00000000,%SmartCardCardModule%

[DestinationDirs]
amd64_CopyFiles=10,system32
x86_CopyFiles=10,system32
wow64_CopyFiles=10,syswow64


; =================== Generic ==================================

[Strings]
FABRIKAMVENDOR ="FabrikamVendor"
MediaDescription="FabrikamVendor Smart Card Minidriver Installation Disk"
FabrikamCardDeviceName="FabrikamVendor Minidriver for Smart Card"
SmartCardName="SOFTWARE\Microsoft\Cryptography\Calais\SmartCards\Fabrikam"
SmartCardNameWOW64="SOFTWARE\Wow6432Node\Microsoft\Cryptography\Calais\SmartCards\Fabrikam"
SmartCardCardModule="Fabrikamcm.dll"
```

The following are required for this type of INF file:

-   The hardware ID that is specified by the %FabrikamCardDeviceName% string must either be the ATR historical bytes of the device or the decoded value of the device’s smart card framework identifier. For more information about this identifier, see the “Windows Smart Card Framework Card Identifier” section in Smart Card Discovery Process.
-   The DefaultInstall section is mandatory in INF files for smart card minidriver packages.

 

 





