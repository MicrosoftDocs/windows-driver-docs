---
title: "!acxkd"
description: "The !acxkd extension displays information about audio class extension ACX drivers."
keywords: ["acxkd Windows Debugging"]
ms.date: 06/14/2024
topic_type:
- apiref
ms.topic: reference
api_name:
- acxkd
api_type:
- NA
---

# !acxkd

The **!acxkd** extension displays information about audio class extension (ACX) drivers. For more information about ACX, see [ACX audio class extensions overview](../audio/acx-audio-class-extensions-overview.md).

## Syntax

```dbgcmd
!acxkd.[Options]
```

### DLL

Acxkd.dll

### Debugger Version

The !acxkd extension is available in WinDbg version 1.2402.24001.0 and later.

### ACX 1.0 debugging

The !acxkd debugger extension offers only partial functionality under ACX 1.0. Updating to ACX 1.1 is recommended.

## Parameters

*Options* - Specifies the type of information to be display.

| Option             | Description                                           | Parameter                                         |
|--------------------|-------------------------------------------------------|---------------------------------------------------|
| !help              | Displays information on available extension commands.  |  `[<command name>]`                               |
| !acxcircuit        | Dump an ACXCIRCUIT object.                             | `<circuit>` - ACXCIRCUIT WDF handle               |
| !acxdataformat     | Dump an ACXDATAFORMAT object.                          | `<dataformat>` - ACXDATAFORMAT WDF handle         |
| !acxdataformatlist | Dump an ACXDATAFORMATLIST object.                      | `<dataformatlist>` - ACXDATAFORMATLIST WDF handle |
| !acxdevice         | Dump an ACXDEVICE object.                              | `<device>` - ACXDEVICE WDF handle                 |
| !acxelement        | Dump an ACXELEMENT object.                             | `<element>` - ACXELEMENT WDF handle               |
| !acxevents         | Dump events of an ACXOBJECT object.                    | `<events>` - ACXOBJECT WDF handle                 |
| !acxfactory        | Dump an ACXFACTORYCIRCUT object.                       | `<factory>` - ACXFACTORYCIRCUIT WDF handle        |
| !acxmanager        | Dump an ACXMANAGER object.                             | None                                              |
| !acxmethods        | Dump methods of an ACXOBJECT object.                   | `<object>` - ACXOBJECT WDF handle                 |
| !acxobjbag         | Dump an ACXOBJECTBAG object.                           | `<objbag>` - ACXOBJECTBAG WDF handle              |
| !acxobject         | Dump an ACXOBJECT object.                              | `<object>` - ACXOBJECT WDF handle                 |
| !acxpin            | Dump an ACXPIN object.                                 | `<pin>` - ACXPIN WDF handle                       |
| !acxproperties     | Dump properties of an ACXOBJECT object.                | `<properties>` - ACXOBJECT WDF handle             |
| !acxstream         | Dump an ACXSTREAM object.                              | `<stream>` - ACXSTREAM handle                     |
| !acxstreambridge   | Dump an ACXSTREAMBRIDGE object.                        | `<bridge>` - ACXSTREAMBRIDGE handle               |
| !acxtarget         | Dump an ACXTARGET object.                              | `<target>` - ACXTARGET WDF handle                 |
| !acxtemplate       | Dump an ACXTEMPLATE object.                            | `<tmpt>` - ACXTEMPLATE handle                     |

## Remarks

### !acxkd.help

To list all available commands, use the acxkd `!help` command.

```dbgcmd
0: kd> !acxkd.help
Commands for C:\Debugger\acxkd.dll:
  !acxcircuit        - Dump a ACXCIRCUT object.
  !acxdataformat     - Dump a ACXDATAFORMAT object.
  !acxdataformatlist - Dump a ACXDATAFORMATLIST object.
  !acxdevice         - Dump a ACXDEVICE object.
  !acxelement        - Dump a ACXELEMENT object.
  !acxevents         - Dump events of a ACXOBJECT object.
  !acxfactory        - Dump a ACXFACTORYCIRCUT object.
  !acxmanager        - Dump a ACXMANAGER object.
  !acxmethods        - Dump methods of a ACXOBJECT object.
  !acxobjbag         - Dump a ACXOBJECTBAG object.
  !acxobject         - Dump a ACXOBJECT* object.
  !acxpin            - Dump a ACXPIN object.
  !acxproperties     - Dump properties of a ACXOBJECT object.
  !acxstream         - Dump a ACXSTREAM object.
  !acxstreambridge   - Dump a ACXSTREAMBRIDGE object.
  !acxtarget         - Dump a ACXTARGET* object.
  !acxtemplate       - Dump a ACX*TEMPLATE object.
  !help              - Displays information on available extension commands
!help <cmd> will give more information for a particular command
```

Use the acxkd `!help` command to learn more about any of the commands, for example the `!acxmanager` command.

```dbgcmd
0: kd> !acxkd.help acxmanager
!acxmanager
Dump a ACXMANAGER object.
```

### !acxkd.acxmanager

Use the `!acxmanager` command to display information about the ACXMANAGER ACX WDF object.

