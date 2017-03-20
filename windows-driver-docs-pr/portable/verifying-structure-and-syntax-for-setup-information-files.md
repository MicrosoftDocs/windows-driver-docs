---
Description: Verifying Structure and Syntax for Setup Information Files
MS-HAID: 'wpddk.verifying\_structure\_and\_syntax\_for\_setup\_information\_files'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: Verifying Structure and Syntax for Setup Information Files
---

# Verifying Structure and Syntax for Setup Information Files


The Windows Driver Kit (WDK) supplies a set of Perl scripts that are referred to as the ChkINF tool. These scripts verify the structure and syntax of setup information (.inf) files. For more information about these scripts, see the Driver Development Tools section of the WDK documentation.

All WPD .inf files must invoke the UMDF co-installer. This means that whenever a CoInstallers section is declared, a \[CopyFiles\] directive must exist. If your driver does not require any additional co-installer binaries (and therefore does not need a CopyFiles directive), you can satisfy the requirement by declaring an empty CopyFiles section and referencing it from within the CoInstallers section.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[wpd_dk\wpddk]:%20Verifying%20Structure%20and%20Syntax%20for%20Setup%20Information%20Files%20%20RELEASE:%20%281/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")



