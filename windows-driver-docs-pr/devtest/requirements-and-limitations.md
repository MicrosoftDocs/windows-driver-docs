---
title: Requirements and Limitations
description: Requirements and Limitations
ms.assetid: 94ca8f45-7f04-47b6-ae23-d9217f6dc648
keywords: ["Perl scripts WDK INF files", "ChkINF", "INF File Syntax Checker", "INF files WDK , syntax checker", "syntax checker WDK INF files", "verifying INF files", "checking INF files", "scripts WDK ChkINF", "ChkINF WDK , requirements", "ChkINF WDK , limitations"]
---

# Requirements and Limitations


## <span id="ddk_requirements_and_limitations_tools"></span><span id="DDK_REQUIREMENTS_AND_LIMITATIONS_TOOLS"></span>


This topic explains the software that is required to run ChkINF and the limitations of the tool.

### <span id="required_perl_interpreter"></span><span id="REQUIRED_PERL_INTERPRETER"></span>Required Perl Interpreter

Starting with the Windows Driver Kit (WDK) for Windows Vista, the ChkINF tool contains a Perl interpreter that is located in the Tools\\chkinf subdirectory of the WDK.

In earlier versions of the Windows Driver Kit (WDK) that were known as the Device Driver Kit (DDK), you needed a Perl interpreter installed on your computer to run ChkINF. ChkINF should work correctly with any version of Perl 5.0 or greater, but it has not been tested with any versions previous to 5.003\_07.

Also, the directory in which the Perl interpreter is located must be added to the %PATH% environment variable on your system. If the installation program does not amend the path, you must do it manually.

Microsoft neither endorses nor recommends any specific third-party Perl interpreters, but ChkINF has been tested with the following Perl interpreters:

-   GNU Perl 5.005\_02 compiled for Win32

-   GNU Perl 5.6.0 compiled for Win32

-   Perl for Win32 5.003\_07 from ActiveWare Internet Corp.

-   ActivePerl 5.6.1.631 from ActiveState (see the [ActiveState](http://go.microsoft.com/fwlink/p/?linkid=10003) website)

### <span id="other_requirements"></span><span id="OTHER_REQUIREMENTS"></span>Other Requirements

To validate **Include** and **Needs** directives in an INF file, you must run ChkINF on the operating system for which the INF file is designed.

### <span id="limitations"></span><span id="LIMITATIONS"></span>Limitations

ChkINF does not support INF files for Windows 98 or Windows Me.

ChkINF validates elements of an INF file specific to a device setup class only for the device setup classes listed in the chkinf.htm file (located in the Tools\\chkinf subdirectory of the Windows Driver Kit \[WDK\].)

ChkINF has limited support for INF files in Unicode format, including Unicode Big Endian and UTF8, but it cannot interpret all extended characters. To validate an INF file in Unicode format, save the file as an ASCII text file before running ChkINF.

ChkINF does not verify the registry keys set by an INF file.

ChkINF incorrectly reports an error if a named service uses different binary names on the x86-based and Itanium-based platforms.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Requirements%20and%20Limitations%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