```dbgcmd
0: kd> !acxmanager
Dumping info for ACXMANAGER 0x000049f6c3c769f8

    Delete pending: No

    # singleton composites: 0
    # Composite factories: 0
    !wdfhandle 000049f6c3c769f8
    dt Acx01000!Acx::AfxManager ffffb6093c3896b0
```

### !acxkd.acxobject

In the output for the !acxmanager an address is provided for the wdfhandle. Use the wdfhandle address with the `!acxobject` command to display information about the ACXMANAGER or any other ACX object.

```dbgcmd
0: kd> !acxobject 000049f6c3c769f8
Dumping info for ACXMANAGER 0x000049f6c3c769f8

    Delete pending: No

    # singleton composites: 0
    # Composite factories: 0
    !wdfhandle 000049f6c3c769f8
    dt Acx01000!Acx::AfxManager ffffb6093c3896b0
```

Click on the `dt` link in the output shown above, to see more information about the internal ACX object structures.

```dbgcmd
0: kd> dt Acx01000!Acx::AfxManager ffffb6093c3896b0
   +0x000 m_Object         : 0x000049f6`c3c769f8 ACXMANAGER__
   =fffff803`8a478ad8 s_AfxManager     : 0xffffb609`3c3896b0 Acx::AfxManager
   +0x008 m_AcxGlobals     : 0xffffb609`403cae24 _ACX_DRIVER_GLOBALS
   +0x010 m_Flags          : 0
   +0x010 m_Unloading      : 0y0
   +0x018 m_CompositesMutex : _FAST_MUTEX
   +0x050 m_CompositeFactoriesList : _LIST_ENTRY [ 0xffffb609`3c389700 - 0xffffb609`3c389700 ]
   +0x060 m_CompositeFactoriesCount : 0n0
   +0x068 m_CompositesList : _LIST_ENTRY [ 0xffffb609`3c389718 - 0xffffb609`3c389718 ]
   +0x078 m_CompositesCount : 0n0
   +0x080 m_FactoriesList  : _LIST_ENTRY [ 0xffffb609`3c389730 - 0xffffb609`3c389730 ]
   +0x090 m_CircuitsList   : _LIST_ENTRY [ 0xffffb609`40a27068 - 0xffffb609`40a27068 ]
   +0x0a0 m_FiltersMutex   : _FAST_MUTEX
   +0x0d8 m_FactoryFiltersList : _LIST_ENTRY [ 0xffffb609`3c389788 - 0xffffb609`3c389788 ]
   +0x0e8 m_CircuitFiltersList : _LIST_ENTRY [ 0xffffb609`3c389798 - 0xffffb609`3c389798 ]
   +0x0f8 m_FactoriesNotificationHandle : 0xffffc70c`b2356790 Void
   +0x100 m_CircuitsNotificationHandle : 0xffffc70c`b2357ec0 Void
   +0x108 m_CommandQueue   : 0xffffb609`3ffc5400 Acx::AfxWorkQueue
```

Note that the debugger output may contain a mix of public ACX objects such as ACXMANAGER, ACXCIRCUITFACTORY, and ACXCIRCUIT and internal structures that are defined to be opaque. The internal types are not guaranteed to stay the same, or be available in different releases of ACX, and must not be called or used directly.

Since ACX objects are WDF objects, you can use the [!wdfkd.wdfhandle](-wdfkd-wdfhandle.md) command to display additional information about the ACXMANAGER object.

```dbgcmd
0: kd> !wdfhandle 000049f6c3c769f8
Treating handle as a KMDF handle!

Dumping WDFHANDLE 0x000049f6c3c769f8
=============================
Handle type is WDFOBJECT [ACXMANAGER]
Refcount: 2
Contexts:
    context:  dt 0xffffb6093c3896b0 Acx01000!AfxManager (size is 0x110 bytes)
    EvtCleanupCallback fffff8038a453070 Acx01000!Acx::WdfCpp::ObjectContext<ACXMANAGER__ *,Acx::AfxManager>::EvtObjectContextCleanupThunk
    EvtDestroyCallback fffff8038a453000 Acx01000!Acx::WdfCpp::ObjectContext<ACXMANAGER__ *,Acx::AfxManager>::EvtObjectContextDestroyThunk

    context:  dt 0xffffb609404c2280 Acx01000!WdfCustomType_ACXMANAGER (size is 0x10 bytes)
    <no associated attribute callbacks>

Parent: !wdfhandle 0x000049f6d4e2d5c8, type is WDFDEVICE
Owning device: !wdfdevice 0x000049f6d4e2d5c8

!wdfobject 0xffffb6093c389600
```

### !acxkd.acxpin

Commands that display other ACX information, such as `!acxpin` require a WDF handle to the object. For information on locating the WDF handle for an ACX object, see [Example ACX driver walkthrough](#example-acx-driver-walkthrough) in this article.

```dbgcmd
0: kd> !acxpin 0x000049f6befeee38
Dumping info for ACXPIN 0x000049f6befeee38

    ID: 0
    Type: AcxPinTypeSink
    Type: AcxPinCommunicationSink

    Category: KSCATEGORY_AUDIO
    Name: {00000000-0000-0000-0000-000000000000}
