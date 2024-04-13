---
title: Driver Package Rank Information in the SetupAPI Log
description: Driver Package Rank Information in the SetupAPI Log
keywords:
- SetupAPI logging WDK Windows Vista , driver rank information
- signature indicators WDK device installations
ms.date: 04/20/2017
---

# Driver Package Rank Information in the SetupAPI Log

When Windows is selecting a driver package to install, the SetupAPI log typically has a *Rank* entry that logs the driver rank in hexadecimal format and a *Signer Score* entry that logs the signature type. The following is an excerpt from a SetupAPI device log that shows an example of a Rank entry and an example of a Signer Score entry. In this excerpt, the Rank entry indicates that the driver has a rank of "0x00FF3101" and the Signer Score entry indicates that the driver is an inbox driver.

```cpp
     utl:      Driver Node:
     utl:           Status         - Outranked
     utl:           Driver INF     - input.inf (C:\WINDOWS\System32\DriverStore\FileRepository\input.inf_amd64_3c85f2862c8bffeb\input.inf)
     utl:           Class GUID     - {745a17a0-74d3-11d0-b6fe-00a0c90f57da}
     utl:           Driver Version - 06/21/2006,10.0.22475.1000
     utl:           Configuration  - USB\Class_03&SubClass_01 [HID_Inst.NT]
     utl:           Driver Rank    - 00FF3101
     utl:           Signer Score   - Inbox (0D000003)
```

Or, in some scenarios, the logging may appear more like this excerpt where the Rank entry indicates that the driver has a rank of "0x00ff0005" and the Signer Score entry indicates that the driver is an inbox driver.
```cpp
     dvi:           Created Driver Node:
     dvi:                HardwareID   - GenCdRom
     dvi:                InfName      - C:\WINDOWS\System32\DriverStore\FileRepository\cdrom.inf_amd64_9f14c614df704f62\cdrom.inf
     dvi:                DevDesc      - CD-ROM Drive
     dvi:                Section      - cdrom_install
     dvi:                Rank         - 0x00ff0005
     dvi:                Signer Score - INBOX
     dvi:                DrvDate      - 06/21/2006
     dvi:                Version      - 10.0.22475.1000
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

For more information about driver ranking, see [How Windows Ranks Drivers](how-setup-ranks-drivers--windows-vista-and-later-.md).

 

 





