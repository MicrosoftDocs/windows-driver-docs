---
title: Pscript Support for Stapling
author: windows-driver-content
description: Pscript Support for Stapling
MS-HAID:
- 'pscript\_eba18c7b-f29b-4f3a-8179-67fd6c981a89.xml'
- 'print.pscript\_support\_for\_stapling'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 75fc11e1-5cd9-4e95-b062-989fe493fdb5
keywords: ["minidrivers WDK Pscript , stapling", "stapling WDK Pscript"]
---

# Pscript Support for Stapling


## <a href="" id="ddk-pscript-support-for-stapling-gg"></a>


The Microsoft Pscript driver supports the following standard stapling features in [*PPD*](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-postscript-printer-description--ppd-) files.

-   \*StapleLocation

-   \*StapleOrientation

-   \*StapleWhen

-   \*StapleX

-   \*StapleY

For more information about these standard stapling features, see *PostScript Printer Description File Format Specification*, Version 4.3, 9 February 1996. (This resource may not be available in some languages and countries.)

To determine whether the device supports stapling, the Pscript driver uses the following logic:

1.  If none of the previously-listed standard stapling features is defined in the PPD file, then stapling is not supported.

2.  If \*StapleOrientation is the only stapling feature that is defined in the PPD file, then stapling is supported.

3.  If one or more of the previously-listed standard stapling features (other than \*StapleOrientation) are defined in the PPD file and if any of the defined features is constrained by the current configuration of an installable feature, then stapling is not supported. For example, if the NotInstalled option of the DuplexerUnit installable feature places a constraint on \*StapleLocation, and the printer's current configuration for DuplexerUnit is NotInstalled, then stapling is not supported.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Pscript%20Support%20for%20Stapling%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