```

Depending on the state of the ACX object, not all information may be available to display.

### !acxkd.acxdataformatlist

Similar to !acxpin, `!acxdataformatlist` displays information on ACX dataformat lists.

```dbgcmd
0: kd> !acxdataformatlist 0x000049f6bf8be668
Dumping info for ACXDATAFORMATLIST 0x000049f6bf8be668

    # Scan count: 0
    # Data formats: 6
    Data formats:
        Sample Rate: 48000, #Channels: 2, #Bits: 16, ValidBits: 16, Mask: 0x3 (default)
        Sample Rate: 48000, #Channels: 2, #Bits: 32, ValidBits: 24, Mask: 0x3
        Sample Rate: 44100, #Channels: 2, #Bits: 16, ValidBits: 16, Mask: 0x3
        Sample Rate: 44100, #Channels: 2, #Bits: 32, ValidBits: 24, Mask: 0x3
        Sample Rate: 32000, #Channels: 2, #Bits: 16, ValidBits: 16, Mask: 0x3
        Sample Rate: 32000, #Channels: 2, #Bits: 32, ValidBits: 24, Mask: 0x3

    !wdfhandle 000049f6bf8be668
    dt Acx01000!Acx::AfxDataFormatList ffffb60940444530
```

## Example ACX driver walkthrough

This section provides a walkthrough of debugging an ACX driver.

### Symbols path

Use [.symfix](-symfix--set-symbol-store-path-.md) and the [.sympath (Set Symbol Path)](-sympath--set-symbol-path-.md) commands to change the symbol path.  If you're using local code with the driver add the path to that code as well. Use the [.reload (Reload Module)](-reload--reload-module-.md) command to reload symbols from the current path.

```dbgcmd
.symfix
.sympath+ C:\Windows-driver-samples-develop\audio\Acx\Samples\AudioCodec\Driver
.reload /f
```

### Debugger context for drivers

If you're debugging an active ACX driver, set a breakpoint. This places the debugger in the context of the ACX objects, to be able to gather amd display information.

These example breakpoints are designed to fire as the sample AudioCodec driver starts up.

```dbgcmd
bm AudioCodec!DriverEntry
bm AudioCodec!AcxDriverInitialize
```

These example breakpoints are designed to fire when specific actions occur, such as pin or circuit creation.

```dbgcmd
bm AudioCodec!AcxPinCreate
bm AudioCodec!AcxCircuitCreate
bm AudioCodec!Codec_EvtBusDeviceAdd
```

### Load the acxkd dll

Use the [.load (Load Extension DLL)](-load---loadby--load-extension-dll-.md) command to load the acxkd.dll extension.

```dbgcmd
.load acxkd.dll
```

### Display information about the ACX driver

To gather information about the target driver, use the [lm (List Loaded Modules)](lm--list-loaded-modules-.md) command to see all loaded drivers. Then use the Dvm options to display information about the ACX driver of interest as shown here.

```dbgcmd
0: kd> lm Dvm AcxHdAudio
Browse full module list
start             end                 module name
fffff803`8a3c0000 fffff803`8a448000   AcxHdAudio   (private pdb symbols)  C:\ProgramData\Dbg\sym\AcxHdAudio.pdb\6AEA2622909B20C1AD149C57ACBB4A6F1\AcxHdAudio.pdb
    Loaded symbol image file: AcxHdAudio.sys
    Mapped memory image file: C:\ProgramData\Dbg\sym\AcxHdAudio.sys\0829423388000\AcxHdAudio.sys
    Image path: \SystemRoot\System32\drivers\AcxHdAudio.sys
    Image name: AcxHdAudio.sys
    Browse all global symbols  functions  data  Symbol Reload
    Image was built with /Brepro flag.
    Timestamp:        08294233 (This is a reproducible build file hash, not a timestamp)
    CheckSum:         00087DD6
    ImageSize:        00088000
    Translations:     0000.04b0 0000.04e4 0409.04b0 0409.04e4
    Information from resource tables:
```

Use the [x (Examine Symbols)](x--examine-symbols-.md) command and a wildcard mask to display specific ACX structures, such as an ACXPIN.

```dbgcmd
0: kd> x /D AcxHdAudio!acxpin*
 A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

