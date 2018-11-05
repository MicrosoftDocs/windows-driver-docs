---
title: wdfkd.wdfdriverinfo
description: The wdfkd.wdfdriverinfo extension displays information about the specified driver, including its device tree, and version information.
ms.assetid: dc758fd3-1226-46e3-b249-2cf37ef3e539
keywords: ["wdfkd.wdfdriverinfo Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- wdfkd.wdfdriverinfo
api_type:
- NA
ms.localizationpriority: medium
---

# !wdfkd.wdfdriverinfo


The **!wdfkd.wdfdriverinfo** extension displays information about the specified driver, including its device tree, the version of the Kernel-Mode Driver Framework (KMDF) library that the driver was compiled with, and a list of the framework device objects that the driver created.

```dbgcmd
!wdfkd.wdfdriverinfo [DriverName [Flags]]
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______DriverName______"></span><span id="_______drivername______"></span><span id="_______DRIVERNAME______"></span> *DriverName*   
Optional. The name of the driver. *DriverName* must not include the .sys file name extension.

<span id="_______Flags______"></span><span id="_______flags______"></span><span id="_______FLAGS______"></span> *Flags*   
Optional. Flags that specify the kind of information to display. *Flags* can be any combination of the following bits:

<span id="Bit_0__0x1_"></span><span id="bit_0__0x1_"></span><span id="BIT_0__0X1_"></span>Bit 0 (0x1)  
The display will include verifier settings for the driver, and will also include a count of WDF objects. This flag can be combined with bit 6 (0x40) to display internal objects.

<span id="Bit_4__0x10_"></span><span id="bit_4__0x10_"></span><span id="BIT_4__0X10_"></span>Bit 4 (0x10)  
The display will include the KMDF handle hierarchy for the driver.

<span id="Bit_5__0x20_"></span><span id="bit_5__0x20_"></span><span id="BIT_5__0X20_"></span>Bit 5 (0x20)  
The display will include context and callback function information for each handle. This flag is valid only when bit 4 (0x10) is set.

<span id="Bit_6__0x40_"></span><span id="bit_6__0x40_"></span><span id="BIT_6__0X40_"></span>Bit 6 (0x40)  
The display will include additional information for each handle. This flag is valid only when bit 4 (0x10) is set. This flag can be combined with bit 0 (0x1) to display internal objects.

<span id="Bit_7__0x80_"></span><span id="bit_7__0x80_"></span><span id="BIT_7__0X80_"></span>Bit 7 (0x80)  
The handle information will be displayed in a more compact format.

<span id="Bit_8__0x100_"></span><span id="bit_8__0x100_"></span><span id="BIT_8__0X100_"></span>Bit 8 (0x100)  
The display will left align internal type information. This flag is valid only when bit 4 (0x10) is set.

<span id="Bit_9__0x200_"></span><span id="bit_9__0x200_"></span><span id="BIT_9__0X200_"></span>Bit 9 (0x200)  
The display will include handles that the driver potentially leaked. KMDF version 1.1 and later support this flag. This flag is valid only when bit 4 (0x10) is set.

<span id="Bit_10__0x400_"></span><span id="bit_10__0x400_"></span><span id="BIT_10__0X400_"></span>Bit 10 (0x400)  
The display will include the device tree in verbose form.

### <span id="DLL"></span><span id="dll"></span>DLL

Wdfkd.dll

### <span id="Frameworks"></span><span id="frameworks"></span><span id="FRAMEWORKS"></span>Frameworks

KMDF 1, UMDF 2

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information, see [Kernel-Mode Driver Framework Debugging](kernel-mode-driver-framework-debugging.md).

Remarks
-------

If you omit the *DriverName* parameter, the default driver is used. You can display the default driver by using the [**!wdfkd.wdfgetdriver**](-wdfkd-wdfgetdriver.md) extension; you can set the default driver by using the [**!wdfkd.wdfsetdriver**](-wdfkd-wdfsetdriver.md) extension.

The following example shows the display from the **!wdfkd.wdfdriverinfo** extension.

```dbgcmd
## kd> !wdfdriverinfo wdfrawbusenumtest 
----------------------------------
Default driver image name:   wdfrawbusenumtest
WDF library image name:      Wdf01000
 FxDriverGlobals  0x83b7af18
 WdfBindInfo      0xf22250ec
##    Version        v1.5 build(1234)
----------------------------------
WDFDRIVER: 0x7cbc90d0

    !WDFDEVICE 0x7ca7b1c0
            context:  dt 0x83584ff8 ROOT_CONTEXT (size is 0x1 bytes)
             <no associated attribute callbacks>

    !WDFDEVICE 0x7cad31c8
            context:  dt 0x8352cff0 RAW_PDO_CONTEXT (size is 0xc bytes)
             <no associated attribute callbacks>
```

 

 





