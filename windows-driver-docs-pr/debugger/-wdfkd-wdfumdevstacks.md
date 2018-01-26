---
title: wdfkd.wdfumdevstacks
description: The wdfkd.wdfumdevstacks extension displays information about all UMDF device stacks in the implicit process.
ms.assetid: 05D09B0D-4ED8-4333-B4BC-5BE28C63312C
keywords: ["wdfkd.wdfumdevstacks Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- wdfkd.wdfumdevstacks
api_type:
- NA
---

# !wdfkd.wdfumdevstacks


The **!wdfkd.wdfumdevstacks** extension displays information about all UMDF device stacks in the [implicit process](controlling-threads-and-processes.md).

```
!wdfkd.wdfumdevstacks [Flags] 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Flags______"></span><span id="_______flags______"></span><span id="_______FLAGS______"></span> *Flags*   
Optional. Specifies the type of information to be displayed. *Flags* can be any combination of the following bits. The default value is 0x01.

<span id="Bit_0__0x01_"></span><span id="bit_0__0x01_"></span><span id="BIT_0__0X01_"></span>Bit 0 (0x01)  
Displays detailed information about each device stack.

<span id="Bit_7__0x80_"></span><span id="bit_7__0x80_"></span><span id="BIT_7__0X80_"></span>Bit 7 (0x80)  
Displays information about the internal framework.

## <span id="DLL"></span><span id="dll"></span>DLL


Wdfkd.dll

## <span id="Frameworks"></span><span id="frameworks"></span><span id="FRAMEWORKS"></span>Frameworks


UMDF 2

## <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information


For more information, see [Kernel-Mode Driver Framework Debugging](kernel-mode-driver-framework-debugging.md).

Remarks
-------

You can use this command in a kernel-mode debugging session or in a user-mode debugging session that is attached to the UMDF host process (wudfhost.exe).

This command displays the same information as the user-mode command [**!wudfext.umdevstacks**](-wudfext-umdevstacks.md).

Before you use this command, use [**!process**](-process.md) to get a list of all UMDF host processes.

```
0: kd> !process 0 0 wudfhost.exe
PROCESS ffffe00000c32900
    SessionId: 0  Cid: 079c    Peb: 7ff782537000  ParentCid: 037c
    DirBase: 607af000  ObjectTable: ffffc00009807940  HandleCount: <Data Not Accessible>
    Image: WUDFHost.exe
```

The preceding output shows that there is one UMDF host process; that is, there is one instance of wudfhost.exe.

Next use [**.process**](-process--set-process-context-.md) to set the implicit process to wudfhost.exe.

```
0: kd> .process /P ffffe00000c32900
Implicit process is now ffffe000`00c32900
.cache forcedecodeptes done
```

Now use **!wdfkd.wdfumdevstacks** to display the UMDF device stacks in the implicit process (wudfhost.exe).

```
0: kd> !wdfkd.wdfumdevstacks
Number of device stacks: 1
  Device Stack: 0x000000a5a3ab5f70     Pdo Name: \Device\00000052
    Active: Yes
    Number of UM devices: 1
    Device 0
      Driver Config Registry Path: MyUmdf2Driver
      UMDriver Image Path: C:\WINDOWS\System32\drivers\UMDF\MyUmdf2Driver.dll
      FxDriver: 0xa5a3acaaa0
      FxDevice: 0xa5a3ac4fc0
      Open UM files (use !wdfumfile <addr> for details): <None>
      Device XFerMode: Deferred RW: Buffered CTL: Buffered
      DevStack XFerMode: Deferred RW: Buffered CTL: Buffered
```

The preceding output shows that there is one UMDF device stack in the implicit process. You can also see that the device stack has one device object (Number of UM devices: 1).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!wdfkd.wdfumdevstacks%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