fffff803`8a3e3216 AcxHdAudio!AcxPinGetRawDataFormatList =  (inline caller) AcxHdAudio!HDACodec_EvtFormatChange+66
fffff803`8a3e31e0 AcxHdAudio!AcxPinGetCircuit =  (inline caller) AcxHdAudio!HDACodec_EvtFormatChange+30
fffff803`8a3e361f AcxHdAudio!AcxPinNotifyDataFormatChange =  (inline caller) AcxHdAudio!HDACodec_EvtFormatChange+46f
fffff803`8a3e7396 AcxHdAudio!AcxPinCreate =  (inline caller) AcxHdAudio!HDACodecR_CreateRenderCircuit+962
fffff803`8a3e74a2 AcxHdAudio!AcxPinGetRawDataFormatList =  (inline caller) AcxHdAudio!HDACodecR_CreateRenderCircuit+a6e
fffff803`8a3e75f8 AcxHdAudio!AcxPinCreate =  (inline caller) AcxHdAudio!HDACodecR_CreateRenderCircuit+bc4
fffff803`8a3e789a AcxHdAudio!AcxPinAddJacks =  (inline caller) AcxHdAudio!HDACodecR_CreateRenderCircuit+e66
fffff803`8a3e5ae5 AcxHdAudio!AcxPinGetCircuit =  (inline caller) AcxHdAudio!HDACodecR_EvtAcxPinRetrieveJackSinkInfo+25
fffff803`8a3e5913 AcxHdAudio!AcxPinGetCircuit =  (inline caller) AcxHdAudio!HDACodecR_EvtAcxPinRetrieveName+73
fffff803`8a3ea277 AcxHdAudio!AcxPinCreate =  (inline caller) AcxHdAudio!HDACodecC_CreateCaptureCircuit+b27
fffff803`8a3ea39c AcxHdAudio!AcxPinGetRawDataFormatList =  (inline caller) AcxHdAudio!HDACodecC_CreateCaptureCircuit+c4c
fffff803`8a3ea4bc AcxHdAudio!AcxPinCreate =  (inline caller) AcxHdAudio!HDACodecC_CreateCaptureCircuit+d6c
fffff803`8a3ea7b2 AcxHdAudio!AcxPinAddJacks =  (inline caller) AcxHdAudio!HDACodecC_CreateCaptureCircuit+1062
```

Depending on the current execution context in the debugger, it may be possible to use the [dx (Display Debugger Object Model Expression)](dx--display-visualizer-variables-.md) to drill down into specific ACX structures.

```dbgcmd
0: kd> dx -r2 AudioCodec!AcxDeviceAddCircuit
AudioCodec!AcxDeviceAddCircuit                 : AudioCodec!AcxDeviceAddCircuit+0x0 [Type: long __cdecl(WDFDEVICE__ *,ACXCIRCUIT__ *)]
0: kd> u fffff8007ead1120
AudioCodec!AcxDeviceAddCircuit [C:\Program Files (x86)\Windows Kits\10\Include\10.0.26016.0\km\acx\km\1.1\AcxDevice.h @ 206]:
fffff800`7ead1120 4889542410      mov     qword ptr [rsp+10h],rdx
fffff800`7ead1125 48894c2408      mov     qword ptr [rsp+8],rcx
fffff800`7ead112a 4883ec38        sub     rsp,38h
fffff800`7ead112e b808000000      mov     eax,8
fffff800`7ead1133 486bc046        imul    rax,rax,46h
fffff800`7ead1137 488d0dc2ab0000  lea     rcx,[AudioCodec!AcxFunctions (fffff800`7eadbd00)]
fffff800`7ead113e 488b0401        mov     rax,qword ptr [rcx+rax]
fffff800`7ead1142 4889442420      mov     qword ptr [rsp+20h],rax
```

Use the [!WDFDRIVERINFO](-wdfkd-wdfdriverinfo.md) command with the name of the driver to gather WDF information, such as the child ACX objects.

```dbgcmd
0: kd> !WDFDRIVERINFO AcxHdAudio.sys 1 -v 
----------------------------------
Default driver image name: AcxHdAudio
WDF library image name: Wdf01000
 FxDriverGlobals  0xffffb609403e3de0
 WdfBindInfo      0xfffff8038a3dd1b0
   Version        v1.25
 Library module   0xffffb60929cc6050
   ServiceName    \Registry\Machine\System\CurrentControlSet\Services\Wdf01000
   ImageName      Wdf01000
----------------------------------
WDFDRIVER: 0x000049f6bfe9d5d8
    context:  dt 0xffffb60940162bc0 AcxHdAudio!CODEC_DRIVER_CONTEXT (size is 0x1 bytes)
    <no associated attribute callbacks>

    context:  dt 0xffffb6093ccead20 Acx01000!AfxDriver (size is 0x20 bytes)
    EvtCleanupCallback fffff8038a455780 Acx01000!Acx::WdfCpp::ObjectContext<WDFDRIVER__ *,Acx::AfxDriver>::EvtObjectContextCleanupThunk
    EvtDestroyCallback fffff8038a455740 Acx01000!Acx::WdfCpp::ObjectContext<WDFDRIVER__ *,Acx::AfxDriver>::EvtObjectContextDestroyThunk
