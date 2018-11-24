---
title: Driver Rank Information in the SetupAPI Log
description: Driver Rank Information in the SetupAPI Log
ms.assetid: 169a1963-3fb3-4254-9634-78034cda2924
keywords:
- SetupAPI logging WDK Windows Vista , driver rank information
- signature indicators WDK device installations
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Driver Rank Information in the SetupAPI Log


Windows uses a signature indicator to represent the signature type. Windows saves this information in a [driver store](driver-store.md) database for internal use.

When Windows installs a driver, SetupAPI adds a *Rank* entry that logs the driver rank in hexadecimal format and a Signer Score entry that logs the signature type. The following is an excerpt from a SetupAPI device log that shows, in bold font style, an example of a Rank entry and an example of a Signer Score entry. In this excerpt, the Rank entry indicates that the driver has a rank of "0x0dff0000" and the Signer Score entry indicates that the driver is an inbox driver.

```cpp
     dvi:      Created Driver Node:
     dvi:           HardwareID   - ROOT\UPDATE
     dvi:           InfName      - D:\Windows\System32\DriverStore\FileRepository\machine.inf_36c3d8da\machine.inf
     dvi:           DevDesc      - Microcode Update Device
     dvi:           DrvDesc      - Microcode Update Device
     dvi:           Provider     - Microsoft
     dvi:           Mfg          - (Standard system devices)
     dvi:           InstallSec   - UPDATE_DRV
     dvi:           ActualSec    - UPDATE_DRV
     dvi:           Rank         - 0x0dff0000
     dvi:           Signer       - Microsoft Windows Component Publisher
     dvi:           Signer Score - INBOX
     dvi:           DrvDate      - 10/01/2002
     dvi:           Version      - 6.0.5270.8
```

The following is a list of the Signer Score entries that Windows logs in the SetupAPI device log for each type of signature:

<a href="" id="premium-whql-signature"></a>Premium WHQL signature  
"Signer Score - WHQL Logo Gold"

<a href="" id="standard-whql-signature"></a>Standard WHQL signature  
"Signer Score - WHQL Logo Silver"

<a href="" id="an-unspecified-microsoft-signature"></a>An unspecified Microsoft signature  
"Signer Score - WHQL Unclassified"

<a href="" id="a-whql-signature-for-a-windows-version-earlier-than-windows-vista-and-equal-to-or-later-than-the-lowerlogoversion-value-of-the-driver-s-device-setup-class-"></a>A WHQL signature for a Windows version earlier than Windows Vista and equal to or later than the [LowerLogoVersion](lowerlogoversion.md) value of the driver's device setup class.  
"Signer Score - WHQL"

<a href="" id="a-microsoft-signature-for-an-inbox-driver"></a>A Microsoft signature for an inbox driver  
"Signer Score - INBOX"

<a href="" id="an-authenticode-signature-or-whql-signature-for-a-windows-version-earlier-than-the-version-that-is-specified-by-lowerlogoversion-for-the-device-setup-class-of-the-driver"></a>An Authenticode signature or WHQL signature for a Windows version earlier than the version that is specified by **LowerLogoVersion** for the device setup class of the driver  
"Signer Score - Authenticode"

<a href="" id="unsigned-driver"></a>Unsigned driver  
"Signer Score - Not digitally signed"

For more information about driver ranking, see [How Windows Ranks Drivers (Windows Vista and Later)](how-setup-ranks-drivers--windows-vista-and-later-.md).

 

 





