---
title: Driver Rank Information in the SetupAPI Log
description: Driver Rank Information in the SetupAPI Log
ms.assetid: 169a1963-3fb3-4254-9634-78034cda2924
keywords: ["SetupAPI logging WDK Windows Vista , driver rank information", "signature indicators WDK device installations"]
---

# Driver Rank Information in the SetupAPI Log


Windows uses a signature indicator to represent the signature type. Windows saves this information in a [driver store](driver-store.md) database for internal use.

When Windows installs a driver, SetupAPI adds a *Rank* entry that logs the driver rank in hexadecimal format and a Signer Score entry that logs the signature type. The following is an excerpt from a SetupAPI device log that shows, in bold font style, an example of a Rank entry and an example of a Signer Score entry. In this excerpt, the Rank entry indicates that the driver has a rank of "0x0dff0000" and the Signer Score entry indicates that the driver is an inbox driver.

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Driver%20Rank%20Information%20in%20the%20SetupAPI%20Log%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