Object Hierarchy: !wdfhandle 0x000049f6bfe9d5d8 0xff
Driver logs: !wdflogdump AcxHdAudio.sys -d
Framework logs: !wdflogdump AcxHdAudio.sys -f

    !wdfdevice 0x000049f6bffba488 ff (FDO)
        Pnp/Power State: WdfDevStatePnpStarted, WdfDevStatePowerD0, WdfDevStatePwrPolStartedWakeCapable
        context:  dt 0xffffb60940045e60 AcxHdAudio!CODEC_DEVICE_CONTEXT (size is 0x110 bytes)
        EvtCleanupCallback fffff8038a3e3c90 AcxHdAudio!HDACodec_EvtDeviceContextCleanup

        context:  dt 0xffffb60933f030f0 Acx01000!AfxDevice (size is 0x150 bytes)
        EvtCleanupCallback fffff8038a451910 Acx01000!Acx::WdfCpp::ObjectContext<WDFDEVICE__ *,Acx::AfxDevice>::EvtObjectContextCleanupThunk
        EvtDestroyCallback fffff8038a451740 Acx01000!Acx::WdfCpp::ObjectContext<WDFDEVICE__ *,Acx::AfxDevice>::EvtObjectContextDestroyThunk

        context:  dt 0xffffb60940a26b90 AcxHdAudio!CODEC_RENDER_DEVICE_CONTEXT (size is 0x38 bytes)
        <no associated attribute callbacks>

        context:  dt 0xffffb609409f2e00 AcxHdAudio!CODEC_CAPTURE_DEVICE_CONTEXT (size is 0x8 bytes)
        <no associated attribute callbacks>
        !wdfdevicequeues 0x000049f6bffba488

        !wdfdevice 0x000049f6bef1a848 ff (PDO)
            Pnp/Power State: WdfDevStatePnpStarted, WdfDevStatePowerD0BusWakeOwner, WdfDevStatePwrPolStartedWakeCapable
            context:  dt 0xffffb609410e5aa0 AcxHdAudio!CODEC_RENDER_DEVICE_CONTEXT (size is 0x38 bytes)
            EvtCleanupCallback fffff8038a3e6400 AcxHdAudio!HDACodecR_EvtDeviceContextCleanup

            context:  dt 0xffffb60933f090d0 Acx01000!AfxDevice (size is 0x150 bytes)
            EvtCleanupCallback fffff8038a451910 Acx01000!Acx::WdfCpp::ObjectContext<WDFDEVICE__ *,Acx::AfxDevice>::EvtObjectContextCleanupThunk
            EvtDestroyCallback fffff8038a451740 Acx01000!Acx::WdfCpp::ObjectContext<WDFDEVICE__ *,Acx::AfxDevice>::EvtObjectContextDestroyThunk
            !wdfdevicequeues 0x000049f6bef1a848

----------------------------------

WDF Verifier settings for AcxHdAudio.sys is OFF
----------------------------------
```

In the output shown above, a link is available to the associated wdfdevice. Click on that link to display information about the associated WDF device objects.  

```dbgcmd
0: kd> !wdfdevice 0x000049f6bef1a848 ff
Treating handle as a KMDF handle!

Dumping WDFDEVICE 0x000049f6bef1a848
=================================

WDM PDEVICE_OBJECTs:  self ffffb60940ddbdd0

Pnp state:  119 ( WdfDevStatePnpStarted )
Power state:  309 ( WdfDevStatePowerD0BusWakeOwner )
Power Pol state:  531 ( WdfDevStatePwrPolStartedWakeCapable )
```

Also available in the `!WDFDRIVERINFO` output is a link to the WDF object hierarchy.

```dbgcmd
Object Hierarchy: !wdfhandle 0x000049f6bfe9d5d8 0xff
```

Clicking on that link displays the WDF object hierarchy for the ACX driver. This can be used to locate the WDF handles to ACX objects of interest.

```dbgcmd
0: kd> !wdfhandle 0x000049f6bfe9d5d8 0xff
Treating handle as a KMDF handle!

Dumping WDFHANDLE 0x000049f6bfe9d5d8
=============================
Handle type is WDFDRIVER
Refcount: 1
Contexts:
    context:  dt 0xffffb60940162bc0 AcxHdAudio!CODEC_DRIVER_CONTEXT (size is 0x1 bytes)
    <no associated attribute callbacks>

    context:  dt 0xffffb6093ccead20 Acx01000!AfxDriver (size is 0x20 bytes)
    EvtCleanupCallback fffff8038a455780 Acx01000!Acx::WdfCpp::ObjectContext<WDFDRIVER__ *,Acx::AfxDriver>::EvtObjectContextCleanupThunk
    EvtDestroyCallback fffff8038a455740 Acx01000!Acx::WdfCpp::ObjectContext<WDFDRIVER__ *,Acx::AfxDriver>::EvtObjectContextDestroyThunk

