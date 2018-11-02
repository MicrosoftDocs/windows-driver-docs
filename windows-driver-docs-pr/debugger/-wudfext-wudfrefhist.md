---
title: wudfext.wudfrefhist
description: The wudfext.wudfrefhist extension displays the reference count stack history for a UMDF object.
ms.assetid: 8999f525-c6ed-4341-be2c-b0debef23a4b
keywords: ["wudfext.wudfrefhist Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- wudfext.wudfrefhist
api_type:
- NA
ms.localizationpriority: medium
---

# !wudfext.wudfrefhist


The **!wudfext.wudfrefhist** extension displays the reference count stack history for a UMDF object.

```dbgcmd
!wudfext.wudfrefhist ObjectAddress
```dbgcmd

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______ObjectAddress______"></span><span id="_______objectaddress______"></span><span id="_______OBJECTADDRESS______"></span> *ObjectAddress*   
Specifies the address of the UMDF object whose reference count stack history is to be displayed. Note that this is the address of the object itself, not of the interface.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Unavailable</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Wudfext.dll</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information, see [User-Mode Driver Framework Debugging](user-mode-driver-framework-debugging.md).

Remarks
-------

The **!wudfext.wudfrefhist** command is not supported by UMDF 1.11.

The *ObjectAddress* parameter must be the address of the UMDF object, not the address of the interface (which is used by many other UMDF extension commands). To determine the address of the UMDF object, use the [**!wudfext.wudfdumpobjects**](-wudfext-wudfdumpobjects.md) command, which displays both the UMDF object address and the interface address. Alternatively, if you know the address of the interface, you can use it as the argument of the [**!wudfext.wudfobject**](-wudfext-wudfobject.md) command, which displays the object address (displayed after the symbol "Fx:").

If the reference count tracking option (**TrackRefCounts**) has been enabled in WDF Verifier, you can use **!wudfext.wudfrefhist** to display each call stack that increments or decrements an object's reference count. You can determine whether a call stack is causing a memory leak by examining its **AddRef** and **Release** calls for references that are being added and not released.

This command can be used at any time, even if UMDF has not broken in to the debugger.

If this command does not display the desired information, make sure that the relevant data is paged in and then try again.

Here is an example of using the **!wudfext.wudfrefhist** command:

```dbgcmd
0:007> !wudfext.umdevstacks
...
      UMDriver Image Path: C:\Windows\System32\drivers\UMDF\WUDFOsrUsbFilter.dll
      Object Tracker Address: 0x0000003792ee9fc0
        Object   Tracking ON
        Refcount Tracking ON

0:007> !wudfext.wudfdumpobjects 0x0000003792ee9fc0
...
WdfTypeIoQueue   Object: 0x0000003792f05ce0, Interface: 0x0000003792f05d58

## 0:007> !wudfext.wudfrefhist 0x0000003792f05ce0
-----------------------------------------------------------------------
## 2  (++)
-----------------------------------------------------------------------
WUDFx!UfxObject::TrackRefCounts+0xb2
WUDFx!CWdfIoQueue::AddRef+0x17adc
WUDFx!CWdfIoQueue::CreateAndInitialize+0xeb
WUDFx!CWdfDevice::CreateIoQueue+0x1e7
WUDFOsrUsbFilter!CMyQueue::Initialize+0x48
WUDFOsrUsbFilter!CMyDevice::Configure+0x7d
WUDFOsrUsbFilter!CMyDriver::OnDeviceAdd+0xca
WUDFx!CWdfDriver::OnAddDevice+0x486
WUDFx!CWUDF::AddDevice+0x43
WUDFHost!CWudfDeviceStack::LoadDrivers+0x320
WUDFHost!CLpcNotification::Message+0x1340
WUDFPlatform!WdfLpcPort::ProcessMessage+0x140
WUDFPlatform!WdfLpcCommPort::ProcessMessage+0x92
WUDFPlatform!WdfLpc::RetrieveMessage+0x20c
```

 

 





