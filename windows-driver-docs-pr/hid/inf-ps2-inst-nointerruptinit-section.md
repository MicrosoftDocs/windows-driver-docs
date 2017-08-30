---
title: INF PS2_Inst.NoInterruptInit Section
author: windows-driver-content
description: INF PS2_Inst.NoInterruptInit Section
ms.assetid: e84cc7fc-8b17-4119-84f9-12ac888c68aa
keywords:
- INF files WDK non-HID keyboard/mouse
- PS2_Inst.NoInterruptInit section
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# INF PS2\_Inst.NoInterruptInit Section


## <a href="" id="ddk-inf-ps2-inst-nointerruptinit-section-kg"></a>


**\[PS2\_Inst.NoInterruptInit\]**
**AddReg** = *add-reg-section***.AddReg**
The mouse class installer executes the directives in this section if the *Disable* entry in an [INF **PS2\_Inst.NoInterruptInit.Bios** section](inf-ps2-inst-nointerruptinit-bioses-section.md) matches the system BIOS version.

### Entries and Values

<a href="" id="add-reg-section"></a>*add-reg-section*  
Specifies an **AddReg** section that the mouse class installer uses to set registry values in a device's hardware key. The registry values determine whether the system initializes a mouse device by using interrupts or by polling.

### <a href="" id="comments"></a>Remarks

This section is only used in combination with an [INF **PS2\_Inst.NoInterruptInit.Bioses** section](inf-ps2-inst-nointerruptinit-bioses-section.md). The primary purpose of this section is to specify an **AddReg** section that adds registry values to a mouse device's hardware key.

### *add-reg section Entries*

**HKR**,,"**DisableInitializePolledUI**",0x00010001,1
**HKR**,,"**MouseInitializePolled**",0x00010001,1

<a href="" id="disableinitializepolledui"></a>**DisableInitializePolledUI**  
Specifies a REG\_DWORD flag that indicates whether the **Fast Initialization** check box on the property page will be available. If **DisableInitializePolledUI** is set to a nonzero value, the check box is unavailable; otherwise, the check box is available.

<a href="" id="mouseinitializedpolled"></a>**MouseInitializedPolled**  
Specifies a REG\_DWORD flag that indicates whether the system must poll the device to initialize it. If **MouseInitializedPolled** is set to one, the system polls the mouse device; otherwise the system uses interrupts.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhid\hid%5D:%20INF%20PS2_Inst.NoInterruptInit%20Section%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