Child WDFHANDLEs of 0x000049f6bfe9d5d8:
    !wdfhandle 0x000049f6bfe9d5d8  dt FxDriver 0xffffb60940162a20 Context ffffb60940162bc0, Context ffffb6093ccead20 Cleanup fffff8038a455780 Destroy fffff8038a455740
        !wdfdevice 0x000049f6bffba488  dt FxDevice 0xffffb60940045b70 Context ffffb60940045e60 Cleanup fffff8038a3e3c90, Context ffffb60933f030f0 Cleanup fffff8038a451910 Destroy fffff8038a451740, Context ffffb60940a26b90, Context ffffb609409f2e00
            WDF INTERNAL   dt FxDefaultIrpHandler 0xffffb6093fa54130
            WDF INTERNAL   dt FxPkgGeneral 0xffffb609401f5610
            WDF INTERNAL   dt FxWmiIrpHandler 0xffffb609401f6510
            WDF INTERNAL   dt FxPkgIo 0xffffb6093f6d2400
                !wdfqueue 0x000049f6c00114b8  dt FxIoQueue 0xffffb6093ffeeb40
            WDF INTERNAL   dt FxPkgFdo 0xffffb6093f2ae020
            !wdfhandle 0x000049f6bfe099f8  dt FxCmResList 0xffffb609401f6600
            !wdfhandle 0x000049f6bfe0a358  dt FxCmResList 0xffffb609401f5ca0
            !wdfchildlist 0x000049f6c09adb98  dt FxChildList 0xffffb6093f652460
            !wdfiotarget 0x000049f6c092d1d8  dt FxIoTarget 0xffffb6093f6d2e20
            !wdfqueue 0x000049f6c04904c8  dt FxIoQueue 0xffffb6093fb6fb30 Context ffffb6093fa8dcd0 Cleanup fffff8038a45a350 Destroy fffff8038a45a310
            !wdfhandle 0x000049f6c09e7ed8  dt FxWorkItem 0xffffb6093f618120 Context ffffb6093f618220
            WDF INTERNAL   dt FxWmiProvider 0xffffb609403d9b50
                WDF INTERNAL   dt FxWmiInstanceExternal 0xffffb60940a11320
            WDF INTERNAL   dt FxWmiProvider 0xffffb609403d9300
                WDF INTERNAL   dt FxWmiInstanceExternal 0xffffb60940a11720
        !wdfdevice 0x000049f6bef1a848  dt FxDevice 0xffffb609410e57b0 Context ffffb609410e5aa0 Cleanup fffff8038a3e6400, Context ffffb60933f090d0 Cleanup fffff8038a451910 Destroy fffff8038a451740
            WDF INTERNAL   dt FxDefaultIrpHandler 0xffffb60940c16450
            WDF INTERNAL   dt FxPkgGeneral 0xffffb60940bc9a10
            WDF INTERNAL   dt FxWmiIrpHandler 0xffffb60940bc9380
            WDF INTERNAL   dt FxPkgIo 0xffffb609400ab5c0
                !wdfqueue 0x000049f6beefd588  dt FxIoQueue 0xffffb60941102a70
            WDF INTERNAL   dt FxPkgPdo 0xffffb609410e6020
            !wdfhandle 0x000049f6bf436e58  dt FxCmResList 0xffffb60940bc91a0
            !wdfhandle 0x000049f6bf436d68  dt FxCmResList 0xffffb60940bc9290
            !wdfqueue 0x000049f6bef185c8  dt FxIoQueue 0xffffb609410e7a30 Context ffffb60940e72ed0 Cleanup fffff8038a45a350 Destroy fffff8038a45a310
            !wdfhandle 0x000049f6bf436b88 [ACXCIRCUIT]  dt FxUserObject 0xffffb60940bc9470 Context ffffb60940bc9520, Context ffffb609410e6c30 Cleanup fffff8038a45cf00 Destroy fffff8038a45ce90, Context ffffb609409f2380
                !wdfhandle 0x000049f6c0d8f378  dt FxDpc 0xffffb6093f270c80 Context ffffb6093f270d90
                !wdfhandle 0x000049f6c0d8ffd8  dt FxDpc 0xffffb6093f270020 Context ffffb6093f270130
                !wdfhandle 0x000049f6c0d8f218  dt FxDpc 0xffffb6093f270de0 Context ffffb6093f270ef0
                !wdfhandle 0x000049f6c0d90ad8  dt FxDpc 0xffffb6093f26f520 Context ffffb6093f26f630
                !wdfhandle 0x000049f6c0d91318  dt FxDpc 0xffffb6093f26ece0 Context ffffb6093f26edf0
                !wdfhandle 0x000049f6c0d8f638  dt FxDpc 0xffffb6093f2709c0 Context ffffb6093f270ad0
                !wdfhandle 0x000049f6bfc27d98  dt FxWorkItem 0xffffb609403d8260 Context ffffb609403d8360 Cleanup fffff8038a4a47d0
                !wdfqueue 0x000049f6bef165c8  dt FxIoQueue 0xffffb609410e9a30 Context ffffb60940e827f0 Cleanup fffff8038a463bf0 Destroy fffff8038a463bf0, Context ffffb60940e73050 Cleanup fffff8038a45a350 Destroy fffff8038a45a310
                !wdfhandle 0x000049f6bf8bf6a8  dt FxString 0xffffb60940740950
                !wdfhandle 0x000049f6bf8be8d8  dt FxString 0xffffb60940741720
                !wdfhandle 0x000049f6beff0958 [ACXELEMENT, ACXMUTE]  dt FxUserObject 0xffffb6094100f6a0 Context ffffb6094100f750, Context ffffb609400eaed0 Cleanup fffff8038a467be0 Destroy fffff8038a467b60, Context ffffb609409f21a0, Context ffffb60940e812f0 Cleanup fffff8038a467e20 Destroy fffff8038a467dc0, Context ffffb609409f2200
                    !wdfhandle 0x000049f6beff0798 [ACXEVENT]  dt FxUserObject 0xffffb6094100f860 Context ffffb6094100f910, Context ffffb60940eeb510 Cleanup fffff8038a466160 Destroy fffff8038a466100, Context ffffb609409f2560
                !wdfhandle 0x000049f6befeee38 [ACXPIN]  dt FxUserObject 0xffffb609410111c0 Context ffffb60941011270, Context ffffb60940a844a0 Cleanup fffff8038a4654e0 Destroy fffff8038a465410, Context ffffb609409f1d80
                    !wdfhandle 0x000049f6bf8bf848 [ACXDATAFORMATLIST]  dt FxUserObject 0xffffb609407407b0 Context ffffb60940443610 Cleanup fffff8038a458eb0 Destroy fffff8038a458e40, Context ffffb609409f22c0
                    !wdfhandle 0x000049f6befee8f8 [ACXEVENT]  dt FxUserObject 0xffffb60941011700 Context ffffb609410117b0, Context ffffb60940eeb620 Cleanup fffff8038a466160 Destroy fffff8038a466100, Context ffffb609409f1de0
                !wdfhandle 0x000049f6befee578 [ACXDATAFORMAT]  dt FxUserObject 0xffffb60941011a80 Context ffffb60941011b30, Context ffffb60940442a60 Cleanup fffff8038a45a060 Destroy fffff8038a459ff0, Context ffffb609409f1a80
                !wdfhandle 0x000049f6befeec78 [ACXDATAFORMAT]  dt FxUserObject 0xffffb60941011380 Context ffffb60941011430, Context ffffb60940444a00 Cleanup fffff8038a45a060 Destroy fffff8038a459ff0, Context ffffb609409f20e0
