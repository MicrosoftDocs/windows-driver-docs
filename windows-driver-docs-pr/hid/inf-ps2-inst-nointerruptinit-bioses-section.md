---
title: INF PS2\_Inst.NoInterruptInit.Bioses Section
author: windows-driver-content
description: INF PS2\_Inst.NoInterruptInit.Bioses Section
MS-HAID:
- 'km-ovr\_5b4cea2d-d8ed-4585-a36b-a1d98f856a08.xml'
- 'hid.inf\_ps2\_inst\_nointerruptinit\_bioses\_section'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 2bf1dc0f-00b6-4f4a-99f0-e9843fe6e66b
keywords: ["INF files WDK non-HID keyboard/mouse", "PS2_Inst.NoInterruptInit.Bioses section"]
---

# INF PS2\_Inst.NoInterruptInit.Bioses Section


## <a href="" id="ddk-inf-ps2-inst-nointerruptinit-bioses-section-kg"></a>


**\[PS2\_Inst.NoInterruptInit.Bioses\]**

*Disable*=*disable-string*
The mouse class installer checks if d*isable-string* is a substring of the string value of **HKLM\\Hardware\\Description\\System\\SystemBiosVersion**. If it is, the class installer executes the INF directives specified in an [INF PS2\_Inst.NoInterruptInit section](inf-ps2-inst-nointerruptinit-section.md).

### Entries and Values

<a href="" id="disable"></a>*Disable*  
Set to the d*isable-string* value.

<a href="" id="disable-string"></a>*disable-string*  
Specifies a substring in **HKLM\\Hardware\\Description\\System\\SystemBiosVersion** that uniquely identifies the system BIOS.

### <a href="" id="comments"></a>Remarks

This section is used only with PS/2 mouse devices and only in combination with an [INF **PS2\_Inst.NoInterruptInit** section](inf-ps2-inst-nointerruptinit-section.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhid\hid%5D:%20INF%20PS2_Inst.NoInterruptInit.Bioses%20Section%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