```

To find the ACXCIRCUIT handle value, use the link in output above that calls [!wdfhandle](-wdfkd-wdfhandle.md) extension for the WDFDRIVER object.

```dbgcmd
0: kd> !wdfhandle 0x000049f6bfe9d5d8 0xff
Treating handle as a KMDF handle!

Dumping WDFHANDLE 0x000049f6bfe9d5d8
=============================
Handle type is WDFDRIVER
Refcount: 1
Contexts:
    context:  dt 0xffffb60940162bc0 AcxHdAudio!CODEC_DRIVER_CONTEXT (size is 0x1 bytes)
    <no associated attribute callbacks>

    context:  dt 0xffffb6093ccead20 Acx01000!AfxDriver (size is 0x20 bytes)
    EvtCleanupCallback fffff8038a455780 Acx01000!Acx::WdfCpp::ObjectContext<WDFDRIVER__ *,Acx::AfxDriver>::EvtObjectContextCleanupThunk
    EvtDestroyCallback fffff8038a455740 Acx01000!Acx::WdfCpp::ObjectContext<WDFDRIVER__ *,Acx::AfxDriver>::EvtObjectContextDestroyThunk

Child WDFHANDLEs of 0x000049f6bfe9d5d8:
    !wdfhandle 0x000049f6bfe9d5d8  dt FxDriver 0xffffb60940162a20 Context ffffb60940162bc0, Context ffffb6093ccead20 Cleanup fffff8038a455780 Destroy fffff8038a455740
        !wdfdevice 0x000049f6bffba488  dt FxDevice 0xffffb60940045b70 Context ffffb60940045e60 Cleanup fffff8038a3e3c90, Context ffffb60933f030f0 Cleanup fffff8038a451910 Destroy fffff8038a451740, Context ffffb60940a26b90, Context ffffb609409f2e00
            WDF INTERNAL   dt FxDefaultIrpHandler 0xffffb6093fa54130
            WDF INTERNAL   dt FxPkgGeneral 0xffffb609401f5610
            WDF INTERNAL   dt FxWmiIrpHandler 0xffffb609401f6510
            WDF INTERNAL   dt FxPkgIo 0xffffb6093f6d2400
                !wdfqueue 0x000049f6c00114b8  dt FxIoQueue 0xffffb6093ffeeb40
```

### Use the !acxkd commands

Once the driver is loaded and the appropriate breakpoint has fired, and valid execution context is available, use !acxkd commands to display information about any ACX object. Use the !acxobject command for general information and a specific command, such as !acxcircuit or !acxpin for more granular information.

For example, to display information about an ACX circuit, use the `!acxcircuit` command with the previously determined WDF handle.

```dbgcmd
0: kd> !acxcircuit 000049f6bf436b88
Dumping info for ACXCIRCUIT 0x000049f6bf436b88

    Name: eHDMIOutTopo
    Type: AcxCircuitTypeRender
    ComponentId: {BFCA9AD9-4EED-46C2-9323-B5D4400761A5}

    State: AfxCircuitStatePoweredUp
    State history:
        0 : AfxCircuitStateInvalid
        1 : AfxCircuitStateInvalid
        2 : AfxCircuitStateInvalid
        3 : AfxCircuitStateCreated
        4 : AfxCircuitStateInitializing
        5 : AfxCircuitStateInitialized
        6 : AfxCircuitStatePoweredDown
        7 : AfxCircuitStatePoweredUp

    Interface is enabled
    SymolicLinkName: \??\HDAUDIO#SUBFUNC_01&VEN_8086&DEV_2815&NID_0001&SUBSYS_00000000&REV_1000#5&f8e61d0&0&0002&00000021#{2c6bb644-e1ae-47f8-9a2b-1d1fa750f2fa}\eHDMIOutTopo

    # Power references: 0
    # Open handles: 8

    !acxproperties 000049f6bf436b88
    !acxmethods 000049f6bf436b88
    !acxevents 000049f6bf436b88

    # Pins: 2
        !acxpin 000049f6befeee38
        !acxpin 000049f6bf8be808

    # Elements: 1
        !acxelement 000049f6beff0958

    # Streams: 0

    !acxcircuit 000049f6bf436b88
    !wdfqueue 000049f6bef165c8
    !acxdevice 000049f6bef1a848
    !wdfdevice 000049f6bef1a848

    !wdfhandle 000049f6bf436b88
    dt Acx01000!Acx::AfxCircuit ffffb609410e6c30
```

In the output handles are provided for other objects such as ACX properties, that can be displayed using the appropriate ACX command.

```dbgcmd
0: kd> !acxproperties 000049f6bf436b88
Dumping properties info for ACXOBJECT 0x000049f6bf436b88

    # sets: 4

        Set: {8C134960-51AD-11CF-878A-94F801C10000}
            Id: 0, Flags: 0x1
            Id: 1, Flags: 0x1

        Set: {720D4AC0-7533-11D0-A5D6-28DB04C10000}
            Id: 0, Flags: 0x1
            Id: 1, Flags: 0x1
            Id: 2, Flags: 0x1
            Id: 3, Flags: 0x1

        Set: {C034FDB0-FF75-47C8-AA3C-EE46716B50C6}
            Id: 1, Flags: 0x1
            Id: 2, Flags: 0x1
            Id: 3, Flags: 0x1

        Set: {4D12807E-55DB-48B8-A466-F15A510F5817}
            Id: 1, Flags: 0x1
```

### Other WDF commands

As ACX drivers are WDF drivers, use any of the WDF kernel debugger commands. For example, use [!wdfkd.wdfldr](-wdfkd-wdfldr.md) to display version information and the binding with WDF.

```dbgcmd
0: kd> !wdfldr AudioCodec
WDF Driver: AudioCodec
----------------------------------
CLIENT_MODULE   0xffff850474ddedb0
  WDF Version   v1.31
  ImageName     AudioCodec.sys
  ImageAddress  0xfffff8079b500000
  ImageSize     0x1e000
  BindingList   0xffff850474ddedf8

  ImageName        WdfVer Ver   WdfGlobals         BindInfo           ImageAddress       ImageSize
  Wdf01000.sys     v1.33  v1.33 0xffff850470564f80 0xffff850470564dc0 0xfffff807833c0000 0x000c7000
  Acx01000.sys     v1.31  v1.1  0xffff850465c0ff90 0xfffff8079b50ba50 0xfffff80797b80000 0x000b3000
```

### WDF log commands

Using [!wdflogdump](-wdfkd-wdflogdump.md) can be useful for troubleshooting an ACX driver by displaying WDF log information.

```dbgcmd
0: kd> !wdflogdump AcxHdAudio.sys -f
Trace searchpath is: 

Trace format prefix is: %7!u!: %!FUNC! - 
Trying to extract TMF information from - C:\ProgramData\Dbg\sym\Wdf01000.pdb\D8C1E014D7F7ED2A204AC175CFB311451\Wdf01000.pdb
Gather log: Please wait, this may take a moment (reading 4024 bytes).
% read so far ... 10, 20, 30, 40, 50, 60, 70, 80, 90, 100
There are 75 log entries
--- start of log ---
36844: FxPowerIdleMachine::ProcessEventLocked - WDFDEVICE 0x000049F6BEF1A848 !devobj 0xFFFFB60940DDBDD0 entering power idle state FxIdleTimerRunning from FxIdleStartTimer
36845: FxPowerIdleMachine::ProcessEventLocked - WDFDEVICE 0x000049F6BEF1A848 !devobj 0xFFFFB60940DDBDD0 entering power idle state FxIdleCancelTimer from FxIdleTimerRunning
36846: FxPowerIdleMachine::ProcessEventLocked - WDFDEVICE 0x000049F6BEF1A848 !devobj 0xFFFFB60940DDBDD0 entering power idle state FxIdleCheckIoCount from FxIdleCancelTimer
36847: FxPowerIdleMachine::ProcessEventLocked - WDFDEVICE 0x000049F6BEF1A848 !devobj 0xFFFFB60940DDBDD0 entering power idle state FxIdleBusy from FxIdleCheckIoCount
...
```

## Additional Information

For more information, see [Kernel Streaming Debugging](../debugger/kernel-streaming-debugging.md). For a walkthrough of debugging with a WDM audio driver, see [Debug Drivers - Step by Step Lab (Sysvad Kernel Mode)](../debugger/debug-universal-drivers--kernel-mode-.md). For more information about ACX, see [ACX audio class extensions overview](../audio/acx-audio-class-extensions-overview.md).
